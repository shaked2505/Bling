from datetime import date, time
class SpecificTimeTraining:
    def __init__(self, connector, specificTimeTrainingDate, trainingID, startTime, endTime, standByTrainer, registeredTrainees):
        self.specificTimeTrainingDate = specificTimeTrainingDate
        self.trainingID = trainingID
        self.startTime = startTime
        self.endTime = endTime
        self.standByTrainer = standByTrainer
        self.registeredTrainees = registeredTrainees
        self.connector = connector

        sql= "INSERT INTO SpecificTimeTraining (specificTimeTrainingDate, trainingID, startTime, endTime, standByTrainer, registeredTrainees ) VALUES (?, ?, ?, ?, ?, ?)"
        values = (self.specificTimeTrainingDate, self.trainingID, self.startTime, self.startTime, self.endTime, self.standByTrainer, self.registeredTrainees )
        self.connector.execute_query(sql, values)

    def set_specificTimeTrainingID(self, specificTimeTrainingID, specificTimeTrainingDate, trainingID):
        sql = "UPDATE SpecificTimeTraining SET specificTimeTrainingID=? WHERE specificTimeTrainingDate=? AND trainingID=?;"
        values = (specificTimeTrainingID, specificTimeTrainingDate, trainingID)
        self.connector.execute_query(sql, values)
        self.specificTimeTrainingID = specificTimeTrainingID


    def delete(self):
        sql = "DELETE FROM SpecificTimeTraining WHERE specificTimeTrainingDate=? AND trainingID=?;"
        values = (self.specificTimeTrainingDate, self.trainingID)
        self.connector.execute_query(sql, values)

    def getStartTime(self, startTime):
        pass
    def setStartTime(self, startTime):
        pass
    def getEndTime(self, endTime):
        pass
    def setEndTime(self, endTime):
        pass
    def updateStandByTrainer(self, standByTrainer):
        pass
    def getRegisteredTrainees(self, registeredTrainees):
        pass



