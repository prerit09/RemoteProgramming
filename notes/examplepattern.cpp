#include <iostream>
using namespace std;

int main() {

    int rows;

    cin >> rows;

    for(int i = 1; i <= rows; ++i) {
        for(int j = 1; j <= i; ++j) {
            cout << "* ";
        }
        cout << "\n";
    }
    return 0;
}
// No. of Rows : * \n* * \n* * * \n

// Expected output : * \n* * \n* * * \n
