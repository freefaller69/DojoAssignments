function runningLogger(){
  console.log("I am running!");
}
runningLogger();

function multiplyByTen(a){
  var result = a * 10;
  return result;
}
console.log(multiplyByTen(11));

function stringReturnOne(){
  var str1 = "What is the airspeed velocity of a cocanut laden swallow?";
  console.log(str1);
  return str1;
}
function stringReturnTwo(){
  var str2 = "I didn't expect the Spanish Inquisition.";
  console.log(str2);
  return str2;
}
stringReturnOne();
stringReturnTwo();

function caller(param){
  if (typeof(param)=='function'){
    param();
  }
}
caller(runningLogger);

function myDoubleConsoleLog(param1,param2){
  if (typeof(param1)=='function' && typeof(param2)=='function'){
    console.log(param1(),param2());
  }
}
myDoubleConsoleLog(stringReturnOne,stringReturnTwo);

function caller2(param){
  console.log('starting');
  var x = setTimeout(function(){
    if (typeof(param)=='function'){
      param(stringReturnOne,stringReturnTwo);
    }
  }, 2000);
console.log('ending');
return "Interesting";
}
caller2(myDoubleConsoleLog);
