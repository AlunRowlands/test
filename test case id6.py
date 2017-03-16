import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
 
class AddComputerInvalidMonth(unittest.TestCase):

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
        
    def test_1_add_a_new_computer(self):
# click the add button
        self.driver.find_element_by_id("add").click()
# switch to new window
        self.driver.switch_to_window(self.driver.window_handles[-1])
# wait to make sure the new window is loaded
        time.sleep(1)
        self.driver.find_element_by_id("name").send_keys("Aspire 6666")
        self.driver.find_element_by_id("introduced").send_keys("2009-01-01")
        self.driver.find_element_by_id("discontinued").send_keys("2015-00-01")
        Select(self.driver.find_element_by_id("company")).select_by_visible_text("ASUS")
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@type='submit' and @value='Create this computer']").click()
# check for rejection      
        try: self.is_text_present("error")
        except AssertionError as e: self.verificationErrors.append(str(e))  
        
#switch back to original window
        self.driver.switch_to_window(self.driver.window_handles[0])
                    
    def test_2_quit(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
        
        
        
