import { Component } from '@angular/core';
import { Applicant } from './applicant';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Registration';

  applicant = new Applicant();
  applicants = [];
  onSubmit(form, event: Event){
    console.log('Form submitted');
    console.log(this.applicant);
    this.applicants.push(this.applicant);
    this.applicant = new Applicant();
  }

}
