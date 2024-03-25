#include <iostream>
using namespace std;

int maximalSquare(vector<vector<int>> matrix);

int main(){
    vector<vector<int>> input = {{1,0,1,0,0},{1,0,1,1,1},{1,1,1,1,1},{1,0,0,1,0}};
    int output = maximalSquare(input);
    cout << output;
}

int maximalSquare(vector<vector<int>> matrix){
    int maxSquare=0, m = matrix.size(), n = matrix[0].size();
    std::vector<vector<int>> dp ((n+1), vector<int>(m+1, 0));

    for(int i=0; i<m;i++){
        for(int j=0;j<n;j++){
            if(matrix[i][j]==1){
                dp[i+1][j+1]=min(dp[i][j], min(dp[i+1][j], dp[i][j+1]))+1;
                maxSquare = max(maxSquare, dp[i+1][j+1]);
            }
        }
    }

    return maxSquare * maxSquare;
}