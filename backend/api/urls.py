from django.urls import path, include
from rest_framework import routers


# modelviewsetを継承した場合はrouterで登録
router = routers.DefaultRouter()

# genericsを継承したviewsを使った場合はurlpatternsに書く
urlpatterns = [

]