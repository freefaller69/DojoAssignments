import { Component, OnInit, Input, OnChanges } from '@angular/core';

@Component({
  selector: 'app-saiyan',
  templateUrl: './saiyan.component.html',
  styleUrls: ['./saiyan.component.css']
})
export class SaiyanComponent implements OnInit {
  @Input() myPower;

  classname: string = this.constructor.name;
  superlative: string;

  constructor() { }

  ngOnInit() {
  }

  ngOnChanges(){
    this.myPower = this.myPower * 10;
    console.log(this.myPower);
    if(this.myPower >= 50000){
      this.superlative = "The One";
    } else if (this.myPower >= 20000){
      this.superlative = "Superlative!"
    }  else if (this.myPower >= 9000){
      this.superlative = "Over 9000!"
    }
  }

}
