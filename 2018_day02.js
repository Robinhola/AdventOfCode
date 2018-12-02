console.log("Day 2, Dec 2018");

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
});

const lines = [];
rl.on('line', (line) => {
    const num = parseInt(line, 10);
    lines.push(line);
});

rl.on('close', () => {
    console.log(`Line: ${lines.length}`);
    const solution = new Day2(lines);
    solution.printCheckSum();
    solution.printTwoCloseDifferences();
});

// We look for IDs that have at least one letter:
//      - repeated no more than 2x
//      - repeated no more than 3x
// The same ID can be satisfy the two conditions and be counted twice.

function countNumOfLetters (id) {
    const letters = new Map();
    for (let i = 0; i < id.length; ++i) {
        const letter = id[i];
        const count = letters.get(letter) || 0;
        letters.set(letter, count + 1);
    }
    return letters;
}

function hasTwoAndOrThreeIdenticalLetters (id) {
    const counts = countNumOfLetters(id).values();
    let hasTwo   = false;
    let hasThree = false;
    for (let count of counts) {
        hasTwo   = hasTwo   || count === 2;
        hasThree = hasThree || count === 3;
        if (hasTwo && hasThree) { break; }
    }

    return {
        hasTwo: hasTwo,
        hasThree: hasThree,
    };
}

function differByOnlyOneLetter(leftLetters, rightLetters) {
    let difference = 0;
    for (key of leftLetters.keys()) {
        const left  = leftLetters.get(key);
        const right = rightLetters.get(key) || 0;
        difference += Math.abs(left - right);
        if (difference > 1) { break; }
    }
    return difference === 1;
}

class Day2 {
    constructor (ids) {
        this.ids = ids;
        this.idsWhohaveTwo = 0;
        this.idsWhohaveThree = 0;
        this.initCounts();
    }

    initCounts () {
        for (let id of this.ids) {
            const { hasTwo, hasThree } = hasTwoAndOrThreeIdenticalLetters(id);
            this.idsWhohaveTwo += hasTwo ? 1 : 0;
            this.idsWhohaveThree += hasThree ? 1 : 0;
        }
    }

    printCheckSum () {
        const { idsWhohaveTwo: two, idsWhohaveThree: three } = this;
        const checksum = two * three;
        console.log(`${two} (two) x ${three} (three) = ${checksum}`);
    }

    printTwoCloseDifferences () {
        const { ids } = this;
        let differByOne = false;
        let leftId, rightId;

        for (let i = 0; i < ids.length; ++i) {
            leftId = ids[i];
            const leftLetters = countNumOfLetters(leftId);
            const rightIds    = ids.slice(i);
            for (let j = 0; j < rightIds.length; ++j) {
                rightId = rightIds[j];
                const rightLetters = countNumOfLetters(rightId);
                differByOne = differByOnlyOneLetter(leftLetters, rightLetters);
                if (differByOne) { break; }
            }
            if (differByOne) { break; }
        }

        console.log(`${leftId} (left) and ${rightId} (right)`);
        let result = "";
        for (let i = 0; i < leftId.length; ++i) {
            result += leftId[i] === rightId[i] ? leftId[i] : '';
        }
        console.log(`${result}`);
    }

};
