from django.urls import path
from . import views
from .views import SearchResultsView

urlpatterns = [
    path('list', views.list_ticket),
    path('<int:id>', views.ticket_detail, name='ticketdetail'),
    path('login', views.user_login),
    path('signup', views.register),
    path('logout', views.user_logout),
    path('search/', SearchResultsView.as_view(), name='search_results')
]
