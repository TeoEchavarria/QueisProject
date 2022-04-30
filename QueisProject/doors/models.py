import datetime
from django.db import models
from django.utils import timezone

class User(models.Model):
    user_name = models.CharField(max_length=80, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)

    def the_user_exists(self):
       return self.user_name in User.objects.all()

class Quei(models.Model):
   title = models.CharField(max_length=200)
   text_description = models.CharField(max_length=100, default="Not description")
   pub_date = models.DateTimeField("date published")
   autor = models.ForeignKey(User, on_delete= models.CASCADE)
   category = models.CharField(max_length=20)

class QueiContent(models.Model):
   quei_referece = models.ForeignKey(Quei, on_delete= models.CASCADE, default=0)
   text_content = models.TextField(default="Not Content")
   votes = models.IntegerField(default=0)

   def __str__(self):
      return self.title
   
   def time_pub_recently(self):
      time_f = timezone.now() - self.pub_date
      if time_f.seconds < 180:
         return f'{time_f.seconds} seconds'
      elif time_f.seconds > 180 and time_f.seconds < 3600:
         return f'{time_f.seconds//60} minutes'
      elif time_f.seconds > 3600 and time_f.seconds < 86400:
         return f'{time_f.seconds//3660} hours'
      elif time_f.days >= 1 and time_f.days < 8:
         return f'{time_f.days} days'
      elif time_f.days > 8 and time_f.seconds < 30:
         return f'{time_f.days//7} weeks'
      elif time_f.days > 30 and time_f.seconds < 365:
         return f'{time_f.days//30} months'
      else:
         return f'{time_f.days//365} years'
      
   def was_published_recently(self):  
      return timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Comment(models.Model):
   quei = models.ForeignKey(QueiContent, on_delete=models.CASCADE)
   comment_text = models.CharField(max_length=300)
   votes = models.IntegerField(default=0)

   def __str__(self):
      return self.comment_texts