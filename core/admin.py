from django.contrib import admin
from .models import Chassi, Carro, Montadora


@admin.register(Montadora)
class MontadoraAdmin(admin.ModelAdmin):
    list_display = ('nome',)


@admin.register(Chassi)
class ChassiAdmin(admin.ModelAdmin):
    list_display = ("numero",)


@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ("montadora", "modelo", "chassi", 'preco', 'get_motoristas')

    def get_motoristas(self, obj):
        """
        Para cada motorista na minha lista de motoristas cadastrados eu quero que retorne o sobrenome do motorista
        :param obj: Objetos cadastrados como motoristas
        :return: O sobrenome do motorista
        """
        return ", ".join([m.username for m in obj.motoristas.all()])

    get_motoristas.short_description = "Motoristas"
