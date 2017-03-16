import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
 
class DisplayPrevoiusPage(unittest.TestCase):

    def setUp(self):
# create a new Firefox session
        firefoxCap = DesiredCapabilities.FIREFOX
#we need to explicitly specify to use Marionette
        firefoxCap['marionette'] = True
#and the path to firefox
        firefoxCap['binary'] = "C:\Program Files\Mozilla Firefox"
        self.driver = webdriver.Firefox(capabilities = firefoxCap)
        self.driver.maximize_window()
# navigate to the application home page
        self.driver.get("http://computer-database.herokuapp.com/computers")
        
    def is_text_present(self, text):
        return str(text) in self.driver.page_source
        
    def test_1_next_page(self):
        self.driver.find_element_by_partial_link_text("Next").click()     
        time.sleep(1)
        self.driver.find_element_by_partial_link_text("Previous").click()     
        try: self.is_text_present("1 to 10")
        except AssertionError as e: self.verificationErrors.append(str(e))
                    
    def test_2_quit(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
        
        
        
