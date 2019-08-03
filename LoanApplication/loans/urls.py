from django.conf.urls import include,url
from . import views

app_name='loans'

urlpatterns = [
        url(r'^loanapp/?$', views.CreateLoanApplicationView.as_view(), name='createapp'),
        url(r'^status/?$', views.StatusLoanApplicationView.as_view(),name='status'),
]
