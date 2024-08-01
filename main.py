from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time



# website url
response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
website = response.text
soup = BeautifulSoup(website,"html.parser")


# price scrapping
price = soup.select("ul li div span")
price_list = [price_of_h.getText().strip() for price_of_h in price ]


# price filtering
filtered_data = [item for item in price_list if item != 'Save this home']


#  address scrapping
address=soup.select("ul li div a address")
address_list=[address_of_h.getText().strip() for address_of_h in address]


#  link scrapping
link=soup.select("ul li div a")
link_list=[l['href'] for l in link]


# FORM FILLING

button='//*[@id="SMMuxb"]/a[1]'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)


driver.get("https://docs.google.com/forms/d/e/1FAIpQLScgvRcP15zmZdLbFlm5aw4fmYKb1oIbKj8nzptBz6MFLOR1kg/viewform")
# gmail_button=driver.find_element(By.XPATH,value=button)
# gmail_button.click()
#
# email=driver.find_element(By.XPATH,value='//*[@id="identifierId"]')
# email.click()
# email.send_keys("hamza226188@gmail.com")
#
# next=driver.find_element(By.XPATH,value='//*[@id="identifierNext"]/div/button/span')
# next.click()

for i in range(len(link_list)):
    time.sleep(2)

    ADDRESS_QUESTION = driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    ADDRESS_QUESTION.click()
    ADDRESS_QUESTION.send_keys(address_list[i])


    PRICE_QUESTION=driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    PRICE_QUESTION.click()
    PRICE_QUESTION.send_keys(filtered_data[i])


    LINK_QUESTION=driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    LINK_QUESTION.click()
    LINK_QUESTION.send_keys(link_list[i])


    Submit_button=driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    Submit_button.click()



    driver.get("https://docs.google.com/forms/d/e/1FAIpQLScgvRcP15zmZdLbFlm5aw4fmYKb1oIbKj8nzptBz6MFLOR1kg/viewform")


