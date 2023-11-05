<img  src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fcdn.procoding.org%2Fdatastructures%2Fbinary-tree%2Fdiameter-of-binary-tree%2Fdiameter-of-binary-tree.png&f=1&nofb=1&ipt=9381fc427416763fd2e0d899f56204c36e8ddbd781e38bf01a205c437ea381df&ipo=images" height ="300px"/>
Diameter of a binary tree is not the number of numbers in the longest path, but the path length itself (i.e., number of lines in the longest path)
- This is can also `right nodes + left nodes` in the oldest ancestor of the longest path. 


```cpp
class Solution {
private:
    int actualAnswer(TreeNode* root, int &diameter){
        if (root == NULL)
            return 0;
        int left = actualAnswer(root->left, diameter);
        int right = actualAnswer(root->right, diameter);
        diameter = max(diameter, left + right);
        return 1 + max(left, right);
    }

public:
    int diameterOfBinaryTree(TreeNode* root) {
        int diameter = 0;
        actualAnswer(root, diameter);
        return diameter;
    }
};
```