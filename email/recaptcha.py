from selenium import webdriver
from selenium.webdriver.common.by import By


def recaptcha(check):
    driver = webdriver.Chrome()
    driver.get('')
    try:
        iframes = driver.find_elements(By.TAG_NAME, 'iframes')
        for frame in iframes:
            driver.switch_to.default_content()
            driver.switch_to.frame(frame)
            for x in ['@class=', '@id=', '@name=', '@for=', 'text()=']:
                try:
                    driver.find_element(By.XPATH, f"//*[{x}'{check}']")
                    return True
                except:
                    continue

    except:
        return False
