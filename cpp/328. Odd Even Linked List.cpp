/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

class Solution{
public:
    ListNode* oddEvenList(ListNode* head){
    /**
    这道题给了我们一个链表，让我们分开奇偶节点，所有奇节点在前，偶节点在后。
    我们可以使用两个指针来做，prev指向奇节点，curr指向偶节点，然后把偶节点curr后面的那个奇节点提前到prev的后面，
    然后pre和cur各自前进一步，此时curr又指向偶节点，prev指向当前奇节点的末尾，以此类推直至把所有的偶节点都提前了即可，代码如下：
     */
        if (!head || !head->next) return head;
        ListNode* prev = head;
        ListNode* curr = head->next;
        while(curr && curr->next){
            ListNode* tmp = prev->next;
            prev->next = curr->next;
            curr->next = curr->next->next;
            prev->next->next = tmp;
            curr = curr->next;
            prev = prev->next;
        }
        return head;
    }
};


