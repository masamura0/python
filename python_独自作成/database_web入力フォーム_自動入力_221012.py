from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser=webdriver.Chrome(ChromeDriverManager().install())
browser.get("http://localhost/input_1001.php")

box1=browser.find_element_by_name("name")
box1.send_keys("tanaka")

box2=browser.find_element_by_name("mail")
box2.send_keys("tanaka`gmail.com")

box1=browser.find_element_by_name("message")
box1.send_keys("yoroshikuonegaishimasu")

search_button=browser.find_element_by_xpath("/html/body/form/center/div[4]/input")
search_button.click()

browser.close()