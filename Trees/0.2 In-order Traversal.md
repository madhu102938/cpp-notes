==Left, Center, Right==

```cpp
class Solution {
private:
    void actualAnswer(TreeNode* root, vector<int> &ds)
    {
        if (root == NULL)
            return;
        actualAnswer(root->left, ds);
        ds.push_back(root->val);
        actualAnswer(root->right, ds);
    }
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> ds;
        actualAnswer(root, ds);
        return ds;
    }
};
```



### Iterative Traversal
```cpp
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> ds;
        stack<TreeNode*> s;
        while (true)
        {
            if (root!= NULL)
            {
                s.push(root);
                root = root->left;
            }
            else
            {
                if (s.empty())  break;
                root = s.top();
                s.pop();
                ds.push_back(root->val);
                root = root->right;
            }
        }
        return ds;
    }
};
```