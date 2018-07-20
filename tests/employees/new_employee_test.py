import pytest
import unittest
from pages.employees.new_employee import NewEmployee
from utilities.read_data import getCVSData
from ddt import ddt,data,unpack


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class TestNewEmployee(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.nemp = NewEmployee(self.driver)

    @pytest.mark.run(order=1)
    @data(*getCVSData("/home/bilalikram/PycharmProjects/Automation_Using_Database/newEmployee.csv"))
    @unpack
    def test_NewEmployee(self, newemp, name, newemp1, lname, newemp2, empcard, newemp3, gender, newemp4, doj, newemp5,
                         depart, newemp6, design, newemp7, report, newemp8, tax, newemp9, urole, newemp10, policy):
        self.nemp.NewEmployeeSmoke(newemp, name, newemp1, lname, newemp2, empcard, newemp3, gender, newemp4, doj,
                                   newemp5, depart, newemp6, design, newemp7, report, newemp8, tax, newemp9, urole,
                                   newemp10, policy)
