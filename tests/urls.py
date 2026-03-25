from django.urls import include, path

urlpatterns = [
    path('markdown/', include('django_markdown.urls')),
]
