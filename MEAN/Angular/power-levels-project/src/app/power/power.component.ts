import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-power',
  templateUrl: './power.component.html',
  styleUrls: ['./power.component.css']
})
export class PowerComponent implements OnInit {
  power: number = 0;

  calculatePowers(powerIn){
    console.log("Powers Activated!");
    if(powerIn.value < 1){
      this.power = 1;
    } else if (powerIn.value > 100){
      this.power = 100;
    } else {
      this.power = powerIn.value;
    }
  }

  constructor() { }

  ngOnInit() {
  }

}
