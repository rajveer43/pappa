//987. Vertical Order Traversal of a Binary Tree


class Solution { 
    public:
    vector<vector<int>> verticalTraversal(TreeNode* root) {
        map<int, map<int, multiset<int>>> m;
        queue<pair<TreeNode*, pair<int, int>>> q;
        q.push({root, {0, 0}});
        while (!q.empty()) {
            auto p = q.front();
            q.pop();
            m[p.second.first][p.second.second].insert(p.first->val);
            if (p.first->left) q.push({p.first->left, {p.second.first - 1, p.second.second + 1}});
            if (p.first->right) q.push({p.first->right, {p.second.first + 1, p.second.second + 1}});
        }
        vector<vector<int>> ans;
        for (auto& it : m) {
            vector<int> v;
            for (auto& it2 : it.second) {
                v.insert(v.end(), it2.second.begin(), it2.second.end());
            }
            ans.push_back(v);
        }
        return ans;
    }
};