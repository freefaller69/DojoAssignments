var i = 1;
var penny = 0.01;
while (i <= 30) {
  penny = penny * 2;
  i++;
}
console.log(penny);

var i = 1;
var penny = 0.01;
while (i <= 30) {
  penny = penny * 2;
  i++;
  if (penny >= 10000) {
    console.log(i);
  }
}
console.log(penny);

var i = 1;
var penny = 0.01;
while (penny <= 1000000000) {
  penny = penny * 2;
  i++;
}
console.log(i);
console.log(penny);

var i = 1;
var penny = 0.01;
while (penny < Infinity) {
  penny = penny * 2;
  i++;
}
console.log(i);
