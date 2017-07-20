import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';

import 'rxjs/Rx';
import { Observable } from 'rxjs/Observable';

@Injectable()
export class HttpService {
  // username: string = "keephopealive";

  constructor(private http: Http) {}

  private baseUrl = 'https://api.github.com/users/';

  getGithubProfileData(username){
    console.log(username);
    if (username) {
    return this.http.get(this.baseUrl + username)
      .map( data => data.json()).toPromise();
    }
  }
}
