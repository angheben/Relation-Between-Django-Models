from django.db import models


class Chassi(models.Model):
    numero = models.CharField(name='numero', max_length=16, help_text="Informe 16 caracteres")

    class Meta:
        verbose_name = 'Chassi'
        verbose_name_plural = 'Chassis'

    def __str__(self):
        return self.numero


class Carro(models.Model):
    """
    Every car can only be relational just with one car
    """
    chassi = models.OneToOneField(Chassi, on_delete=models.CASCADE)
    modelo = models.CharField('Modelo', max_length=50, help_text="Informe 16 caracteres")
    preco = models.DecimalField("Preço", max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'

    def __str__(self):
        return self.modelo

