# Python版の実行・検証方法

[概要](../README.md) · [本文コード](../codes/README.md) · [章末問題](../solutions/README.md)

## 実行する

Python標準ライブラリだけで実行できます。検証環境はCPython 3.15.2です。翻訳コードはPython 3.10以降で利用できる構文・APIに限定していますが、それ以外のバージョンでの実行検証はしていません。

リポジトリのルートで実行する例です。

```sh
python3 codes/chap05/code_5_1.py <<'INPUT'
4
10 30 40 20
INPUT
```

出力は `30` です。入力のないデモは、たとえば次のように実行します。

```sh
python3 codes/chap10/code_10_5.py
```

出力は順に `7`, `5`, `11` です。

関数例や、ソートのように元から標準出力のない例は、関数を読み込んで結果を観察できます。

```python
from codes.chap12.code_12_2 import merge_sort

values = [5, 1, 4, 1]
merge_sort(values, 0, len(values))
print(values)  # [1, 1, 4, 5]
```

各 `.py` は独立しています。学習時にファイルを1本コピーして使えるように、原文で重複していたデータ構造の実装も各ファイルに残しています。モジュールをimportしても標準入力を読みません。

章末の `solutions/chap05/block_04.py` の `04` は**その章のC++コードブロックの掲載順**です。問題番号はファイル先頭と索引に明記しています。同じ問題の改善前後や遷移の断片を区別するための名前です。

## 検証する

全検証には、PythonとC++17対応の `clang++` または `g++` が必要です。追加のPythonパッケージやネットワーク接続は不要です。

```sh
python3 -B tests/run_checks.py
```

最新の検証記録も更新する場合は次を実行します。

```sh
python3 -B tests/run_checks.py --report docs/verification.json
```

Pythonのアルゴリズム検証だけを行う場合：

```sh
python3 -B -m unittest discover -s tests -p 'test_algorithms.py' -v
```

C++比較用の原文は `tests/reference/` に収録しています。EUC-JPのファイルはUTF-8へ変換し、原文の文字コードとSHA-256を記録しています。コンパイルの一時ファイルはOSの一時領域に作り、終了時に削除します。

## 利用上の前提

再帰を学ぶ例では再帰を保持しています。深い木・長い配列などではPythonの再帰上限に達します。また、指数時間・三次元DPなど、比較や理解のために意図的に遅い実装も含みます。すべての競技プログラミング問題の最大制約での通過や、実行時間・メモリ制限への適合を保証するものではありません。各例の計算量と入力前提は索引と[制約一覧](deviations.md)を参照してください。
