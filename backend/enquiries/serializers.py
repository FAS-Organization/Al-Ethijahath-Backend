from rest_framework import serializers
from .models import DispatchRequest,EquipmentPortfolio,EquipmentCategory,Blog


class EquipmentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentCategory
        fields = [
            "id",
            "name",
        ]

    
class DispatchRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = DispatchRequest
        fields = [
            "id",
            "company_name",
            "contact_person",
            "phone",
            "equipment_category",
            "issue_description",
            "photo",
            "status",
            "created_at",
        ]
        read_only_fields = [
            "id",
            "status",
            "created_at",
        ]

    def validate_phone(self, value):
        if not value.isdigit():
            raise serializers.ValidationError(
                "Phone number must contain numbers only."
            )

        return value

    def validate_photo(self, value):
        if value is None:
            return value

        max_size = 10 * 1024 * 1024

        if value.size > max_size:
            raise serializers.ValidationError(
                "Photo size must be 10 MB or less."
            )

        return value

class EquipmentPortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentPortfolio
        fields = [
            "id",
            "title",
            "portfolio_image",
            "description",
        ]
        read_only_fields = ["id"]


class BlogSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(
        format="%d %B %Y, %I:%M %p"
    )

    class Meta:
        model = Blog
        fields = [
            "id",
            "name",
            "designation",
            "title",
            "description",
            "is_active",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]