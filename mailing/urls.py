from django.urls import path
from mailing.views import MailingCreateView, MailingUpdateView, MailingDestroyView, MailingDetailStatisticsView, \
    MailingStatisticsView

urlpatterns = [
    path('create/', MailingCreateView.as_view(), name='create-mailing'),
    path('<int:pk>/update/', MailingUpdateView.as_view(), name='update-mailing-information'),
    path('<int:pk>/delete/', MailingDestroyView.as_view(), name='delete-mailing'),
    path('statistics/', MailingStatisticsView.as_view(), name='mailing-statistics'),
    path('<int:pk>/detail-statistics/', MailingDetailStatisticsView.as_view(), name='mailing-detail-statistics'),
]