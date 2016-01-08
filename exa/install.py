# -*- coding: utf-8 -*-
'''
Initialization
====================================
This module is run after successfully installing this package using
setup.py. It is responsible for setting up a new location at which
to store files generated by exa as well as setting up some the
configuration to third-party features (e.g. databases).
'''
from exa.tools import install_widget_javascript


def initialize():
    '''
    '''
    install_widget_javascript()