/* 练习版：基于链表实现的栈 */
#include <vector>
#include <stdexcept>
using namespace std;
typedef struct ListNode {
    int val;
    struct ListNode *next;
}ListNode;

class LinkedListStack {
  private:
    ListNode *stackTop; // 栈顶节点
    int stkSize;        // 栈的长度

  public:
    LinkedListStack(){
      stackTop = nullptr;
      stkSize = 0;
    }
    ~LinkedListStack(){
      while (stackTop != nullptr){
        ListNode* temp = stackTop;
        stackTop = stackTop->next;
        delete temp;
      }
    }

    /* 获取栈的长度 */
    int size(){
      return stkSize;
    }

    /* 判断栈是否为空 */
    bool isEmpty(){
      return stkSize == 0;
    }

    /* 入栈 */
    void push(int num){
      stkSize ++;
      ListNode* node =  new ListNode;
      node->val = num;
      node->next = stackTop;
      stackTop = node; 
    }

    /* 出栈 */
    int pop(){
      if(isEmpty()){throw out_of_range("empty");}
      int res = stackTop->val;
      ListNode* to_delete = stackTop;
      stackTop = stackTop->next;
      delete to_delete;
      stkSize--;
      return res;
    }

    /* 访问栈顶元素 */
    int top(){
      if(isEmpty()){throw out_of_range("empty");}
      return stackTop->val;
    }

    /* 将 List 转换为 Array 并返回 */
    vector<int> toVector(){
      vector<int> res(size());
      ListNode* node = stackTop;
      for(int i = size() -1; i >= 0; i--){
        res[i] = node->val;
        node = node->next;
      }
      return res;
    }
};

/* 练习提示：
 * 1. 链表栈可以直接把头节点当作栈顶。
 * 2. 入栈时，新节点接到原栈顶前面。
 * 3. 出栈时，先保存栈顶值，再释放旧节点。
 * 4. 遍历转数组时，注意结果顺序要和栈底到栈顶一致。
 */

