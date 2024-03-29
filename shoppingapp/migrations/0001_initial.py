# Generated by Django 2.0.2 on 2018-02-27 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=15)),
                ('uname', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=15)),
                ('fname', models.CharField(max_length=15)),
                ('lname', models.CharField(max_length=15)),
                ('dob', models.DateTimeField(verbose_name='date published')),
                ('mno', models.IntegerField(max_length=15)),
                ('email', models.CharField(max_length=15)),
                ('image', models.CharField(max_length=15)),
            ],
        ),
    ]
