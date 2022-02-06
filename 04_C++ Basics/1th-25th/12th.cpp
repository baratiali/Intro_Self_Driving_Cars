#include <vector>

using namespace std;

int main() {
    
    std::vector<int> myvector (10, 6);
    std::vector<float> myvector1 = {5.0, 3.0, 2.7, 8.2, 7.9};
    vector<float> vector1(4);
    vector1[0] = 4.5;
    vector1[1] = 2.1;
    vector1[2] = 8.54;
    vector1[3] = 9.0;
    vector<float> vector(4, 3.5);

    vector<int> intvariable;
    intvariable.assign(10,16);
    intvariable.push_back(25);


    
    return 0;
}