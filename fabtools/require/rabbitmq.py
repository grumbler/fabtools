from fabtools.rabbitmq import *


def vhost(vhost_name):
    if not vhost_exists(vhost_name):
        create_vhost(vhost_name)


def user(username, password):
    if not user_exists(username):
        create_user(username, password)


def vhost_user(vhost_name, username, password):
    if not user_exists(username):
        create_user(username, password)
    if not vhost_exists(vhost_name):
        create_vhost(vhost_name)
    set_permissions(vhost_name, username)
