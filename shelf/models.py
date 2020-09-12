from django.db import models

# Create your models here.

#test line 123

class Book(models.Model):
    book_name = models.CharField(max_length=100)
    author_name = models.CharField(max_length=101)
    book_publication = models.CharField(max_length=100)
    book_qty = models.IntegerField()
    book_price = models.FloatField()

    class Meta:
        db_table = 'Book_Detail'

#----cmd for seeing the sql query which is availble after makemigrations
#            manage.py sqlmigrate shelf 0002

#-------------Following example when u want to make abstract model.

class CommonInfo(models.Model):                  # This table will not be created as abstract=True
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True

class Student(CommonInfo):
    home_group = models.CharField(max_length=5)



# -------------Meta data fields-----------
# abstract
# ordering
# db_table
# unique_together
# verbose_name_plural
#-------------------------------

