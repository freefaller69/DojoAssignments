function fib() {
  // Some variables here
  var fb = 0;
  var first = 0;
  var second = 1;
  function nacci() {
    // do something to those variables here
    if(fb === 0){
      console.log("fb: " + second);
      fb = second;
    } else {
    fb = first + second;
    first = second;
    second = fb;
    console.log("fb: " + fb);
    }
  }
  return nacci;
}
var fibCounter = fib();
fibCounter();
fibCounter();
fibCounter();
fibCounter();
fibCounter();
fibCounter();
