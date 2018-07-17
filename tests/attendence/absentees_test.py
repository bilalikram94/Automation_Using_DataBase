import pytest
import unittest
from pages.attendence.absentees import Absentees
from ddt import ddt, data, unpack
from utilities.read_data import getCVSData


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class TestAbsentees(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.abs = Absentees(self.driver)

    @pytest.mark.run(order=1)
    @data(*getCVSData("/home/bilalikram/PycharmProjects/Automation_Using_Database/absenteesPath.csv"))
    @unpack
    def test_Absentees(self, AbsenteesT, absentees, Absentees1, logsC, Absentees2, detail, Absentees3, moreoptions, Absentees4, searchbar, Absentees5, addnew, Absentees6, table, Absentees7, table1):
        self.abs.absenteesSmoke(AbsenteesT, absentees, Absentees1, logsC, Absentees2, detail, Absentees3, moreoptions, Absentees4, searchbar, Absentees5, addnew, Absentees6, table, Absentees7, table1)


    @pytest.mark.run(order=2)
    @data(*getCVSData("/home/bilalikram/PycharmProjects/Automation_Using_Database/absenteesText.csv"))
    @unpack
    def test_AbsenteesText(self, absentees, absenteesC, absentees1, detail, absentees2, logs, absentees3, department, absentees4, name, absentees5, phone1, absentees6, phone2):
        self.abs.AbsenteesText(absentees, absenteesC, absentees1, detail, absentees2, logs, absentees3, department, absentees4, name, absentees5, phone1, absentees6, phone2)
