from time import sleep
from config import username, password
import undetected_chromedriver.v2 as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


LOGGINED = False

options = uc.ChromeOptions()

driver = uc.Chrome(options=options)


def login(username, password):
    global LOGGINED

    driver.get('https://vavadamqp.com')

    try:
        loginButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/header/div/div/div[1]/button')))
        loginButton.click()
    except Exception:
        print("Loading took too much time!")

    usernameField = driver.find_element(By.ID, '_username')
    usernameField.click()
    usernameField.clear()
    usernameField.send_keys(username)

    passwordFiled = driver.find_element(By.ID, '_password')
    passwordFiled.click()
    passwordFiled.clear()
    passwordFiled.send_keys(password)
    passwordFiled.send_keys(Keys.ENTER)

    LOGGINED = True


def enterPromo(promo: str):

    driver.get('https://vavadamqp.com/ru/profile/bonus/')

    try:
        promoInput = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'promo_code_form_token')))
    except Exception:
        print("Loading took too much time!")
    
    promoInput.clear()
    promoInput.send_keys(promo)
    promoInput.send_keys(Keys.ENTER)


def startSiteWork(promocods: list = []):
    global password, username
    if not LOGGINED:
        login(username, password)

    if promocods:
        for promo in promocods:
            enterPromo(promo)
