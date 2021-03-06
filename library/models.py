from django.db import models
from user.models import Student,Semester
import uuid #for unique book instances 
from datetime import date

class Books(models.Model):    
    name = models.CharField(max_length = 200)
    semester = models.ForeignKey(Semester,on_delete=models.CASCADE)
    author = models.CharField (max_length = 200)
    nou_avaible = models.PositiveIntegerField(default = 1)
    nou_borrowed = models.PositiveIntegerField(default = 0)
    nou_registered = models.PositiveIntegerField(default = 1)

    def __str__(self):
        return self.name
    
    def reset(self):
        self.nou_avaible = self.nou_registered
        self.nou_borrowed = 0
        self.save()

    @property
    def is_avaiable(self):
        if self.nou_avaible == 0:
            return False
        return True

    def assigned(self):
        self.nou_avaible = self.nou_avaible - 1
        self.nou_borrowed = self.nou_borrowed + 1
        super().save()
        return True

    def returned(self):
        self.nou_avaible = self.nou_avaible +1
        self.nou_borrowed = self.nou_borrowed - 1
        super().save()
        return True


class BookInstance(models.Model):
    book = models.ForeignKey(Books,on_delete = models.CASCADE)
    #uuid will be used for qr code sys 
    uuid = models.UUIDField(primary_key=True,default= uuid.uuid4,help_text="Unique ID for this particular book across whole library")
    assigned_to = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True,blank=True)
    due_date = models.DateField(null=True,blank=True)
    is_assigned = models.BooleanField(default=False)

    def __str__(self):
        return self.book.name

    @property
    def is_overdue(self):
        if self.due_date and date.today() > self.due_date:
            return True
        return False

    def save(self, *args, **kwargs):
        if self.is_assigned == False: 
            self.assigned_to = None
            self.due_date = None
            self.book.returned()
            super().save(*args, **kwargs)
        elif self.is_assigned == True: 
            self.book.assigned()
            super().save(*args, **kwargs)  # Call the "real" save() method.
        