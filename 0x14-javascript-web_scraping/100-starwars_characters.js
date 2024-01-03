#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const film = JSON.parse(body);
    getCharacters(film.characters, 0);
  }
});

function getCharacters (characters, i) {
  if (i >= characters.length) {
    return;
  }

  request(characters[i], function (error, response, body) {
    if (!error && response.statusCode === 200) {
      console.log(JSON.parse(body).name);
      getCharacters(characters, i + 1);
    }
  });
}
