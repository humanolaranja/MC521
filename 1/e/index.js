const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

const iqTest = (line) => {
    let odd = [];
    let even = [];

    for (let i = 0; i < line.length; i++) {
        const element = line[i];
        element % 2 === 0 ? even.push(i + 1) : odd.push(i + 1);
    }

    return odd.length > even.length ? even[0] : odd[0];
}

var inputs = 0;

readline.on('line', line => {
    inputs == 1 ? readline.close() || console.log(iqTest(line.toString().split(' ').map(Number))) : inputs++;
});