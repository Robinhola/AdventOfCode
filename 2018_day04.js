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
    const solution = new Day4(lines);
    solution.part1();
    solution.part2();
});

// Goal1: Find the guard who has been asleep the most and at which minute
// How:
//      - sort
//      - per line, update guard number of hours asleep
//      - for the guard who has been asleep the most, find the minute with the most of occurences

function parseLogLines (lines) {
    const logLines = [];

    for (let line of lines) {
        const date   = line.split(']')[0].split('[')[1];
        const minute = parseInt(date.split(' ')[1].split(':')[1]);
        const action = line.split(']')[1].slice(1);

        logLines.push({
            date: date,
            minute: minute,
            action: action,
        });
    }

    return logLines.sort((a, b) => {
        if (a.date < b.date) return -1;
        else return 1;
    });
}

function getId (action) {
    return parseInt(action.split(' ')[1].slice(1));
}

function findMostTiredGuards (logLines) {
    const guardsSleepingRecords = new Map();

    let id = -1;
    let start = 0;
    let max = 0;
    let mostTiredGuard = -1;
    for (let logLine of logLines) {
        const { action, minute } = logLine; 
        if (action.startsWith('Guard')) {
            id = getId(action);
            if (!guardsSleepingRecords.has(id)) {
                guardsSleepingRecords.set(id, 0);
            }
        }
        else if (action.startsWith('falls')) {
            start = minute;
        }
        else if (action.startsWith('wakes')) {
            const record = guardsSleepingRecords.get(id);
            const newRecord = record + minute - start;
            if (max < newRecord) {
                max = newRecord;
                mostTiredGuard = id;
            }
            guardsSleepingRecords.set(id, newRecord);            
        }
    }
    return mostTiredGuard;
}

function findMostTiringMinute (logLines, mostTiredGuard) {
    const minutes = new Array(60).fill(0);

    let id = -1;
    let start = 0;
    let goodGuard = false;
    for (let logLine of logLines) {
        const { action, minute } = logLine; 
        if (action.startsWith('Guard')) {
            id = getId(action);
            goodGuard = id === mostTiredGuard;
            continue;
        }

        if (!goodGuard) {
            continue;
        }

        if (action.startsWith('falls')) {
            start = minute;
        }
        else if (action.startsWith('wakes')) {
            const end = minute;
            // console.log(`start=${start} end=${end}`);
            for (let i = start; i < end; ++i) {
                minutes[i] += 1;
            }
        }
    }

    let max = 0;
    let maxMinute = -1;
    for (let i = 0; i < 60; ++i) {
        const minute = minutes[i];
        if (max < minute) {
            max = minute;
            maxMinute = i;            
        }
    }

    return maxMinute;
}

function findMostTiringMinuteForX (logLines) {
    guardsSleepingRecords = new Map();

    let id = -1;
    let start = 0;
    let minutes;
    for (let logLine of logLines) {
        const { action, minute } = logLine;

        if (action.startsWith('Guard')) {
            id = getId(action);
            if (!guardsSleepingRecords.has(id)) {
                guardsSleepingRecords.set(id, new Array(60).fill(0));
            }
            minutes = guardsSleepingRecords.get(id);
        }
        else if (action.startsWith('falls')) {
            start = minute;
        }
        else if (action.startsWith('wakes')) {
            const end = minute;
            // console.log(`start=${start} end=${end}`);
            for (let i = start; i < end; ++i) {
                minutes[i] += 1;
            }
        }
    }

    let elMaximus = 0;
    let elMaximusMinute = -1;
    let elMaximusGuard = -1;

    for (let guard of guardsSleepingRecords.keys()) {
        const minutes = guardsSleepingRecords.get(guard);
        let max = 0;
        let maxMinute = -1;
        for (let i = 0; i < 60; ++i) {
            const minute = minutes[i];
            if (max < minute) {
                max = minute;
                maxMinute = i;            
            }
        }

        console.log(`For guard ${guard}, max is ${max}`);

        if (elMaximus < max) {
            elMaximus = max;
            elMaximusMinute = maxMinute;
            elMaximusGuard = guard;
        }
    }

    return {
        guard: elMaximusGuard,
        minute: elMaximusMinute,
    }
}

class Day4 {
    constructor (input) {
        const logLines = parseLogLines(input);
        const mostTiredGuard = this.mostTiredGuard = findMostTiredGuards(logLines);
        this.mostTiringMinute = findMostTiringMinute(logLines, mostTiredGuard);
        this.mostRegularGuard = findMostTiringMinuteForX(logLines);
        // console.log(logLines);
    }

    part1 () {
        const { mostTiredGuard: id, mostTiringMinute: minute } = this;
        const product = id * minute;
        console.log(`ID (${id}) * Minute (${minute}) = ${product}`)
    }

    part2 () {
        const { guard: id, minute } = this.mostRegularGuard;
        const product = id * minute;
        console.log(`ID (${id}) * Minute (${minute}) = ${product}`)
    }

};
