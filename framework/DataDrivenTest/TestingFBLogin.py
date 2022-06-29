import time

from selenium import webdriver
import XLutils
import openpyxl
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://demo.opencart.com/admin/")
driver.maximize_window()
path="E:\logintest.xlsx"
# Sheet1
rows=XLutils.CountRow(path,'Sheet1')
cols=XLutils.CountCloumn(path,'Sheet1')
mail=driver.find_element(By.ID, "input-username")
passcode=driver.find_element(By.ID, "input-password")
# print(rows)
# print(cols)
# datawr=XLutils.WriteData(path,'Sheet1',2,3,"checking")
# readre=XLutils.ReadData(path,'Sheet1',2,3)
# print(readre)
for r in range(2,rows+1):
    driver.implicitly_wait(10)
    username=XLutils.ReadData(path,'Sheet1',r,1)
    password=XLutils.ReadData(path,'Sheet1',r,2)
    mail.clear()
    passcode.clear()
    mail.send_keys(username)
    passcode.send_keys(password)
    driver.find_element(By.XPATH,'//button[@type="submit"]').click()
    if driver.title=='Dashboard':
        print('test passed')
        XLutils.WriteData(path,"Sheet1",r,3,"passed")
    else:
        print("testfailed")
        XLutils.WriteData(path,"Sheet1",r,3,"failled")
        driver.find_element(By.XPATH,"//*[contains(text(),'Logout')]").click()

