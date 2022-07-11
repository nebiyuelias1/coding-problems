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
    ListNode* reverseList(ListNode* head) {
        ListNode* iterator = head;
        ListNode* previousValue = nullptr;
        ListNode* newHead = head;
        while (iterator != nullptr) {
            if (iterator->next == nullptr) {
                newHead = iterator;
            }
            ListNode* tempNext = iterator->next;
            iterator->next = previousValue;
            previousValue = iterator;
            iterator = tempNext;
            
        }
        return newHead;
    }
};

int main(int argc, char const *argv[])
{
    
    return 0;
}