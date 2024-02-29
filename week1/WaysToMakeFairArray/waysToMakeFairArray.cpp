#include <iostream>
using namespace std;

int waysToMakeFairArray(vector<int> numbers);

int main(){
    vector<int> input = {2,1,6,4};
    int output = waysToMakeFairArray(input);
    cout << output;
}

int waysToMakeFairArray(vector<int> numbers){
    int found =0, remover = 0, index=0, oddSum=0, evenSum=0;
    while(remover < numbers.size()){
        printf("remove: %d  ", remover);
        for(int i=0; i < numbers.size(); i++){
            if (i == remover){
                continue;
            }
            else if (i < remover){
                index = i;
            } else if (i > remover){
                index = i - 1;
            }

            printf("--- i is: %d AND index: %d   ", i, index);
            if (index % 2 == 0 ){
                printf("even value is: %d ", numbers[i]);
                evenSum += numbers[i];
            } else {
                printf("odd value is: %d ", numbers[i]);
                oddSum += numbers[i];
            }
        }
        if(evenSum == oddSum){
          found++;
        }
       
        printf("evenSum: %d ", evenSum);
        printf("oddSum: %d\n", oddSum);
        evenSum =0;
        oddSum=0;
        remover++;
    }
    return found;
}