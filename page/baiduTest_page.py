from poium import Page, Element


class BaiduPAGE(Page):
    search_input = Element(id_="kw", describe="搜索框")
    search_button = Element(id_="su", describe="搜索按钮")
    settings = Element(css="#s-usersetting-top", describe="设置")
    search_setting = Element(css="#s-user-setting-menu > div > a.setpref.first > span", describe="搜素设置选项")
    saving_setting = Element(css="#se-setting-7 > a.prefpanelgo.setting-btn.c-btn.c-btn-primary", describe="保存设置")