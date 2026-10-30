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

// 辺を表す構造体
using pint = pair<int, int>;  // 両端点
using Edge = pair<long long, pint>;  // (重み, 両端点)

int main() {
    // 入力
    int N, M;
    cin >> N >> M;
    vector<Edge> edges(M);
    for (int i = 0; i < M; ++i) {
        int u, v, w;
        cin >> u >> v >> w;
        --u, --v;
        edges[i] = Edge(w, pint(u, v));
    }

    // 各辺を重みの小さい順にソート
    sort(edges.begin(), edges.end());

    // id 番目の辺を削除した場合の最小全域木を求める関数
    // id == -1 のときは、通常の最小全域木を求める
    // res は、最小全域木をなす辺番号が格納される
    auto calc = [&](vector<int> &res, int id = -1) -> long long {
        long long cost = 0;
        res.clear();

        // Kruskal 法
        UnionFind uf(N);
        for (int i = 0; i < edges.size(); ++i) {
            if (i == id) continue;
            int u = edges[i].second.first, v = edges[i].second.second;
            if (uf.issame(u, v)) continue;
            res.push_back(i);
            cost += edges[i].first;
            uf.merge(u, v);
        }

        // N-1 本に満たない場合は連結でない
        if (res.size() < N - 1) return (1LL<<60);
        return cost;
    };
    
    // もとのグラフの最小全域木を求める
    vector<int> mst;
    long long base = calc(mst);

    // 最小全域木 mst に含まれる各辺 e を 1 本ずつ除去して調べる
    vector<int> dammy;
    long long num = 0, res = 0;
    for (auto id : mst) {
        if (calc(dammy, id) > base) {
            ++num;
            res += edges[id].first;
        }
    }
    cout << num << " " << res << endl;
}
