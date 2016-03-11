var config = {};

config.createdTimeLimit =  180;
config.extendExitTime =  60;
config.httpPort = process.env.PORT || 8080; 
config.httpsPort = 55555;
config.db = 'mongodb://localhost/test';

module.exports = config;