# Finding a node in BST
You are given the `root` of a binary search tree (BST) and an integer `val`.

Find the node in the BST that the node's value equals `val` and return the subtree rooted with that node. If such a node does not exist, return `null`.

**Recursive Approach**
```cpp
	// Passing the pointer as pass by reference
    void actualAnswer(TreeNode* root, int val, TreeNode* &ans)
    {
        if (root == nullptr)
            return;
        
        if (root->val == val)
        {
            ans = root;
            return;
        }

        if (val < root->val)
            actualAnswer(root->left, val, ans);
        else
            actualAnswer(root->right, val, ans);
    }
    
    TreeNode* searchBST(TreeNode* root, int val) 
    {
        TreeNode* ans = nullptr;
        actualAnswer(root, val, ans);
        return ans;
    }
```


**Iterative Approach**
```cpp
    TreeNode* searchBST(TreeNode* root, int val) 
    {
        while (root != nullptr && root->val != val)
            root = val < root->val ? root->left : root->right;
    
        return root;
    }
```

# Minimum element of BST
You are given a **Binary Search Tree**
Find **Minimum** element in it.

```cpp
int minVal(Node* root)
{
	if (root == nullptr)
		return -1;
	int ans = root->data;
	while (root->left != nullptr)
	{
		root = root->left;
		ans = root->data;
	}
	return ans;
}
```