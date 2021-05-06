/**
 * OpenWeatherMapJSON (v1.0.3)
 * By Banana (2017-May-03)
 * Mod GoToLoop (2017-May-04)
 *
 * https://Forum.Processing.org/two/discussion/22370/
 * need-help-making-weather-api-buttons-in-p5#Item_4
 *
 * https://Bl.ocks.org/GoSubRoutine/5fbc03e019c53254a2ba7e7fd3318b45
 */

"use strict";

const HTML = 'https' + '://',
      SITE = 'api.OpenWeatherMap.org',
      FOLD = '/data/2.5/weather' + '?',
      CITY = '&zip=94040,us',
      UNIT = '&units=imperial',
      API_KEY = '&appid=0a59bb3a87d56084a596f8eb5f50ee42',
      //API_KEY = '&appid=f77c39703fb6be71e2c5a96e58edc077',
      PATH = HTML + SITE + FOLD + CITY + UNIT + API_KEY,
      TOGGLE = 'Toggle to ',
      IMPERIAL = (TOGGLE + 'Imperial').bold(),
      METRIC = (TOGGLE + 'Metric').bold(),
      F = ' °F', C = ' °C', MPH = ' mph', KPH = ' kph';

let weather, temp, wind, deg, vel;

function preload() {
  weather = loadJSON(PATH, print);
}

function setup() {
  noCanvas(), noLoop();

  createP('City: '.bold() + weather.name);
  createP('Weather: '.bold() + weather.weather[0].description);
  createP('Temp: '.bold() + `<temp>${weather.main.temp}</temp><deg>${F}</deg>`);
  createP('Wind: '.bold() + `<wind>${weather.wind.speed}</wind><vel>${MPH}</vel>`);

  createButton(METRIC).mousePressed(toggleStandardUnit);

  temp = select('temp'), deg = select('deg');
  wind = select('wind'), vel = select('vel');
}

function toggleStandardUnit() {
  const isMetric = ~this.value();
  this.value(isMetric);
  this.html(isMetric && IMPERIAL || METRIC);
  isMetric? setMetric() : setImperial();
}

function setImperial() {
  temp.html(weather.main.temp), deg.html(F);
  wind.html(weather.wind.speed), vel.html(MPH);
}

function setMetric() {
  temp.html(nf(toCelsius(weather.main.temp), 0, 2)), deg.html(C);
  wind.html(nf(toKph(weather.wind.speed), 0, 2)), vel.html(KPH);
}

function toCelsius(fahrenheit) {
  return 5/9 * (fahrenheit - 32);
}

function toKph(mph) {
  return 1.609344 * mph;
}