#include "../libs/jamutil.h"

#include <iostream>
#include <vector>

namespace {

enum TYPE {
    e_EMPTY = 0,
    e_VALUE = 1,
    e_REGIS = 2,
};

struct DATA {
    std::string ins;
    char        reg;
    TYPE        typ;
    int         val;
    char        des;
};

using INPUT = std::vector<DATA>;

void readInput(INPUT *input, std::istream& is)
{
    std::string lineInput;
    while (getline(is, lineInput)) {
          DATA d;
          std::istringstream ss(lineInput);
          ss >> d.ins >> d.reg;
          const std::string& end = lineInput.substr(5, lineInput.size() - 5);

          std::cout << d.ins << d.reg;
          if (Rob::toInt(&d.val, end.c_str())) {
              d.typ = e_VALUE;
              std::cout << " " << d.val;
          }
          else if (ss >> d.des) {
              d.typ = e_REGIS;
              std::cout << " " << d.des;
          }
          else {
              d.typ = e_EMPTY;
          }

          input->push_back(d);
          std::cout << '\n';
    }
}

/*
snd X plays a sound with a frequency equal to the value of X.
set X Y sets register X to the value of Y.
add X Y increases register X by the value of Y.
mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
mod X Y sets register X to the remainder of dividing the value contained in register X by the value of Y (that is, it sets X to the result of X modulo Y).
rcv X recovers the frequency of the last sound played, but only when the value of X is not zero. (If it is zero, the command does nothing.)
jgz X Y jumps with an offset of the value of Y, but only if the value of X is greater than zero. (An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)
*/

int lastSound(const INPUT& input)
{
    int result;
    int regs[26];
    for (int& i : regs) { i = 0; }

    for (size_t i = 0; ; ) {
        const auto& d = input[i];
        const int val = d.typ == e_REGIS ? regs[d.des - 'a'] : d.val;
        std::cout << i << ": " << d.ins << " " << d.reg;
        std::cout << (d.typ == e_REGIS ? d.des : ' ');
        if (d.typ != e_EMPTY) {
            std::cout << val;
        }
        std::cout << "\n";

        if ("snd" == d.ins) {
            result = regs[d.reg - 'a'];
        }
        else if ("set" == d.ins) {
            regs[d.reg - 'a'] = val;
        }
        else if ("add" == d.ins) {
            regs[d.reg - 'a'] += val;
        }
        else if ("mul" == d.ins) {
            regs[d.reg - 'a'] *= val;
        }
        else if ("mod" == d.ins) {
            regs[d.reg - 'a'] %= val;
        }
        else if ("rcv" == d.ins) {
            std::cout << "reading " << d.reg
                      << ":" << regs[d.reg - 'a'] << "\n";
            if (regs[d.reg - 'a']) {
                return result;                                        // RETURN
            }
        }
        else if ("jgz" == d.ins) {
            if (regs[d.reg - 'a']) {
                i += val;
                continue;                                           // CONTINUE
            }
        }
        ++i;
    }
    return -1;
}


} // close anonymous namespace

int main(int argc, char *argv[])
{
    for (size_t i = 0; i < argc; ++i) {
        auto& c = argv[i];
        std::cout << c << '\n';
    }

    std::vector<DATA> input;
    readInput(&input, std::cin);
    std::cout << lastSound(input);

    return 0;
}
