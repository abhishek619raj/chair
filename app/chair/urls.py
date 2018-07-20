from app.chair import views
from app.chair.views import ChairTypeView
from django.conf.urls import include, url






urlpatterns = [
	url(r'',views.ChairView.as_view()),
	url(r'^(?P<chair_id>[0-9]+)$',views.ChairView.as_view()),
	# (?# url(r'^(?P<chairtype_id>[0-9]+)$',views.ChairTypeView.as_view()),)
	# url(r'chairtype/',views.ChairTypeView.as_view()),
    # (?# url(r'^$', views.ChairTypeView.as_view()), ## OK)
]