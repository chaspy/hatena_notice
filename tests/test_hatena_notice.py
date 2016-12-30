# -*- coding: utf-8 -*-
import unittest
import hatena_notice
import datetime

class TestHatenaNotice(unittest.TestCase):

    def test_get_reserve_return_empty(self):
        reserve = [["test blog","2015-1-1T12:00:00+09:00"]]
        self.assertEqual(hatena_notice.get_reserve(reserve),[])

    def test_get_reserve(self):
        reserve = [["test blog","2035-1-1T12:00:00+09:00"]]
        self.assertEqual(hatena_notice.get_reserve(reserve),[['test blog', datetime.datetime(2035, 1, 1, 12, 0)]])
    
    def test_get_reserve_filter(self):
        reserve = [["test blog","2035-1-1T12:00:00+09:00"],["test blog","2015-1-1T12:00:00+09:00"]]
        self.assertEqual(hatena_notice.get_reserve(reserve),[['test blog', datetime.datetime(2035, 1, 1, 12, 0)]])

    def test_tweet_extract(self):
        reserve = [["test blog",datetime.datetime(2035, 1, 1, 12, 0)]]
        self.assertEqual(hatena_notice.tweet_extract(reserve),'update notice:01/01:test blog')
        
    def test_tweet_extract_length_over(self):
        reserve = [["test blog",datetime.datetime(2035, 1, 1, 12, 0)],["test bloggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg",datetime.datetime(2035, 1, 1, 12, 0)]]
        self.assertEqual(hatena_notice.tweet_extract(reserve),'update notice:01/01:test blog')



