const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

const petyaandStrings = (strings) => {
    if(strings[0] === strings[1]) {
        return 0;
    }
    return strings[0] < strings[1] ? -1 : 1;
}

var inputs = 0;
var elements = [];

const pushInArray = (line) => {
    elements.push(String(line).toLowerCase());
}

readline.on('line', line => {
    pushInArray(line);
    inputs == 1 ? readline.close() || console.log(petyaandStrings(elements)) : inputs++;
});