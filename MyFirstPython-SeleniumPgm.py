from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
#TASK1

driver = webdriver.Chrome(executable_path="C:\\Users\\Rakesh\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get(" https://www.charmhealth.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.find_element_by_xpath("//span[contains(text(),'Login')]").click()
time.sleep(3)
driver.find_element_by_id("lid").send_keys("Dev+7@deepscribe.ai")
driver.find_element_by_id("pwd").send_keys("vgS9Y3RDhq2tnhE")
driver.find_element_by_id("signin_submit").click()

time.sleep(30)
driver.find_element_by_xpath("//i[@id='NEW_DIALOG_CLOSE_MARK']").click()

driver.find_element_by_class_name("patient-menu-icon").click()
driver.find_element_by_xpath("//*[contains(text(),'TEST0001')]").click()
#driver.find_element_by_xpath("//*[@id=\"patientList\"]/tbody/tr[1]").click()
driver.find_element_by_class_name("charts-menu-icon").click()
#TASK2
driver.find_element_by_class_name("v2-back-icon").click()
driver.find_element_by_xpath("//*[@id='encounterTitle_569635000000061005']").click()
time.sleep(30)
Edit = driver.find_element_by_xpath("//button[@name='pastEncButton']")
driver.execute_script("arguments[0].click();", Edit)
time.sleep(30)
driver.find_element_by_id("encounterTab_3").click()
time.sleep(30)
Templates=driver.find_element_by_xpath("//*[@id='PE_VIEW']/div/table/tbody/tr/td/div[3]/div[1]")
Templates.click()
driver.close()

