import time
import requests
from selenium import webdriver
import xlwt
excel=xlwt.Workbook()
excelsave='尾部爬虫.xls'#要保存的excel位置及文件名
wd = webdriver.Chrome(r'H:\.......')#这个地方写你的浏览器驱动地址
userid=''#账号
passwd=''#密码
txt=('123.txt')#域名或IP的TXT存储文本，每行一个域名或IP
wd.get('https://passport.threatbook.cn/popupLogin?service=x&callbackURL=https://x.threatbook.cn/')#请求的URL
#写入excel的首行
sheet=excel.add_sheet('微步爬虫返回数据')
head=['域名或IP','微步标签','相关事件','通讯录样本','URL']
for h in range(len(head)):
    sheet.write(0,h,head[h])
row=1
#登录部分
elements = wd.find_element_by_class_name(u'field')
time.sleep(1)
#输入账号
elements.find_element_by_class_name('control').find_element_by_class_name('input').send_keys(userid)
time.sleep(1)
#输入密码
elements.find_element_by_class_name('field.passward-field').find_element_by_class_name(u'input').send_keys(passwd)
time.sleep(2)
#点击验证码
elements.find_element_by_class_name('geetest_btn').find_element_by_class_name('geetest_radar_tip').click()
time.sleep(10)
#点击登录按钮
elements.find_element_by_css_selector("[class='pure-button pure-button-primary login-btn']").click()
time.sleep(5)
#接收微步在线首页数据
for handle in wd.window_handles:
    wd.switch_to.window(handle)
    if '微步在线' in wd.title:
        break
#读取本地文件循环打印
for line in open(txt):
    #发送请求查询数据
    shuru=wd.find_element_by_class_name('tab-content').find_element_by_css_selector("[class='ioc-search J-ioc-search']")
    shuru.send_keys(line)
    ipyuming=wd.find_element_by_css_selector("[class='zone basic-info J-basic-zone']").find_element_by_css_selector("[class='name bold']")
    weibubiaoqian=wd.find_element_by_css_selector("[class='zone basic-info J-basic-zone']").find_element_by_css_selector("[class='tag-info']").find_element_by_class_name('tag-list')
    xiangguanshijian=wd.find_element_by_css_selector("[class='J-tab-content report-tab-content']").find_element_by_class_name('relate-event').find_element_by_class_name('content').find_element_by_class_name('table-responsive').find_element_by_class_name('table').find_element_by_tag_name('tbody')
    yangben=wd.find_element_by_class_name('communicate-sample').find_element_by_class_name('content').find_element_by_class_name('table-responsive').find_element_by_class_name('table').find_element_by_tag_name('tbody')
    urldizhi=wd.find_element_by_css_selector("[class='J-tab-content report-tab-content']").find_element_by_class_name('contain-url').find_element_by_class_name('content').find_element_by_class_name('table-responsive').find_element_by_class_name('table').find_element_by_tag_name('tbody')
    sheet.write(row, 0, ipyuming.text)
    sheet.write(row, 1, weibubiaoqian.text)
    sheet.write(row, 2, xiangguanshijian.text)
    sheet.write(row, 3, yangben.text)
    sheet.write(row, 4, urldizhi.text)
    time.sleep(8)
    row += 1
    #打印结果
excel.save(excelsave)
print("爬完收工，赶快跑路！！！")