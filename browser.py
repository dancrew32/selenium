import getpass
import pickle
import time
from io import BytesIO

from PIL import Image
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def new(name, **kwargs):
    return Browser(name=name, **kwargs)


class Browser:
    max_wait = 10

    def __init__(self, name, headless=False):
        self.name = name
        self.headless = headless
        self.username = None
        self.start()

    def start(self):
        self.log('starting')
        options = Options()
        if self.headless:
            options.add_argument('--headless')
        self.driver = Firefox(options=options)
        self.elem = None
        self.log('started')

    def get(self, url):
        self.driver.get(url)

    def maximize(self):
        self.driver.maximize_window()
        self.log('maximize')

    def size(self, width=800, height=600):
        self.driver.set_window_size(width, height)
        self.log(f'width: {width}, height: {height}')

    def user(self):
        self.username = input('username: ').strip()

    def password(self):
        self.password = getpass.getpass('password: ').strip()

    def save_cookies(self):
        cookies = self.driver.get_cookies()
        with open(f'{self.name}.pkl', 'wb') as f:
            pickle.dump(cookies, f)
        self.log('save loaded')

    def load_cookies(self):
        with open(f'{self.name}.pkl', 'rb') as f:
            cookies = pickle.load(f)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
        self.log('cookies loaded')

    def log(self, message, **kwargs):
        print(f'browser: {message}', kwargs)

    def html(self):
        html = self.driver.page_source
        self.log(html)

    def done(self):
        self.log('closing')
        self.elem = None
        self.username = None
        self.password = None
        self.driver.close()
        self.log('done')

    def pause(self, seconds):
        self.log('sleep', seconds=seconds)
        time.sleep(seconds)

    def find(self, selector):
        self.log('finding', selector=selector)
        wait = WebDriverWait(self.driver, self.max_wait)
        self.elem = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
        self.log('found', elem=self.elem)

    def type(self, value):
        self.elem.send_keys(value)
        self.log('type', value)

    def click(self):
        self.elem.click()
        self.log('click')

    def screenshot(self, name, show=False):
        image = Image.open(BytesIO(self.elem.screenshot_as_png))
        fname = f'./{name}.png'
        image.save(fname)
        self.log(fname)
        if show:
            image.show()

