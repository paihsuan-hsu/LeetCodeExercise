#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

vector<string> longestSubstringWithoutRepeatingCharacters(string numbers);
void backtrack(string numbers, string letters, vector<string> &output);

unordered_map<char,string> phone_map;

int main(){
    phone_map['1']="";
    phone_map['2']="abc";
    phone_map['3']="def";
    phone_map['4']="ghi";
    phone_map['5']="jkl";
    phone_map['6']="mno";
    phone_map['7']="pqrs";
    phone_map['8']="tuv";
    phone_map['9']="wxyz";
    string input = "23";
    vector<string> output = longestSubstringWithoutRepeatingCharacters(input);
    for (auto i: output){
        std::cout << i << '\n';
    }
}

void backtrack(string numbers, string letters, vector<string> &output){
    if(numbers.length()== 0){
        output.push_back(letters);
    }
    for (auto& [key, value]: phone_map){
        if (key == numbers[0]){
            backtrack(numbers.substr(1, numbers.length()), letters+value, output);
        }
    }
}

vector<string> longestSubstringWithoutRepeatingCharacters(string numbers){
    string letters = "";
    vector<string> output;
    backtrack(numbers, letters, output);
   
    return output;
}