#include <iostream>
using namespace std;

std::string longestPalindromicSubstring(std::string str);
bool isPalindromic(std::string s);

int main(){
    // Input: s = "babad"  Output: "bab"
    std::string input ="babad";
    std::string output="";
    output = longestPalindromicSubstring(input);
    cout << output;
}

bool isPalindromic(std::string s){
    if (s.length()==1){
        return true;
    }
    int left=0, right=s.length()-1;
    while(left<right){
        if(s[left] != s[right]){
            return false;
        }
        left++;
        right--;
    }
    return true;
}

std::string longestPalindromicSubstring(std::string str){
    if (str.length()<=1){
        return str;
    }
    int max_len=1;
    std::string max_str=str.substr(0,1);
    for(int i=0; i<str.length();i++){
        for(int j=i;j<str.length();j++){
            if (j-i > max_len && isPalindromic(str.substr(i,j))){
                max_len = j-i;
                max_str = str.substr(i,j);
            }
        }
    }
    return max_str;
}