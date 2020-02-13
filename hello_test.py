import unittest

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument('--headless')
        self.driver = Firefox(firefox_options=options)

    def tearDown(self):
        self.driver.close()


class PythonOrgSearch(BaseTestCase):

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get('http://www.python.org')
        self.assertIn('Python', driver.title)
        elem = driver.find_element_by_name('q')
        elem.send_keys('pycon')
        elem.send_keys(Keys.RETURN)
        assert 'No results found.' not in driver.page_source
