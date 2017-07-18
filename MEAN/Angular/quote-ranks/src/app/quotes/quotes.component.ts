import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';

import { Quote } from './quote.model';

@Component({
  selector: 'app-quotes',
  templateUrl: './quotes.component.html',
  styleUrls: ['./quotes.component.css']
})
export class QuotesComponent implements OnInit {
// @Input() allQuotes;
@Input() allQuotes: {quote: string, author: string};
@Output() deleteQuoteEvent = new EventEmitter<Quote>();
quote: Quote = this.quote;

  constructor() { }

  ngOnInit() {
  }

  ngOnChanges() {
  }

  upVote(quoteEl){
    console.log("quote: " + quoteEl.rank);
    console.log("this quote: " + this.quote);
    console.log("this: " + this);
    quoteEl.rank++;
  }

  downVote(quoteEl){
    quoteEl.rank--;
  }

  delete(quoteEl){
    this.deleteQuoteEvent.emit(quoteEl);
  }

}
