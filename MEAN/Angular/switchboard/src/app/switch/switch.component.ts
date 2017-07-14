import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-switch',
  templateUrl: './switch.component.html',
  styleUrls: ['./switch.component.css']
})
export class SwitchComponent implements OnInit {

  activeSwitch: string = 'Off';
  flipSwitch: boolean;

  constructor(){
  }

  getSwitchStatus(){
    return this.activeSwitch;
  }

  onToggle(event: any){
    this.flipSwitch = !this.flipSwitch;
    this.flipSwitch === true ? this.activeSwitch = 'On' : this.activeSwitch = 'Off';
  }

  ngOnInit() {
    this.activeSwitch = Math.random() > 0.5 ? 'On' : 'Off';
    this.activeSwitch === 'On' ? this.flipSwitch = true : this.flipSwitch = false;
  }

}
