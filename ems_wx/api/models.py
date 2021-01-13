from django.db import models


# Create your models here.

class User(models.Model):
    gender_choices = {
        (0, 'male'),
        (1, 'female')
    }
    username = models.CharField(max_length=60)
    password = models.CharField(max_length=128)
    real_name = models.CharField(max_length=80)
    gender = models.SmallIntegerField(choices=gender_choices, default=0)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'bz_user'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Employee(models.Model):
    emp_name = models.CharField(max_length=60)
    img = models.ImageField(upload_to='img', default='img/1.jpg')
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    age = models.SmallIntegerField()

    @property
    def full_img(self):
        return "%s%s%s" % ('http://127.0.0.1:8000/', 'media/', self.img)

    class Meta:
        db_table = 'employee'
        verbose_name = '员工表'
        verbose_name_plural = verbose_name
