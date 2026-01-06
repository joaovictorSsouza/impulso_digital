from django.template.defaultfilters import default
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator
from localflavor.br.validators import BRCPFValidator
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

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

class EmployeeManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('O email é obrigatorio')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        #Criptografia da senha
        user.set_password(password)

        #Salva no Banco de dados
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


#classe para a construção da tabela | falta a photo
class Employee(AbstractBaseUser, PermissionsMixin):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
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
    status = models.CharField(max_length=20, choices=status_choices, default='Active')
    access_allowed = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)


    objects = EmployeeManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'cpf']


    def __str__(self):
        return self.name
    

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        # Lógica de Sincronização
        if self.status == 'Active':
            self.is_active = True
        else:
            self.is_active = False
        # Chama o método save original do Django para concluir a gravação
        super().save(*args, **kwargs)
    
