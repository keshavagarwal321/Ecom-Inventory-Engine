from rest_framework import serializers
from django.db import transaction
from .models import Order, OrderItem
from products.models import Product

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'price_at_purchase']

class OrderSerilaizer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    
    class Meta:
        model = Order
        fields = ['id', 'user', 'total_amount', 'status', 'created_at', 'items']
        read_only_fields = ['user', 'status']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        with transaction.atomic():
            order = Order.objects.create(**validated_data)
            for item_data in items_data:
                product = item_data['product']
                quantity_requested = item_data['quantity']
                if product.stock_quantity < quantity_requested:
                    raise serializers.ValidationError({
                        "error": f"Insufficient stock for {product.name}. Only {product.stock_quantity} left."
                    })
                
                product.stock_quantity -= quantity_requested
                product.save()

                OrderItem.objects.create(order=order, **item_data)

        return order