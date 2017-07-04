const express = require('express');
const path = require('path');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');

const Schema = mongoose.Schema;
const app = express();

const port = process.env.PORT || 8000;

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, './views'));

app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static(path.join(__dirname, './static')));

mongoose.connect('mongodb://localhost/dojoMessageBoard');

const messageSchema = new Schema({
  name: {
    type: String,
    required: [true, 'All messages must have a name to go with them'],
    minlength: [2, 'Name must be at least 2 characters in length'],
    trim: true
  },
  message: {
    type: String,
    required: [true, 'A blank message is not really a message'],
    minlength: [2, 'Message must be at least 2 characters in length'],
    trim: true
  },
  comments: [
    {
      type: Schema.Types.ObjectId,
      ref: 'Comment'
    }
  ],
}, {timestamps: true});

const commentSchema = new Schema({
  name: {
    type: String,
    required: [true, 'All comments must have a name to go with them'],
    minlength: [2, 'Name must be at least 2 characters in length'],
    trim: true
  },
  comment: {
    type: String,
    required: [true, 'A blank comment is not really a comment'],
    minlength: [2, 'Comment must be at least 2 characters in length'],
    trim: true
  },
  message: {
    type: Schema.Types.ObjectId,
    ref: 'Message'
  },
}, {timestamps: true});

const Message = mongoose.model('Message', messageSchema);
const Comment = mongoose.model('Comment', commentSchema);

app.get('/', function(req, res){
  Message.find({}).sort({createdAt: -1}).populate('comments').exec(function(error, messages){
    if(error){
      throw(error);
    }
    res.render('index', { messages });
  });
});

app.post('/messages', function(req, res){
  Message.create(req.body)
    .then(function(message){
      res.redirect('/');
    })
    .catch(function(error){
      res.render('index', {
        errors: Object.keys(error.errors)
                  .map(errorKey => error.errors[errorKey].message)
        });
    });
});

app.post('/comments', function(req, res){
  Comment.create(req.body)
    .then(function(comment){

      return Message.findById(comment.message)
        .then(function(message){
          if(!message){
            throw new Error('cannot find message');
          }
          message.comments.push(comment);
          return message.save()
            .then(function(){
              res.redirect('/');
            });
      });
    })
    .catch(function(error){
      res.render('index', {
        errors: Object.keys(error.errors)
                  .map(errorKey => error.errors[errorKey].message)
        });
    });
});


app.listen(port, function(){
  console.log('listening on port ' + port);
});
