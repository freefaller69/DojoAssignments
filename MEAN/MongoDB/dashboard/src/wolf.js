const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const WolfSchema = new Schema({
  name: {
    type: String,
    validate: {
      validator:(name) => name.length > 2 ,
      message: 'Name must be longer than two characters.'
    },
    required: [true, 'Name is required.']
  },
});


const Wolf = mongoose.model('Wolf', WolfSchema);

module.exports = Wolf;
