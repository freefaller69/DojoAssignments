const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const QuoteSchema = new Schema({
  name: String,
  quote: String
}, {timestamps: true});

const Quote = mongoose.model('quote', QuoteSchema);

module.exports = Quote;
