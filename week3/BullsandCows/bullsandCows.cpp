#include <iostream>
using namespace std;

std::string bullsAndCows(std::string secret,  std::string guess);

int main(){
    // Input: secret = "1807", guess = "7810"
    // Output: "1A3B"
    // Input: secret = "1123", guess = "0111"
    // Output: "1A1B"

    std::string secret = "1807";
    std::string guess = "7810";
    std::string output = bullsAndCows(secret, guess);
    cout << output << "\n";

    std::string secret2 = "1123";
    std::string guess2 = "0111";
    std::string output2 = bullsAndCows(secret2, guess2);
    cout << output2;
}

std::string bullsAndCows(std::string secret, std::string guess){
    int bulls = 0;
    int cows = 0;
    std::string output="";
    int n = secret.size();

    // create map
    std::unordered_map<char, int> mp;
    for(int x = 0; x< n; x++){
        mp[secret[x]]=1;
    }
    // checking for bulls
    for(int j=0;j<n;j++){
        if (secret[j]==guess[j]){
            bulls++;
            secret[j]=-1;
        }
    }
    printf("beofer checking cows\n");
    for(auto& it: mp){
        cout << it.first << " : " << it.second << endl;
    }

    // checking for cows
    for(int i=0; i<n; i++){
        if (secret.find(guess[i])!=-1 && mp[guess[i]]!=-1){
            cows++;
            mp[guess[i]]=-1;
            guess[i]=-1;
        }
    }
    output = to_string(bulls)+"A"+to_string(cows)+"B";
    return output;
}