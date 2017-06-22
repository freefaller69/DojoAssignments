$( document ).ready(function() {
  var game = {
    players: [],
    addPlayer: function(name){
      this.players.push(playerConstructor(name));
    }
  };
  function playerConstructor(name){
    player = {};
    player.id = game.players.length + 1;
    player.name = name;
    player.hand = [];
    player.addCard = function(card){
      player.hand.push(card);
    };

    return player;
  }

    //create a card
  function cardConstructor() {
    card = {};
    var randPokemon = Math.floor(Math.random() * 151 + 1);
    $.ajax({url: `http://pokeapi.co/api/v1/pokemon/${ randPokemon }`, success: function(result){
      card.img = `http://pokeapi.co/media/img/${ randPokemon }.png`;
      card.name = result.name;
      card.defense = result.defense;
      card.attack = result.attack;
    }});
    //console.log(card);
    return card;
  }
    // Add players to the game when button is clicked
    $( '#add_player' ).click(function(event){
      //hide form when 2 players have been added.
      if ( game.players.length === 1 ) {
        $( "#player_form" ).hide();
        $( 'header' ).append( '<a id="playGame" href="#">Time to Play!</a>' );
      }
      //add the player to the game
      game.addPlayer( $( "#player_name" ).val() );
      var newPlayer = game.players[game.players.length-1];
      console.log(newPlayer);
      $( '#playersAdded' ).append( `<div id="player${ newPlayer.id }"><h2>Player: ${ newPlayer.name }</h2></div>` );
      console.log(player.name);
    });

    // Get the addCard button element for each player when the game is started
    $( document ).on( 'click', '#playGame', function(event) {
      $( '#playGame' ).hide();
      $(  '#player1' ).append('<div><button id="addCardP1">Get Card</button></div>');
      $(  '#player2' ).append('<div><button id="addCardP2">Get Card</button></div>');
    });

    $( document ).on( 'click', '#addCardP1', function(event) {
      console.log(player.name);
      var newCard1 = cardConstructor();
      console.log(newCard1);
      game.players[0].addCard(newCard1);
      console.log(game.players[0].hand);
      $( '#player1' ).append( `<div class="card"><h3>${ game.players[0].hand[0]['name'] }</h3></div>` );
    })

    $( document ).on( 'click', '#addCardP2', function(event) {
      console.log(player.name);
      var newCard2 = cardConstructor();
      game.players[1].addCard(newCard2);
      $( '#player2' ).append( `<div class="card"><h3>${ game.players[1].hand[0]['name'] }</h3></div>` );
    })






});
