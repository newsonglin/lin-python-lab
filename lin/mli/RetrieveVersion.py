import os
import time

import pyautogui
import pyperclip
from pyautogui import press, typewrite
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
actions = ActionChains(driver)

driver.get("https://rancher-monitoring.dev.aws06.mlic.cloud/dashboard/auth/login")

username = WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, '//label[text()="Username "]/following::input[1]')))
username.send_keys('sli')

pas = WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, '//label[text()="Password "]/following::input[1]')))
pas.send_keys(os.environ['my.domain.password'])

login = driver.find_element(By.XPATH, '//button[@type="submit"]')
login.click()

WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, '//a[contains(@href,"/dashboard/c/local/explorer")]')))

# navigate to pods
driver.get("https://rancher-monitoring.dev.aws06.mlic.cloud/dashboard/c/local/explorer/pod")
# maximum the browser window
pyautogui.hotkey('alt', 'space', interval=0.25)
pyautogui.press('x')

time.sleep(3)
print('pyautogui.size()=:' + str(pyautogui.size()))
# switch ime to English
pyautogui.moveTo(1706, 1048, duration=0.3)  # move to ime
pyautogui.click()

pyautogui.moveTo(1648, 789, duration=0.3)  # move to English
pyautogui.click()

time.sleep(10)
actions.key_down(Keys.CONTROL).send_keys('`').key_up(Keys.CONTROL).perform()
time.sleep(25)

# switch ime to English

# kubectl get pods -n mli-qa02  -o custom-columns=NAME:.metadata.name,IMAGE:.spec.containers[0].image
typewrite("kubectl get pods -n mli-qa02  -o custom-columns=NAME:.metadata.name,IMAGE:.spec.containers[0].image", interval=0.3)
press('enter', interval=1)

# moves mouse to command end
pyautogui.moveTo(133, 930, duration=0.3)
pyautogui.click()

# drag and select
pyautogui.dragTo(1, 1, 8, button='left')

# move mouse to content area, and copy contents
pyautogui.moveTo(178, 913, duration=0.3)
pyautogui.click(button='right')
pyautogui.moveTo(292, 383, duration=0.3)
pyautogui.click()

# write copied contents to file
s = pyperclip.paste()
# print(s)
with open('D:/projects/python/mli/billing/data/qa02-app-versions.txt', 'w') as g:
    g.write(s)
time.sleep(2)
