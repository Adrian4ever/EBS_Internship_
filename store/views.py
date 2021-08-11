from rest_framework import status
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from store.models import Product, Image
from store.serializers import ProductsSerializer, ImageSerializer, ProductItemSerializer


class ImageViewSet(GenericAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = ImageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)
        file = request.data['name']
        serializer.save()
        return Response(serializer.data)


class ProductsListView(GenericAPIView):
    serializer_class = ProductsSerializer
    queryset = Product.objects.all()

    permission_classes = (AllowAny,)
    authentication_classes = ()

    def get(self, request):
        product = Product.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(product, request)
        serializer = ProductsSerializer(result_page, many=True, context={'request': request})
        response = Response(serializer.data, status=status.HTTP_200_OK)
        return response

    def post(self, request):
        serializer = ProductsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class ProductsItemView(GenericAPIView):
    serializer_class = ProductItemSerializer

    permission_classes = (AllowAny,)
    authentication_classes = ()

    def get(self, request, pk):
        product = get_object_or_404(Product.objects.filter(pk=pk))

        return Response(ProductItemSerializer(product, context={'request': request}).data)

    def delete(self, request, pk):
        product = get_object_or_404(Product.objects.filter(pk=pk))
        product.delete()

        return Response()

    def put(self, request, pk):
        product = get_object_or_404(Product.objects.filter(pk=pk))
        serializer = ProductItemSerializer(instance=product, data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
