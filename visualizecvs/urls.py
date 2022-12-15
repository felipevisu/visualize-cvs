from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .graphql.views import GraphQLView

urlpatterns = [
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True)), name="api"),
    path("", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Currículos Visualize'
admin.site.index_title = 'Gerenciador'