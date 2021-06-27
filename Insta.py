from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

realFollowList = []
realFollowerList = []

enteredName = input("Phone number, username or email : ")
enteredPassword = input("Password : ")

browser = webdriver.Firefox()
browser.get("https://www.instagram.com/")
time.sleep(2)

username = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")
username.send_keys(enteredName) # name
password.send_keys(enteredPassword) # password
time.sleep(1)

login = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div")
login.click()
time.sleep(6)

profile = browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]")
profile.click()
time.sleep(3)

profile = browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[1]/div/div[2]/div/div/div/div")
profile.click()
time.sleep(3)

follow = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a")
follow.click()
time.sleep(2)

followNumber = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span")
followNumberText = followNumber.text


for i in range (int(followNumberText)):

    time.sleep(0.3)
    src = WebDriverWait(browser, 10).until(ec.presence_of_element_located((By.XPATH,"/html/body/div[5]/div/div/div[2]")))
    browser.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', src)

followList = browser.find_elements_by_css_selector(".FPmhX.notranslate._0imsa")

i = 0
for name in followList:

    i = i + 1
    print(str(i) + " " + name.text)
    realFollowList.append(name.text)

followNum = i

print("-----------------------------------------------------")

exit = browser.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button/div")
exit.click()

followersNumber = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span")
followersNumberText = followersNumber.text


followers = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
followers.click()

for i in range (int(followersNumberText)):
    time.sleep(0.3)
    src = WebDriverWait(browser, 10).until(ec.presence_of_element_located((By.XPATH,"/html/body/div[5]/div/div/div[2]")))
    browser.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', src)

followersList = browser.find_elements_by_css_selector(".FPmhX.notranslate._0imsa")

i = 0
for name in followersList:

    i = i + 1
    print(str(i) + " " + name.text)
    realFollowerList.append(name.text)

followersNum = i

print("-----------------------------------------------------")

exit = browser.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button/div")
exit.click()

print("Follow : "+ str(followNum) + " Followers : " + str(followersNum))


print("-----------------------------------------------------")

for name in realFollowList:
    if name not in realFollowerList:
        print(name + " is not follow you !")

print("-----------------------------------------------------")

for name in realFollowerList:
    if name not in realFollowList:
        print(name + " is not followed !")

print("-----------------------------------------------------")