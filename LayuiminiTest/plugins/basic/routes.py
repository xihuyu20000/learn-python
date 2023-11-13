from flask import Blueprint, render_template, request, redirect

bp = Blueprint('basic', __name__,
               template_folder='templates',
               static_folder='static',
               static_url_path='/core/static')

@bp.route('/basic/<page>')
def page(page):
    return render_template(f'basic/{page}')

@bp.route('/api/init.json')
def api_init():
    return {
        "homeInfo": {
            "title": "首页",
            "href": "/basic/welcome-1.html?t=1"
        },
        "logoInfo": {
            "title": "LAYUI MINI",
            "image": "/static/layui/images/logo.png",
            "href": ""
        },
        "menuInfo": [
            {
                "title": "常规管理",
                "icon": "fa fa-address-book",
                "href": "",
                "target": "_self",
                "child": [
                    {
                        "title": "主页模板",
                        "href": "",
                        "icon": "fa fa-home",
                        "target": "_self",
                        "child": [
                            {
                                "title": "主页一",
                                "href": "/basic/welcome-1.html",
                                "icon": "fa fa-tachometer",
                                "target": "_self"
                            },
                            {
                                "title": "主页二",
                                "href": "/basic/welcome-2.html",
                                "icon": "fa fa-tachometer",
                                "target": "_self"
                            },
                            {
                                "title": "主页三",
                                "href": "/basic/welcome-3.html",
                                "icon": "fa fa-tachometer",
                                "target": "_self"
                            }
                        ]
                    },
                    {
                        "title": "菜单管理",
                        "href": "/basic/menu.html",
                        "icon": "fa fa-window-maximize",
                        "target": "_self"
                    },
                    {
                        "title": "系统设置",
                        "href": "/basic/setting.html",
                        "icon": "fa fa-gears",
                        "target": "_self"
                    },
                    {
                        "title": "表格示例",
                        "href": "/basic/table.html",
                        "icon": "fa fa-file-text",
                        "target": "_self"
                    },
                    {
                        "title": "表单示例",
                        "href": "",
                        "icon": "fa fa-calendar",
                        "target": "_self",
                        "child": [
                            {
                                "title": "普通表单",
                                "href": "/basic/form.html",
                                "icon": "fa fa-list-alt",
                                "target": "_self"
                            },
                            {
                                "title": "分步表单",
                                "href": "/basic/form-step.html",
                                "icon": "fa fa-navicon",
                                "target": "_self"
                            }
                        ]
                    },
                    {
                        "title": "登录模板",
                        "href": "",
                        "icon": "fa fa-flag-o",
                        "target": "_self",
                        "child": [
                            {
                                "title": "登录-1",
                                "href": "/basic/login-1.html",
                                "icon": "fa fa-stumbleupon-circle",
                                "target": "_blank"
                            },
                            {
                                "title": "登录-2",
                                "href": "/basic/login-2.html",
                                "icon": "fa fa-viacoin",
                                "target": "_blank"
                            },
                            {
                                "title": "登录-3",
                                "href": "/basic/login-3.html",
                                "icon": "fa fa-tags",
                                "target": "_blank"
                            }
                        ]
                    },
                    {
                        "title": "异常页面",
                        "href": "",
                        "icon": "fa fa-home",
                        "target": "_self",
                        "child": [
                            {
                                "title": "404页面",
                                "href": "/basic/404.html",
                                "icon": "fa fa-hourglass-end",
                                "target": "_self"
                            }
                        ]
                    },
                    {
                        "title": "其它界面",
                        "href": "",
                        "icon": "fa fa-snowflake-o",
                        "target": "",
                        "child": [
                            {
                                "title": "按钮示例",
                                "href": "/basic/button.html",
                                "icon": "fa fa-snowflake-o",
                                "target": "_self"
                            },
                            {
                                "title": "弹出层",
                                "href": "/basic/layer.html",
                                "icon": "fa fa-shield",
                                "target": "_self"
                            }
                        ]
                    }
                ]
            },
            {
                "title": "组件管理",
                "icon": "fa fa-lemon-o",
                "href": "",
                "target": "_self",
                "child": [
                    {
                        "title": "图标列表",
                        "href": "/basic/icon.html",
                        "icon": "fa fa-dot-circle-o",
                        "target": "_self"
                    },
                    {
                        "title": "图标选择",
                        "href": "/basic/icon-picker.html",
                        "icon": "fa fa-adn",
                        "target": "_self"
                    },
                    {
                        "title": "颜色选择",
                        "href": "/basic/color-select.html",
                        "icon": "fa fa-dashboard",
                        "target": "_self"
                    },
                    {
                        "title": "下拉选择",
                        "href": "/basic/table-select.html",
                        "icon": "fa fa-angle-double-down",
                        "target": "_self"
                    },
                    {
                        "title": "文件上传",
                        "href": "/basic/upload.html",
                        "icon": "fa fa-arrow-up",
                        "target": "_self"
                    },
                    {
                        "title": "富文本编辑器",
                        "href": "/basic/editor.html",
                        "icon": "fa fa-edit",
                        "target": "_self"
                    },
                    {
                        "title": "省市县区选择器",
                        "href": "/basic/area.html",
                        "icon": "fa fa-rocket",
                        "target": "_self"
                    }
                ]
            },
            {
                "title": "其它管理",
                "icon": "fa fa-slideshare",
                "href": "",
                "target": "_self",
                "child": [
                    {
                        "title": "多级菜单",
                        "href": "",
                        "icon": "fa fa-meetup",
                        "target": "",
                        "child": [
                            {
                                "title": "按钮1",
                                "href": "/basic/button.html?v=1",
                                "icon": "fa fa-calendar",
                                "target": "_self",
                                "child": [
                                    {
                                        "title": "按钮2",
                                        "href": "/basic/button.html?v=2",
                                        "icon": "fa fa-snowflake-o",
                                        "target": "_self",
                                        "child": [
                                            {
                                                "title": "按钮3",
                                                "href": "/basic/button.html?v=3",
                                                "icon": "fa fa-snowflake-o",
                                                "target": "_self"
                                            },
                                            {
                                                "title": "表单4",
                                                "href": "/basic/form.html?v=1",
                                                "icon": "fa fa-calendar",
                                                "target": "_self"
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "title": "失效菜单",
                        "href": "/basic/error.html",
                        "icon": "fa fa-superpowers",
                        "target": "_self"
                    }
                ]
            }
        ]
    }


@bp.route('/')
def index():
    return render_template('index.html')