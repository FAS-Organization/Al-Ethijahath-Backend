from django.contrib import admin

from django.contrib import admin
from .models import EquipmentCategory, DispatchRequest


@admin.register(EquipmentCategory)
class EquipmentCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(DispatchRequest)
class DispatchRequestAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "company_name",
        "contact_person",
        "phone",
        "equipment_category",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "equipment_category",
        "created_at",
    )

    search_fields = (
        "company_name",
        "contact_person",
        "phone",
        "issue_description",
    )

    readonly_fields = ("created_at", "updated_at")

    ordering = ("-created_at",)
