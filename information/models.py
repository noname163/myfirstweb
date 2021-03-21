from django.db import models
from django.db.models.deletion import CASCADE

class species(models.Model):
    Name_species= models.CharField(max_length=225)

    def __str__(self):
        return self.Name_species

class issue(models.Model):
    kind_Of_issue= models.CharField(max_length=225)
    def __str__(self):
        return self.kind_Of_issue

class Tree(models.Model):
    picture= models.ImageField()
    name= models.CharField(max_length=255)
    indenty= models.CharField(max_length=255)
    detail= models.TextField(max_length=1000)
    name_species= models.ForeignKey(species,on_delete=models.CASCADE)
    kind_Of_Issue= models.ForeignKey(issue,on_delete=CASCADE)

    def __str__(self):
        return self.name



