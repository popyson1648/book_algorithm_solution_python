#include <iostream>
#include <vector>
using namespace std;

// グラフを表す型
using Graph = vector<vector<int>>;

// 深さ優先探索
vector<bool> seen;
void dfs(const Graph &G, int v) {
    // 頂点 v を訪問済みにする
    seen[v] = true;

    // 頂点 v に隣接する各頂点を探索
    for (auto next_v: G[v]) {
        // 探索済みの頂点は探索しない
        if (seen[next_v]) continue;

        // 再帰的に探索
        dfs(G, next_v);
    }
}

int main() {
    // 頂点数と辺数
    int N, M;
    cin >> N >> M;

    // グラフ入力受け取り
    Graph G(N);
    for (int i = 0; i < M; ++i) {
        int a, b;
        cin >> a >> b;
        G[a].push_back(b);
        G[b].push_back(a);
    }

    // 全頂点が探索済みになるまで DFS
    int result = 0;
    seen.assign(N, false);  // 全頂点を未訪問に初期化
    for (int v = 0; v < N; ++v) {
        // 探索済みの連結成分はスキップする
        if (seen[v]) continue;

        // 頂点 v を始点とした DFS
        dfs(G, v);

        // 連結成分数が増える
        ++result; 
    }

    cout << result << endl;
}
