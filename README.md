# 様々なディレクトリ構造でのimportとfromの挙動解説
---

ここではpythonのimport文とfrom文の挙動を解説する．しかしmoduleの入れ子構造の場合は解説しない．なんでって、めんどくさくなったから。気になったら自分で試して。 
必要であれば[main.py](/directory_A/main.py)も適宜参照せよ．

### ディレクトリ構造
<pre>
.
├── directory_A
│   ├── directory_C
│   │   ├── module_C
│   │   │   ├── __init__.py
│   │   │   └── core.py
│   │   └── util_c.py
│   ├── main.py
│   ├── module_A
│   │   ├── __init__.py
│   │   └── core.py
│   ├── test.ipynb
│   └── util_a.py
└── directory_B
    ├── module_B
    │   ├── __init__.py
    │   └── core.py
    └── util_b.py
</pre>
##### 意味のない解説
topdirectory内にdirectoryAとdirectoryBが入っており、directoryA内にはdirectoryCが含まれる．また各directoryには1つのmoduleと1つのutil.pyが備わっているとする．これを元にしてこれらのmoduleとfileのimportとfromの挙動を確認していく．実際にimportとfromで行き詰まった状況では手元のdirectory構造と同じ部分のみを切り出して確認するば良い．


### 本題
結論から述べる．
ただし，以下では実行しているpython fileのあるdirectoryをcurrent directoryと呼ぶ．例えそのfile内で他fileをimportしようともcurrent directoryは変化しない．このcurrent directoryは`sys`ライブラリの`sys.path`で確認できる．

- moduleの場合
  - import文では，current directory内moduleのみimport可能．
  - from文は存在しない．fromはfile内のobjectを直接importする際に使用するため，module単体に対しては存在しない．
    - (moduleに対しても行うことは出来るが，fileの場合と挙動は同じである)
- fileの場合
  - import文では，current directory内のfileと，その子directoryのみimport可能．
  - from文もimportと同じ挙動を取り，current directory内のfileと，その子directoryのみfrom import可能．

なぜこのような挙動になるのかというと，基本的にpythonはcurrent directoryのみを探索するようになっているからである．また，pythonではいわゆる"親"へのアクセスを禁止する習慣，仕様，思想がある．これは混乱を避けるためであり，directory含めpython内のobjectにも共通する．しかし実際には`sys.path`のdirectoryを順番に探索しているだけであるため，`sys.path`に任意のpathを追加すると任意のdirectoryがimport可能となる．（しかしなぜmoduleのimportは子directoryの探索を行わないのかと言うと，moduleは多くの場合で入れ子にするからである．これによりmoduleではtoplevelのmoduleを介して全てのmoduleにアクセスすることが望まれるため，それらを禁止している）

### main.pyの実行出力
```
$ python main.py
-----------以下utilファイルa,b,cとモジュールa,b,cのimportを試みる．-----------
called Util A!
util_Bのインポート時のエラー: No module named 'directory_B'
called Util C!
called Module A!
module_Bのインポート時のエラー: No module named 'module_B'
module_Cのインポート時のエラー: No module named 'module_C'
--------以下utilファイルa,b,cとモジュールa,b,cのfrom importを試みる．---------
called Util A!
util_B内の関数をfromにより直接インポートする時のエラー: attempted relative import with no known parent package
called Util C!
called Module A!
module_B内のファイルの関数をfromにより直接インポートする時のエラー: attempted relative import with no known parent package
called Module C!
```








