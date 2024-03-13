#include <iostream>
using namespace std;

struct ListNode{
    int value;
    ListNode* next;
    ListNode(): value(0), next(nullptr){}
    ListNode(int x):value(x), next(nullptr){}
    ListNode(int x, ListNode* next): value(x), next(next){}
};

ListNode* addTowNumbers(ListNode* head);

int main(){
    // head = [1,8,9] and output = [3,7,8]
    ListNode* input1 = new ListNode();
    ListNode* input1_1 = new ListNode();
    ListNode* input1_2 = new ListNode();
    input1->value=9;
    input1->next=input1_1;
    input1_1->value=8;
    input1_1->next=input1_2;
    input1_2->value=1;
    input1_2->next=NULL;

    ListNode* output = new ListNode();
    output=addTowNumbers(input1);
    while(output!=NULL){
        cout << output->value << "\n";
        output=output->next;
    }
}

ListNode* addTowNumbers(ListNode* head){
    ListNode* output = new ListNode();
    ListNode* dummy = output;
    int carry=0;
    while( head || carry){
        int db = 0;
        if(head){
            int x = head->value;
            db = x*2;
            head=head->next;
        }
        db += carry;
        carry = db/10;
        ListNode* tmp = new ListNode(db%10, NULL);
        dummy->next=tmp;
        dummy=dummy->next;
    }
    return output->next;
}
