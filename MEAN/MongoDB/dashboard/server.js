const express = require('express');
const path = require('path');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const Wolf = require('./src/wolf');

const app = express();

const port = process.env.PORT || 8000;

app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static(path.join(__dirname, './static')));

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, './views'));


mongoose.connect('mongodb://localhost/wolves');
mongoose.connection.on('connected', () => {
  console.log('connected to wolvesDB')
});


  app.get('/', function(req, res){
    Wolf.find({})
      .then(function(wolves){
        res.render('../views/index', { wolves });
      })
      .catch(function(error){
        console.log(error);
      });
  });

  app.get('/wolves/:id', function(req, res){
    Wolf.find({ _id: req.params.id })
      .then(function(wolves){
        res.render('../views/show', { wolf: wolves[0] });
      })
      .catch(function(error){
        console.log(error);
      });
  });

  app.get('/wolves/:id/edit', function(req, res){
    Wolf.find({ _id: req.params.id })
      .then(function(wolves){
        res.render('../views/edit', { wolf: wolves[0] });
      })
      .catch(function(error){
        console.log(error);
      });
  });

  app.post('/wolves/:id', function(req, res){
    Wolf.update({ _id: req.params.id }, req.body)
      .then(function(wolves){
        res.redirect('/');
      })
      .catch(function(error){
        console.log(error);
      });
  });

  app.get('/wolves/new', function(req, res){
    res.render('../views/new');
  });

  app.post('/wolves', function(req, res){
    Wolf.create(req.body)
      .then((wolf) => {
        res.redirect('/')
      })
      .catch((error) => {
        response.render('wolves/new', {
          errors: Object.keys(error.errors)
            .map(errorKey => error.errors[errorKey].message)
        });
      });
  });

  app.post('/wolves/:id/delete', function(req, res){
    Wolf.remove({ _id: req.params.id })
      .then(function(wolves){
        res.redirect('/');
      })
      .catch(function(error){
        console.log(error);
      });
  });

app.listen(port, function(){
  console.log('listening on port ' + port);
});
