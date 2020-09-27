from .models import Post, Comment
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for DB model 'Comment'
    Takes all fields except 'post_pk'
    """

    class Meta:
        model = Comment
        fields = ["pk", "author_name", "creation_date", "content"]


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for DB model 'Post'
    Takes all fields and ads two additional:
    - url - absolute url for each instance of 'Post'
    - comments - serialized instances of 'Comment' that are related to
        instance of 'Post' (ForeignKey)
    """

    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = [
            "url",
            "pk",
            "title",
            "creation_date",
            "amount_of_upvotes",
            "author_name",
            "comments",
        ]
