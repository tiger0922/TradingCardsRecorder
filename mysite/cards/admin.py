from django.contrib import admin

from .models import Card

# Register your models here.
class CardAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Number',  {'fields': ['number']}),
        ('Member',  {'fields': ['member']}),
        ('Piece',   {'fields': ['piece']}),
        ('Album',   {'fields': ['album']}),
    ]
    list_display = ('number', 'member', 'piece', 'album')
    list_filter = ['number']

admin.site.register(Card, CardAdmin)
