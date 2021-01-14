#include <iostream>
#include <iomanip>
#include <fstream>

using namespace std;

class Solution {
public:
    int numWaterBottles(int numBottles, int numExchange) {
        int totalBottles = 0;
        int emptyBottles = 0;
        
        
        while (numBottles > 0) {
            totalBottles += numBottles;
            int consumed = numBottles;
            numBottles /= numExchange;
            emptyBottles += consumed % numExchange;
            
            if(emptyBottles >= numExchange){
                numBottles+=(emptyBottles/numExchange);
                emptyBottles=emptyBottles % numExchange;
            }
        }
        return totalBottles;
    }
};