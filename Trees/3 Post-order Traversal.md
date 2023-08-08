==Left, Right, Center==

```cpp
class Solution {
private:
    void actualAnswer(TreeNode* root, vector<int> &ds)
    {
        if (root == NULL)
            return;
        actualAnswer(root->left, ds);
        actualAnswer(root->right, ds);
        ds.push_back(root->val);
    }
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> ds;
        actualAnswer(root, ds);
        return ds;
    }
};
```



### Iterative Traversal
*2 Stack method*
```cpp
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> ds;
        if (root == NULL)
            return ds;
        stack<TreeNode*> s1, s2;
        s1.push(root);
        while (!s1.empty())
        {
            root = s1.top();
            s1.pop();
            s2.push(root);
            if (root -> left)
                s1.push(root -> left);
            if (root -> right)
                s1.push(root -> right);
        }
        while (!s2.empty())
        {
            ds.push_back(s2.top()->val);
            s2.pop();
        }
        return ds;
    }
};
```