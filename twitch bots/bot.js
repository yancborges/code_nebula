const tmi = require('tmi.js');

var fs = require("fs");
var text = fs.readFileSync("C://Users//Yan//Desktop//Scripting//twitch_key.txt").toString();

conts = options = {
	options: {
		debug: true,
	},
	connection: {
		secure: true,
		reconnect: true
	},
	identity: {
		username: 'anta_bot',
		password: text
	},
	channels: ['anta_lord']
}

const client = new tmi.client(options);

client.connect();

client.on('message', onMessageHandler);
client.on('connected', onConnectedHandler);

function onMessageHandler (target, context, msg, self) {
  if (self) { return; }

  const commandName = msg.trim();

  if (commandName === '!dice') {
	const num = rollDice();
	client.say(target, `You rolled a ${num}`);
	console.log(`* Executed ${commandName} command`);
  }
  else if(commandName === 'do you love antas?') {
	client.say(target, 'I do');
  }
  else {
	console.log(`* Unknown command ${commandName}`);
  }
}

function rollDice () {
  const sides = 6;
  return Math.floor(Math.random() * sides) + 1;
}

function onConnectedHandler (addr, port) {
  console.log(`* Connected to ${addr}:${port}`);
}