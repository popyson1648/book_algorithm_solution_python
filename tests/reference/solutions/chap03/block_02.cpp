#include <iostream>
#include <vector>
using namespace std;
const int INF = 20000000;   // 十分大きな値に

int main() {
    // 入力を受け取る
    int N;
    cin >> N;
    vector<int> a(N);
    for (int i = 0; i < N; ++i) cin >> a[i];

    // 線形探索
    int worst_value = INF;
    int second_value = INF;
    for (int i = 0; i < N; ++i) {
        if (a[i] < worst_value) {
            second_value = worst_value;
            worst_value = a[i];
        }
        else if (a[i] < second_value) second_value = a[i];
    }

    // 結果出力
    cout << second_value << endl;
}
