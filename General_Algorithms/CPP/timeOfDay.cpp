#include <iostream>

#define MIDNIGHT 12

#define SECONDS_IN_DAY 24 * 60 * 60
#define SECONDS_IN_HOUR 3600
#define SECONDS_IN_MINUTE 60

#define TRUE 1
#define FALSE 0
#define ERROR -1

void outputTime(int time_in_seconds);

int main() {
    int input_time;

    std::cout << "Enter the Number of Seconds to Convert : ";
    std::cin >> input_time;
    std::cout << std::endl;

    if (input_time < SECONDS_IN_DAY) {
        outputTime(input_time);
        return TRUE;
    }
    else {
        std::cout << "Error";
        return FALSE;
    }
}

void outputTime(int time_in_seconds) {
    int hours, minutes;

    hours = time_in_seconds/SECONDS_IN_HOUR;
    time_in_seconds -= hours * SECONDS_IN_HOUR;

    minutes = time_in_seconds/SECONDS_IN_MINUTE;
    time_in_seconds -= minutes * SECONDS_IN_MINUTE;

    if (hours > MIDNIGHT) std::cout << hours - MIDNIGHT;
    else if (hours == FALSE) std::cout << hours + MIDNIGHT;
    else std::cout << hours;

    if (minutes < 10) std::cout << ":0" << minutes;
    else std::cout << ":" << minutes;

    if (time_in_seconds < 10) std::cout << ":0" << time_in_seconds;
    else std::cout << ":" << time_in_seconds;

    if (hours >= MIDNIGHT) std::cout << "PM";
    else std::cout << "AM";
}
