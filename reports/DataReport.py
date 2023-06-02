import datetime

class DataReport:
    def __init__(self, connector, reportID, dateCreated, summary):
        self.reportID = reportID
        self.dateCreated = datetime.date.today()
        self.summary = summary
        self.connector = connector

    def generate_report(self, month, year):
        year = year[:4]
        month = month[5:7]
        sql = "SELECT * FROM Payment WHERE YEAR(dateOfPayment) = ? AND MONTH(dateOfPayment) = ?"
        values = (year, month)
        result = self.connector.execute_query(sql, values)

        # Check if the result is None or empty
        if not result:
            print("No payments found for the specified month.")
            return []  # Return empty list if no payments found

        # Process the result to create the report data
        report_data = []
        for row in result:
            paymentID = row[0]
            amount = row[1]
            dateOfPayment = row[2]
            paymentStatus = row[3]
            customerID = row[4]
            membershipID = row[5] if row[5] is not None else None
            productID = row[6] if row[6] is not None else None

            # Add the payment information to the report data
            payment_info = {
                'paymentID': paymentID,
                'amount': amount,
                'dateOfPayment': dateOfPayment,
                'paymentStatus': paymentStatus,
                'customerID': customerID,
                'membershipID': membershipID,
                'productID': productID
            }
            report_data.append(payment_info)

        return report_data




    def generateReport(self, reportID):
        pass
    def getReportViewing(self, reportID):
        pass
    def setReportUpdating(self, reportID):
        pass
