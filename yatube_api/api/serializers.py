from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Post, Group, Follow, User


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Post
        fields = (
            'id', 'author', 'text',
            'pub_date', 'image', 'group',
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


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(
        read_only=True,
        slug_field='username',
    )
    following = SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = ('user', 'following')

    def validate_following(self, value):
        if value == self.context['request'].user:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя!'
            )
        if Follow.objects.filter(
            user=self.context['request'].user, following=value
        ).exists():
            raise serializers.ValidationError(
                'Вы уже подписаны на текущего пользователя!'
            )
        return value
