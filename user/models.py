from django.db import models
import os.path

# Create your models here.

class TbUser(models.Model):
    user_email = models.EmailField(primary_key=True, unique=True, max_length=50)
    user_pw = models.CharField(max_length=500)
    user_nick = models.CharField(max_length=30)

    def __str__(self):
        return self.user_nick

    class Meta:
        db_table = 'tb_user'

class Document(models.Model):
    user_email = models.EmailField(primary_key=True, unique=True, max_length=50)
    title = models.CharField(max_length=200, null=True)
    uploadedFile = models.FileField(null=True, upload_to="", blank=True)
    dateTimeOfUpload = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_email

    def get_file_name(self):
        return os.path.basename(self.uploadedFile)


    class Meta:
        db_table = 'document'
