from django.urls import path


from . import views


urlpatterns = [
    path('talk/', views.talk_view, name='talk'),
    path('train/', views.train_data_view, name='talk')
]
