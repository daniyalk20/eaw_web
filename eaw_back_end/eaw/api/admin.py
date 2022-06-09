from django.contrib import admin
from . import models
# Register your models here.

class CategoriesEntitiesAdmin(admin.ModelAdmin):
    list_display = ('id','name')

class CategoryEntitiesAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    
class EntitiesAdmin(admin.ModelAdmin):
    list_display = ('id','name')

class EntitiesRelationAdmin(admin.ModelAdmin):
    list_display = ('entity_id','created_at', 'updated_at')
    
class MigrationsAdmin(admin.ModelAdmin):
    list_display = ('id','migration', 'batch')
    
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'company_name', 'email')

admin.site.register(models.CategoriesEntities, CategoriesEntitiesAdmin)
admin.site.register(models.CategoryEntities, CategoryEntitiesAdmin)
admin.site.register(models.Entities, EntitiesAdmin)
admin.site.register(models.EntitiesRelation, EntitiesRelationAdmin)
admin.site.register(models.Migrations, MigrationsAdmin)
admin.site.register(models.Users, UsersAdmin)