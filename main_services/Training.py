import datetime

class Training:
    def __init__(self, connector, trainingID, trainingType, capacity, duration, trainingDescription):
        self.trainingID = trainingID
        self.trainingType = trainingType
        self.capacity = capacity
        self.duration = duration
        self.trainingDescription = trainingDescription
        self.connector=connector

        sql= "INSERT INTO Training (trainingID, trainingType, capacity, duration, trainingDescription ) VALUES (?, ?, ?, ?, ?)"
        values = (self.trainingID, self.trainingType, self.capacity, self.duration, self.trainingDescription)
        self.connector.execute_query(sql, values)

    def set_trainingID(self, trainingID):
        sql = "UPDATE Training SET trainingID=? WHERE trainingID=?;"
        values = (trainingID, self.trainingID)
        self.connector.execute_query(sql, values)
        self.trainingID = trainingID  

    def delete(self):
        sql = "DELETE FROM Training WHERE trainingID=?;"
        self.connector.execute_query(sql, self.trainingID)
  
        
        
        
        
        
        
        
        
        
        
        
        
   

    def getTrainer(self, Trainer):
        pass
    def setTrainer(self, Trainer):
        pass
    def getCapacity(self, capacity):
        pass
    def setCapacity(self, capacity):
        pass










