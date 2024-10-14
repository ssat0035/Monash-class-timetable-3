from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://classtimetable.monash.edu/2025/")


element = driver.find_element(By.ID, "element_id")



