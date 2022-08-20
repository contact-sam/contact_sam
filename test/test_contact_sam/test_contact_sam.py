#!/usr/bin/env python3

import sys
import unittest

sys.path.append('../src')
import contact_sam

class TestContactSam(unittest.TestCase):

    def test_name(self):
        """
        Tests my full name.
        
        :return: My full name 
        :rtype: str
        """
        self.assertEqual('Samuel Mehalko', contact_sam.name())

    def test_title(self):
        """
        Tests my title at the company that I am employeed.
        
        :return: My title
        :rtype: str
        """
        self.assertEqual('Embedded Software Engineer', contact_sam.title())
    
    def test_company(self):
        """
        Tests the name of the company that I am employeed.
        
        :return: My company
        :rtype: str
        """
        self.assertEqual('Northrop Grumman Corporation', contact_sam.company())
    
    def test_email(self):
        """
        Tests my office email address.
        
        :return: My email address 
        :rtype: str
        """
        self.assertEqual('samuel.mehalko@ngc.com', contact_sam.email())
    
    def test_phone(self):
        """
        Tests my office phone number.
        
        :return: My phone number 
        :rtype: str
        """
        self.assertEqual('(410)-993-6848', contact_sam.phone())
    
    def test_site(self):
        """
        Tests the url of the this package on the Python Package Index (pypi) website.
        
        :return: This package's pypi url
        :rtype: str
        """
        self.assertEqual('https://pypi.org/project/contact_sam', contact_sam.site())
    
    def test_source(self):
        """
        Tests the url of the this package's source github url.
        
        :return: This source code's github url.
        :rtype: str
        """
        self.assertEqual('https://github.com/contact-sam/contact_sam', contact_sam.source())

if __name__ == "__main__":
    unittest.main(verbosity=2)