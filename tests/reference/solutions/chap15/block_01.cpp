#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// Union-Find
struct UnionFind {
    vector<int> par;

    UnionFind() { }
    UnionFind(int n) : par(n, -1) { }
    void init(int n) { par.assign(n, -1); }
    
    int root(int x) {
        if (par[x] < 0) return x;
        else return par[x] = root(par[x]);
    }
    
    bool issame(int x, int y) {
        return root(x) == root(y);
    }
    
    bool merge(int x, int y) {
        x = root(x); y = root(y);
        if (x == y) return false;
        if (par[x] > par[y]) swap(x, y); // merge technique
        par[x] += par[y];
        par[y] = x;
        return true;
    }
    
    int size(int x) {
        return -par[root(x)];
    }
};

int main() {
    // 辺数
    int N, M;
    while (cin >> N >> M, N) {
        // 辺を表す構造体
        using pint = pair<int, int>;  // 両端点
        using Edge = pair<long long, pint>;  // (重み, 両端点)
        
        // 入力
        vector<Edge> edges(M);
        for (int i = 0; i < M; ++i) {
            cin >> edges[i].second.first >> edges[i].second.second
                >> edges[i].first;
            --edges[i].second.first;
            --edges[i].second.second;
        }

        // 辺を重み順にソート
        sort(edges.begin(), edges.end());

        // Kruskal 法 
        UnionFind uf(N);
        int num = 0;  // 辺の本数
        long long res = 0;  // 答え
        for (auto e: edges) {
            long long w = e.first;
            int u = e.second.first, v = e.second.second;

            // 辺 (u, v) は追加できない場合
            if (uf.issame(u, v)) continue;

            // 辺 (u, v) を追加するとき
            uf.merge(u, v);
            ++num;

            // メディアンに到達
            if (num == (N + 1) / 2) {
                res = w;
                break;
            }
        }
        cout << res << endl;
    }
}
