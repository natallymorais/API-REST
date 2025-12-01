from django.contrib import admin 
from django.urls import path, include 
from rest_framework.routers import DefaultRouter 
from rest_framework.authtoken.views import obtain_auth_token
from tarefas.views import ProjetoViewSet, TarefaViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

router = DefaultRouter()

router.register(r'projetos', ProjetoViewSet) 

router.register(r'tarefas', TarefaViewSet)     

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'), # Adicionado para o drf-spectacular
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'), # Adicionado para o drfspectacular
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'), # Adicionado para o drf-spectacular
]