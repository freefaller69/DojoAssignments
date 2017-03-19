function rangePrint(start, end, skip) {
  if (skip === "") {
    skip = 1;
  }
  if (end === "") {
    end = start;
    start = 0;
  }
  for (i = start; i < end; i+=skip) {
    console.log(i);
  }
  console.log("xxxxxxxxxxxxxxxxxxxxxx");
}
rangePrint(2, 10, 2);
rangePrint(-17, 10, 3);
rangePrint(5, 100, 11);
