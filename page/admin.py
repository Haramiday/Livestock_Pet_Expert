from django.contrib import admin
from .models import GoatSym,GoatDisInfo,CowSym,CowDisInfo,AnimalInfo,ChickenSym,ChickenDisInfo,DogSym,DogDisInfo,CatSym,CatDisInfo,Prescription
# Register your models here.


admin.site.register(GoatSym)
admin.site.register(GoatDisInfo)
admin.site.register(CowSym)
admin.site.register(CowDisInfo)
admin.site.register(ChickenSym)
admin.site.register(ChickenDisInfo)
admin.site.register(AnimalInfo)
admin.site.register(DogSym)
admin.site.register(DogDisInfo)
admin.site.register(CatSym)
admin.site.register(CatDisInfo)
admin.site.register(Prescription)