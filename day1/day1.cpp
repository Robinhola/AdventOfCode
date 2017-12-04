#include <iostream>

using namespace std;

int main()
{
    string input;
    cin >> input;

    // First Part
    cout << "First Part:\n";
    int sum = 0;
    int range = 0;
    int size  = input.size();
    for (const char&  c : input) {
         if (c == input[++range % size]) {
             sum += c - '0';
         }
    }
    cout << sum << endl;

    // Second Part
    cout << "Second Part:\n";
    sum   = 0;
    range = 0;
    int i = 0;
    for (const char&  c : input) {
        range = i + size / 2;
        i++;
        if (c == input[range % size]) {
            sum += c - '0';
        }
    }
    cout << sum << endl;
    return 0;
}
