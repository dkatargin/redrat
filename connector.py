import configparser
from redmine import Redmine


def redmine():
    config_path = 'settings.conf'
    config = configparser.ConfigParser()
    config.read(config_path)
    host = config.get('RedmineServer', 'host')
    username = config.get('RedmineServer', 'username')
    password = config.get('RedmineServer', 'password')
    redmine = Redmine(host, username=username, password=password)
    return redmine