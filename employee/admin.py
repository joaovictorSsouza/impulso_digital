from django.contrib import admin
from employee.models import Employee, Sector, Hierarchical_Level

# colunas: id, name, age. cpf, id_sector, sector, contract_time, salary, photo

class EmployeeAdmin(admin.ModelAdmin):

    list_display = ('name', 'age', 'cpf', 'sector', 'contract_time', 'salary', 'photo')
    search_fields = ('name', 'cpf',)

admin.site.register(Employee, EmployeeAdmin)

class SectorAdmin(admin.ModelAdmin):

    list_display = ('sector',)
    search_fields = ('sector',)

admin.site.register(Sector, SectorAdmin)

class HierarchicalAdmin(admin.ModelAdmin):

    list_display = ('hierarchical_level',)
    search_fields = ('hierarchical_level',)

admin.site.register(Hierarchical_Level, HierarchicalAdmin)
