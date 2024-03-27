#include <iostream> 
using namespace std;

int countPathsinGrid(vector<vector<int>> prid);
int walkOverGrid(int i, int j, int prev, vector<vector<int>> dp, vector<vector<int>> prid);

int main(){
    vector<vector<int>> input = {{1,1},{3,4}};
    int output = countPathsinGrid(input);
    cout << output;
}

int countPathsinGrid(vector<vector<int>> prid){
    int m = prid.size(), n = prid[0].size(), totalPath = 0;
    vector<vector<int>> dp (n, vector<int>(m,-1));
    
    for(int i=0; i<m;i++){
        for(int j=0;j<n;j++){
            totalPath+=walkOverGrid(i,j,-1,dp,prid);
        }
    }

    return totalPath;
}

int walkOverGrid(int i, int j, int prev, vector<vector<int>> dp, vector<vector<int>> prid){
    int total=1;
    // checking no over range
    if(i<0 || i >= prid.size() || j<0 || j >= prid[0].size() || prid[i][j] <= prev){
        return 0;
    }
    // chekc the cell already visted
    if (dp[i][j] != -1){
        return dp[i][j];
    }
    // walk over diff direction
    if (dp[i][j] == -1){
        vector<pair<int,int>> direction = {{1,0},{-1,0},{0,1},{0,-1}};
        for(auto &dir : direction){
            total+=walkOverGrid(i+dir.first, j+dir.second, prid[i][j], dp, prid);
        }
    }
    dp[i][j] = total;
    // return with mod
    int mod = 1e9+7;
    return int(total%mod);
}