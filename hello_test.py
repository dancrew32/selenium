import unittest
import browser

class BrowserTest(unittest.TestCase):

    def test_danmasq(self):
        b = browser.new('danmasq')
        b.get('https://danmasq.com')
        b.html()
        b.done()
