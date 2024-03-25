#include <iostream>
using namespace std;

int longestIncreasingPath(vector<vector<int>> maxtrix);
int walk_over_maxtrix(int i, int j, int prev, int m, int n, vector<vector<int>> dp, vector<vector<int>> maxtrix);

int main(){
    vector<vector<int>> input = {{3,4,5},{3,2,6},{2,2,1}};
    int output = longestIncreasingPath(input);
    cout << output;
}

int walk_over_maxtrix(int i, int j, int prev, int m, int n, vector<vector<int>> dp, vector<vector<int>> maxtrix){
    if(i<0 || i>=m|| j<0|| j>=n|| prev>=maxtrix[i][j]){
        return 0;
    }
    if(dp[i][j] == -1){
        // walk over 4 dir
        dp[i][j] = std::max(
            walk_over_maxtrix(i+1, j, maxtrix[i][j], m,n,dp,maxtrix),
            max(walk_over_maxtrix(i-1, j, maxtrix[i][j], m,n,dp,maxtrix),
            max(walk_over_maxtrix(i, j+1, maxtrix[i][j], m,n,dp,maxtrix),
            walk_over_maxtrix(i, j-1, maxtrix[i][j], m,n,dp,maxtrix)))
        ) + 1;
    }

    return dp[i][j];
}

int longestIncreasingPath(vector<vector<int>> maxtrix){
    int m = maxtrix.size(), n = maxtrix[0].size(), maxPath=0; 
    vector<vector<int>> dp (n, vector<int>(m, -1));
    for(int i=0; i<m;i++){
        for(int j=0; j<n;j++){
            int path_len = walk_over_maxtrix(i,j,-1,m,n,dp, maxtrix);
            maxPath = std::max(maxPath, path_len);
        }
    }
    return maxPath;
}




// Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
// Output: 4
// The longest increasing path is [1, 2, 6, 9]

// Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
// Output: 4
// The longest increasing path is [3, 4, 5, 6]