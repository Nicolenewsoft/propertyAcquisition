from django.db import models


class Users(models.Model):
    INCOME = (
        ('Formal', 'Formal'),
        ('Informal', 'Informal'),
        ('Mista', 'Mista'),
    )

    MARITAL_STATUS = (
        ('Solteiro(a)', 'Solteiro(a)'),
        ('Casado(a)', 'Casado(a)'),
        ('Viúvo(a)', 'Viúvo(a)'),
        ('Separado(a)', 'Separado(a)'),
        ('Divorciado(a)', 'Divorciado(a)'),
    )

    SERVICE = (
        ('Habitacional', 'Habitacional'),
        ('Comercial', 'Comercial'),
    )
    employees = models.ForeignKey('employees.Employees', on_delete=models.CASCADE)
    name = models.CharField('Nome', max_length=50, blank=False, null=False)
    cpf = models.CharField('CPF', max_length=50, blank=False, null=False)
    phone = models.CharField('Telefone', max_length=50, blank=False, null=False)
    email = models.CharField('Email', max_length=50, blank=False, null=False)
    birth_date = models.DateField('Data de nascimento', blank=False, null=False)
    income = models.CharField('Renda', max_length=50, choices=INCOME, blank=False, null=False)
    marital_status = models.CharField('Estado Civil', max_length=50, choices=MARITAL_STATUS, blank=False, null=False)
    cpf_spouse = models.CharField('CPF do cônjuge', max_length=50, blank=True, null=True)
    broker = models.CharField('Telefone do corretor', max_length=50, blank=False, null=False)
    real_estate = models.CharField('Imobiliária', max_length=50, blank=True, null=True)
    agency = models.CharField('Agência', max_length=50, blank=False, null=False)
    service = models.CharField('Renda', max_length=50, choices=SERVICE, blank=False, null=False)
    enterprise = models.CharField('Empreendimento', max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


