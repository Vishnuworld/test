from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import BookOperations, Extra_api_root

# router = SimpleRouter(trailing_slash=False)
router = DefaultRouter()

router.register(r'books', BookOperations, basename='Books')


# router.register(r'extras', Extra_api_root, basename='extra')  # Created for seeing one more api root.

urlpatterns = router.urls



print('--------------urls---------------------')

# for i in urlpatterns:
#     print(i)

print('-----------------------------------')

#-----------------Simple Router()--------------------------#

# <URLPattern '^books$' [name='Books-list']>
# <URLPattern '^books/(?P<pk>[^/.]+)$' [name='Books-detail']>
# <URLPattern '^books/(?P<pk>[^/.]+)/extra_action_url$' [name='Books-extra_action_url']>

#-----------------Default Router()-------------------------#

# <URLPattern '^books/$' [name='Books-list']>
# <URLPattern '^books\.(?P<format>[a-z0-9]+)/?$' [name='Books-list']>   eg. http://127.0.0.1:8000/v1/books/?format=json
# <URLPattern '^books/(?P<pk>[^/.]+)/$' [name='Books-detail']>
# <URLPattern '^books/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$' [name='Books-detail']>  eg. http://127.0.0.1:8000/v1/books/4/?format=api
# <URLPattern '^books/(?P<pk>[^/.]+)/extra_action_url/$' [name='Books-extra_action_url']>
# <URLPattern '^books/(?P<pk>[^/.]+)/extra_action_url\.(?P<format>[a-z0-9]+)/?$' [name='Books-extra_action_url']>
# <URLPattern '^$' [name='api-root']>
# <URLPattern '^\.(?P<format>[a-z0-9]+)/?$' [name='api-root']>


# In Developing an application, we'll write our required API's. To Document these API's we use Django Rest Swagger.
# Django Rest Swagger is used to provide Documentation for all API's which are used in your application with brief description
#about each API individually.
# It is Open Source so you can contribute to the project.
# If your API's available to the users with description, so UI developers can understand and test your API's and use it accordingly.


#-------Custome Router----------#
# https://www.django-rest-framework.org/api-guide/routers/#custom-routers


from rest_framework.routers import Route, DynamicRoute, SimpleRouter

class CustomReadOnlyRouter(SimpleRouter):
    """
    A router for read-only APIs, which doesn't use trailing slashes.
    """
    routes = [
        Route(
            url=r'^{prefix}$',
            mapping={'get': 'list'},
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': 'List'}
        ),
        Route(
            url=r'^{prefix}/{lookup}$',
            mapping={'get': 'retrieve'},
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'Detail'}
        ),
        DynamicRoute(
            url=r'^{prefix}/{lookup}/{url_path}$',
            name='{basename}-{url_name}',
            detail=True,
            initkwargs={}
        )
    ]

