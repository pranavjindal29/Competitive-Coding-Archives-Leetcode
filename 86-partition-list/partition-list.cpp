/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
 ListNode* partition(ListNode* head, int x) {
        // Dummy nodes for the two partitions
        ListNode less_dummy(0);  // Dummy node for nodes less than x
        ListNode greater_dummy(0);  // Dummy node for nodes greater than or equal to x
        
        // Pointers to build the two partitions
        ListNode* less = &less_dummy;
        ListNode* greater = &greater_dummy;
        
        // Traverse the original list
        ListNode* current = head;
        while (current) {
            if (current->val < x) {
                less->next = current;
                less = less->next;
            } else {
                greater->next = current;
                greater = greater->next;
            }
            current = current->next;
        }
        
        // Connect the two partitions
        greater->next = nullptr;  // End the greater list
        less->next = greater_dummy.next;  // Link less list to greater list
        
        // Return the head of the partitioned list
        return less_dummy.next;
    }
};