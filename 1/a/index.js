const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

const beautifulMatrix = (matrix) => {
    for (let i = 0; i < matrix.length; i++) {
        const line = matrix[i];
        for (let j = 0; j < line.length; j++) {
            const element = line[j];
            if(!!element) {
                return Math.abs(2 - i) + Math.abs(2 - j);
            }
        }
    }
}

var inputs = 0;
var elements = [];

const pushInArray = (line) => {
    const items = line.toString().split(' ').map(Number);
    elements.push(items);
}

readline.on('line', line => {
    pushInArray(line);
    inputs == 4 ? readline.close() || console.log(beautifulMatrix(elements)) : inputs++;
});