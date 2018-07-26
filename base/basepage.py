"""
@package base

Base Page Class Implementation
It implements methods which are common to all the pages throughout the application

This class needs to be inherited by all the page classes
This should not be used by creating object instances

Example:
    Class LoginPage(BasePage)
"""
from base.selenium_drivers import SeleniumDriver
from traceback import print_stack
from utilities.util import Util
from utilities.teststatus import Status
from pages.home.navigation import Navigation
import pymysql.cursors


class BasePage(SeleniumDriver):
    def __init__(self, driver):

        """
        Inits BasePage class
        Returns:
            None
        """
        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Util()
        self.stat = Status(driver)
        self.nav = Navigation(driver)

    def verifyPageTitle(self, titleToVerify):
        """
        Verify the page Title
        Parameters:
             titleToVerify: Title on the page that needs to be verified
        """
        try:
            actualTitle = self.getTitle()
            return self.util.verifyTextContains(actualTitle, titleToVerify)
        except:
            self.log.error("### Failed to get page title !!!")
            print_stack()
            return False

    def DBGetElement(self, tablename, name):
        # Connect to the database
        connection = pymysql.connect(host='localhost',
                                     user='bilal',
                                     password='Bilal@123',
                                     db='testing',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        self.log.info("Connection Established with DB")
        try:
            sql = "SELECT Locator, LocatorType FROM " + tablename + " WHERE Name = '" + name + "'"

            with connection.cursor() as cursor:
                # Read a single record
                cursor.execute(sql)
                result = cursor.fetchall()
                self.log.info("Query Successfully Ran")

            new_row = []
            for record in result:
                new_row.append(record['Locator'])
                new_row.append(record['LocatorType'])
                self.log.info("Data Retrieved with: " + tablename + " and Name: " + name)
            return new_row

        except:
            self.log.error("Can't run Query")


        finally:
            connection.close()

    def DBText(self, tablename, name):
        """
        New Method
        tablename:
        name:
        :return: Name column from the database
        """
        # Connect to the database
        connection = pymysql.connect(host='localhost',
                                     user='bilal',
                                     password='Bilal@123',
                                     db='testing',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        self.log.info("Connection Established with DB")
        try:
            sql = "SELECT Name FROM " + tablename + " WHERE Name = '" + name + "'"

            with connection.cursor() as cursor:
                # Read a single record
                cursor.execute(sql)
                result = cursor.fetchall()
                self.log.info("Query Successfully Ran")

            new_row = []
            for record in result:
                new_row.append(record['Name'])
                self.log.info("Data Retrieved with: " + tablename + " and Name: " + name)
            return new_row

        except:
            self.log.error("Can't run Query")


        finally:
            connection.close()
