#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
const characterId = '18';

request(apiUrl, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0;
    for (const film of films) {
      for (const character of film.characters) {
        if (character.endsWith('/' + characterId + '/')) {
          count++;
          break;
        }
      }
    }
    console.log(count);
  }
});
