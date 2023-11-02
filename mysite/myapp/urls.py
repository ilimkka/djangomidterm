from django.urls import path

from . import views

app_name = "myapp"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("add_question/", views.add_question, name='add_question'),
    path("<int:question_id>/delete_question/", views.delete_question, name='delete_question'),
    path("<int:question_id>/update_question/", views.update_question, name='update_question'),
    path('<int:question_id>/add_answer/', views.add_answer, name='add_answer'),

]