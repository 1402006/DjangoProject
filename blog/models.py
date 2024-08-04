from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 50)
    
    def __str__(self) :
        return self.name 
    
class Article(models.Model) :
    title=models.CharField(max_length = 50)
    category= models.ForeignKey(Category,on_delete = models.CASCADE)
    desc=models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now = True)
    image = models.ImageField(upload_to="")
    
    def __str__(self):
        return self.title

 
# Create your models here.
