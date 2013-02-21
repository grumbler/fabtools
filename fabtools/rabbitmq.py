from fabric.api import settings, sudo, hide


def vhost_exists(vhost_name):
    with settings(hide('running', 'stdout', 'stderr'), warn_only=True):
        return sudo('rabbitmqctl list_vhosts | grep -c {0}'.format(vhost_name)) >= '1'


def user_exists(username):
    with settings(hide('running', 'stdout', 'stderr'), warn_only=True):
        return sudo('rabbitmqctl list_users | grep -c {0}'.format(username)) >= '1'


def create_vhost(vhost_name):
    with settings(hide('running', 'stdout')):
        sudo('rabbitmqctl add_vhost {vhost}'.format(vhost=vhost_name))


def create_user(username, password):
    with settings(hide('running', 'stdout')):
        sudo('rabbitmqctl add_user {username} {password}'.format(username=username, password=password))


def set_permissions(vhost, user):
    with settings(hide('running', 'stdout')):
        sudo('rabbitmqctl set_permissions -p {vhost} {user} ".*" ".*" ".*"'.format(vhost=vhost, user=user))
