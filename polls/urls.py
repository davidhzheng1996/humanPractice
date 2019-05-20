from django.urls import path

from . import views, viewsets

urlpatterns = [
    path('', views.index, name='index'),
    path('results', views.results),
    path('results/<int:resultid>',views.text),
    path('show_results/<int:resultid>',views.words),
    path('api/file_import/',viewsets.processText),
    path('api/disable_stop/',viewsets.disableStopWords),
    path('api/save_result/',viewsets.saveWords),
    path('api/get_results/',viewsets.getResults),
    path('api/get_text/<int:resultid>',viewsets.getText),
    path('api/get_words/<int:resultid>',viewsets.getWords),
]