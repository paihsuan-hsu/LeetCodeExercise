#include <iostream>
#include <queue>
using namespace std;

int lastStoneWeight(vector<int> stones);

int main(){
    vector<int> input = {2,7,4,1,8,1};
    int output = lastStoneWeight(input);
    printf("last stone: %d", output);
}

int lastStoneWeight(vector<int> stones){
    priority_queue<int> st (stones.begin(), stones.end());

    while (st.size() > 1) {
        int x = st.top();
        st.pop();
        int y = st.top();
        st.pop();
        if (x!=y){
            st.push(abs(x-y));
        }
    }
    
    return st.top();
}