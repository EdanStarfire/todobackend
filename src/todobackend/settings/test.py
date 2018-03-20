from base import *
import os

# Installed Apps
INSTALLED_APPS += ('django_nose', )
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
TEST_OUTPUT_DIR = os.environ.get('TEST_OUTPUT_DIR', '.')
NOSE_ARGS = [
    '--verbosity=2',                                        # Verbose output
    '--nologcapture',                                       # don't output log capture
    '--with-coverage',                                      # Activate coverage report
    '--cover-package=todo',                                 # Coverage report will apply to these packages
    '--with-spec',                                          # Spec style tests
    '--spec-color',
    '--with-xunit',                                         # Enable xunit plugin
    '--xunit-file=%s/unittests.xml' % TEST_OUTPUT_DIR,
    '--cover-xml',                                          # Produce XML coverage info
    '--cover-xml-file=%s/coverage.xml' % TEST_OUTPUT_DIR,
]

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('MYSQL_DATABASE', 'todobackend'),
        'USER': os.environ.get('MYSQL_USER', 'todo'),
        'PASSWORD': os.environ.get('MYSQL_PASSWORD', 'Tr2d3dee0.'),
        'HOST': os.environ.get('MYSQL_HOST', 'localhost'),
        'PORT': os.environ.get('MYSQL_PORT', '3306'),
    }
}