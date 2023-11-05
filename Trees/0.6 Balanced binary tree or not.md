```cpp
class Solution {
private:
    int actualAnswer(TreeNode* root)
    {
        if (root == NULL)
            return 0;
        
        int left = actualAnswer(root->left);
        if (left == -1) return -1;
        
        int right = actualAnswer(root->right);
        if (right == -1) return -1;
    
    
        if (abs(right - left) > 1)  return -1;
        return 1 + max(left, right);
    }
public:
    bool isBalanced(TreeNode* root) {
        if (actualAnswer(root) == -1)
            return false;
        else
            return true;
    }
};
```