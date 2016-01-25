import configparser
import os
from redmine import Redmine


def redmine():
    rootdir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    config_path = os.path.join(rootdir, 'settings.conf')
    config = configparser.ConfigParser()
    config.read(config_path)
    host = config.get('RedmineServer', 'host')
    username = config.get('RedmineServer', 'username')
    password = config.get('RedmineServer', 'password')
    redmine = Redmine(host, username=username, password=password)
    return redmine