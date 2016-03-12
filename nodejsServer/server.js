var express    = require('express');        // call express
var app        = express();                 // define our app using express
var https = require('https');
var bodyParser = require('body-parser');
var mongoose = require('mongoose');
var Ticket     = require('./app/models/ticket');
var fs = require('fs');
var timediff = require('timediff');
var config = require('./config');

mongoose.connect(config.db);
// configure app to use bodyParser()
// this will let us get the data from a POST
1411150100035
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

var port = config.httpPort       // set our port

https.createServer({
      key: fs.readFileSync('key.pem'),
      cert: fs.readFileSync('cert.pem')
    }, app).listen(config.httpsPort);

// ROUTES FOR OUR API
// =============================================================================
var router = express.Router();              // get an instance of the express Router

// middleware to use for all requests
router.use(function(req, res, next) {
    // do logging
    console.log('Something is happening.');
    next(); // make sure we go to the next routes and don't stop here
}); 

// more routes for our API will happen here

// on routes that end in /tickets
// ----------------------------------------------------
router.route('/tickets')

    // create a ticket (accessed at POST http://localhost:8080/api/tickets)
    .post(function(req, res) {
        
        var ticket = new Ticket();      // create a new instance of the Ticket model
			ticket.Id = req.body.Id;
			ticket.TicketNumber = req.body.TicketNumber;
			ticket.TicketControlNumber = req.body.TicketControlNumber;
			ticket.EnterTime = req.body.EnterTime;
			ticket.ExitTime = req.body.ExitTime;
			ticket.Category = req.body.Category;
			ticket.EnterTerminalId = req.body.EnterTerminalId;
			ticket.ExitTerminalId = req.body.ExitTerminalId;
			ticket.IsClosed = req.body.IsClosed;
			ticket.ValidForExitUntil = req.body.ValidForExitUntil;
			ticket.ValidForEntryUntil = req.body.ValidForEntryUntil;
			ticket.CreatedTime = req.body.CreatedTime;
			ticket.UpdatedTime = req.body.UpdatedTime;
        // save the ticket and check for errors
        ticket.save(function(err) {
            if (err)
                res.send(err);

            res.json({ message: 'Ticket created!' });
        });
        
    })
	
	.get(function(req, res) {
        Ticket.find(function(err, tickets) {
            if (err)
                res.send(err);

            res.json(tickets);
        });
    })
	
	router.route('/tickets/:ticket_number')

    // get the ticket with that id (accessed at GET http://localhost:8080/api/tickets/:ticket_number)
    .get(function(req, res) {
		
        Ticket.findOne({TicketNumber : req.params.ticket_number.substring(0,12), TicketControlNumber : req.params.ticket_number.substring(12)}, function(err, ticket) {			
            if (err)
                res.send(err);
			
			if(!ticket) // check if ticket exists 
				res.json({ "validationSuccess": "error",  "validationMessage": "Dogodila se pogreska! <br /> Pokusajte ponovo!" });
			else
			{
				if(ticket.IsClosed == true) // check is ticket closed
					res.json({ "validationSuccess": "error",  "validationMessage": "Tiket nije validan!" });	
				else
				{
					var now = new Date(); // get current timestamp
					now.setHours(now.getHours() - now.getTimezoneOffset() / 60); // set to local time
					now = now.toISOString(); // convert to JSON
					var diffJSON = timediff(ticket.EnterTime, now, 'm'); // get difference between Ticket EnterTime and current time
					var diff = diffJSON['minutes'] // get integer value
				}
			
				if(diff>config.createdTimeLimit) // check is ticket older from time set in config file
					res.json({ "validationSuccess": "error",  "validationMessage": "Tiket nije placen!" });	
				else
				{
					// if everything passess update ticket ValidForExitUntil for value in config file and send positive response
					var now = new Date();
					now.setMinutes(now.getMinutes() + config.extendExitTime);
					now.setHours(now.getHours() - now.getTimezoneOffset() / 60);
					now = now.toISOString();
					ticket.ValidForExitUntil = now; // update ticket exit time

					// save the ticket
					ticket.save(function(err) {
						if (err)
							res.send(err);
			});
			res.json({ "validationSuccess": "ok",  "validationMessage": "Vas tiket je validiran <br /> za izlaz!" }); 
				}
					
			}			
        });
    })
	
	.put(function(req, res) {

        // use our ticket model to find the ticket we want
        Ticket.findOne({TicketNumber : req.params.ticket_number.substring(0,12), TicketControlNumber : req.params.ticket_number.substring(12)}, function(err, ticket) {

            if (err)
                res.send(err);
			
			if(ticket) {
				ticket.Id = req.body.Id;
				ticket.TicketNumber = req.body.TicketNumber;
				ticket.TicketControlNumber = req.body.TicketControlNumber;
				ticket.EnterTime = req.body.EnterTime;
				ticket.ExitTime = req.body.ExitTime;
				ticket.Category = req.body.Category;
				ticket.EnterTerminalId = req.body.EnterTerminalId;
				ticket.ExitTerminalId = req.body.ExitTerminalId;
				ticket.IsClosed = req.body.IsClosed;
				ticket.ValidForExitUntil = req.body.ValidForExitUntil;
				ticket.ValidForEntryUntil = req.body.ValidForEntryUntil;
				ticket.CreatedTime = req.body.CreatedTime;
				ticket.UpdatedTime = req.body.UpdatedTime;
				// save the ticket
				ticket.save(function(err) {
					if (err)
						res.send(err);

				res.json({ message: 'Ticket updated!' });
				});
			}
			else
			{
				 res.json({ message: 'Ticket not found!' });				
			}     
        });
    })
	
	.delete(function(req, res) {
        Ticket.remove({
            _id: req.params.ticket_number
        }, function(err, ticket) {
            if (err)
                res.send(err);

            res.json({ message: 'Successfully deleted' });
        });
    });

// test route to make sure everything is working (accessed at GET http://localhost:8080/api)
router.get('/', function(req, res) {
    res.json({ message: 'Hello, it is good!' });   
});

// more routes for our API will happen here

// REGISTER OUR ROUTES -------------------------------
// all of our routes will be prefixed with /api
app.use('/api', router);

// START THE SERVER
// =============================================================================
app.listen(port);
console.log('Magic happens on port ' + port);