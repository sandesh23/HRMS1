from rest_framework.routers import SimpleRouter

from .views import *

router = SimpleRouter()

router.register('basicinfo', ModelViewSet)
router.register('department', DepartmentViewSet)
router.register('role', RoleViewSet)
router.register('degree', DegreeViewSet)
router.register('state', StateViewSet)
router.register('designation', DesignationViewSet)
router.register('location', LocationViewSet)
router.register('sourceofhire', SourceOfHireViewSet)
router.register('employeetype', EmployeeTypeViewSet)
router.register('jobtitle', JobTitleViewSet)
router.register('country', CountryViewSet)

urlpatterns = router.urls