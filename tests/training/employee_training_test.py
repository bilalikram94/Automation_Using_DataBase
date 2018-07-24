import pytest
import unittest
from pages.training.employee_training import Training
from ddt import ddt, data, unpack
from utilities.read_data import getCVSData


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class TestEmployeeTraining(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.et = Training(self.driver)

    @pytest.mark.run(order=1)
    @data(*getCVSData("/home/bilalikram/PycharmProjects/Automation_Using_Database/employeeTrainingText.csv"))
    @unpack
    def test_EmployeeTraining(self, train, search, train1, page, train2, emptrain, train3, evaluation, train4, trainers,
                              train5, events, train6, assess, train7, training, train8, traintype, train9, table,
                              train10,
                              train_frm, train11, train_to, train12, actions, train13, more_options):
        self.et.EmployeeTrainingSmoke(train, search, train1, page, train2, emptrain, train3, evaluation, train4,
                                      trainers, train5, events, train6, assess, train7, training, train8, traintype,
                                      train9, table, train10, train_frm, train11, train_to, train12, actions, train13,
                                      more_options)
