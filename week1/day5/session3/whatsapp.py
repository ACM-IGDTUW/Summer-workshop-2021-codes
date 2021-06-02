# https://www.youtube.com/watch?v=5hr0IdVM7Qg

from selenium import webdriver
import time
import random

driver = webdriver.Chrome()
driver.get('http://web.whatsapp.com')

name = input('Enter the name of user or group : ')
msg = input('Enter the message : ')

count = int(input('Enter the count : '))

#Scan the code before proceeding further
input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name)) #make sure the name of the user/group is somewhere in the top 10-12 of the side panel, if it is not send a message on that group, it will come right on top


user.click()

msg_box = driver.find_element_by_class_name('_3uMse') #this is dynamic, this is the parent-div of the div which gets 'focussed' class attribute 

for i in range(count):
    msg_box.send_keys(str(i+1)+" "+msg)
    driver.find_element_by_class_name('_1U1xa').click() #this is also dynamic button, it is easy to spot. It automatically appears when you type something in the message box
