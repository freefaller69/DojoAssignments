let myNum: number = 5;
let myString: string = "Hello Universe";
let myArr: number[] = [1,2,3,4];
const myObj = { name:'Bill'};
let anythingVariable: any = "Hey";
let anythingVariable: any = 25;
let arrayOne: boolean[] = [true, false, true, true];
let arrayTwo: any[] = [1, 'abc', true, 2];
let myObj: number = { x: 5, y: 10 };
// object constructor
class MyNode {(function () {
    function MyNode(val) {
        this.val = 0;
        this.val = val;
    }
    MyNode.prototype.doSomething = function () {
        this._priv = 10;
    };
    return MyNode;
}())};
let myNodeInstnace = new MyNode(1);
console.log(myNodeInstnace.val);
function myFunction(val: string) {
    console.log("Hello World");
    return;
}
function sendingErrors(message: string) {
	throw new Error('Error message');
}
