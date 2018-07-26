import pytest
import unittest
from pages.support_ticket.support_ticket import SupportTicket
from utilities.read_data import getCVSData
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class TestSupportTicket(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.st = SupportTicket(self.driver)

    @pytest.mark.run(order=1)
    @data(*getCVSData("/home/bilalikram/PycharmProjects/Automation_Using_Database/supportTicket.csv"))
    @unpack
    def test_SupportTicket(self, support, tickets, support1, company, support2, search, support3, openT, support4,
                           ticket, support5, textSupport):
        self.st.SupportTicketSmoke(support, tickets, support1, company, support2, search, support3, openT, support4,
                                   ticket, support5, textSupport)
