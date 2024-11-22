#!/usr/bin/node
const request = require('request');

// Function to get all characters
function getStarWarsCharacters () {
  // API URL
  const url = 'https://swapi-api.alx-tools.com/api/people/';
  // Send request to the API
  request(url, function (error, response, body) {
    if (error) {
      console.error('Error occurred:', error);
    } else if (response.statusCode !== 200) {
      console.error('HTTP Error:', response.statusCode);
    } else {
      // Parse JSON response
      const data = JSON.parse(body);
      // Print characters
      data.results.forEach(character => {
        console.log(character.name);
      });
    }
  });
}

getStarWarsCharacters();
