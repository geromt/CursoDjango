from django.contrib import admin
from .models import AutorModel, FraseModel, Profesion


admin.site.site_header = "Hola"
admin.site.index_title = "Hola 2"
admin.site.site_title = "Hola 3"


@admin.register(Profesion)
class ProfesionAdmin(admin.ModelAdmin):
    list_display = ["nombre"]
    fields = ["nombre"]


# Register your models here.
class FraseInLine(admin.TabularInline):
    model = FraseModel
    extra = 1


class AutorAdmin(admin.ModelAdmin):
    fields = ["nombre", "fecha_nacimiento", "fecha_fallecimiento", "profesion", "nacionalidad"]
    list_display = ["nombre", "fecha_nacimiento"]
    inlines = [FraseInLine]

    def actualizar_o(self, request, queryset):
        for o in queryset:
            if "O" in o.nombre:
                nombre1 = o.nombre
                o.nombre = nombre1.replace("O", "o")
                o.save()

        self.message_user(request, "Exitosamente")

    actualizar_o.short_description = "Actualizar letras O"
    actions = ["actualizar_o"]


admin.site.register(AutorModel, AutorAdmin)


@admin.register(FraseModel)
class FraseAdmin(admin.ModelAdmin):
    fields = ["cita", "autor_fx"]
    list_display = ["cita"]
