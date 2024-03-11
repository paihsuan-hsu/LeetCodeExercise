#include <iostream>
#include <cstddef>

using namespace std;

struct ListNode {
    int value;
    ListNode *next;
    ListNode(): value(0), next(nullptr){}
    ListNode(int x): value(x), next(nullptr){}
    ListNode(int x, ListNode *next): value(x), next(next){}
};

//l1 = [2,4,3], l2 = [5,6,4]
// output = [8,0,7]
ListNode* addTowNumbers(ListNode* num1, ListNode* num2);

int main(){
    ListNode* input1 = NULL;
    ListNode* input1_1 = NULL;
    ListNode* input1_2 = NULL;
    ListNode* input2 = NULL;
    ListNode* input2_1 = NULL;
    ListNode* input2_2 = NULL;
    input1 = new ListNode();
    input1_1 = new ListNode();
    input1_2 = new ListNode();
    input2 = new ListNode();
    input2_1 = new ListNode();
    input2_2 = new ListNode();
    input1->value = 3;
    input1->next = input1_1;
    input1_1->value = 4;
    input1_1->next = input1_2;
    input1_2->value = 2;
    input2->value = 4;
    input2->next = input2_1;
    input2_1->value = 6;
    input2_1->next = input2_2;
    input2_2->value = 5;
    ListNode* ouput = addTowNumbers(input1, input2);
    
    while(ouput != NULL){
        cout << ouput->value << " ";
        ouput = ouput->next;
    }
}

ListNode* addTowNumbers(ListNode* num1, ListNode* num2){
    ListNode* output = new ListNode();
    ListNode* dummy = output;
    int carry = 0;
    
    while(num1||num2||carry){
        int sum =0;
        if(num1){
            int x = num1->value;
            sum += x;
            num1 = num1->next;
        }
        if(num2){
            int y = num2->value;
            sum += y;
            num2 = num2->next;
        }
        sum += carry;
        carry = sum/10;
        printf("sum is: %d  carry is: %d\n", sum, carry);

        dummy->next = new ListNode(sum%10);
        dummy = dummy->next;
    }

    return output->next;
}