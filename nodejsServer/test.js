var timediff = require('timediff');
var now = new Date();
now.setMinutes(now.getMinutes() + 60);
now.setHours(now.getHours() - now.getTimezoneOffset() / 60);
now = now.toISOString();

console.log(now)