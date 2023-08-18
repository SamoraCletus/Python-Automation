from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random


class TwitterBot(webdriver.Chrome):
    def __init__(self):
        options = webdriver.ChromeOptions()
        super(TwitterBot, self).__init__(options=options)
        self.maximize_window()
        self.implicitly_wait(10)

    def landing_page(self):
        self.get('https://twitter.com')

    def login(self, username, password):
        self.username = username
        self.password = password

        login_btn = self.find_element(By.CSS_SELECTOR, 'a[href="/login"]')
        login_btn.click()

        username_input = self.find_element(
            By.CSS_SELECTOR, 'input[autocomplete ="username"]')

        username_input.send_keys(self.username)
        username_input.send_keys(Keys.RETURN)
        time.sleep(random.randint(2, 5))

        password_input = self.find_element(
            By.CSS_SELECTOR, 'input[name="password"]')
        password_input.send_keys(self.password)
        password_input.send_keys(Keys.RETURN)
        time.sleep(random.randint(2, 5))

    def like_tweet(self, hashtag):
        self.get('https://twitter.com/search?q=' +
                 hashtag + '&src=typed_query')

        time.sleep(random.randint(2, 5))

        for i in range(1, 5):
            self.execute_script(
                'window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(2)

        tweets_container = self.find_element(
            By.CSS_SELECTOR, 'div[aria-label="Timeline: Search timeline"]')
        tweets = tweets_container.find_elements(
            By.CSS_SELECTOR, 'div[data-testid="cellInnerDiv"]')

        links = [elem.find_element(By.TAG_NAME, 'a').get_attribute(
            'href') for elem in tweets]
        print(links)


bot = TwitterBot()
bot.landing_page()
bot.login('samoracuteecletus@gmail.com', '95879587')
bot.like_tweet("webdevelopment")

# aria-label="Timeline: Search timeline"  #for finding one
# data-testid="cellInnerDiv" # for finding many
