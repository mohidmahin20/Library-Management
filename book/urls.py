from django.urls import path
from .import views

urlpatterns = [
    path('details/<int:id>', views.DetailsPostView.as_view(), name='details_post'),
    path('purchase/<int:id>/', views.BorrowBookView.as_view(), name='borrow_book'),
]