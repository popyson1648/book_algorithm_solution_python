#include <iostream>
#include <vector>
using namespace std;
using Graph = vector<vector<int>>;

vector<bool> used;
void rec(const Graph &G, int v, int p = -1) {
    // 子頂点の中に採用済みの頂点があるかどうか
    bool exist = false;
    for (auto ch: G[v]) {
        if (ch == p) continue;

        // 再帰的探索
        rec(G, ch, v);
        if (used[ch]) exist = true;
    }

    // 子頂点の中に採用済みの頂点がなければ採用する
    if (!exist) used[v] = true;
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
    used.assign(N, false);
    rec(G, 0);

    // 数える
    int res = 0;
    for (int v = 0; v < N; ++v) {
        if (used[v]) ++res;
    }
    cout << res << endl;
}
