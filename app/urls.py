from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from employee.views import EmployeeViews, home, new_Employee

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/', include('employee.urls')),
    path('', home, name='home'),
    path('new_employee', new_Employee, name='new_employee'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
