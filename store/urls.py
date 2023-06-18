# from rest_framework_nested import routers

# from app_store.views import AddressViewSet, CartItemViewSet, CartViewSet, CollectionViewSet, CustomerViewSet, OrderItemViewSet, OrderViewSet, ProductViewSet


# router = routers.DefaultRouter()
# # parent routers
# router.register('collections', CollectionViewSet, basename='collections')
# router.register('products', ProductViewSet, basename='products')
# router.register('customers', CustomerViewSet, basename='customers')
# router.register('orders', OrderViewSet, basename='orders')
# router.register('carts', CartViewSet, basename='carts')

# order_router = routers.NestedDefaultRouter(router, 'orders', lookup='order')
# cart_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
# customer_router = routers.NestedDefaultRouter(
#     router, 'customers', lookup='customer')
# # nested routers
# order_router.register('items', OrderItemViewSet, basename='order_items')
# cart_router.register('items', CartItemViewSet, basename='cart_items')
# customer_router.register('addresses', AddressViewSet, basename='addresses')


# urlpatterns = router.urls + order_router.urls + \
#     cart_router.urls + customer_router.urls
