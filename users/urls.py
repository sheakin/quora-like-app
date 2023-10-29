from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("profile/<slug:slug>", views.ProfileDetailView.as_view(), name="profile"),
    path(
        "profile/<slug:slug>/questions",
        views.ProfileQuestionListView.as_view(),
        name="profile_questions",
    ),
    path(
        "profile/<slug:slug>/answers",
        views.ProfileAnswerListView.as_view(),
        name="profile_answers",
    ),
    path(
        "profile/<slug:slug>/answers/<str:is_pin>/<int:answer_pk>",
        views.profile_answer_pin,
        name="is_pin_answer",
    ),
    path("edit/", views.ProfileUpdateView.as_view(), name="edit"),
    path("add/workplace/", views.WorkPlaceFormAddView.as_view(), name="workplace_add"),
    path("edit/workplace/", views.WorkPlaceUpdateView.as_view(), name="workplace_edit"),
    path("delete/workplace/", views.delete_workplace, name="workplace_delete"),
    path("add/education/", views.EducationFormAddView.as_view(), name="education_add"),
    path("edit/education/", views.EducationUpdateView.as_view(), name="education_edit"),
    path("delete/education/", views.delete_education, name="education_delete",),
    path("logout/", views.logout_request, name="logout"),
    path("register/", views.UserRegisterView.as_view(), name="register"),
]
