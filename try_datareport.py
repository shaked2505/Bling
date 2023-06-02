from reports.DataReport import DataReport
from DBConnector.DBFunctions import DBConnector
import datetime
import socket


# Create a DBConnector instance
connector = DBConnector(server=socket.gethostname(), database='BLING_System')
connector.connect()

# Create a DataReport instance
report = DataReport(connector, 1, datetime.date.today(), "Monthly Payments Report")

# Specify the desired month and year
month = "03"
year = "2023"

# Generate the payment report for the specified month and year
payment_report = report.generate_report(month, year)

# Print the payment report
for payment in payment_report:
    print(payment)

# Disconnect from the database
connector.disconnect()

