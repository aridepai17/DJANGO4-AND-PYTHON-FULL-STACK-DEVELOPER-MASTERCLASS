from django.urls import path
from .views import Homeview, ThankYouView, ContactFormView, TeacherCreateView, TeacherListView, TeacherDetailView, TeacherUpdateView, TeacherDeleteView

appname = 'classroom'

urlpatterns = [
    path('', Homeview.as_view() ,name='home'),
    path('thankyou/', ThankYouView.as_view() ,name='thankyou'),
    path('contact/', ContactFormView.as_view() ,name='contact'),
    path('createteacher/', TeacherCreateView.as_view() ,name='createteacher'),
    path('teacherlist/', TeacherListView.as_view() ,name='teacherlist'),
    path('teacherdetail/<int:pk>/', TeacherDetailView.as_view() ,name='teacherdetail'),
    path('teacherupdate/<int:pk>/', TeacherUpdateView.as_view() ,name='teacherupdate'),
    path('teacherdelete/<int:pk>/', TeacherDeleteView.as_view())
]