import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { Response } from '@angular/http';

import { WeatherService } from '../weather.service';

@Component({
  selector: 'app-burbank',
  templateUrl: './burbank.component.html',
  styleUrls: ['./burbank.component.css']
})
export class BurbankComponent implements OnInit {
  city: string;
  weather;
  temp;
  maxTemp;
  minTemp;
  humidity;
  wind;
  clouds;

  constructor(private weatherService: WeatherService,
              private router: Router,
              private route: ActivatedRoute) { }

  ngOnInit() {
    this.weather = this.weatherService.getWeatherData('burbank')
    .then( weather => {
      this.humidity = weather.main.humidity;
      this.temp = weather.main.temp;
      this.maxTemp = weather.main.temp_max;
      this.minTemp = weather.main.temp_min;
      this.clouds = weather.weather[0].description;
    });
  }

}
