#include <iostream>
#include <vector>
using namespace std;
using Graph = vector<vector<int>>;

// MOD
const int MOD = 1000000007;

// 木上の動的計画法
// dp1: 部分木の根を選ばない場合、dp2: 部分木の根を選ぶ場合
vector<long long> dp1, dp2;
void rec(const Graph &G, int v, int p = -1) {
    // 子頂点を再帰的に探索する
    for (auto ch: G[v]) {
        if (ch == p) continue;
        rec(G, ch, v);
    }

    // dp1: 各部分木の安定集合 (根の選択によらない) の個数の積
    // dp2: 各部分木の安定集合 (根は選ばない) の個数の積
    for (auto ch: G[v]) {
        if (ch == p) continue;
        dp1[v] = dp1[v] * (dp1[ch] + dp2[ch]) % MOD;
        dp2[v] = dp2[v] * dp1[ch] % MOD;
    }
}

int main() {
    // 入力
    int N;
    cin >> N;
    Graph G(N);
    for (int i = 0; i < N - 1; ++i) {
        int u, v;
        cin >> u >> v;
        --u, --v;
        G[u].push_back(v);
        G[v].push_back(u);
    }

    // 頂点 0 を根として探索
    dp1.assign(N, 1), dp2.assign(N, 1);
    rec(G, 0);
    cout << (dp1[0] + dp2[0]) % MOD << endl;
}
