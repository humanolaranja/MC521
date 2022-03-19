const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

const helpfulMaths = (line) => {
    const output = line.sort();
    return output.join('+');
}

readline.on('line', line => {
    readline.close();
    console.log(helpfulMaths(line.toString().split('+').map(Number)));
});