import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Retro Barcode Designer';
  colors = [
    '#008080',
    '#8A2BE2',
    '#DC143C',
    '#00008B',
    '#006400',
    '#8FBC8F',
    '#FF00FF',
    '#FFD700',
    '#FF8C00',
    '#7CFC00',
  ]

  getColor(){
    return this.colors[Math.floor(Math.random() * 10)+1];
  }

}
