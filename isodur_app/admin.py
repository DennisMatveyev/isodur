from django.contrib import admin

from .models import (Project,
                     ProjectPhoto,
                     Partner,
                     Product1)


class ProjectPhotoInline(admin.TabularInline):
    model = ProjectPhoto


class PartnerAdmin(admin.ModelAdmin):
    class Meta:
        model = Partner


admin.site.register(Partner, PartnerAdmin)


class ProductAdmin(admin.ModelAdmin):
    class Meta:
        model = Product1

admin.site.register(Product1, ProductAdmin)


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectPhotoInline, ]

    class Meta:
        model = Project


admin.site.register(Project, ProjectAdmin)
