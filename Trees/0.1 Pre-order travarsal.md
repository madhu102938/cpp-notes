==Center, Left, Right==

### Recursive Way
```cpp
void preorder(node* root)
{
	if (root == NULL)
		return;
	cout << root->data;
	preorder(root->left);
	preorder(root->right);	
}
```


### Iterative way
```cpp
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> ds;
        stack <TreeNode*> s;
        if (root == NULL)
            return ds;
        s.push(root);
        while (!s.empty())
        {
            TreeNode* topNode = s.top();
            s.pop();
            ds.push_back(topNode->val);
            if (topNode->right != NULL)
                s.push(topNode->right);
            if (topNode->left != NULL)
                s.push(topNode->left);
        }
        return ds;
    }
};
```
