#include <iostream>
using namespace std;

vector<int> twoSum(vector<int>& numbers, int taregt);

int main(){
    vector<int> input = {2,7,11,15};
    int taregt = 9;
    vector<int> output = twoSum(input, taregt);
    for(auto it: output){
        cout << it << '\n';
    }
}

vector<int> twoSum(vector<int>& numbers, int taregt){
    vector<int> output = {};
    for(int i = 0; i < numbers.size();i++){
        for(int j=0; j < numbers.size(); j++){
            if(numbers[i]+numbers[j]==taregt){
                output.push_back(i);
                output.push_back(j);
                return output;
            }
        }
    }

    return output;
}
