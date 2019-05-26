from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'priorities', views.PriorityViewSet)
router.register(r'department', views.DepartmentViewSet, basename='department')
router.register(r'nationality', views.NationalityViewSet, basename='nationality')
router.register(r'religion', views.ReligionViewSet, basename='religion')
router.register(r'jobtype', views.JobTypeViewSet,basename='jobtype')
router.register(r'employmentterms', views.EmploymentTermsViewSet, basename='employmentterms')
router.register(r'requesttype', views.RequestTypeViewSet, basename='requesttype')
router.register(r'casestatus', views.CaseStatusViewSet, basename='casestatus')
router.register(r'jobposition', views.JobPositionViewSet, basename='jobposition')
# router.register(r'jobgroup', views.JobGroupViewSet,basename='jobgroup')
# router.register(r'probationtypes', views.ProbationTypeViewSet, basename='probationtypes')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls))
]