function fancyArray(arr, sym) {
  if (sym === "") {
    sym = "->";
  }
  for (i = 0; i < arr.length; i++) {
    console.log(i + " " + sym + " " + arr[i]);
  }
}
var arr = ["James", "Jill", "Jane", "Jack"];
var sym = "=+=";
fancyArray(arr, sym);
