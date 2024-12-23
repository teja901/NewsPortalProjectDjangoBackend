from django.db import models

# Create your models here.
class Categories(models.Model):
    categoryName=models.CharField(max_length=100,null=True,blank=True,unique=True)
    
    def __str__(self):
        return f"{self.categoryName}"
    
    def save(self,*args,**kwargs):
        admin=AdminEmployeeCredentials.objects.get(role="ADMIN")
        super().save(*args, **kwargs) 
        admin.categories.add(self)
        

class AdminEmployeeCredentials(models.Model):
    categories=models.ManyToManyField(Categories,blank=True,related_name='adminemployee')
    profilePhoto=models.ImageField(upload_to='Images/Admin/',null=True,blank=True)
    name=models.CharField(max_length=100,null=True,blank=True)
    phoneNumber=models.CharField(max_length=50,null=True,blank=True)
    email=models.EmailField(blank=True,null=True)
    password=models.CharField(max_length=100,null=True,blank=True)
    role=models.CharField(max_length=50,null=True,blank=True)
    status=models.BooleanField(default=True,null=True)
    
class SubCategories(models.Model):
    category=models.ForeignKey(Categories,on_delete=models.CASCADE,null=True,blank=True,related_name='subcategories')
    subcategoryName=models.CharField(max_length=100,null=True,blank=True,unique=True)