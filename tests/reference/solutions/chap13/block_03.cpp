#include <iostream>
#include <vector>
#include <queue>
using namespace std;

// グラフを表す型
using Graph = vector<vector<int>>;

// 頂点 s を始点とした BFS
vector<int> dist;  // BFS に用いる距離配列
void bfs(const Graph &G, int s) {
    queue<int> que;

    // 初期条件
    dist[s] = 0;
    que.push(s);

    // キューが空になるまで探索
    while (!que.empty()) {
        // キューから先頭要素を取り出す
        int v = que.front();
        que.pop();

        // 頂点 v に隣接する各頂点を探索
        for (auto next_v: G[v]) {
            // 探索済みの頂点は探索しない
            if (dist[next_v] != -1) continue;

            // 新たな頂点をキューに追加
            dist[next_v] = dist[v] + 1;
            que.push(next_v);
        }
    }
}

int main() {
    // 頂点数と辺数、s と t
    int N, M, s, t;
    cin >> N >> M >> s >> t;

    // グラフ入力受け取り
    Graph G(N);
    for (int i = 0; i < M; ++i) {
        int a, b;
        cin >> a >> b;
        G[a].push_back(b);
        G[b].push_back(a);
    }

    // 配列 dist 全体を -1 に初期化して BFS
    dist.assign(N, -1);
    bfs(G, s);

    // t にたどり着けるかどうか
    if (dist[t] != -1) cout << "Yes" << endl;
    else cout << "No" << endl;
}
