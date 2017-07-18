import { Component, OnChanges, OnInit, ViewChild } from '@angular/core';
import { NgForm } from '@angular/forms';

import { Quote } from './quotes/quote.model';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  @ViewChild('f') quoteForm: NgForm;
  title = 'Quote Ranks';
  rank:number = 0;
  quotes: Quote[] = [
    {
      quote: 'Veni!  Vidi!  Vici!',
      author: 'Gaius Julius Caesar',
      rank: 11
    },
    {
      quote: 'Four score and seven years ago...',
      author: 'Abraham Lincoln',
      rank: 20
    }
  ];

  newQuote = { quote: "", author: "", rank: 0 };

  ngOnInit() {
  }

  onSubmit(form: NgForm) {
    this.newQuote = form.value;
    this.newQuote.rank = 0;
    this.quotes.push(this.newQuote);
    this.quoteForm.reset();
  }

  deleteQuote(quote: Quote): void {
    console.log(quote);
    const idx = this.quotes.indexOf(quote);
    console.log(idx);
    this.quotes.splice(idx, 1);
  }

}
