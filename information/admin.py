from django.contrib import admin
from .models import species, issue,Tree

class speciesAdmin(admin.ModelAdmin):
    list_display=('id','Name_species')

class typeOfProblemAdmin(admin.ModelAdmin):
    list_display=('id','kind_Of_issue')

class TreeAdmin(admin.ModelAdmin):
    list_display=('id','name')

admin.site.register(species,speciesAdmin)
admin.site.register(issue,typeOfProblemAdmin)
admin.site.register(Tree,TreeAdmin)
