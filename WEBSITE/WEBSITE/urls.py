"""WEBSITE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from WEBSITE.views import recipe				#如果想要用食譜用資料庫來做，但是所有資料庫的內容都是只能透過更改views.py(WEBSITE/views.py)才能做更動
#from WEBSITE_db.views import recipe	#如果你想要食譜做成ORM(可以透過python指令新增資料入內)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^recipe/$', recipe),
]
