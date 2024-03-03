#include <iostream>
using namespace std;

class shuffleArray{
    vector<int> org;
    int n;
public:
    void set(vector<int>numbers){
        this->org = numbers;
        this->n = numbers.size();
        cout << "this is org size list: " << n << "\n";
    }

    vector<int> reset(){
        return org;
    }

    vector<int> shuffle(){
        vector<int> shuffle = org;
        int randNum = n;
        for(int i=0; i< n; i++){
            int tmp = rand()%randNum;
            swap(shuffle[i], shuffle[tmp]);
        }

        return shuffle;
    }
};

int main(){
    vector<int> input = {1,2,3};
    shuffleArray arr;
    arr.set(input);
    vector<int> output = arr.shuffle();
    for(auto it: output){
        cout << it << " ";
    }
    vector<int> outputReset = arr.reset();
    for(auto it: outputReset){
        cout << it << " ";
    }
}