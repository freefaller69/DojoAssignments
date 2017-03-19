function randomChance(quarters, cutoff) {
  for (var q = quarters; q > cutoff; q--) {
    var r = (Math.floor(Math.random()*100)+1);
    if (r > 99) {
      var winnings = (Math.floor(Math.random() * 10) + 51);
      console.log("Your number was " + r + "!  You have won " + winnings + " quarters!");
      q+=winnings;
      console.log("You now have " + q + " quarters!");
    } else {
      console.log("You now have " + q + " quarters!");
      console.log("Your number was " + r + "!  Spin again!");
    }
  }
  console.log("Thanks for playing.  You have " + q + " quarters.");
}
var quarters = 1000;
var cutoff = 50;
randomChance(quarters, cutoff);
