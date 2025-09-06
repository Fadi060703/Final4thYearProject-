from rest_framework import serializers 
from ...models import ProductStock, Product

class ShipmentSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(write_only=True)
    
    class Meta:
        model = ProductStock 
        fields = ['product_name', 'stock']
         
    def create(self, validated_data):
        product_name = validated_data.pop('product_name')
        stock_to_add = int(validated_data.pop('stock'))
        
        # First get the Product instance
        try:
            product = Product.objects.get(name=product_name)
        except Product.DoesNotExist:
            raise serializers.ValidationError(f"Product with name '{product_name}' does not exist")
        
        # Then handle ProductStock
        product_stock, created = ProductStock.objects.get_or_create(
            product=product,
            defaults={'stock': stock_to_add}
        )
        
        if not created:
            product_stock.stock += stock_to_add
            product_stock.save()
        
        return product_stock