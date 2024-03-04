#include <iostream>
#include <string>
using namespace std;

int minNumberOfFrogs(string croakOfFrogs);

int main(){
    string input1 = "croakcroak";
    int output1 = minNumberOfFrogs(input1);
    cout << output1 << "\n";
    string input2 = "crcoakroak";
    int output2 = minNumberOfFrogs(input2);
    cout << output2 << "\n";
    string input3 = "croakcrook";
    int output3 = minNumberOfFrogs(input3);
    cout << output3 << "\n";
}

int minNumberOfFrogs(string croakOfFrogs){
    int c=0,r=0,o=0,a=0,k=0,found=0,same_frog=0;
    for ( auto croak: croakOfFrogs){
        if (croak == 'c'){
            if(c==k && c!=0){
                same_frog++;
            }
            c++;
        } else if ( croak == 'r'){
            r++;
        } else if ( croak == 'o'){
            o++;
        } else if ( croak == 'a'){
            a++;
        } else if ( croak == 'k'){
            k++;
        }
        if (c < r || r < o || o < a || a < k){
            return -1;
        }
    }
    if (c != r || r != o || o != a || a != k){
        return -1;
    }
    return c - same_frog;
}