import pytest
import unittest
from pages.employees.employees import Employees
from ddt import ddt, data, unpack
from utilities.read_data import getCVSData


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class TestEmployees(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.emp = Employees(self.driver)

    @pytest.mark.run(order=1)
    @data(*getCVSData("/home/bilalikram/PycharmProjects/Automation_Using_Database/employeeSmoke.csv"))
    @unpack
    def test_Employees(self, emp, pageheader, emp1, newemp, emp2, searchbar):
        self.emp.EmployeesSmoke(emp, pageheader, emp1, newemp, emp2, searchbar)

    @pytest.mark.run(order=2)
    @data(*getCVSData("/home/bilalikram/PycharmProjects/Automation_Using_Database/employeepagetext.csv"))
    @unpack
    def test_TextEmployee(self, emp, newemp, emp1, name, emp2, designation, emp3, department, emp4, location, emp5,
                          status):
        self.emp.TextEmployee(emp, newemp, emp1, name, emp2, designation, emp3, department, emp4, location, emp5,
                              status)
