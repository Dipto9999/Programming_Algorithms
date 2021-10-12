#include <iostream>

#define MAX_VOLTAGE 13100
#define MIN_CONSECUTIVE 5

#define TRUE 1
#define FALSE 0
#define ERROR -1

int over_voltage(int voltage_read[], std::size_t size) {
    int error_minutes = 0;
    int consecutive_errors = 0;
    int index = 0;

    for (index = 0; index < size; index++) {
        /* Check for Consecutive Errors. */
        if (voltage_read[index] > MAX_VOLTAGE) consecutive_errors++;
        else consecutive_errors = 0;

        /* Consecutive Errors Must Exceed Minimum Number. */
        if (consecutive_errors > MIN_CONSECUTIVE) error_minutes++;
        else if (consecutive_errors == MIN_CONSECUTIVE) error_minutes += MIN_CONSECUTIVE;
    }
    return error_minutes;
}

int main() {
    int test_array_1[7] = {12000, 13100, 13101, 13101, 13101, 13102, 13100}; // Returns 0
    std::cout << "Output For Test Array 1 : " << over_voltage(test_array_1, 7) << std::endl;

    int test_array_2[7] = {12000, 13100, 13101, 13101, 13101, 13102, 13101}; // Returns 5
    std::cout << "Output For Test Array 2 : " << over_voltage(test_array_2, 7) << std::endl;

    int test_array_3[7] = {12000, 13103, 13101, 13101, 13101, 13102, 13101}; // Returns 6
    std::cout << "Output For Test Array 3 : " << over_voltage(test_array_3, 7) << std::endl;

    int test_array_4[11] = {12000, 13103, 13101, 13101, 13101, 13102, 13101, 11598, 13110, 13105, 13175}; // Returns 6
    std::cout << "Output For Test Array 4 : " << over_voltage(test_array_4, 11) << std::endl;

    return FALSE;
}