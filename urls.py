from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import views, api, pdf, network, functions_nmap, ndiff

urlpatterns = [
    path('', views.index, name='index'),
    path('setscanfile/<scanfile>', views.setscanfile, name='setscanfile'),
    path('report/<address>/', views.details, name='details'),
    path('report/<port>/', views.port, name='port'),
    path('report/service/<filterservice>/', views.index, name='service'),
    path('portid/<filterportid>/', views.index, name='portid'),
    path(
        'api/v1/scan/<scanfile>/<faddress>',
        api.apiv1_hostdetails,
        name='apiv1_hostdetails',
    ),
    path('api/v1/scan/<scanfile>', api.apiv1_hostdetails, name='apiv1_hostdetails'),
    path('api/v1/scan', api.apiv1_scan, name='apiv1_scan'),
    path(
        'api/v1/nmap/scan/active',
        functions_nmap.nmap_scaninfo,
        name='apiv1_scan_active',
    ),
    path('api/v1/nmap/scan/new', functions_nmap.nmap_newscan, name='apiv1_scan_new'),
    path('api/v1/nmap/ndiff/<f1>/<f2>', ndiff.ndiff, name='ndiff'),
    path('api/setlabel/<objtype>/<label>/<hashstr>/', api.label, name='api_label'),
    path('api/rmlabel/<objtype>/<hashstr>/', api.rmlabel, name='api_rmlabel'),
    path('api/pdf/', api.genPDF, name='genPDF'),
    path('api/getcve/', api.getCVE, name='getCVE'),
    path('api/savenotes/', api.saveNotes, name='genPDF'),
    path('api/rmnotes/<hashstr>/', api.rmNotes, name='api_rmnotes'),
    path('api/<address>/<portid>/', api.port_details, name='api_port'),
    path('report/view/login/', views.login, name='login'),
    path('report/view/pdf/', pdf.reportPDFView, name='reportPDFView'),
    path('report/view/network/', network.visjs, name='network_view'),
    path('report/view/ndiff/<f1>/<f2>', views.scan_diff, name='ndiffview'),
    # path('report/', include('urls')),
    # path('admin/', admin.site.urls),
]

if settings.DEBUG:
    # import debug_toolbar
    # urlpatterns = [
    #     path('__debug__/', include(debug_toolbar.urls)),
    # ] + urlpatterns
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
