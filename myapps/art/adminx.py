# from django.contrib import admin
import xadmin
from xadmin import views

from art.models import Category, Art




#  配置主题

class BaseSetting:
    enable_themes = True
    use_bootswatch = True

#  全局配置
class GlobalSettings(object):
    # 整体配置
    site_title = '千鋒文章后台管理系统'
    site_footer = '千锋教育python项目'
    menu_style = 'accordion'  # 菜单折叠
    # 搜索模型
    global_search_models = [Category, Art]

    # 模型的图标(参考bootstrap图标插件)
    global_models_icon = {
        Art: "glyphicon glyphicon-book",
        Category: "fa fa-cloud"
    }  # 设置models的全局图标

class CategoryAdmin:
    list_display = ['t_name','add_time']
    search_fields = ['name']

class ArtAdmin:
    list_display = ['title', 'author', 'publish_time', 'category']
    search_fields = ['titile','category__name']
    style_fields = {
        'content': 'ueditor',

    }
# Register your models here.
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)

xadmin.site.register(Category,CategoryAdmin)
xadmin.site.register(Art, ArtAdmin)


