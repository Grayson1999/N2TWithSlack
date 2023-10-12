from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# ChromeDriverManager를 사용하여 ChromeDriver 설치
service = Service(ChromeDriverManager().install())
service.log_path = "/home/grayson_p/N2TWithSlack/chromedriver.log"