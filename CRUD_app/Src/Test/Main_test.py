__author__ = 'rkourav'

import unittest


class BlogProfilesTests(unittest.TestCase):

    def test_creation_profile(self):
        profile = {'username': "Ruby", 'name': "Rossum", 'email': "rossum@python.com"}
        self.assertEqual(type(profile['username']), str)

    def test_update_profile(self):
        profile1 = {'username': "Pyron", 'email': "python@guido.com"}
        self.assertIsNone(profile1.get('email'))

    def test_creation_blog(self):
        blog = {'username': "Ruber", 'text': "this is my new blog"}
        self.assertEqual(type(blog['text']), str)

    def test_update_blog(self):
        blog1 = {'text': "My next blog will be awesome"}
        self.assertIsNone(blog1.get('text'))
