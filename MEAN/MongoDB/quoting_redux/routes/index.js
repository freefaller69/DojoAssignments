const Quote = require('../src/quote');
const express = require('express');
const app = express();
const mongoose = require("mongoose");

app.set('view engine', 'ejs');

mongoose.Promise = global.Promise;
mongoose.connect("mongodb://localhost/quotes");
mongoose.connection.on('connected', () => console.log('Connected to quotesDB'));

module.exports = function Route(app, server) {

  app.get('/', function (req, res) {
    res.render('index');
  });

  app.get('/all_quotes', function (req, res) {
    quotes = Quote.find().sort({createdAt: -1})
      .then((quotes) => {
        console.log(quotes);
        res.render('../views/quotes', { "quotes": quotes} );
      });
  });

  app.post('/quotes', function (req, res) {
    const new_quote = new Quote(req.body);
    new_quote.save();
    res.redirect('/all_quotes');
  });

};
