from rest_framework import serializers 
from ...models import ProductStock 

class StockSerializerMain(serializers.ModelSerializer):
    product_id = serializers.SerializerMethodField()
    product_name = serializers.SerializerMethodField()
    product_manufacturing_lab = serializers.SerializerMethodField()
    product_code = serializers.SerializerMethodField()
    
    class Meta:
        model = ProductStock
        fields = [ 'product_id', 'product_name', 'product_manufacturing_lab', 'product_code', 'stock']
    
    def get_product_id(self, obj):
        return obj.product.id
    
    def get_product_name(self, obj):
        return obj.product.name
    
    def get_product_manufacturing_lab(self, obj):
        return obj.product.manufacturing_lab.name
    
    def get_product_code(self, obj):
        return obj.product.code