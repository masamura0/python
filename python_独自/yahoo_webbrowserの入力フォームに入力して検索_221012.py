from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser=webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.yahoo.co.jp/")

box=browser.find_element_by_name("p")
box.send_keys("python")

search_button=browser.find_element_by_xpath("/html/body/div[1]/div/header/section[1]/div/form/fieldset/span/button")
search_button.click()