import datetime
from app import db

class DataReport:
    def __init__(self, reportID, dateCreated, summary):
        self.reportID = reportID
        self.dateCreated = datetime.date.today()
        self.summary = summary

    def generateReport(self, reportID):
        pass
    def getReportViewing(self, reportID):
        pass
    def setReportUpdating(self, reportID):
        pass
