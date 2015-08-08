from django.conf.urls import patterns, include, url

urlpatterns = patterns('tictactoe.views',
    url(r'^invite$', 'new_invitation', name='tictactoe_invite')
)
