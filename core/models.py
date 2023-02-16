from django.db import models
from django.contrib.auth import get_user_model


class Chassi(models.Model):
    numero = models.CharField(name='numero', max_length=16, help_text="Informe 16 caracteres")

    class Meta:
        verbose_name = 'Chassi'
        verbose_name_plural = 'Chassis'

    def __str__(self):
        return self.numero


class Montadora(models.Model):
    nome = models.CharField('Nome', max_length=50)

    class Meta:
        verbose_name = 'Montadora'
        verbose_name_plural = 'Montadoras'

    def __str__(self):
        return self.nome


def set_default_montadora():
    """
    Essa função faz com que seja atribuído ao objecto carro criado uma montadora padrão ou que seja criada
    uma com esse nome
    :return: (object, boolean) -> Essa função retorna uma tupla com um objeto e um boolean, ou seja, se a
    montadora não existe, ela irá criar e retornar True, caso exista ela pegará o primeiro elemento
    dessa tupla '[0]' e o boolean False.
    """
    return Montadora.objects.get_or_create(nome='Padrão')[0]


class Carro(models.Model):
    """
    OneToOneField -> Every car can only be relational just with one chassi
    ForeingKey -> One 'montadora' can have more than one car
    ManyToMany -> One car can be driven by a lot of drivers and a driver can drive a lot of cars
    """
    chassi = models.OneToOneField(Chassi, on_delete=models.CASCADE)
    montadora = models.ForeignKey(Montadora, on_delete=models.SET(set_default_montadora))
    motoristas = models.ManyToManyField(get_user_model())
    modelo = models.CharField('Modelo', max_length=50, help_text="Informe 16 caracteres")
    preco = models.DecimalField("Preço", max_digits=8, decimal_places=2)    # Testing

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'

    def __str__(self):
        return f'{self.montadora} {self.chassi} {self.modelo} {self.motoristas}'
