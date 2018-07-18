import pytest
import unittest
from pages.attendence.details import Details
from ddt import ddt, data, unpack
from utilities.read_data import getCVSData


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class TestDetails(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.dt = Details(self.driver)

    @pytest.mark.run(order=1)
    @data(*getCVSData("/home/bilalikram/PycharmProjects/Automation_Using_Database/detailSmoke.csv"))
    @unpack
    def test_Details(self, detail, logs, detail1, absentees, detail2, searchbar, detail3, moreoptions, detail4, export, detail5, addnew, detail6, table, detail7, table1):
        self.dt.DetailsSmoke(detail, logs, detail1, absentees, detail2, searchbar, detail3, moreoptions, detail4, export, detail5, addnew, detail6, table, detail7, table1)

    @pytest.mark.run(order=2)
    @data(*getCVSData("/home/bilalikram/PycharmProjects/Automation_Using_Database/detailsText.csv"))
    @unpack
    def test_DetailsText(self, detail, day, detail1, date, detail2, timein, detail3, timeout, detail4, timespent, detail5, breaktime, detail6, worktime, detail7, absentees, detail8, detailC, detail9, logs, detail10, addnew, detail11, export):
        self.dt.DetailsVerifyText(detail, day, detail1, date, detail2, timein, detail3, timeout, detail4, timespent, detail5, breaktime, detail6, worktime, detail7, absentees, detail8, detailC, detail9, logs, detail10, addnew, detail11, export)
