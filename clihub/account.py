# -*- coding: utf-8 -*-
import os
import imp
from contextlib import contextmanager


class Account(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    @contextmanager
    def load_from_config(cls):
        config_file = cls.config_file()
        d = imp.new_module('config')
        d.__file__ = config_file
        try:
            execfile(config_file, d.__dict__)
            yield Account(d.username, d.password)
        except IOError, e:
            e.strerror = 'Unable to load configuration file (%s)' % e.strerror
            raise

    @classmethod
    def save_to_config(cls, username, password):
        try:
            with open(cls.config_file(), 'w') as fp:
                fp.write('username="{username}"\npassword="{password}"\n'.format(username=username, password=password))
        except IOError, e:
            e.strerror = 'Unable to save configuration file (%s)' % e.strerror
            raise

    @classmethod
    def remove_config(cls):
        try:
            os.unlink(cls.config_file())
        except OSError:
            pass

    @classmethod
    def config_file(cls):
        return os.path.join(os.environ['HOME'], '.clihub')
