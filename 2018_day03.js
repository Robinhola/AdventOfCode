console.log("Day 3, Dec 2018");

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
});

const lines = [];
rl.on('line', (line) => {
    lines.push(line);
});

rl.on('close', () => {
    console.log(`Number of lines: ${lines.length}`);
    const solution = new Day3(lines);
    solution.part1();
    solution.part2();
});

function createSurface (length) {
    const surface = new Array(length);
    for (let i = 0; i < length; ++i) {
        surface[i] = Array(length).fill('.');
    }
    return surface;
}

function parseLine (line) {
    const input = line.split(' ');
    const position = input[2].split(',');
    const dimensions = input[3].split('x');
    return {
        id: input[0].split('#')[1],
        x: parseInt(position[0]),
        y: parseInt(position[1].split(':')[0]),
        lengthX: parseInt(dimensions[0]),
        lengthY: parseInt(dimensions[1]),
    };
}

function parseInput (input) {
    const lines = [];
    for (let line of input) {
        lines.push(parseLine(line));
    }
    return lines;
}
// Goal1: find the number of overlaping squares
// Goal2: find the holy clain that does not overlap
// How:
// - draw the surface
// - draw each each square:
//      if not '.':
//          mark cross
//          if new cross:
//              increment solution
//              mark the previous and current claim unholy

class Day3 {
    constructor (input) {
        this.numberOfX = 0;
        this.nbOfHolyClaims = 0;
        this.holyClaims = new Set();


        // const surface = this.surface = createSurface(8);
        const surface = this.surface = createSurface(1000);
        const rectangles = this.rectangles = parseInput(input);

        for (let rectangle of rectangles) {
            this.drawRectangle(rectangle);
        }

        // console.log(surface);

    }

    part1 () {
        console.log(`${this.numberOfX} square inches are overlaping`);
    }

    part2 () {
        const holyClaims = this.holyClaims;
        if (1 !== holyClaims.size) {
            console.log("Oops");
            return;
        }

        const holyClaim = holyClaims.values().next().value;

        console.log(`${holyClaim} is a holy claim (out of ${this.nbOfHolyClaims} potentially claims)`
        );
    }

    drawRectangle (rectangle) {
        const { surface } = this;
        const { id, x, y, lengthX, lengthY } = rectangle;

        let holy = true;

        // console.log(`Drawing ${JSON.stringify(rectangle)}`);

        for (let i = 0; i < lengthY; ++i) {
            const posY = i + y;
            const row = surface[posY];

            for (let j = 0; j < lengthX; ++j) {
                const posX = j + x;
                let value = row[posX];

                if ('.' === value) {
                    value = id;
                }
                else if ('x' !== value) {
                    // remove previous from the holy
                    this.holyClaims.delete(value);
                    value = 'x';
                    this.numberOfX += 1;
                }

                holy = holy && id === value;
                row[posX] = value;
                // console.log(`x: ${posX}, y: ${posY}, val: ${value}`);
            }
        }

        if (holy) {
            this.nbOfHolyClaims += 1;
            this.holyClaims.add(id);
        }
        else {
            this.holyClaims.delete(id);
        }

    }

};
