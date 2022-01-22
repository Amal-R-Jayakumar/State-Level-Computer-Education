from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class Static_Sitemap(Sitemap):

    priority = 1.0
    changefreq = 'yearly'

    def items(self):
        return [
            'index',
            'about',
            'multimedia',
            'software',
            'hardware',
            'dca',
            'more2019',
            'pgdca',
            'dchm',
            'san',
            'aoc',
            'dgda',
            '2d',
            '3d',
            'cttc',
            'dabd',
            'dao',
            'dhne',
            'dma',
            'mwd',
            'dtp',
            'wd',
            'oa',
            'pdcad',
            'pdcfa',
            'contact',
        ]

    def location(self, item):
        return reverse(item)
