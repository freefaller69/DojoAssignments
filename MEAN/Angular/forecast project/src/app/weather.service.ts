import { Http, Response } from '@angular/http';
import { Injectable } from '@angular/core';

import 'rxjs/Rx';

@Injectable()
export class WeatherService {

  constructor(private http: Http) {}

  private baseUrl = "http://api.openweathermap.org/data/2.5/weather?q=";
  private city = "seattle";
  private units = "&units=imperial";
  private key = "&appid=f49f6f436bfaedc90abf3a40f7c13025&appid=";

  getWeatherData(city: string){
    console.log(city);
    return this.http.get(this.baseUrl + city + this.units + this.key)
      .map( data => data.json()).toPromise();
  }
}
