# 第6章 二分探索法

境界の不変条件と単調性を追う。二分探索そのものと、bisectを使う応用を区別する。

[全体の使い方](../../README.md) · [差分と制約](../../docs/deviations.md)

| ファイル | 対応・目的 | 利用方法 | 計算量 |
| --- | --- | --- | --- |
| [code_6_1.py](code_6_1.py) | 6.1：配列の二分探索 | 直接実行可：`binary_search` | 時間 O(log N)、追加領域 O(1) |
| [code_6_2.py](code_6_2.py) | 6.3–6.4：単調な判定条件に対する二分探索 | 関数／クラス例：`binary_search` | 判定 O(T) のとき時間 O(T log(R-L))、追加領域 O(1) |
| [code_6_3.py](code_6_3.py) | 6.5：年齢当てゲーム | 直接実行可 | 質問回数 O(log(R-L))、領域 O(1) |
| [code_6_4.py](code_6_4.py) | 6.6：lower_boundの活用：ペア和 | 直接実行可：`minimum_pair_sum` | 時間 O(N log N)、領域 O(N) |
| [code_6_5.py](code_6_5.py) | 6.7：射撃王：最適化を判定問題へ | 直接実行可：`shooting_king` | 時間 O(N log N log M)、領域 O(N) |

各ファイルの先頭に固定コミットの原文リンクを掲載。入出力のある例は原文の形式に従い、具体的な比較入力は [tests/cases.json](../../tests/cases.json) でファイルに対応するキーから参照できる。
