const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

const registrationSystem = (names) => {
    let registered = {};
    
    for (let index = 0; index < names.length; index++) {
        const element = names[index];
        if(registered[element] === undefined) {
            console.log('OK');
            registered[element] = 1;
        } else {
            console.log(`${element}${registered[element]}`);
            registered[element]++;
        }
        
    }
}

var i = 0;
var inputs = 0;
var elements = [];

const pushInArray = (line) => {
    elements.push(line);
}

readline.on('line', line => {
    if (i == 0) {
        inputs = line;
        i++;
    } else {
        pushInArray(line);
        if (i == inputs) {
            readline.close(), registrationSystem(elements);
        } else {
            i++
        }
    }
});