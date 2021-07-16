/*A function in java script*/
function cde() {

    /*Regular function with one d array*/
    const array = [1, 2, 3, 4, 5]

    for (items in array) {
        /*Items will store the index of element in the array*/
        console.log(array[items]);
    }

}

const abc = () => {
    /*Arrow function with two d array*/
    const array = [[1, 2, 3, 4, 1], [1, 2, 3, 4, 5]]

    for (number in array) {
        /*Number will store the index of element in the array*/

        console.log(array[number])
    }
}
/*Function call*/
cde()
abc()

/*Creating a javascript object*/
var obj = {
    fname: "Bikash",
    lname: "Sharma",
    age: 20
};
/*Printing value of obj in differents ways*/
console.log(obj.fname)
console.log(obj.lname)
console.log(obj.age)
console.log(obj["fname"])
console.log(obj["lname"])
console.log(obj["age"])

/*Printing using for in loop*/
for (value in obj) {
    console.log(typeof (obj[value])) //typeof() return the type of provided object
}

/*JavaScript string*/

var x = "Java Script is very  good language"

console.log(x.length) //----> return the length in integer
console.log(x.toLowerCase()) //----> return the string in lower case
console.log(x.toUpperCase()) //----> return the string in upper case
console.log(x.includes("Ja")) // -----> Checks whether it includes the Ja or not adn return booolen 
console.log(x.startsWith("is"))// -----> Check whether the string start with is or not  and return boolean*/
console.log(x.endsWith("  ")) //----> Check whether the string ends with provided sets of character and return boolean*/
console.log(x.search("Ja")) // -----> Search Ja in the string adn return its first string
console.log(x.match(/is/g))//-----> Match the is in the string and return the list containing the match */
console.log(x.indexOf("is"))// ----> Finds the index of first is
console.log(x.lastIndexOf("ge"))// ----> Finds the index of last ge in string*/
console.log(x.replace("is", "are"))// ----> Replace is by are in the string
console.log(x.charAt(30))// ----> Return the character present in the index 30 of the string*/

/*Creating of data object*/
var noe = new Date()
console.log(noe) //Prints the date
console.log(noe.toDateString()) //return date in string compare it with above line result
console.log(noe.getDate()) //Return day on month
console.log(noe.getHours())//Return the current hour
noe.setFullYear(201)// Set the year to 201
console.log(noe.getFullYear()) // Return the full year

// Array method
/*
pop -- take out from last
shift -- TAke out from front
unshift -- Add items to front
sort -- Sort the array
reverse --- reverse the array
slice -- take out some value from array
splice
join -- add provided items to each element of array
Array.isArray -- check whether the value passed is array or not
some -- call provided fucntion with value of array(must be number)
find --
findIndex --
filter --
map -
concat--
*/
