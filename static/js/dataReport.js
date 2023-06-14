
function dateValidator() {
    var startDate = document.getElementById('start-date').value;
    var endDate = document.getElementById('end-date').value;
    
    if (startDate === '' || endDate === '') {
        alert('Start and end dates are required.');
        console.log('Start and end dates are required.');
        return false;
    }

    // Validate end date before start date
    var startTimestamp = Date.parse(startDate);
    var endTimestamp = Date.parse(endDate);
    if (endTimestamp < startTimestamp) {
        alert('End date should be after the start date.');
        console.log('End date should be after the start date.');
        return false;
    }

    return true;
}
function generateData(parent) {
    var startDate = document.getElementById('start-date').value;
    var endDate = document.getElementById('end-date').value;
    var incomeType = document.getElementById('income-filter').value;
    var data = {
        startDate: startDate,
        endDate: endDate,
        incomeType: incomeType
    };


    fetch('/get_data_to_report', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
        .then(function (response) {
            if (response.ok) {
                return response.json(); // Parse the response as JSON
            }
            throw new Error('Failed to send cancellation request.');
        })
        .then(function (dataList) {
            // Handle the data
            var body = document.createElement('tbody');
            dataList.forEach(data => {
                var row = document.createElement('tr');
                var td = document.createElement('td');
                td.textContent = data['id']
                td.classList.add('table-cell');
                row.appendChild(td)
                var td = document.createElement('td');
                td.textContent = data['traineeID']
                row.appendChild(td)
                var td = document.createElement('td');
                td.textContent = data['date_of_payment']
                row.appendChild(td)
                var td = document.createElement('td');
                td.textContent = data['amount'] + "₪"
                row.appendChild(td)
                if (data.hasOwnProperty('productID')) {
                    var td = document.createElement('td');
                    td.textContent = data['productID']
                    row.appendChild(td)
                }
                if (data.hasOwnProperty('membershipID')) {
                    var td = document.createElement('td');
                    td.textContent = data['membershipID']
                    row.appendChild(td)
                }
                console.log(data)

                body.appendChild(row)
            });
            parent.appendChild(body)

            // You can perform any additional actions with the data here if needed
        })
        .catch(function (error) {
            // Handle error
            console.error(error.message);
            // You can display an error message or perform any additional error handling here
        });
}

function createTable() {
    if (dateValidator()) {
        var table = document.getElementById('report-table')
        var exportExcel = document.getElementById('export-button')

        if (table.classList.contains('show-table')) {
            table.classList.remove('show-table')
            table.classList.add('hide-table')
            exportExcel.classList.remove('show-table')
            exportExcel.classList.add('hide-table')
        } else if (table.classList.contains('hide-table')) {
            table.classList.remove('hide-table')
            table.classList.add('show-table')
            exportExcel.classList.remove('hide-table')
            exportExcel.classList.add('show-table')

            table.innerHTML = ""
            var headline = document.createElement('caption')
            table.appendChild(headline)
            var head = document.createElement('thead')
            var headRow = document.createElement('tr')
            var option = document.getElementById('income-filter')
            if (option.value === 'mem_plans') {
                var headlineContent = 'Revenue from Membership Plans'
                var columns = ['Payment ID', 'Trainee Name', 'Date Of Payment', 'Amount', 'Plan Type']
            } else if (option.value === 'branded') {
                var headlineContent = 'Revenue from Branded Merchandise'
                var columns = ['Payment ID', 'Trainee Name', 'Date Of Payment', 'Amount', 'Product Name']
            } else {
                var headlineContent = 'All Revenue'
                var columns = ['Payment ID', 'Trainee Name', 'Date Of Payment', 'Amount', 'Product Name', 'Plan Type']
            }
            headline.textContent = headlineContent
            columns.forEach(function (column) {
                var th = document.createElement('th')
                th.textContent = column
                headRow.appendChild(th)
            })
            head.appendChild(headRow)
            table.append(head)
            generateData(table)
        }
    } else {
        console.log('Can not show table')
    }
} 

function exportToExcel() {
    var startDate = document.getElementById('start-date').value;
    var endDate = document.getElementById('end-date').value;
    var incomeType = document.getElementById('income-filter').value;
    var data = {
      startDate: startDate,
      endDate: endDate,
      incomeType: incomeType
    };
  
    fetch('/get_report_csv', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    })
      .then(function (response) {
        if (response.ok) {
          return response.blob(); // Parse the response as a Blob object
        }
        throw new Error('Failed to send the request.');
      })
      .then(function (blob) {
        // Create a temporary anchor element to trigger the download
        var now = new Date();
        var year = now.getFullYear();
        var month = String(now.getMonth() + 1).padStart(2, "0");
        var day = String(now.getDate()).padStart(2, "0");
        var hours = String(now.getHours()).padStart(2, "0");
        var minutes = String(now.getMinutes()).padStart(2, "0");
        var timestamp = `${year}-${month}-${day}_${hours}-${minutes}`;
        var filename = "report_" + timestamp + ".csv";
        var link = document.createElement('a');
        link.href = URL.createObjectURL(blob);
        link.download = filename;
        link.click();
        URL.revokeObjectURL(link.href);
  
        // You can perform any additional actions after the download here if needed
      })
      .catch(function (error) {
        // Handle error
        console.error(error.message);
        // You can display an error message or perform any additional error handling here
      });
  }