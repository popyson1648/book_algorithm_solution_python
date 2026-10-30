#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <stack>
using namespace std;

bool check(const string &S) {
    stack<int> st; // 左括弧の index を格納するスタック
    vector<pair<int,int> > ps; // 対応を表すペア

    // ループを回す
    for (int i = 0; i < (int)S.size(); ++i) {
        if (S[i] == '(') st.push(i);
        else {
            if (st.empty()) {
                cout << "error" << endl;
                return false;
            }
            int t = st.top();
            st.pop();
            ps.push_back({t, i});
        }
    }

    // スタックが空でなかったら左括弧が過剰
    if (!st.empty()) {
        cout << "too many (" << endl;
        return false;
    }

    // 整合を出力
    sort(ps.begin(), ps.end());
    for (int i = 0; i < (int)ps.size(); ++i) {
        if (i) cout << ", ";
        cout << "(" << ps[i].first << ", " << ps[i].second << ")";
    }
    cout << endl;
    return true;
}

int main() {
    check("((()())())"); // (0, 9) (1, 6), (2, 3), (4, 5), (7, 8)
    check("())"); // error
    check("(()"); // too many (
}
