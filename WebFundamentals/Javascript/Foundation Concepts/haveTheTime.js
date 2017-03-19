function haveTime() {
if (minute < 15) {
  frac = "It is about quarter after " + hour + period;
} else if (minute < 30) {
  frac = "It is just after " + hour + period;
} else if (minute === 30) {
  frac = "The time is half past " + hour + period;
} else if (minute > 30) {
  frac = "It is almost " + hour + period;
}
if (period === "AM") {
  dayPart = " in the morning.";
} else if (period === "PM" && hour < 5) {
  dayPart = " in the afternoon.";
} else if (period === "PM" && hour < 8) {
  dayPart = " in the evening.";
} else {
  dayPart = " at night.";
}
console.log(frac + dayPart);
}
var hour = 8;
var minute = 50;
var period = "AM";
haveTime(hour, minute, period);

var hour = 7;
var minute = 15;
var period = "PM";
haveTime(hour, minute, period);
