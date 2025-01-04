from rest_framework import serializers
from rest_framework.relations import SlugRelatedField, StringRelatedField


from posts.models import Comment, Post, Group


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    group = StringRelatedField(
        read_only=True,
        required=False,
    )

    class Meta:
        model = Post
        fields = (
            'id', 'text', 'author', 'image',
            'group', 'pub_date', 'comments'
        )


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = (
            'id', 'title', 'slug', 'description',
        )


class CommentSerializer(serializers.ModelSerializer):
    post = SlugRelatedField(
        slug_field='id',
        read_only=True,
    )
    author = SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    class Meta:
        model = Comment
        fields = (
            'id', 'author', 'post', 'text', 'created',
        )
