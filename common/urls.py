from django.urls import path

from common.views import landing_page, original_page

urlpatterns = [
    path('', original_page),
    path('not_original', landing_page)
]