class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (!head || !head->next || k == 0) return head;
        
        ListNode* tail = head;
        int length = 1;
        
        while (tail->next) {
            tail = tail->next;
            length++;
        }
        
        k %= length;
        if (k == 0) return head;
        
        tail->next = head;
        int stepsToNewHead = length - k;
        ListNode* newTail = tail;
        
        while (stepsToNewHead--) {
            newTail = newTail->next;
        }
        
        ListNode* newHead = newTail->next;
        newTail->next = nullptr;
        
        return newHead;
    }
};