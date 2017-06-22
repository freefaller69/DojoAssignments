var game = {
  players: [],
};

var Player = function(name){
  this.name = name;
  this.hand = [];
  return this;
};

Player.prototype.addCard = function(card){
  this.hand.push(card);
};

var dave = new Player("Dave");
var kate = new Player("Kate");
