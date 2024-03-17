#include <iostream>
#include <string>
using namespace std;

std::string addBinary(std::string num1, std::string num2);

//Input: a = "11", b = "1" Output: "100"
int main(){
    std::string num1 = "11";
    std::string num2="1";
    std::string output="";
    output = addBinary(num1, num2);
    cout << output;
}
std::string addBinary(std::string num1, std::string num2){
    std::string output="";
    int i = num1.length()-1;
    int j = num2.length()-1;
    int carry=0;
   
    while (i>=0 || j >=0 || carry){
        int sum =0;
        if(i>=0){
            string s = "";
            s+=num1[i];
            int x = std::stoi(s);
            sum+=x;
        }
        if(j>=0){
            string s = "";
            s+=num2[j];
            int y = std::stoi(s);
            sum+=y;
        }
        sum+= carry;
        carry = sum/2;
        output+=std::to_string(sum%2);
        i--;
        j--;
    }
    std::string rOutput(output.rbegin(), output.rend());

    return rOutput;
}