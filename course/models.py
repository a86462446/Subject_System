from django.db import models


# 課程資訊
class course(models.Model):
   name= models.CharField(max_length= 20, verbose_name= '科目名稱', null= False, default= "")
   code= models.CharField(max_length= 10, verbose_name= '選課代碼', null= False, default= "")
   classs= models.CharField(max_length= 20, verbose_name= '開課班級', null= False, default= "")
   required_elective= models.CharField(max_length= 20, verbose_name= '必選修', null= False, default= "")
   credit= models.IntegerField(verbose_name= '學分', null= False, default= 0)
   time= models.CharField(max_length= 25, verbose_name= '課程時間', null= False, default= "")
   start_session= models.IntegerField(verbose_name= '開始節次', null= False, default= 0)
   end_session= models.IntegerField(verbose_name= '結束節次', null= False)
   week= models.CharField(max_length= 3, verbose_name= '星期', null= False, default= "")

   def __str__(self):
        return f"{self.code}"
   

# 學生帳戶資訊
class Student(models.Model):
   student_name= models.CharField(max_length= 10, verbose_name= "學生名稱", null= False)
   student_number= models.CharField(max_length= 15, verbose_name= "學號", null= False)
   student_class= models.CharField(max_length= 15, verbose_name= "系級", null= False)
   student_credit= models.IntegerField(verbose_name= "學分", default= 0)

   def __str__(self):
        return f"{self.student_number}"


# 學生選課資訊
class Student_course(models.Model):
   student_number= models.CharField(max_length= 15, verbose_name= "學號", null= False, default= "")
   name= models.CharField(max_length= 20, verbose_name= '科目名稱', null= False, default= "")
   code= models.CharField(max_length= 10, verbose_name= '選課代碼', null= False, default= "")
   classs= models.CharField(max_length= 20, verbose_name= '開課班級', null= False, default= "")
   required_elective= models.CharField(max_length= 20, verbose_name= '必選修', null= False, default= "")
   credit= models.DecimalField(max_digits= 10, decimal_places= 0, verbose_name= '學分', null= False, default= 0)
   time= models.CharField(max_length= 25, verbose_name= '課程時間', null= False, default= "")
   start_session= models.IntegerField(verbose_name= '開始節次', null= False, default= 0)
   end_session= models.IntegerField(verbose_name= '結束節次', null= False, default= 0)
   week= models.CharField(max_length= 3, verbose_name= '星期', null= False, default= "")

   def __str__(self):
        return f"{self.student_number}"