const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const app = express();
const Wolf = require('../src/wolf');

mongoose.Promise = global.Promise;
mongoose.connect('mongodb://localhost/wolves');
mongoose.connection.on('connected', () => {
  console.log('connected to wolvesDB')
});

module.exports = function Route(app, server){

  app.get('/', function(req, res){
    Wolf.find({})
      .then(function(wolves){
        res.render('../views/index', { wolves });
      })
      .catch(function(error){
        console.log(error);
      });
  });

  app.get('/wolves/new', function(req, res){
    res.render('../views/new');
  });

  app.post('/wolves', function(req, res){
    console.log(req.body);
    Wolf.create(req.body)
      .then((wolf) => {
        console.log(wolf);
        res.redirect('/')
      })
      .catch((error) => {
        response.render('wolves/new', {
          errors: Object.keys(error.errors)
            .map(errorKey => error.errors[errorKey].message)
        });
      });
  });





}
