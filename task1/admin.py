from django.contrib import admin
from .models import Game, Buyer

# Register your models here.

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_filter = ('size', 'cost',)             #Фильтрацию по полям size и cost.
    list_display = ('title', 'cost', 'size',)   #Отображение title, cost и size при отображении всех полей списком.
    search_fields = ('title',)                  #Поиск по полю title.
    list_per_page = 20                          #Ограничение кол-ва записей до 20.

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_filter = ('balance', 'age',)          #Фильтрацию по полям balance и age.
    list_display = ('name', 'balance', 'age',) #Отображение name, balance и age при отображении всех полей списком.
    search_fields = ('name',)                  #Поиск по полю name.
    list_per_page = 30                         #Ограничение кол-ва записей до 30.
    readonly_fields = ('balance',)             #Доступным только для чтения поле balance.

