#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const tasks = JSON.parse(body);
    const tasksCompleted = {};

    for (const task of tasks) {
      if (task.completed) {
        if (tasksCompleted[task.userId]) {
          tasksCompleted[task.userId]++;
        } else {
          tasksCompleted[task.userId] = 1;
        }
      }
    }

    console.log(tasksCompleted);
  }
});
