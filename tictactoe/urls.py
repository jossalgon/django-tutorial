from django.conf.urls import url
from tictactoe import views


urlpatterns = [
    url(r'^invite$', views.new_invitation, name='tictactoe_invite'),
]
