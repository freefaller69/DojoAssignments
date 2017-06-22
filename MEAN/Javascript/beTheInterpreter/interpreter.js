console.log(first_variable);
var first_variable = "Yipee I was first!";
function firstFunc() {
  first_variable = "Not anymore!!!";
  console.log(first_variable);
}
console.log(first_variable);

//declarations get hoisted
var first_variable;
function firstFunc() {
  first_variable = "Not anymore!!!";
  console.log(first_variable);
}
//assignments and invocation maintain order
console.log(first_variable);
first_variable = "Yipee I was first!";
firstFunc();
console.log(first_variable);

// ************************************************

var food = "Chicken";
function eat() {
  food = "half-chicken";
  console.log(food);
  var food = "gone";       // CAREFUL!
  console.log(food);
}
eat();
console.log(food);

//declarations get hoisted
var food;
function eat(){
  var food;
  food = "half-chicken";
  console.log(food);
  food = "gone";       // CAREFUL!
  console.log(food);
}
eat();
console.log(food);

//assignments and invocation maintain order
food = "Chicken";
eat();
console.log(food);

// ************************************************

var new_word = "NEW!";
function lastFunc() {
  new_word = "old";
}
console.log(new_word);

//declarations get hoisted
var new_word;
function lastFunc() {
  new_word = "old";
}
new_word = "NEW!";
console.log(new_word);

//assignments and invocation maintain order
new_word = "NEW!";
lastFunc();
console.log(new_word);
