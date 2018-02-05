from unittest import TestCase

import glhtmlcomb


class TestJoke(TestCase):
    def test_is_string(self):
        s = glhtmlcomb.joke()
        self.assertTrue(isinstance(s, str))
