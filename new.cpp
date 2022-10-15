//1448. Count Good Nodes in Binary Tree

class Solution{
public:
    int goodNodes(TreeNode* root){
        return dfs(root, INT_MIN);
    }
    int dfs(TreeNode* root, int max){
        if(!root) return 0;
        int res = 0;
        if(root->val >= max){
            res++;
            max = root->val;
        }
        res += dfs(root->left, max);
        res += dfs(root->right, max);
        return res;
    }
};
