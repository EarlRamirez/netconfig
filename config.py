#!/usr/bin/python

#################################################
#
# Do not modify the contents of this file
# Any settings that can be modified by the user
#  can be found in ./instance/settings.py
#
#################################################

import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False

WTF_CSRF_ENABLED = True

# Redis setup
# Redis is used for temporarily storing hashed user credentials
#  locally on the server.  These do not need to be changed
#  unless you want to access a remote Redis server
# -Using a remote Redis server is not tested nor currently supported
DB_HOST = 'localhost'
DB_PORT = 6379
DB_NO = 0

# Celery setup
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_TASK_SERIALIZER = 'json'

# Logging settings
# LOGFILE is currently not used
# SYSLOGFILE is the location where syslog type logs are stored,
#  for tracking and troubleshooting purposes
LOGFILE = os.path.join(basedir, 'app/log/access.log')
SYSLOGFILE = os.path.join(basedir, 'app/log/syslog.log')

# Settings file location
SETTINGSFILE = os.path.join(basedir, 'instance/settings.py')

# Bootstrap configuration
BOOTSTRAP_SERVE_LOCAL = True

# Global SSH new connection timeout
SSH_TIMEOUT = 10

# GitHub Master branch config file location
GH_MASTER_BRANCH_URL = 'https://raw.githubusercontent.com/v1tal3/netconfig/master/config.py'

# Current version
VERSION = '1.3.5 (beta)'
