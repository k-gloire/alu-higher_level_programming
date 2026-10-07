#!/usr/bin/node
const request = require('request');

const characterId = '18';

request.get(process.argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const films = JSON.parse(body).results;
    let count = 0;
    for (const film of films) {
      if (film.characters.some(c => c.includes(`/people/${characterId}/`))) {
        count++;
      }
    }
    console.log(count);
  }
});
