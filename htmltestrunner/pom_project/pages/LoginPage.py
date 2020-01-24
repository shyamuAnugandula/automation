class LoginPage():

    def __init__(self, driver): #constructor
        self.driver = driver

        self.username_text_box_id = 'Emailid'
        self.password_text_box_id = 'password'
        self.login_text_box_id = 'Login'

    def enter_username(self,username):
        self.driver.find_element_by_id(self.username_text_box_id).clear()
        self.driver.find_element_by_id(self.username_text_box_id).send_keys(username)  #

    def enter_password(self,password):
        self.driver.find_element_by_id(self.password_text_box_id).clear()
        self.driver.find_element_by_id(self.password_text_box_id).send_keys(password)  #

    def click_login(self):
        self.driver.find_element_by_id(self.login_text_box_id).click()