//967. Numbers With Same Consecutive Differences

class Solution {
    public:
     vector<int> numsSameConsecDiff(int N, int K) {
        vector<int> res;
        if (N == 1) {
            res.push_back(0);
        }
        for (int i = 1; i < 10; i++) {
            dfs(i, N - 1, K, res);
        }
        return res;
    }

    void dfs(int num, int N, int K, vector<int>& res) {
        if (N == 0) {
            res.push_back(num);
            return;
        }
        int last = num % 10;
        if (last + K < 10) {
            dfs(num * 10 + last + K, N - 1, K, res);
        }
        if (last - K >= 0 && K != 0) {
            dfs(num * 10 + last - K, N - 1, K, res);
        }
    }
};
