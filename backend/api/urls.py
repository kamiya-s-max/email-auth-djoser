from django.urls import path, include
from rest_framework import routers
from .views import CreateUserView

# modelviewsetを継承した場合はrouterで登録
router = routers.DefaultRouter()

# genericsを継承したviewsを使った場合はurlpatternsに書く
urlpatterns = [
    # djoserで提供する認証メール送信はこのurlじゃないはず
    path('create/', CreateUserView.as_view(), name='create'),
]