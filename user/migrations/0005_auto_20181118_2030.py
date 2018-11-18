# Generated by Django 2.1 on 2018-11-18 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20181109_1911'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Semester')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Semester')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveIntegerField(default=2018)),
            ],
        ),
        migrations.AddField(
            model_name='result',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Year'),
        ),
        migrations.AddField(
            model_name='student',
            name='year',
            field=models.ForeignKey(default=2018, on_delete=django.db.models.deletion.CASCADE, to='user.Year'),
        ),
    ]
