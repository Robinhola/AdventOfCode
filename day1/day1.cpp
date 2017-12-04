#include <iostream>

using namespace std;

int main()
{
    string input;
    cin >> input;

    int sum = 0;
    int range = 0;

    for (const char&  c : input) {
         if (c == input[++range % input.size()]) {
             sum += c - '0';
         }
    }

    cout << sum << endl;
    return 0;
}
