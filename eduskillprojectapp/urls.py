from django.urls import path, include
from django.conf.urls import url
from .sitemap import Static_Sitemap
from . import views
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'static': Static_Sitemap(),
}
urlpatterns = [
    path('', views.home_view, name='index'),
    path('about/', views.about_page, name='about'),
    path('multimedia/', views.multimedia_page, name='multimedia'),
    path('software/', views.software_page, name='software'),
    path('hardware/', views.hardware_page, name='hardware'),
    path('dca/', views.dca_page, name='dca'),
    path('more2019/', views.more2019_page, name='more2019'),
    path('pgdca/', views.pgdca_page, name='pgdca'),
    path('dchm/', views.dchm_page, name='dchm'),
    path('san/', views.dchm_page, name='san'),
    path('aoc/', views.aoc_page, name='aoc'),
    path('dgda/', views.dgda_page, name='dgda'),
    path('twod/', views.twod_page, name='2d'),
    path('threed/', views.threed_page, name='3d'),
    path('cttc/', views.cttc_page, name='cttc'),
    path('dabd/', views.dabd_page, name='dabd'),
    path('dao/', views.dao_page, name='dao'),
    path('dhne/', views.dhne_page, name='dhne'),
    path('dma/', views.dma_page, name='dma'),
    path('mwd/', views.mwd_page, name='mwd'),
    path('dtp/', views.dtp_page, name='dtp'),
    path('wd/', views.wd_page, name='wd'),
    path('oa/', views.oa_page, name='oa'),
    path('pdcad/', views.pdcad_page, name='pdcad'),
    path('pdcfa/', views.pdcfa_page, name='pdcfa'),
    path('enroll/', views.enroll_page, name='enroll'),
    path('contact/', views.contact_page, name='contact'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
]
