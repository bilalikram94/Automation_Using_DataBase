import pytest
import unittest
from pages.sidemenu.side_menu import SideMenu
from ddt import ddt, data, unpack
from utilities.read_data import getCVSData
"""
when using pytest the test cases must start with test_("testname") and the test must start with small 't' otherwise 
the test will not be collected 
"""


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class TestSideMenu(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.sm = SideMenu(self.driver)

    @pytest.mark.run(order=1)
    @data(*getCVSData("/home/bilalikram/PycharmProjects/Automation_Using_Database/sideMenuSmoke.csv"))
    @unpack
    def test_SideMenu(self, side, sidemenu, side1, attendance, side2, emp, side3, support, side4, train, side5,
                      timeoff):
        self.sm.SideMenuSmoke(side, sidemenu, side1, attendance, side2, emp, side3, support, side4, train, side5,
                              timeoff)

    @pytest.mark.run(order=2)
    @data(*getCVSData("/home/bilalikram/PycharmProjects/Automation_Using_Database/sidemenuText.csv"))
    @unpack
    def test_Side(self, side, attendance, side1, emp, side2, support, side3, train, side4, timeoff):
        self.sm.SideMenuText(side, attendance, side1, emp, side2, support, side3, train, side4, timeoff)
