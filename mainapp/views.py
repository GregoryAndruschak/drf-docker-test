from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action


class PostViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve',
    'update' and 'destroy' actions for DB model 'Post'.

    Additionally also provide an extra 'upvote' action.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=True, methods=["POST"])
    def upvote(self, request, *args, **kwargs):
        """Add 1 to amount_of_upvotes of an instance of DB model 'Post'"""
        post = self.get_object()
        post.amount_of_upvotes += 1
        post.save()
        return Response(status=status.HTTP_202_ACCEPTED)


class CommentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve',
    'update' and 'destroy' actions for DB model 'Comment'.

    Added 'perform_create' function which overrides 'create'
    """

    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(post_pk=self.kwargs["post_pk"])

    def perform_create(self, serializer):
        """
        Create new instance of 'Comment' in DB with 'post_pk' as ForeignKey
        """
        serializer.save(
            post_pk=Post.objects.get(pk=int(self.kwargs["post_pk"]))
        )
