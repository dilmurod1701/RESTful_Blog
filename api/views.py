from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import BasicAuthentication
from rest_framework.throttling import UserRateThrottle
from .models import Blog
from .serializers import BlogSerializer, ForListView
from .permissions import IsOwner

# Create your views here.


class TenReqThrottle(UserRateThrottle):
    rate = '10/min'


class ThreeReqThrottle(UserRateThrottle):
    rate = '3/min'


class Blogs(ListAPIView):
    throttle_classes = [TenReqThrottle]
    queryset = Blog.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ForListView
    authentication_classes = [BasicAuthentication]


class DetailBlog(RetrieveAPIView):
    throttle_classes = [TenReqThrottle]
    permission_classes = [IsAuthenticated]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = [BasicAuthentication]
    lookup_field = "id"


class CreateBlog(CreateAPIView):
    throttle_classes = [ThreeReqThrottle]
    permission_classes = [IsOwner, IsAuthenticated]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = [BasicAuthentication]


class UpdateBlog(UpdateAPIView):
    throttle_classes = [ThreeReqThrottle]
    permission_classes = [IsOwner, IsAuthenticated]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = "id"
    authentication_classes = [BasicAuthentication]


class DeleteBlog(DestroyAPIView):
    throttle_classes = [ThreeReqThrottle]
    permission_classes = [IsOwner, IsAuthenticated]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = "id"
    authentication_classes = [BasicAuthentication]


class UserDetail(ListAPIView):
    throttle_classes = [TenReqThrottle]
    permission_classes = [IsAuthenticated]
    queryset = Blog
    serializer_class = BlogSerializer
    authentication_classes = [BasicAuthentication]

    def get_queryset(self):
        user = self.request.user
        return Blog.objects.filter(user=user)


class SortByName(ListAPIView):
    queryset = Blog
    serializer_class = BlogSerializer
    throttle_classes = [TenReqThrottle]
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]

    def filter_queryset(self, queryset):
        queryset = super(SortByName, self).filter_queryset(queryset)
        return queryset.objects.order_by('title')
