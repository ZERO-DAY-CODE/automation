from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
opt = Options()
opt.add_experimental_option("debuggerAddress","localhost:8989")
driver = webdriver.Chrome(options=opt)
driver.implicitly_wait(50)
x=int(input("Enter Number Of Messages. "))
msg = input("Enter Message. ")
y=0
while x!=y:
    driver.find_element(By.XPATH, "//*[@tabindex='10']").send_keys("Ram Ram")
    driver.find_element(By.XPATH, "//*[@data-icon='send']").click()
    y+=1
