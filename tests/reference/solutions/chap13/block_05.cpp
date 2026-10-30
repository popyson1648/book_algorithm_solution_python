#include <iostream>
#include <vector>
#include <queue>
#include <string>
using namespace std;

// 上下左右への動きを表すベクトル
const vector<int> dx = {1, 0, -1, 0};
const vector<int> dy = {0, 1, 0, -1};

int main() {
    // 入力
    int H, W;  // 縦の長さ, 横の長さ
    cin >> H >> W;
    vector<string> field(H);
    for (int i = 0; i < H; ++i) cin >> field[i];

    // スタートとゴールのマスを割り出す
    int sx = -1, sy = -1, gx = -1, gy = -1;
    for (int i = 0; i < H; ++i) {
        for (int j = 0; j < W; ++j) {
            if (field[i][j] == 'S') sx = i, sy = j;
            if (field[i][j] == 'G') gx = i, gy = j;
        }
    }

    // 各頂点は pair<int,int> 型で表すことにする
    using Node = pair<int,int>;
    queue<Node> que;  // キュー 

    // 初期条件
    // dist[i][j] はマス (i, j) への最短路長を表す
    que.push({sx, sy});
    vector<vector<int>> dist(H, vector<int>(W, -1));
    dist[sx][sy] = 0;

    // BFS 開始
    while (!que.empty()) {
        auto [x, y] = que.front();
        que.pop();

        // 隣接頂点を順にみていく
        for (int dir = 0; dir < 4; ++dir) {
            int nx = x + dx[dir];
            int ny = y + dy[dir];

            // 盤面外はスキップ
            if (nx < 0 || nx >= H || ny < 0 || ny >= W) continue;

            // 壁には入れない
            if (field[nx][ny] == '#') continue;

            // 探索済みでなければ新たにキューに追加
            if (dist[nx][ny] == -1) {
                dist[nx][ny] = dist[x][y] + 1;
                que.push(Node(nx, ny));
            }
        }
    }

    // 最短路長
    cout << dist[gx][gy] << endl;
}
