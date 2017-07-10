const myString = 'string';
const myNumber = 34;

let index: number;

index = 37

const array = [1, '2'];
const first: number = <number>array[0];  // typecasting - <number> or <string> or what have you

const myArray: (number | string | boolean)[] = [1, '2'];

class User implements IUser {
    username: string;
    email: string;
    password: string;
}

interface IUser extends ILogin {
    username: string;
}

interface ILogin {
    email: string;
    password: string;
}

class Person extends User {
    name: string;
}

function add(num1: number, num2: number): number {
    return num1 + num2;
}

function map<T, TResult>(array: T[], callback: (element: T, index?: number) => TResult): TResult[] {
    const results: TResult[] = [];

    for(let index = 0; index < array.length; index++) {
        results.push(callback(array[index], index));
    }
    return results;
}

const stringArray: string[] = ['1', '2', '3', '4', '5', '6'];
const numberArray: number[] = map(stringArray, function(element){
    return parseInt(element, 10);
});