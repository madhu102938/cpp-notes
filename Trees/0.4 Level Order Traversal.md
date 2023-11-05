```cpp
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        queue<TreeNode*> q;
        vector<vector<int>> ans;
        if (root == NULL)
            return ans;
        q.push(root);
        while (!q.empty())
        {
            int n = q.size();
            vector<int> ans_vec;
            for (int i = 0; i < n; i++)
            {
                TreeNode* temp = q.front();
                q.pop();
                if (temp->left != NULL) q.push(temp->left);
                if (temp->right != NULL) q.push(temp->right);
                ans_vec.push_back(temp->val);
            }
            ans.push_back(ans_vec);
        }
        return ans;
    }
};
```