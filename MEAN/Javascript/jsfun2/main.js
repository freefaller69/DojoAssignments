function sumRange(x,y){
  var sum = 0;
  for(var i = x; i <= y; i++){
    sum+=i;
  }
  console.log(sum);
  return sum;
}
sumRange(5,10);

function findMin(arr){
  min = arr[0];
  for(var i = 0; i < arr.length; i++){
    if(arr[i] < min){
      min = arr[i];
    }
  }
  return min;
}
myArr = [1, 5, 90, 25, -3, 0];
console.log(findMin(myArr));

function getAvg(arr){
  var avg;
  var sum = 0;
  for(i = 0; i < arr.length; i++){
    sum+=arr[i];
  }
  avg = sum/arr.length;
  return avg;
}
avgArr = [1, 5, 90, 25, -3, 0];
console.log(getAvg(avgArr));

var rangeSum = function (x,y){
  var sum = 0;
  for(var i = x; i <= y; i++){
    sum+=i;
  }
  return sum;
};
console.log(rangeSum(5,10));

var minNum = function (arr){
  min = arr[0];
  for(var i = 0; i < arr.length; i++){
    if(arr[i] < min){
      min = arr[i];
    }
  }
  return min;
};
myArr = [1, 5, 90, 25, -3, 0];
console.log(minNum(myArr));

var avg = function (arr){
  var avg;
  var sum = 0;
  for(i = 0; i < arr.length; i++){
    sum+=arr[i];
  }
  avg = sum/arr.length;
  return avg;
};
avgArr = [1, 5, 90, 25, -3, 0];
console.log(avg(avgArr));

var obj = {
  rangeSum: function (x,y){
  var sum = 0;
  for(var i = x; i <= y; i++){
    sum+=i;
  }
  return sum;
},
  minNum: function (arr){
  var min = arr[0];
  for(var i = 0; i < arr.length; i++){
    if(arr[i] < min){
      min = arr[i];
    }
  }
  return min;
},
  avg: function (arr){
  var avg;
  var sum = 0;
  for(i = 0; i < arr.length; i++){
    sum+=arr[i];
  }
  avg = sum/arr.length;
  return avg;
}};
avgArr = [1, 5, 90, 25, -3, 0];

var person = {};
person = {
  name : 'Michael',
  distance_traveled: 0,
  say_name : function(){
    console.log(person.name);
  },
  say_something : function(phrase){
    console.log('${person.name} says ${phrase}');
  },
  walk : function(){
    console.log('${person.name} is walking!');
    person.distance_traveled += 3;
    return person;
  },
  run : function(){
    console.log('${person.name} is running!');
    person.distance_traveled += 10;
    return person;
  },
  crawl : function(){
    console.log('${person.name} is crawling!');
    person.distance_traveled += 1;
    return person;
  },
};
