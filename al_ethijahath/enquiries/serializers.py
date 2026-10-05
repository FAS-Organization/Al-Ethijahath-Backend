from rest_framework import serializers
from .models import DispatchRequest


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