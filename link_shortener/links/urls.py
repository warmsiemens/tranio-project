from django.urls import path
from . import views

urlpatterns = [
    path('', views.AddLinkView.as_view(), name='add_link'),
    path('<str:shortened_link>', views.RedirectLinkView.as_view(), name='redirect_link'),
    path('stats/', views.StatsView.as_view(), name='stats'),
]
