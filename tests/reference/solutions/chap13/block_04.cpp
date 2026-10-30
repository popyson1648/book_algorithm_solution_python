#include <iostream>
#include <vector>
#include <queue>
using namespace std;

// グラフを表す型
using Graph = vector<vector<int>>;

// 頂点 s を始点とした BFS
vector<int> color;  // 1: 黒色, 0: 白色, -1: 未確定
bool bfs(const Graph &G, int s) {
    queue<int> que;

    // 初期条件
    color[s] = 0;
    que.push(s);

    // キューが空になるまで探索
    bool is_bipartite = true;
    while (!que.empty()) {
        // キューから先頭要素を取り出す
        int v = que.front();
        que.pop();

        // 頂点 v に隣接する各頂点を探索
        for (auto next_v: G[v]) {
            // 隣接頂点がすでに色確定していた場合
            if (color[next_v] != -1) {
                // 同じ色が隣接した場合は二部グラフではない
                if (color[next_v] == color[v]) {
                    is_bipartite = false;
                }
                continue;
            }
            
            // 隣接頂点の色を変更して、キューに push
            color[next_v] = 1 - color[v];
            que.push(next_v);
        }
    }
    return is_bipartite;
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

    // 配列 color 全体を -1 に初期化して BFS
    color.assign(N, -1);
    bool is_bipartite = true;
    for (int v = 0; v < N; ++v) {
        // v が探索済みの場合は探索しない
        if (color[v] != -1) continue;

        // 頂点 v を始点とした BFS
        // もし連結成分が二部グラフでなければ、全体の答えも false
        if (!bfs(G, v)) is_bipartite = false;
    }
    
    if (is_bipartite) cout << "Yes" << endl;
    else cout << "No" << endl;
}
