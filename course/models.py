from django.db import models

# Create your models here.

class course(models.Model):
   name= models.CharField(max_length= 20, verbose_name= '科目名稱')
   code= models.DecimalField(max_digits= 10, decimal_places= 0, verbose_name= '選課代碼')
   classs= models.CharField(max_length= 20, verbose_name= '開課班級')
   required_elective= models.CharField(max_length= 20, verbose_name= '必選修')
   credit= models.DecimalField(max_digits= 10, decimal_places= 0, verbose_name= '學分')
   time= models.CharField(max_length= 25, verbose_name= '課程時間')

   def __str__(self):
        return f"{self.code}"
   
class D1051831_course(models.Model):
   name= models.CharField(max_length= 20, verbose_name= '科目名稱')
   code= models.DecimalField(max_digits= 10, decimal_places= 0, verbose_name= '選課代碼')
   classs= models.CharField(max_length= 20, verbose_name= '開課班級')
   required_elective= models.CharField(max_length= 20, verbose_name= '必選修')
   credit= models.DecimalField(max_digits= 10, decimal_places= 0, verbose_name= '學分')
   time= models.CharField(max_length= 25, verbose_name= '課程時間')

   def __str__(self):
        return f"{self.code}"