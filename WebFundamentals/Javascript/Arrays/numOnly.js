function numOnly(arr) {
  var newArray = [];
  for (i = 0; i < arr.length; i++) {
    if (typeof arr[i] === "number") {
      newArray.push(arr[i]);
    }
  }
  console.log(newArray);
}
test = [1, "apple", -3, "orange", 0.5];
numOnly(test);

function numOnly(arr) {
  for (i = 0; i < arr.length; i++) {
    if (typeof arr[i] !== "number") {
      arr[i] = "";
    }
  }
  console.log(arr);
}
test = [1, "apple", -3, "orange", 0.5];
numOnly(test);
