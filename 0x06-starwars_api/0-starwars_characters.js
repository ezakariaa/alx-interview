#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
if (!movieId) {
  console.error("Please provide a Movie ID.");
  process.exit(1);
}

// URL for the specific film using the movie ID
const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error("Error:", error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to retrieve movie with ID ${movieId}.`);
    return;
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  characters.forEach(characterUrl => {
    request(characterUrl, (err, res, charBody) => {
      if (err) {
        console.error("Error:", err);
        return;
      }

      if (res.statusCode === 200) {
        const character = JSON.parse(charBody);
        console.log(character.name);
      } else {
        console.error("Failed to retrieve character.");
      }
    });
  });
});
