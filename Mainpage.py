from selenium import webdriver
from Pageobjmodel.LoginPage import LoginPage

driver = webdriver.Chrome(executable_path="C:/Users/HP/Downloads/chromedriver_win32/chromedriver.exe")
driver.maximize_window()


driver.get("https://magnus.jalatechnologies.com/")

login = LoginPage(driver)
login.enter_username("training@jalaacademy.com")
login.enter_password("jobprogram")
login.click_login()

print("Test Completed")
