#include <iostream>
using namespace std;

int minimumOperationsToReduceIntegerToZero(int number);

int main(){
    int input = 39;
    int output = minimumOperationsToReduceIntegerToZero(input);
    cout << output;
}

int minimumOperationsToReduceIntegerToZero(int number){
    int count =0, diff = number;
    while(diff !=0){
        double logNum = log2(diff);
        int x = round(logNum);
        int y = pow(2,x);
        diff = abs(diff - y);
        printf("diff is: %d\n", diff);
        count++;
    }
    return count;
}