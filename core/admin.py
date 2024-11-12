from django.contrib import admin
from .models import GustoHelado


class GustoHeladoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'descripcion', 'imagen')
    search_fields = ('nombre', 'categoria')

admin.site.register(GustoHelado, GustoHeladoAdmin)
