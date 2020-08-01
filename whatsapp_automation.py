# %%
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
# import pyttsx3

# %%
# Replace below path with the absolute path
# to chromedriver in your computer


pathOfDriver = r"C:\Users\Shivam Sundram\OneDrive\Desktop\New folder\chromedriver.exe"


driver = webdriver.Chrome(pathOfDriver)

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

# Replace 'Friend's Name' with the name of your friend
# or the name of a group
target = 'Friends'

# Replace the below string with your own message
msg = "Message sent using python!"
input("Press Enter after scanning: ")



#%%
while(True):

    target = input("Enter the target (Empty for stop) : ")
    # target = "Rashmi"
    # input("Press Enter")
    if(target == ''):
        break
    print("Target set", target)

    # For the searching ans automatically selecting the first one
    search_box = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    search_box.send_keys(target + Keys.ENTER)
    print(search_box)

    message_input = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

    msg = input("Enter the message to be sent: ")
    # msg = "test"

    count = int(input("Enter the count: "))

    for i in range(count):
        message_input.send_keys(msg)
        # message_input.send_keys(' '+str(i))
        message_input.send_keys(Keys.ENTER)


    

    print("Messages sent!")

print("Done")
#%% Pattern Birthday Wish
while(True):

    target = input("Enter the target (Empty for stop) : ")
    # target = "Rashmi"
    # input("Press Enter")
    if(target == ''):
        break
    print("Target set", target)

    # For the searching ans automatically selecting the first one
    search_box = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    search_box.send_keys(target + Keys.ENTER)
    print(search_box)

    message_input = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

      # msg = input("Enter the message to be sent: ")
      # msg = "test"

    wishMsg = input("Enter the name only: ")
    if(wishMsg == ''):
        continue
    wishMsg = 'Happy Birthday ' + wishMsg
    print(wishMsg)
    
    i=1
    while(i<=len(wishMsg)):
        message_input.send_keys(wishMsg[:i])
        message_input.send_keys(Keys.ENTER)
        i+=1
    print("Messages sent!")

print("Done")
# Happy Birthday Naresh

#%% Pattern message
while(True):

    target = input("Enter the target (Empty for stop) : ")
    # target = "Rashmi"
    # input("Press Enter")
    if(target == ''):
        break
    print("Target set", target)

    # For the searching ans automatically selecting the first one
    search_box = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    search_box.send_keys(target + Keys.ENTER)
    print(search_box)

    message_input = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

      # msg = input("Enter the message to be sent: ")
      # msg = "test"

    wishMsg = input("Enter the message: ")
    if(wishMsg == ''):
        continue
    print(wishMsg)
    
    i=1
    while(i<=len(wishMsg)):
        message_input.send_keys(wishMsg[:i])
        message_input.send_keys(Keys.ENTER)
        i+=1
    print("Messages sent!")

print("Done")
# Happy Birthday Naresh

# %% Quit
driver.quit()
