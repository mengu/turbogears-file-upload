# -*- coding: utf-8 -*-
"""
Functional test suite for the root controller.

This is an example of how functional tests can be written for controllers.

As opposed to a unit-test, which test a small unit of functionality,
functional tests exercise the whole application and its WSGI stack.

Please read http://pythonpaste.org/webtest/ for more information.

"""
from nose.tools import assert_true

from fileupload.tests import TestController


class TestRootController(TestController):
    def test_index(self):
        response = self.app.get('/')
        msg = 'TurboGears 2 is rapid web application development toolkit '\
              'designed to make your life easier.'
        # You can look for specific strings:
        assert_true(msg in response)
        
        # You can also access a BeautifulSoup'ed response in your tests
        # (First run $ easy_install BeautifulSoup 
        # and then uncomment the next two lines)  
        
        #links = response.html.findAll('a')
        #print links
        #assert_true(links, "Mummy, there are no links here!")
