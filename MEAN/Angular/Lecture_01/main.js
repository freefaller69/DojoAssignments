var __extends = (this && this.__extends) || (function () {
    var extendStatics = Object.setPrototypeOf ||
        ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
        function (d, b) { for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p]; };
    return function (d, b) {
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var myString = 'string';
var myNumber = 34;
var index;
index = 37;
var array = [1, '2'];
var first = array[0]; // typecasting - <number> or <string> or what have you
var myArray = [1, '2'];
var User = (function () {
    function User() {
    }
    return User;
}());
var Person = (function (_super) {
    __extends(Person, _super);
    function Person() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    return Person;
}(User));
function add(num1, num2) {
    return num1 + num2;
}
function map(array, callback) {
    var results = [];
    for (var index_1 = 0; index_1 < array.length; index_1++) {
        results.push(callback(array[index_1], index_1));
    }
    return results;
}
var stringArray = ['1', '2', '3', '4', '5', '6'];
var numberArray = map(stringArray, function (element) {
    return parseInt(element, 10);
});
