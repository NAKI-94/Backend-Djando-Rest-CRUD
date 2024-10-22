from django.urls import include, path
from rest_framework import routers
from CRUD import views
from rest_framework.documentation import include_docs_urls


router =routers.DefaultRouter()
router.register(r'crud', views.CrudView,'crud')

urlpatterns =[
    path ("api/v1/", include(router.urls) ),
    path('docs/', include_docs_urls(title='Crud API'))

]