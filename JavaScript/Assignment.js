/*Write a program in JavaScript to find the day exactly after 8 years from now and display that date in given order.

output:
    your_day
    date, <space>Month_in_alphabet<space>Full year
must use:
    date object method
    concatenation operator
    switch case
*/

var day_after_8_year = (current_day, current_date, current_month, current_year) => {
    "Function to count the future day month year"

    current_year = current_year + 8;

    /*Two year, leap year and remaining year normal year and I assume the each month is of 30 days and divide the added day of 8 years it by 3 to get remainder as in the form of day*/
    initial_date = current_date
    current_date = (initial_date + (3 * 12 + 2) * 2 + 6 * 3 * 12) % 3;

    /*For month*/
    (current_date < initial_date) ? (current_month = current_month + 1) : (current_month = current_month);


    /*In year there will be 51 weeks and 3 days according to 30 days in a year concept*/
    current_day = (current_day + 3 * 6 + 4 * 2) % 7;

    return [current_day, current_date, current_month, current_year]
}

var displayData = (date) => {
    "To display date in provided pattern"

    /*Printing data using concatenation operator*/
    console.log(getWeek(date[0]) + "\n" + date[1] + ", " + getMonth(date[2]) + " " + date[3])
}

/*Convert index month into string one*/
var getMonth = (monthIndex) => {
    "This function return the respective month name in the provided index."

    /*Switch case*/
    switch (monthIndex) {
        case 0:
            return "January"
        case 1:
            return "February"
        case 2:
            return "March"
        case 3:
            return "April"
        case 4:
            return "May"
        case 5:
            return "June"
        case 6:
            return "July"
        case 7:
            return "August"
        case 8:
            return "September"
        case 9:
            return "October"
        case 10:
            return "November"
        case 11:
            return "December"
    }
}

var getWeek = (weekIndex) => {
    "This function return the respective week name in the provided index."


    switch (weekIndex) {
        case 0:
            return "Sunday"
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
    }
}


/*Using Data Object Method*/
var new_date = new Date()

var current_day = new_date.getDay()
var current_data = new_date.getDate()
var current_month = new_date.getMonth()
var current_year = new_date.getFullYear()

console.log("Present Day: ")
displayData([current_day, current_data, current_month, current_year])

console.log("\n\nAfter 8 years...")
displayData(day_after_8_year(current_day, current_data, current_month, current_year))

/*I had used node to run this JavaScript files*/