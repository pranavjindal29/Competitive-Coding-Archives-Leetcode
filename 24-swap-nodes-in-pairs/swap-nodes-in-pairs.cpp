#include <iostream>
using namespace std;


class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if (!head || !head->next) return head;

        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        ListNode* prev = dummy;

        while (prev->next && prev->next->next) {
            ListNode* first = prev->next;
            ListNode* second = prev->next->next;

            first->next = second->next;
            second->next = first;
            prev->next = second;

            prev = first;
        }

        return dummy->next;
    }
};