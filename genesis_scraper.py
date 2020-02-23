from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys


class GenesisScraper:

    def __init__(self):
        self.driver = Chrome("./chromedriver")
        self.driver.get("https://parents.ebnet.org/genesis/sis/view?gohome=true")

    def close(self):
        self.driver.close()

    def login(self, usr, pwd):
        usr_field = self.driver.find_element_by_xpath("//input[@id='j_username']")
        pwd_field = self.driver.find_element_by_xpath("//input[@id='j_password']")

        usr_field.clear()
        pwd_field.clear()

        usr_field.send_keys(usr)
        pwd_field.send_keys(pwd, Keys.ENTER)

    def getData(self):
        data = []
        data_ind = 0

        for ind in range(2, 12):
            data.append([])

            base_str = "//table[@class='list' and @border='0']/tbody/tr[" + str(ind) + "]"

            class_name = self.driver.find_element_by_xpath(base_str + "/td[1]").text
            class_name = class_name.title()
            data[data_ind].append(class_name)

            #the teacher requires a little bit of clean up
            teacher_str = self.driver.find_element_by_xpath(base_str + "/td[2]").text
            #remove "email" from the end of the string and strip
            teacher_str.lstrip()
            teacher_str = teacher_str[:-6].lstrip().rstrip()
            #adjust capitalization
            teacher_str = teacher_str.title()
            data[data_ind].append(teacher_str)

            data[data_ind].append(self.driver.find_element_by_xpath(base_str + "/td[3]").text)

            data_ind += 1

        return data

    def getDataFrom(self, file):
        self.driver.get("./" + file)
        return self.getData()
