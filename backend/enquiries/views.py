from rest_framework.decorators import api_view, throttle_classes
from rest_framework.throttling import AnonRateThrottle
from rest_framework.response import Response
from rest_framework import status

from .models import DispatchRequest,EquipmentPortfolio,EquipmentCategory,Blog
from .serializers import DispatchRequestSerializer,EquipmentPortfolioSerializer,EquipmentCategorySerializer,BlogSerializer

class DispatchRequestThrottle(AnonRateThrottle):
    rate = "10/hour"

@api_view(["POST"])
@throttle_classes([DispatchRequestThrottle])
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


@api_view(["GET"])
def equipment_category_list(request):
    categories = EquipmentCategory.objects.filter(
        is_active=True
    )

    serializer = EquipmentCategorySerializer(
        categories,
        many=True
    )

    return Response(serializer.data)

@api_view(["GET"])
def equipment_portfolio_list(request):
    portfolios = EquipmentPortfolio.objects.filter(
        is_active=True
    ).order_by("id")

    serializer = EquipmentPortfolioSerializer(portfolios, many=True)

    return Response(serializer.data)


@api_view(["GET"])
def blog_list(request):
    blogs = Blog.objects.filter(
        is_active=True
    ).order_by("-created_at")[:6]

    serializer = BlogSerializer(
        blogs,
        many=True
    )

    return Response(serializer.data)

    
