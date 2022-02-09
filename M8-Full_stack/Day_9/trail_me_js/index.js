 // comment 
 // console.log("hello world!");
// variable wit let keyword
let name = "Sivareddy";

let surname = "Bodapati"
let age =27; 
//console.log(name,surname);
// let isApproved = false // boolean literal
// let firstName = undefined;
// let isSelected = null;

// static and dynamic names where dynamic is we can overwrite it . but
// but when we use const instead of let no one can overwrite it.
let person = {
    name:"Babi",
    age:25,
};
// Dot notation
person.name ="John";

//Bracket notation
let selection ='name';
person[selection]='Siva';

person.surname ="Boda"
person["surname"] ="Bodapati"
console.log(person);

let selectColors = ['red','blue'];
selectColors[2]='greeen';
selectColors.push('pnk');
console.log(selectColors);

// function 
function greet(name) {
    console.log('hello '+ name);
}
greet('SivaReddy<>');
greet('Mr Bodapati<>');

function square(number) {
    return number*number;
}

let result = square(3);
console.log('result : ' +result);