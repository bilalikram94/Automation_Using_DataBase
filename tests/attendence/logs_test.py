import pytest
import unittest
from pages.attendence.logs import Logs
from ddt import ddt, data, unpack
from utilities.read_data import getCVSData


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class TestLogs(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lg = Logs(self.driver)

    @pytest.mark.run(order=1)
    @data(*getCVSData("/home/bilalikram/PycharmProjects/Automation_Using_Database/logs.csv"))
    @unpack
    def test_Logs(self, tablename, name, tablename1, name1, tablename2, name2, tablename3, name3, tablename4, name4, tablename5, name5, tablename6, name6, tablename7, name7, tablename8, name8):
        self.lg.LogsSmoke(tablename, name, tablename1, name1, tablename2, name2, tablename3, name3, tablename4, name4, tablename5, name5, tablename6, name6, tablename7, name7, tablename8, name8)

    @pytest.mark.run(order=2)
    @data(*getCVSData("/home/bilalikram/PycharmProjects/Automation_Using_Database/logsText.csv"))
    @unpack
    def test_LogsText(self, logs1, logs, logs2, name, logs3, datetime, logs4, status, logs5, absentees, logs6, detail):
        self.lg.LogsText(logs1, logs, logs2, name, logs3, datetime, logs4, status, logs5, absentees, logs6, detail)

