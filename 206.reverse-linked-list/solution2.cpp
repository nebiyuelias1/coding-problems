#include <bits/stdc++.h>

using namespace std;

/**
 * Definition for singly-linked list.

 */
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
 
class Solution {
public:
    ListNode* rec(ListNode* curr, ListNode* prev) {
        if (curr->next == nullptr) {
            curr->next = prev;
            return curr;
        }

        ListNode* newNext = curr->next;
        ListNode* newPrev = curr;
        curr->next = prev;
        return this->rec(newNext, newPrev);   
    }
    
    ListNode* reverseList(ListNode* head) {
        return this->rec(head, nullptr);    
    }
};

int main(int argc, char const *argv[])
{
    
    return 0;
}