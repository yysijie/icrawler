# -*- coding: utf-8 -*-

import logging
import sys
from datetime import date
from icrawler.examples import GoogleImageCrawler
from icrawler.examples import BingImageCrawler
from icrawler.examples import BaiduImageCrawler
from icrawler.examples import FlickrImageCrawler
from icrawler.examples import GreedyImageCrawler


def test_google():
    google_crawler = GoogleImageCrawler('images/google', log_level=logging.INFO)
    google_crawler.crawl('cloudy', 0, 10, date(2016, 2, 1),
                         date(2016, 3, 15), 1, 1, 4)


def test_bing():
    bing_crawler = BingImageCrawler('images/bing')
    bing_crawler.crawl('sunny', 0, 10, 1, 1, 4)


def test_baidu():
    baidu_crawler = BaiduImageCrawler('images/baidu')
    baidu_crawler.crawl('sunny', 0, 10, 1, 1, 4)


def test_flickr():
    flickr_crawler = FlickrImageCrawler('your_own_apikey',
                                        'images/flickr')
    flickr_crawler.crawl(max_num=10, downloader_thr_num=4, tags='family,child',
                         tag_mode='all', group_id='68012010@N00')


def test_greedy():
    greedy_crawler = GreedyImageCrawler('images/greedy/')
    greedy_crawler.crawl('bbc.com/sport', 10, 4, 1, min_size=(200, 200))


def main():
    if len(sys.argv) > 1:
        dst = sys.argv[1]
    else:
        dst = 'all'
    if dst == 'all':
        test_google()
        test_bing()
        test_baidu()
        test_flickr()
        test_greedy()
    elif dst == 'google':
        test_google()
    elif dst == 'bing':
        test_bing()
    elif dst == 'baidu':
        test_baidu()
    elif dst == 'flickr':
        test_flickr()
    elif dst == 'greedy':
        test_greedy()


if __name__ == '__main__':
    main()
