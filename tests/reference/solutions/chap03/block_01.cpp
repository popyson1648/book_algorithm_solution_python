#include <iostream>
#include <vector>
using namespace std;

int main() {
    // 入力を受け取る
    int N, v;
    cin >> N >> v;
    vector<int> a(N);
    for (int i = 0; i < N; ++i) cin >> a[i];

    // 線形探索
    int counter = 0;
    for (int i = 0; i < N; ++i) {
        if (a[i] == v) {
            ++counter;  // カウントを増やす
        }
    }

    // 結果出力
    cout << counter << endl;
}
