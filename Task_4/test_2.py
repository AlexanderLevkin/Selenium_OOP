from selenium.common import NoSuchElementException

from Credentials import credentials
from login_page import USER

user1 = USER(user_name=credentials()[1], login_password=credentials()[0])
user2 = USER(user_name=credentials()[2], login_password=credentials()[0])
user3 = USER(user_name=credentials()[3], login_password=credentials()[0])
user4 = USER(user_name=credentials()[4], login_password=credentials()[0])

a = [user1, user2, user3, user4]

while True:
    for i in a:
        try:
            i.getintosite()
        except NoSuchElementException as exception:
            print("we catch this exception")
            continue
    break

