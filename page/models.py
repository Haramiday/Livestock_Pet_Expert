from django.db import models

# Create your models here.

class GoatSym(models.Model):
	symptom = models.CharField(max_length=1000)
	imageurl = models.URLField()

	def __str__(self):
		return self.symptom

class GoatDisInfo(models.Model):
	disease = models.CharField(max_length=100000)
	symptoms = models.CharField(max_length=100000)
	prevention = models.CharField(max_length=100000)
	sym = models.CharField(max_length=100000)

	def __str__(self):
		return self.disease


class CowSym(models.Model):
	symptom = models.CharField(max_length=1000)
	imageurl = models.URLField()

	def __str__(self):
		return self.symptom

class CowDisInfo(models.Model):
	disease = models.CharField(max_length=100000)
	symptoms = models.CharField(max_length=100000)
	prevention = models.CharField(max_length=100000)
	sym = models.CharField(max_length=100000)

	def __str__(self):
		return self.disease


class ChickenSym(models.Model):
	symptom = models.CharField(max_length=1000)
	imageurl = models.URLField()

	def __str__(self):
		return self.symptom

class ChickenDisInfo(models.Model):
	disease = models.CharField(max_length=100000)
	symptoms = models.CharField(max_length=100000)
	prevention = models.CharField(max_length=100000)
	sym = models.CharField(max_length=100000)

	def __str__(self):
		return self.disease

class DogSym(models.Model):
	symptom = models.CharField(max_length=1000)
	imageurl = models.URLField()

	def __str__(self):
		return self.symptom

class DogDisInfo(models.Model):
	disease = models.CharField(max_length=100000)
	symptoms = models.CharField(max_length=100000)
	prevention = models.CharField(max_length=100000)
	sym = models.CharField(max_length=100000)

	def __str__(self):
		return self.disease

class CatSym(models.Model):
	symptom = models.CharField(max_length=1000)
	imageurl = models.URLField()

	def __str__(self):
		return self.symptom

class CatDisInfo(models.Model):
	disease = models.CharField(max_length=100000)
	symptoms = models.CharField(max_length=100000)
	prevention = models.CharField(max_length=100000)
	sym = models.CharField(max_length=100000)

	def __str__(self):
		return self.disease

class AnimalInfo(models.Model):
	info_id = models.IntegerField()
	name = models.CharField(max_length=100000)
	info = models.CharField(max_length=10000000)
	imagelink = models.CharField(max_length=10000000)

	def __str__(self):
		return self.name

class Prescription(models.Model):
	disease = models.CharField(max_length=100000)
	prescription = models.CharField(max_length=1000000000)

	def __str__(self):
		return self.disease