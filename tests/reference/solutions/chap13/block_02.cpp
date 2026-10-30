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

    // 配列 dist 全体を -1 に初期化
    dist.assign(N, -1);

    // 各頂点からの BFS
    int result = 0;
    for (int v = 0; v < N; ++v) {
        // 探索済みの連結成分はスキップする
        if (dist[v] != -1) continue;

        // 頂点 v を始点とした DFS
        bfs(G, v);

        // 連結成分数が増える
        ++result; 
    }

    cout << result << endl;
}
