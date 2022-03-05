import time
from selenium import webdriver
from random import randint
from bs4 import BeautifulSoup
import requests
import csv

driver = webdriver.Chrome('/Users/kierrahill/Desktop/JOU4950/python/scraping/chromedriver')
driver.get('https://gsaauctions.gov/gsaauctions/gsaauctions/')

#link1 = driver.find_element_by_link_text('Vehicles').click()
#link2 = driver.find_element_by_link_text('2').click()
#link3 = driver.find_element_by_link_text('3').click()
#link4 = driver.find_element_by_link_text('4').click()
#link5 = driver.find_element_by_link_text('5').click()

vehicle_url = 'https://gsaauctions.gov/gsaauctions/gsaauctions/'
vehicle_list = []
base_url = 'https://gsaauctions.gov/gsaauctions/aucitsrh/?sl='
url_list = []
def get_urls(link_url):
    s = randint(1,10)
    time.sleep(s)
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    tables = soup.find_all('tbody')
    for table in tables:
        tabl = table.find_all('a', class_="thumbnail")
    for tab in tabl:
        vehicle_list.append(tab.attrs['href'])

hrefs_list = get_urls(driver.find_element_by_link_text('Vehicles').click())
hrefs_list = get_urls(driver.find_element_by_link_text('2').click())
hrefs_list = get_urls(driver.find_element_by_link_text('3').click())
hrefs_list = get_urls(driver.find_element_by_link_text('4').click())
##hrefs_list = get_urls(driver.find_element_by_link_text('5').click())

driver.close()

for vehicle in vehicle_list:
    clean = vehicle.split('"')
    urls = base_url + clean[1] + clean[3]
    url_list.append(urls)

def write_csv(url_list):
    csvfile = open('project.csv', 'w', newline='', encoding='utf-8')
    c = csv.writer(csvfile)
    c.writerow( ['vehicle','location','price','closing date'] )
    for url in url_list:
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        vehicle = soup.find('h2', class_="title")
        vehicles = vehicle.get_text()
        detail = soup.find_all('dd')
        locations = detail[1].text
        prices = detail[2].text[5:15]
        dates = detail[4].text[0:17]
        details = [vehicles,locations,prices,dates]
        c.writerow(details)
    csvfile.close()

write_csv(url_list)
