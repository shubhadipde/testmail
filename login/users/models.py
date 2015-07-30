from django.db import models

# Create your models here.


class UserInfo(models.Model):
    email = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100)
    picture = models.ImageField(upload_to= 'pic_folder/', default='pic_folder/none')

    def __unicode__(self):
    	return self.email



class EmailApp(models.Model):
	to = models.ForeignKey(UserInfo,related_name="ToEmail")
	frm = models.ForeignKey(UserInfo,related_name="FromEmail")
	body = models.TextField()


