import { Component } from '@angular/core';
import { NgForm } from '@angular/forms';
import { Response } from '@angular/http';

import { HttpService } from './http.service'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  username = null;
  userExists = null;
  score: number = 0;
  promise;

  constructor(private httpService: HttpService) {}

  onGetGit(){
    console.log("getting");
    console.log(this.promise);
    this.promise = this.httpService.getGithubProfileData(this.username)
      console.log(this.promise);
      if (this.promise) {
        this.promise.then( (user) => {
          if (user.id) {
            this.userExists = true;
            this.score = user.public_repos + user.followers;
          } else {
            this.userExists = false;
            this.score = null;
          }
          this.username = null;
          console.log(this.username)
        })
        .catch( (err) => {
          this.userExists = false;
        });
      } else {
        this.userExists = false;
      }
  }

}
