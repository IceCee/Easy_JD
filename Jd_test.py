# python ->for_JD
#coding=UTF-8
from splinter import Browser
import time

url = 'http://club.jd.com/myJdcomments/myJdcomments.action'
brow = Browser()
brow.visit(url)
time.sleep(10)

num = raw_input('Numbers:')
time.sleep(5)

for i in range(int(num)):
      brow.find_by_text('点击评价').click()
      brow.find_by_text(u'商品是否给力').click()
      #brow.fill('感觉还不错')
      #brow.find_by_text("评分").mouse_over()
      time.sleep(30)
      brow.find_by_text('发表评价').click()
      time.sleep(5)
      
      
