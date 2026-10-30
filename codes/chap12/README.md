# 第12章 ソート

5種類のソートをそれぞれ実装する。選択の疑似コードはmedian of mediansとして具体化する。

[全体の使い方](../../README.md) · [差分と制約](../../docs/deviations.md)

| ファイル | 対応・目的 | 利用方法 | 計算量 |
| --- | --- | --- | --- |
| [code_12_1.py](code_12_1.py) | 12.3：挿入ソート | 直接実行可：`insertion_sort` | 最悪時間 O(N²)、追加領域 O(1) |
| [code_12_2.py](code_12_2.py) | 12.4：マージソート | 直接実行可：`merge_sort` | 時間 O(N log N)、追加領域 O(N) |
| [code_12_3.py](code_12_3.py) | 12.5：クイックソート | 直接実行可：`quick_sort` | 平均時間 O(N log N)、最悪時間 O(N²)、最悪再帰領域 O(N) |
| [code_12_4.py](code_12_4.py) | 12.6：ヒープソート | 直接実行可：`heapify`, `heap_sort` | 時間 O(N log N)、再帰領域 O(log N) |
| [code_12_5.py](code_12_5.py) | 12.8：バケットソート（累積度数） | 直接実行可：`bucket_sort` | 時間・追加領域 O(N+MAX) |

各ファイルの先頭に固定コミットの原文リンクを掲載。入出力のある例は原文の形式に従い、具体的な比較入力は [tests/cases.json](../../tests/cases.json) でファイルに対応するキーから参照できる。
