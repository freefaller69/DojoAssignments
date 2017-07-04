require('dotenv').load();

const express = require('express');
const path = require('path');
const parse = require('body-parser');
const port = process.env.PORT || 8000;
const mongoose = require('mongoose');

// object destructing finds propterty Schema on object mongoose
// const Schema = mongoose.Schema;
const { Schema } = mongoose;
const app = express();

app.set('view engine', 'ejs');
app.set('views', path.resolve('views'));

app.use(parse.urlencoded({extended: true}));
mongoose.connect('mongodb://localhost/books');

mongoose.connection.on('connected', () => console.log('Connected to booksDB'));

const authorSchema = new Schema({
  name: {
    type: String,
    required: true,
    minlength: 2,
    trim: true
  },
  age: Number,
  isAlive: {
    type: Boolean,
    default: true
  },
  books: [
    {
      type: Schema.Types.ObjectId,
      ref: 'Book'
    }
  ]
});

const bookSchema = new Schema({
  title: {
    type: String,
    required: true,
    trim: true
  },
  pageCount: Number,
  year: Number,
  author: {
    type: Schema.Types.ObjectId,
    ref: 'Author'
  }
});

const Author = mongoose.model('Author', authorSchema);
const Book = mongoose.model('Book', bookSchema);

app.get('/', function (request, response) {
  response.redirect('/authors');
});

app.get('/authors', function (request, response) {
  Author.find({}, function (error, authors) {
    if(error){
      throw error;
    }
    response.render('authors/index', { authors });
  })
});

app.get('/authors/new', function (request, response) {
  response.render('authors/new');
});

app.post('/authors', function (request, response) {
  console.log(request.body);
  Author.create(request.body)
    .then(function(author) {
      response.redirect('/authors');
    })
    .catch(function(error) {
      response.redirect('/authors');
    })
});






app.listen(port, () => console.log(`Listening to server on port ${ port }`));
