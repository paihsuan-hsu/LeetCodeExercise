#include <iostream>
using namespace std;

int countSqaures(vector<vector<int>> matrix);

int main(){
    vector<vector<int>> input = {{1,0,1}, {1,1,0}, {1,1,0}};
    int output = countSqaures(input);
    cout << output;
}

int countSqaures(vector<vector<int>> matrix){
    int found=0, m=matrix.size(), n=matrix[0].size();
    std::vector<vector<int>> dp ((n+1), vector<int>(m+1, 0));
    
    for(int i =0;i<m;i++){
        for(int j=0;j<n;j++){
            if (matrix[i][j]==1){
                dp[i+1][j+1]=std::min(dp[i][j],std::min(dp[i+1][j],dp[i][j+1]))+1;
                found+=dp[i+1][j+1];
            }
        }
    }

    return found;
}


// m * n
// [1,0,1]
// [1,1,0]
// [1,1,0]

// size 1x1 is 6
// size 2x2 is 1
// size 3x3 is 0
// found = 7