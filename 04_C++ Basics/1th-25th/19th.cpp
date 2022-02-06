#include <iostream>

float distance(float velocity, float acceleration, float time_elapsed);

int main() {

    std::cout << distance(3, 4, 5) << std::endl;  
    std::cout << distance(7.0, 2.1, 5.4) << std::endl;

    return 0;   
}

float distance(float velocity, float acceleration, float time_elapsed) {
    return velocity*time_elapsed + 0.5*acceleration*time_elapsed*time_elapsed;
}