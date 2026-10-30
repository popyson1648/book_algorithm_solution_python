#include <iostream>
#include <vector>
using namespace std;

// fibo(N) の答えをメモ化する配列
vector<long long> memo;

long long func(int N) {
    // ベースケース
    if (N == 0) return 0;
    else if (N == 1) return 0;
    else if (N == 2) return 1;

    // メモをチェック (すでに計算済みならば答えをリターンする)
    if (memo[N] != -1) return memo[N];

    // 答えをメモ化しながら，再帰呼び出し
    return memo[N] = func(N - 1) + func(N - 2) + func(N - 3);
}

int main() {
    int N;
    cin >> N;

    // メモ化用配列を -1 で初期化する
    memo.assign(N + 1, -1);

    // fibo(N) をよびだす
    cout << func(N) << endl;
}
