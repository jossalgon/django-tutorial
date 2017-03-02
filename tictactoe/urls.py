from django.conf.urls import url
from tictactoe import views


urlpatterns = [
    url(r'^invite$', views.new_invitation, name='tictactoe_invite'),
    url(r'^invitation/(?P<pk>\d+)/$', views.accept_invitation, name='tictactoe_accept_invitation'),
    url(r'^game/(?P<pk>\d+)/$', views.game_detail, name='tictactoe_game_detail'),
]
