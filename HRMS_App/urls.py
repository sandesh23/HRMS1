from rest_framework.routers import SimpleRouter

from .views import *

router = SimpleRouter()

router.register('basicinfo', EmpInfoViewSet)
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
router.register('personaldetails', PersonalDetailsViewSet)
router.register('workexperience', WorkExperienceViewSet)
router.register('education', EducationViewSet)
router.register('workdetail', WorkDetailViewSet)
router.register('summary', SummaryViewSet)
router.register('dependant', DependantViewSet)


urlpatterns = router.urls
