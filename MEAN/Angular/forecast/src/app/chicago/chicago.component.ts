import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { Response } from '@angular/http';

import { WeatherService } from '../weather.service';

@Component({
  selector: 'app-chicago',
  templateUrl: './chicago.component.html',
  styleUrls: ['./chicago.component.css']
})
export class ChicagoComponent implements OnInit {
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
    this.city = this.route.snapshot.url[0].path;
    this.weather = this.weatherService.getWeatherData(this.city)
    .then( weather => {
      this.humidity = weather.main.humidity;
      this.temp = weather.main.temp;
      this.maxTemp = weather.main.temp_max;
      this.minTemp = weather.main.temp_min;
      this.clouds = weather.weather[0].description;
    });
  }

}
