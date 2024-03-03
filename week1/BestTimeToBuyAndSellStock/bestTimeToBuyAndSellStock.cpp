#include <iostream>
using namespace std;

int bestTimeToBuyAndSellStock(vector<int> prices);

int main(){
    vector<int> prices = {7,1,5,3,6,4};
    int output = bestTimeToBuyAndSellStock(prices);
    cout << output << "\n";

    prices = {7,6,4,3,1};
    output = bestTimeToBuyAndSellStock(prices);
    cout << output;
}

int bestTimeToBuyAndSellStock(vector<int> prices){
    int max_profit=0, low = prices[0];
    for(int i=0; i< prices.size(); i++){
        low = min(low, prices[i]);
        max_profit = max(max_profit, prices[i] - low);
    }
    return max_profit;
}