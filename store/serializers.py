from django.contrib.auth.models import User
from rest_framework import serializers

from store.models import Product, Image


class ProductsSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_image_url(self, obj):
        print(obj.image_set.all())
        image = obj.image_set.first()
        if image:
            request = self.context.get("request")
            return request.build_absolute_uri(image.image.url)
        else:
            return None


class ProductItemSerializer(serializers.ModelSerializer):
    image_urls = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_image_urls(self, obj):
        a = []
        print(obj.image_set.all())
        image = obj.image_set.all()
        # for x in Product
        if image:
            request = self.context.get("request")
            a = request.build_absolute_uri(image.image.url).append(1)

        return a


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

# class ImageUrlSerializer(serializers.ModelSerializer):
#     image_url = serializers.SerializerMethodField('name')
#
#     class Meta:
#         model = Image
#         fields = ('field',
#                   'image',
#                   'name')
#
