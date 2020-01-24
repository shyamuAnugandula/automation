class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.logout_id = 'logout'

    def click_logut(self):
        self.driver.find_element_by_id(self.logout_id).click()