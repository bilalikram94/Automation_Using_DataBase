"""
@package base
WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

    Example:
        wdf = WebDriverFactory(driver)
        wdf.getWebDriverInstance()

Is called in conftest file instead of Selenium Webdriver

"""


from selenium import webdriver
import pymysql.cursors


class WebDriverFactory:


    def __init__(self, browser):
        self.browser = browser
        """
        Inits WebDriverFactory class

        Returns:
            None

        """

    """
    
        Set Chrome driver and iexplorer environment based on OS
        
    """

    def getWebDriverInstance(self):
        """
        Get WebDriver Instance based  on the browser configurations
        :return:
            'WebDriver Instance'
        """
        db = self.getURL("hrms")
        url = db[0]
        baseURL = url
        if self.browser == "iexplorer":

            # Set IE Driver

            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()

        else:
            driver = webdriver.Chrome("/usr/bin/chromedriver")

        # Setting Driver Implicit Time Out for an Element

        driver.implicitly_wait(3)

        # Maximize Window

        driver.maximize_window()

        # Loading Browser with App URL

        driver.get(baseURL)
        return driver

    @staticmethod
    def getURL(name):
        connection = pymysql.connect(host='localhost',
                                     user='bilal',
                                     password='Bilal@123',
                                     db='testing',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

        try:
            sql = "SELECT URL FROM Base WHERE Name = '" + name + "'"

            with connection.cursor() as cursor:
                # Read a single record
                cursor.execute(sql)
                result = cursor.fetchall()


            new_row = []
            for record in result:
                new_row.append(record['URL'])
            print("database testing = ", new_row)
            return new_row
        except:
            print("Something went Wrong")
