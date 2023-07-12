from django.urls import path
from .views import UserSignupView, UserLoginView
from django.urls import path
from .views import BookListView, BookCreateView
from .views import BookUpdateDeleteView
urlpatterns = [
    path('signup/', UserSignupView.as_view()),
    path('login/', UserLoginView.as_view()),
    path('books_list/', BookListView.as_view()),
    path('books_create/', BookCreateView.as_view()),
    path('books/<int:pk>/', BookUpdateDeleteView.as_view()),
]

