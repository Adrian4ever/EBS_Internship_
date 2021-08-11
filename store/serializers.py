from rest_framework import serializers

from store.models import Product, Image


class ProductsSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_image_url(self, obj):
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
        urls_list = []
        images = obj.image_set.all()
        request = self.context.get("request")
        for image in images:
            urls_list.append(request.build_absolute_uri(image.image.url))

        return urls_list


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
