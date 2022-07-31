from selenium import webdriver
import pandas as pd
import time
import math

#excel cf names
df = pd.read_excel("C:\\Users\\dhanu\\OneDrive\\Desktop\\codeforces_automation\\Hurricane Enrollment Form(1-91).xlsx")
req = df["Enter Your Codeforces Handle"]
arr = list(req)

notvalid=list()

for i in range(len(arr)):
    if(str(arr[i])=='nan'):
        notvalid.append(i+3)

arr=[x for x in arr if str(x) != 'nan']

print(arr)

last_index=90                   #to make it faster to update

driver=webdriver.Firefox(executable_path=r'C:\Users\dhanu\Downloads\geckodriver-v0.31.0-win64\geckodriver.exe')

driver.get('https://codeforces.com/enter')
username=driver.find_element_by_xpath('//*[@id="handleOrEmail"]')
username.send_keys("enter_handle")
password=driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys("Password")
password.submit()
time.sleep(3)

for i in range(last_index,len(arr)):
    driver.get("https://codeforces.com/profile/"+arr[i])
    cu=driver.current_url
    if(("https://codeforces.com/profile/"+arr[i])!=cu):
        continue
    # driver.get('https://codeforces.com/enter?back=%2Fprofile%2F'+i)

    #Wait for page load
    time.sleep(2)

    friendstar_status=driver.find_element_by_xpath('/html/body/div[6]/div[4]/div[2]/div[2]/div[5]/div[2]/div/h1/img').get_attribute("class").split(' ')[0]

    if friendstar_status=='addFriend':
            driver.find_element_by_xpath('/html/body/div[6]/div[4]/div[2]/div[2]/div[5]/div[2]/div/h1/img').click()
    time.sleep(2)
print(len(arr))
# update len(arr) to last_index after running