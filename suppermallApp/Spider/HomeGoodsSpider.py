import requests
from lxml import etree,html
import time
import xlrd,xlwt
import random
from selenium import webdriver

# '//img10.360buyimg.com/n7/jfs/t1/145006/19/2357/178955/5f0412dbEe9374821/28ab4e91be2128c2.jpg'
# 'https://coll.jd.com/list.html?sub=53461&page=2&JL=6_0_0'
# 'https://coll.jd.com/list.html?sub=53461&page=3&JL=6_0_0'

# 'https://img10.360buyimg.com/n7/jfs/t1/115571/17/11661/174531/5f00ad9fE85195404/50d3f920d8139c47.jpg'
def Excel(img_name,img_url,goods_price):
    print('开始写')

    conunt = len(img_url)

    page = 0
    collectionCount=0

    work = xlwt.Workbook(encoding='utf-8')
    sheet1 = work.add_sheet('sheet1')
    for i in range(conunt):
        if i % 20 == 0:
            page += 1
        sheet1.write(i,0,i)
        sheet1.write(i,1,img_name[i])
        sheet1.write(i,2, "https:"+img_url[i])
        sheet1.write(i,3,goods_price[i])
        sheet1.write(i,4,page)
        sheet1.write(i,5,collectionCount)
    work.save('homeGoods.xls')
    print('写完了')

url = ["https://coll.jd.com/list.html?sub=53461",'https://coll.jd.com/list.html?sub=53461&page=2&JL=6_0_0','https://coll.jd.com/list.html?sub=53461&page=3&JL=6_0_0']

# Excel(name,image_url,price)


def getGoods(count):
    #count 代表想要爬去多少页
    goodsImgUrl = []
    goodsName=[]
    goodsPrice=[]
    driver = webdriver.Chrome(executable_path='E:\Driver\chromedriver.exe')
    driver.get('https://coll.jd.com/list.html?sub=53461')
    for i in range(count):
        time.sleep(2)
        driver.execute_script('window.scrollTo(0,1000)')
        time.sleep(2)
        driver.execute_script('window.scrollTo(0,2000)')
        time.sleep(2)
        driver.execute_script('window.scrollTo(0,3000)')
        time.sleep(2)
        driver.execute_script('window.scrollTo(0,4000)')
        time.sleep(2)
        driver.execute_script('window.scrollTo(0,5000)')
        time.sleep(2)

        page = driver.page_source
        pageX = etree.HTML(page)
        goodsImgUrl += pageX.xpath("//div[@id='plist']/ul/li/div[1]/div[1]/a/img/@src")
        goodsName += pageX.xpath("//div[@id='plist']/ul/li/div/div[3]/a/em/text()")
        goodsPrice += pageX.xpath("//div[@id='plist']/ul/li/div/div[2]/strong/i/text()")
        driver.find_element_by_xpath("//a[@class='pn-next']").click()
        time.sleep(4)
        print(len(goodsPrice))
        print(len(goodsImgUrl))
        print(len(goodsName))
    return goodsName,goodsImgUrl,goodsPrice
img_name,img_url,goodsPrice = getGoods(10)
Excel(img_name,img_url,goodsPrice)



