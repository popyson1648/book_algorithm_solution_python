#include <iostream>
#include <vector>
using namespace std;

template<class T> inline bool chmin(T& a, T b) {
    if (a > b) {
        a = b;
        return 1;
    }
    return 0;
}

// 無限大を表す値
const long long INF = 1LL<<60;

int main() {
    // 入力
    int N;
    cin >> N;
    vector<long long> a(N);
    for (int i = 0; i < N; ++i) cin >> a[i];

    // 累積和をとる
    vector<long long> S(N+1, 0);
    for (int i = 0; i < N; ++i) S[i+1] = S[i] + a[i];

    // DP
    vector<vector<long long>> dp(N+1, vector<long long>(N+1, INF));

    // 初期条件
    for (int i = 0; i < N; ++i) dp[i][i+1] = 0;

    // 更新
    for (int bet = 2; bet <= N; ++bet) {
        for (int i = 0; i + bet <= N; ++i) {
            int j = i + bet;

            // dp[i][j] を更新する
            for (int k = i+1; k < j; ++k) {
                chmin(dp[i][j], dp[i][k] + dp[k][j] + S[j]-S[i]);
            }
        }
    }

    cout << dp[0][N] << endl;
}
