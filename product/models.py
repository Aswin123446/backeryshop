from django.db import models

# Create your models here.
class product_collection(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='pic')
    desc=models.TextField()
    date=models.DateTimeField(auto_now_add=True)


class comment_box(models.Model):
    fkey=models.ForeignKey(product_collection,related_name="comments",on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    msg=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

