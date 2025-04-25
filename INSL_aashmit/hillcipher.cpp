#include <iostream>
#include <cstring>
using namespace std;

const int SIZE = 2;
const int MOD = 26;

char alphabet[26] = {
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
};

int charToIndex(char c) {
    return c - 'a';
}

char indexToChar(int idx) {
    return alphabet[idx % 26];
}

void multiplyMatrix(int key[SIZE][SIZE], int pt[SIZE], int ct[SIZE]) {
    for (int i = 0; i < SIZE; i++) {
        ct[i] = 0;
        for (int j = 0; j < SIZE; j++) {
            ct[i] += key[i][j] * pt[j];
        }
        ct[i] %= MOD;
    }
}

int main() {
    // Define 2x2 key matrix (must be invertible mod 26 for decryption)
    int key[SIZE][SIZE] = {
        {3, 3},
        {2, 5}
    };

    char plaintext[100];
    cout << "Enter plaintext (lowercase, no spaces): ";
    cin >> plaintext;

    int len = strlen(plaintext);
    if (len % 2 != 0) {
        plaintext[len] = 'x';
        plaintext[len + 1] = '\0';
        len++;
    }

    cout << "Encrypted text: ";
    for (int i = 0; i < len; i += 2) {
        int pt[SIZE];
        pt[0] = charToIndex(plaintext[i]);
        pt[1] = charToIndex(plaintext[i + 1]);

        int ct[SIZE];
        multiplyMatrix(key, pt, ct);

        cout << indexToChar(ct[0]) << indexToChar(ct[1]);
    }

    cout << endl;
    return 0;
}
