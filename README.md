# 概要

本リポジトリは、大槻兼資著・秋葉拓哉監修『問題解決力を鍛える！アルゴリズムとデータ構造』の[著者公開リポジトリ](https://github.com/drken1215/book_algorithm_solution)に対応する、**非公式のPython版**です。

元リポジトリと同じ場所・番号からコードを探せるよう、次の構成にしています。

- [本書で掲載しているソースコード](codes/README.md)（`codes/` 以下）
- [各章の章末問題への略解：Pythonコードへの案内](solutions/README.md)（`solutions/chap01.md`〜`chap18.md`）
- [正誤表への案内](errata.md)

| 元リポジトリ | Python版 |
| --- | --- |
| `codes/chapXX/code_X_Y.cpp` | `codes/chapXX/code_X_Y.py` |
| `solutions/chapXX.md` | 同じパス。元の問題番号順にPythonコードと著者の解説へリンク |
| `errata.md` | 同じパス。著者の正誤表とPython版の補足へリンク |
| `LICENSE` | 元ファイルをそのまま収録 |

本文67ファイルと章末解答のC++コードブロック44個、計111件をPythonに移植しています。章末の実行用コードは `solutions/chapXX/block_YY.py` にあり、問題番号から章別Markdownを通して辿れます。`docs/` と `tests/` はPython版の補足資料・検証用です。

元のC++コードと章別解答は [references/](references/) に、元リポジトリの構造・ファイル名・文字コードを保って収録しています。

```text
codes/                         Pythonの本文コード
solutions/                     Pythonの章末コードと問題別の案内
references/
  codes/chapXX/code_X_Y.cpp     著者の本文コード（原本）
  solutions/chapXX.md           著者の章別解答（原本）
docs/                          Python版の補足資料
tests/                         Python版の検証コード・入力データ
```

`references/` は取得元コミットのコード関連部分を収録したものです。元リポジトリには `docs/`・`tests/` はありません。README・LICENSE・正誤表・画像はここには重複して置いていません。

[書籍情報（講談社）](https://www.kspub.co.jp/book/detail/5128442.html)

# 使用言語と動作環境

Python標準ライブラリだけで実行できます。Python 3.10以降で利用できる構文・APIを用い、CPython 3.15.2で検証しています。他のバージョンでの実行検証はしていません。

リポジトリのルートから、たとえば次のように実行します。

```sh
python3 codes/chap05/code_5_1.py <<'INPUT'
4
10 30 40 20
INPUT
```

出力は `30` です。元が完成プログラムの89件は直接実行でき、関数例・コード片など22件は関数／クラスとして利用できます。[詳しい実行・検証方法](docs/usage.md)を参照してください。

# 注意事項・補足

移植元はコミット [`bf4af1b13b6fb1f58b8a921ab319096422f064d6`](https://github.com/drken1215/book_algorithm_solution/tree/bf4af1b13b6fb1f58b8a921ab319096422f064d6) です。著者・出版社による公式Python版ではありません。

Pythonコードは各ファイルで独立しています。実装やコメントにはPython向けの調整があり、元のC++と行単位では一致しません。再帰の深さや実行時間などの制約は[原文との差分・補完・既知の制約](docs/deviations.md)にまとめています。

- [全111件の対応表・計算量](docs/catalog.md)
- [ソースコードの章別対応と学習上の補足](docs/book_map.md)
- [翻訳方針と調査出典](docs/translation_policy.md)
- [検証方法と結果](docs/verification.md)

`references/solutions/` には、コードを含む著者公開リポジトリの章別Markdownをそのまま収録しています。図版・書影は原文のリンクから参照でき、元の `fig/` の画像ファイルは収録していません。

# License

元リポジトリのコードはCC0です。[LICENSE](LICENSE)は原本をそのまま保持しています。このリポジトリの翻訳コード・検証コード・独自ドキュメントもCC0で提供します。リンク先の書籍・解説文・図版の利用条件を変更するものではありません。
