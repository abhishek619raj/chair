from app.parts import views
# from app.chair.views import ChairTypeView
from django.conf.urls import include, url

urlpatterns = [
	url(r'^part/(?P<part_id>[0-9]+)$',views.PartView.as_view()),
	url(r'part/$',views.PartView.as_view()),
	url(r'^parttype/(?P<parttype_id>[0-9]+)$',views.PartTypeView.as_view()),
	url(r'parttype/',views.PartTypeView.as_view()),
]