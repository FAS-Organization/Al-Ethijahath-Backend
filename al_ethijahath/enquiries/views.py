from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import DispatchRequest
from .serializers import DispatchRequestSerializer


@api_view(["POST"])
def enquiry_submit(request):
    serializer = DispatchRequestSerializer(data=request.data)

    if serializer.is_valid():
        enquiry = serializer.save()

        return Response(
            {
                "message": "Enquiry submitted successfully.",
                "data": DispatchRequestSerializer(enquiry).data,
            },
            status=status.HTTP_201_CREATED,
        )

    return Response(
        {
            "message": "Invalid data.",
            "errors": serializer.errors,
        },
        status=status.HTTP_400_BAD_REQUEST,
    )