from .views import ContactList, ContactDetailView
from django.urls import path, include

urlpatterns = [
    path('', ContactList.as_view()),
    path('<int:id>',ContactDetailView.as_view())
]
