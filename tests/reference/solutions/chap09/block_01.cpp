#include <iostream>
#include <stack>
#include <string>
using namespace std;

// 逆ポーランド記法で記述された値を計算する
double calc(const string &exp) {
    stack<double> st;
    for (auto c: exp) {
        if (c >= '0' && c <= '9') {
            // '7' のような文字リテラルを 7 のような数値に変換
            double add = c - '0';
            st.push(add);
        } else {
            // 演算子の場合は演算を実施する
            double a = st.top();
            st.pop();
            double b = st.top();
            st.pop();

            // 演算の実施結果をスタックに積む
            if (c == '+') st.push(b + a);
            else if (c == '-') st.push(b - a);
            else if (c == '*') st.push(b * a);
            else st.push(b / a);
        }
    }
    return st.top();
}

int main() {
    string exp = "34+12-*";
    cout << calc(exp) << endl;
}
