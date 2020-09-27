"""
ViewSets provide all basic CRUD functionality,
plus we can use Router for automatic URL routing
API guide:
https://www.django-rest-framework.org/api-guide/routers/#defaultrouter
"""
from .views import PostViewSet, CommentViewSet
from django.urls import include
from django.conf.urls import url
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register(r"post", PostViewSet)

comments_router = routers.NestedDefaultRouter(router, r"post", lookup="post")
comments_router.register(r"comment", CommentViewSet, basename="Comment")

urlpatterns = [
    url(r"^", include(router.urls)),
    url(r"^", include(comments_router.urls)),
]
