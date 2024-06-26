from django.urls import include, path

from .api import views as ipam_api_views
from .api.urls import get_api_urls


def get_urls(api_views):
    """
    returns:: all the urls of the immunity-ipam module
    arguements::
        api_views: location for getting API views
    """
    return [
        path(
            'api/v1/ipam/', include((get_api_urls(api_views), 'ipam'), namespace='ipam')
        ),
        path('accounts/', include('immunity_users.accounts.urls')),
    ]


urlpatterns = [path('', include(get_urls(ipam_api_views)))]
