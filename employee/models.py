from django.template.defaultfilters import default
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator
from localflavor.br.validators import BRCPFValidator

# colunas: id, name, age. cpf, id_sector, sector, contract_time, salary, photo, email, phone, hare_date, birth_date, status, cargo 

#classe para o menu suspenso de sector
class Sector(models.Model):

    id = models.AutoField(primary_key=True)
    sector = models.CharField(max_length=200)

    def __str__(self):
        return self.sector


#Classe para o menu suspens do hierarchical level
class Hierarchical_Level(models.Model):

    id = models.AutoField(primary_key=True)
    hierarchical_level = models.CharField(max_length=200)

    def __str__(self):
        return self.hierarchical_level


#Criando o choices para relacionar ao Status.
status_choices = [('Active', 'Active'), ('Inactive', 'Inactive'),]

#classe para a construção da tabela | falta a photo
class Employee(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True, blank=True, null=True)
    phone = models.CharField(max_length=12, blank=True, null=True)
    age = models.IntegerField()
    cpf = models.CharField(max_length=14, unique=True, validators=[MinLengthValidator(11), MaxLengthValidator(14), BRCPFValidator()])
    birth_date = models.DateField(blank=True, null=True)
    hire_date = models.DateField(blank=True, null=True)
    sector = models.ForeignKey(Sector, on_delete=models.PROTECT, related_name='list_sector')
    hierarchical_level = models.ForeignKey(Hierarchical_Level, on_delete=models.PROTECT, related_name='list_hierarchical', null=True)
    contract_time = models.CharField(max_length=200)
    salary = models.FloatField()
    photo = models.ImageField(upload_to='employee/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=status_choices, default='Activate')

    def __str__(self):
        return self.name
    
