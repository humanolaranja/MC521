const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

const youngPhysicist  = (matrix) => {
    for (let i = 0; i < matrix.length; i++) {
        const line = matrix[i];
        if(line.reduce((a, b) => a + b, 0) !== 0) {
            return "NO";
        }
    }
    return "YES";
}

const transposeMatrix = m => m[0].map((x,i) => m.map(x => x[i]))
// https://stackoverflow.com/a/36164530

var i = 0;
var inputs = 0;
var elements = [];

const pushInArray = (line) => {
    const items = line.toString().split(' ').map(Number);
    elements.push(items);
}

readline.on('line', line => {
    if (i == 0) {
        inputs = line;
        i++;
    } else {
        if (i == inputs) {
            pushInArray(line);
            readline.close(), console.log(youngPhysicist(transposeMatrix(elements)));
        } else {
            i++
            pushInArray(line);
        }
    }
});