from app.order import views
from app.chair.views import ChairTypeView
from django.conf.urls import include, url

urlpatterns = [
	url(r'^order/(?P<order_id>[0-9]+)$',views.OrderView.as_view()),
	url(r'order/',views.OrderView.as_view()),
]