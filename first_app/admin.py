from django.contrib import admin
from .models import Topicos,Paginas, RegistroAcesso, Produto

# Register your models here.

admin.site.register(Topicos)
admin.site.register(Paginas)
admin.site.register(RegistroAcesso)
admin.site.register(Produto)


