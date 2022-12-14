from Selenium_OOP.Task_4.NEW.Credentials import credentials
from login_page import USER

user1 = USER(user_name=credentials()[1], login_password=credentials()[0])
user2 = USER(user_name=credentials()[2], login_password=credentials()[0])
user3 = USER(user_name=credentials()[3], login_password=credentials()[0])
user4 = USER(user_name=credentials()[4], login_password=credentials()[0])

# users = [user1, user2, user3, user4]
#
# while
user1.getintosite()
user2.getintosite()
user3.getintosite()
user4.getintosite()
