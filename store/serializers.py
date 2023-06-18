from rest_framework import serializers

from store.models import (
    Address,
    Cart,
    CartItem,
    Collection,
    Customer,
    Order,
    OrderItem,
    Product,
)


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ["id", "title"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "description",
            "price",
            "inventory",
            "last_update",
            "collection",
        ]


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["id", "phone", "birth_date", "membership", "user"]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id", "placed_at", "payment_status", "customer"]


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ["id", "quantity", "unit_price", "order", "product"]


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ["id", "street", "city", "customer"]


class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "title", "price"]


class CartItemSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer()
    total_price = serializers.SerializerMethodField(method_name="item_total_price")

    def item_total_price(self, item):
        return item.quantity * item.product.price

    class Meta:
        model = CartItem
        fields = ["id", "quantity", "product", "total_price"]


class CartSerializer(serializers.ModelSerializer):
    cart_total_price = serializers.SerializerMethodField(method_name="get_total_price")
    id = serializers.UUIDField(read_only=True)
    items = CartItemSerializer(many=True, read_only=True)

    def get_total_price(self, cart):
        return sum([item.quantity * item.product.price for item in cart.items.all()])

    class Meta:
        model = Cart
        fields = ["id", "items", "cart_total_price"]
