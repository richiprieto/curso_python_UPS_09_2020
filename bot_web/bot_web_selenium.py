import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome("./chromedriver")
driver.get("https://dentalprimeapp.com/#/")
driver.fullscreen_window()
time.sleep(3)
driver.find_elements_by_xpath('//*[@id="input-44"]')[0].send_keys("richiprieto@crice.org")
driver.find_elements_by_xpath('//*[@id="logPassword"]')[0].send_keys(
    "1234567890"
)
driver.find_elements_by_xpath('/html/body/div/div[2]/div/main/div/div/div/div[3]/div/div/div[2]/button/span')[0].click()
time.sleep(10)
driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[1]/div/div[3]/button[1]').click()
driver.find_element_by_xpath('//*[@id="app-bar"]/div/div[2]/div/button/span/i').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="core-navigation-drawer"]/div[2]/div[2]/a[1]/div[2]/div[1]').click()
creado = driver.find_element_by_xpath('//*[@id="user-profile"]/div[3]/div[1]/div/div[2]/p[1]').text
print("El perfil fue creado en:", creado)
time.sleep(3)
driver.quit()
