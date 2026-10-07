#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const todos = JSON.parse(body);
    const result = {};
    for (const todo of todos) {
      if (todo.completed) {
        if (result[todo.userId] === undefined) {
          result[todo.userId] = 0;
        }
        result[todo.userId]++;
      }
    }
    console.log(result);
  }
});
