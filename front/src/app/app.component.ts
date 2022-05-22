import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import {
  AbstractControl,
  FormControl,
  FormGroup,
  ValidatorFn,
  Validators,
} from '@angular/forms';
import { map } from 'rxjs';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent implements OnInit {
  public songs: any[] = [];
  public songsSelected: any[] = [];
  public recommended = [];

  public form = new FormGroup({
    song: new FormControl('', [Validators.required, this.validSong()]),
  });

  get songErrors() {
    //@ts-ignore
    return this.form.controls.song.errors;
  }

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.getSongs();
  }

  private getSongs() {
    this.http
      .get('http://localhost:5000/get-songs')
      .subscribe((result: any) => {
        this.songs = result.data;
      });
  }

  public getRecommended() {
    this.http
      .post(`http://localhost:5000/get-recomendations`, this.songsSelected)
      .pipe(
        map((songs: any) => {
          return songs.data.map((item: any) => {
            let obj = this.songs.find((song) => song.id == item[1]);
            return [obj.song, obj.artist];
          });
        })
      )
      .subscribe((result: any) => {
        this.recommended = result.slice(0, 10);
      });
  }

  private validSong(): ValidatorFn {
    return (control: AbstractControl): { [key: string]: any } | null => {
      let songIndex = this.songs.findIndex(
        (song) => song.song === control.value
      );
      return songIndex !== -1 ? null : { validSong: true };
    };
  }

  public songSelected(song: any) {
    let obj = this.songs.find((item) => item.song == song);
    if (obj) {
      this.songsSelected.push(obj);
      this.form.reset();
      this.getRecommended();
    }
  }
}
