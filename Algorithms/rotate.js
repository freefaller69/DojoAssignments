function rotate(arr, shiftBy) {
  var count = 0;
  var x = arr.length;
  if(shiftBy < 0){
    shiftBy = x + shiftBy;
  }
  console.log("step 1 = " + arr);
  // pushes front to end of array
  for (var i = 0; i < x - shiftBy ; i++){
    arr.push(arr[i]);
    count++;
  }
  console.log("count = " + count);
  console.log("step 2 = " + arr);
  // resorts array to move all values left
  for (var j = 0; j < x; j++){
    arr[j] = arr[j + count];
  }
  console.log("step 3 = " + arr);
  // removes dupes at end
  var adj = arr.length - x;
  console.log("adj = " + adj);
  while(count > 0){
    arr.length--;
    count--;
  }
  console.log("arr = " + arr);
}
rotate([1,2,3,4,5,6,7],3);
