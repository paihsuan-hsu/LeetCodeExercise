#include <iostream>
#include <string>
#include <unordered_set>
using namespace std;

int longestSubstringWithoutRepeatingCharacters(string s);

int main(){
    string input = "abcabcbb";
    int output = longestSubstringWithoutRepeatingCharacters(input);
    std:: cout << output;
}

int longestSubstringWithoutRepeatingCharacters(string s){
    int maxLen = 0, subWalker=0;
    unordered_set<char> charSet;

    for(int i =0; i < s.length(); i++){
        if(!charSet.count(s[i])){
            charSet.insert(s[i]);
            maxLen = charSet.size();
        } else {
            while(charSet.count(s[i])){
                charSet.erase(s[subWalker]);
                subWalker++;
            }
            charSet.insert(s[i]);
        }
    }

    return maxLen;
}