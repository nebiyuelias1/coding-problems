#include <bits/stdc++.h>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* reverseLinkedList(ListNode* curr, ListNode* prev) {
        if (curr->next == nullptr) {
            curr->next = prev;
            return curr;
        }

        ListNode* newNext = curr->next;
        ListNode* newPrev = curr;
        curr->next = prev;
        return this->reverseLinkedList(newNext, newPrev);   
    }

    bool isPalindrome(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;

        while (fast != nullptr && fast->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;
            if (fast != nullptr && fast->next == nullptr) {
                slow = slow->next;
            }
        }

        ListNode* rightHalfStartPosition = this->reverseLinkedList(slow, nullptr);

        while (rightHalfStartPosition != nullptr) {
            if (head->val != rightHalfStartPosition->val) {
                return false;
            }
            rightHalfStartPosition = rightHalfStartPosition->next;
            head = head->next;
        }

        return true;
    }
};

int main(int argc, char const *argv[])
{
    
    return 0;
}
