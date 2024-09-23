from django.db import models

# Create your models here.
class branches(models.Model):
    name = models.CharField(max_length=50,unique=True)
    address = models.CharField(max_length=100,help_text="enter full address")
    phone = models.CharField(max_length=12,null=True)
    email = models.EmailField(max_length=60,null = True)

    def __str__(self):
        return self.name
    


class departments(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200,help_text="write description about the department")
    branch = models.ForeignKey(branches,related_name="departmentsBranche",on_delete=models.CASCADE) 

    class Meta:
        unique_together = ('name', 'branch')
        
    def __str__(self):
        return self.name  
