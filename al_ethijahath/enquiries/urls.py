from django.urls import path
from .views import enquiry_submit,equipment_portfolio_list,equipment_category_list,blog_list

urlpatterns = [
    path('enquiry-sumbmit/',enquiry_submit ),
    path('equipment-portfolio/',equipment_portfolio_list),
    path("equipment-categories/",equipment_category_list),
    path("blogs/",blog_list),

]