function CardConstructor(value,suit){
  this.value = value;
  this.suit = suit;
  this.cardName = value + " of " + suit;

  var suits = ["diamonds", "hearts", "spades", "clubs"];
  var values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"];
  deck = new Array(values.length * suits.length);
  for(i = 0; i < suits.length; i++){
    for(j = 0; j < values.length; j++){
      deck[j + i + values.length] = new Card(values[j],suits[i]);
    }
  }
}
