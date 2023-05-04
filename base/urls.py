from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns=[
    path('', views.endpoints,name='endpoints'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('advocates/',views.advocates_list,name='advocates'),
    # path('advocates/<str:username>/',views.advocates_details,name='advocates_details'),
    path('advocates/<str:username>/',views.AdvocateDetail.as_view()),

    path('company/',views.company_list,name='company')

     
]