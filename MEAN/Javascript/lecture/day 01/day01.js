var counter;

function counter(){
  var count = 0;

  function childCounter(){
    count++;
    return count;
  }
  return childCounter;
}

counter = counter();
console.log(counter());
console.log(counter());
console.log(counter());
console.log(counter());
