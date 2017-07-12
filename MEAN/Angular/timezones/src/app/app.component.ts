import { Component } from '@angular/core';
import * as moment from 'moment';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'US Time Zone Display';
  
  pacific: number = -7; // America/Los_Angeles (-7)
  mountain: number = -6; // America/Denver (-6)
  central: number = -5; // America/Chicago (-5)
  eastern: number = -4; // America/New_york (-4)

  rightNow = moment().utc().format("MMMM D, YYYY, h:mm:ss a");
  timeZoneSelected = null;

  getTime(timezone){
    this.timeZoneSelected = timezone;
    this.rightNow = moment().utc().add(timezone, 'h').format("MMMM D, YYYY, h:mm:ss a");
    console.log(this.timeZoneSelected);
    return this.rightNow;
    // return rightNow = moment().utc().add(timezone, 'h').format("MMMM D, YYYY, h:mm:ss a");
  }

  reset(){
    this.timeZoneSelected = null;
    return this.timeZoneSelected;
  }

}
