#include <iostream>
#include <vector>
#include <string>
using namespace std;

int maxArea(vector<int>& height);

int main(){
    vector<int> height = {1,8,6,2,5,4,8,3,7};
    int output = maxArea(height);
    std:: cout << output;
}

int maxArea(vector<int>& height){
    int left=0, right=height.size()-1, area=0, maxArea=0;

    while(left<right){
        area=(right-left) * min(height[left], height[right]);
        maxArea = max(maxArea,area);

        if(left<right){
            left++;
        } else {
            right--;
        }
    }
    return maxArea;
}