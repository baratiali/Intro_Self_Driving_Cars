#include <iostream>
#include <vector>

using namespace std;

int main() {

    vector<float> example;

    for (int i = 0; i < 5; i++) {
        example.push_back(i*5.231);
    }

    for (int i = 0; i < example.size(); i++) {
        cout << example[i] << endl;
    }

    return 0;
}

/*
int i = 5;
int x = i++; // x = 5, i = 6 (called postfix)
int x = ++i; // x = 6, i = 6 (called prefix)
*/