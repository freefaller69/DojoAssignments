function Card(value,suit){
  this.value = value;
  this.suit = suit;
  this.cardName = value + " of " + suit;
}

function Deck(){
  this.createDeck();
}

Deck.prototype.createDeck = function (){
  this.cards = [];

  var suits = ["diamonds", "hearts", "spades", "clubs"];
  var values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"];

  for(i = 0; i < suits.length; i++){
    for(j = 0; j < values.length; j++){
      this.cards.push(new Card(values[j],suits[i]));
    }
  }
  return this;
};

Deck.prototype.shuffle = function(){
  var unshuffled = this.cards.length, cardIdx, temp;

  while (unshuffled > 0) {
    cardIdx = Math.floor(Math.random() * unshuffled);
    unshuffled -= 1;

    temp = this.cards[cardIdx];
    this.cards[cardIdx] = this.cards[unshuffled];
    this.cards[unshuffled] = temp;
  }
  return this;
};

Deck.prototype.dealCard = function(){
  if(this.cards.length > 0){
    return this.cards.pop();
  }
};

Deck.prototype.reset = function(){
  this.createDeck().shuffle();
};

function Player(name){
  this.name = name;
  this.hand = [];
}

Player.prototype.takeCard = function(){
  this.hand.push(deck.dealCard());
  return this;
};

Player.prototype.discard = function(playerCardIdx){
  if(this.hand.length > playerCardIdx){
    this.hand.splice(playerCardIdx, 1);
  }
  return this;
};

var Mikus = new Player('Mikus');
var deck = new Deck
