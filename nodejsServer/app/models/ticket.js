var mongoose     = require('mongoose');
var Schema       = mongoose.Schema;

var TicketSchema   = new Schema({
    Id: Number,
	TicketNumber : String,
	TicketControlNumber : String,
	EnterTime : Date,
	ExitTime : Date,
	Category : Number,
	EnterTerminalId : Number,
	ExitTerminalId : Number,
	IsClosed : Boolean,
	ValidForExitUntil : Date,
	ValidForEntryUntil : Date,
	CreatedTime : Date,
	UpdatedTime : Date
	
});

module.exports = mongoose.model('Ticket', TicketSchema);