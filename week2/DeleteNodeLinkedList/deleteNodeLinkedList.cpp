#include <iostream>
using namespace std;

struct ListNode{
    int value;
    ListNode* next;
    ListNode():value(0), next(nullptr){}
    ListNode(int x):value(x), next(nullptr){}
    ListNode(int x, ListNode* next):value(x), next(next){}
};

ListNode* deleteNode(ListNode* input, int taregt);

// head = [4,5,1,9], node = 5 Output: [4,1,9]
int main(){
    int taregt = 5;
    ListNode* input1=new ListNode(9, nullptr);
    ListNode* input2=new ListNode(1, nullptr);
    ListNode* input3=new ListNode(5, nullptr);
    ListNode* input4=new ListNode(4, nullptr);
    input1->next=input2;
    input2->next=input3;
    input3->next=input4;
    input4->next=NULL;

    ListNode* output = deleteNode(input1, taregt);
    while(output){
        cout << output->value << "\n";
        output=output->next;
    }
}

ListNode* deleteNode(ListNode* input, int taregt){
    ListNode* output = new ListNode();
    output = input;
    ListNode* dummy = output;
    while(dummy){
        cout << dummy->value << "\n";
        if(dummy->value == taregt){
            dummy->value = dummy->next->value;
            dummy->next = dummy->next->next;
        }
        dummy=dummy->next;
    }
    return output;
}