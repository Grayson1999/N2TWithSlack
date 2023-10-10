from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.tistory.com/oauth/authorize?client_id=e674d81d586e2169a896eb7680164c6e&redirect_uri=http://comgong-stone.tistory.com&response_type=code")

input()