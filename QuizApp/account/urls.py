from django.urls import path
from .import views
from .views import (
    QuizListView,
    quiz_view,
    quiz_data_view,
    save_quiz_view
)

app_name = 'account'

urlpatterns = [
    path('', QuizListView.as_view(), name='main-view'),
    path('<int:myid>/', quiz_view, name='quiz-view'),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path('<pk>/data/',quiz_data_view, name = 'quiz_data_view'),
    path('<pk>/save/',save_quiz_view, name = 'save_view'),
    path("about/",views.about, name="about"),
    path('result/',views.result, name = "result")
]