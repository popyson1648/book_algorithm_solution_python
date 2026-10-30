# 第6章 二分探索法

境界の不変条件と単調性を追う。二分探索そのものと、bisectを使う応用を区別する。

[問題番号から探す](../chap06.md) · [全体の使い方](../../README.md) · [差分と制約](../../docs/deviations.md)

| ファイル | 対応・目的 | 利用方法 | 計算量 |
| --- | --- | --- | --- |
| [block_01.py](block_01.py) | 章末問題6.1・コード片：lower_boundの添字 | 関数／クラス例：`rank_in_sorted` | 時間 O(log N)、領域 O(1) |
| [block_02.py](block_02.py) | 章末問題6.1：ソートと二分探索による順位 | 直接実行可：`coordinate_ranks` | 時間 O(N log N)、領域 O(N) |
| [block_03.py](block_03.py) | 章末問題6.4：Aggressive cows：最小間隔の最大化 | 直接実行可：`maximum_spacing` | 時間 O(N log N+N log(A+1))、領域 O(N) |

番号は問題番号ではなくコードブロック順。同じ問題の説明用断片や改善前後の実装も個別に収録している。

各ファイルの先頭に固定コミットの原文リンクを掲載。入出力のある例は原文の形式に従い、具体的な比較入力は [tests/cases.json](../../tests/cases.json) でファイルに対応するキーから参照できる。
