from django.shortcuts import get_object_or_404
from rest_framework import filters, permissions, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.exceptions import ValidationError, NotAuthenticated, MethodNotAllowed

from posts.models import Post, Group, Comment, Follow
from .permissions import IsAuthorOrReadOnly, ReadOnly
from .serializers import (
    PostSerializer, GroupSerializer, CommentSerializer, FollowSerializer
)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]
    pagination_class = LimitOffsetPagination


    def perform_create(self, serializer):
        if not self.request.user.is_authenticated:
            raise NotAuthenticated(
                'Для создания поста необходима авторизация!'
            )
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthorOrReadOnly]


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]


    def get_post(self):
        return get_object_or_404(Post, id=self.kwargs.get('post_id'))

    def get_queryset(self):
        return Comment.objects.filter(post=self.get_post())

    def perform_create(self, serializer):
        if not self.request.user.is_authenticated:
            raise NotAuthenticated(
                'Для создания комментария необходима авторизация!'
            )
        serializer.save(author=self.request.user, post=self.get_post())


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        queryset = Follow.objects.filter(user=self.request.user)
        return self.filter_queryset(queryset)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def get_permissions(self):
        if self.request.method not in ['GET', 'POST']:
            raise MethodNotAllowed(self.request.method)
        return super().get_permissions()
