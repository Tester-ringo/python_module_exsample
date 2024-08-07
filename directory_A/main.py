"""
MAIN.py

各状況においてのimportとfromの挙動を試みる．
"""


print("{:-^60s}".format(
    "以下utilファイルa,b,cとモジュールa,b,cのimportを試みる．"
))


try: # util_a.pyを呼び出すプログラム．同じディレクトリであるため実行可能．
     # いわゆる通常のimport
    import util_a
    util_a.hello_util_a()
except Exception as e:
    print(f"util_Aのインポート時のエラー: {e}")


try: # util_b.pyを呼び出すプログラム．親ディレクトリを介してimportするため実行不可．
     # 一見directory_Bの前に`..`などを含むと良さそうだが，
     # import文に相対パスを含むことはシンタックスエラーである．
    import directory_B as util_b
    util_b.hello_util_b()
except Exception as e:
    print(f"util_Bのインポート時のエラー: {e}")


try: # util_c.pyを呼び出すプログラム．
     # 関数ファイルをまとめる目的により子ディレクトリであれど実行可能．(わかんないけど多分．
    import directory_C.util_c as util_c
    util_c.hello_util_c()
except Exception as e:
    print(f"util_Cのインポート時のエラー: {e}")


try: # module_Aを呼び出すプログラム．同じディレクトリであるため実行可能．
    import module_A
    module_A.hello_module_a()
except Exception as e:
    print(f"module_Aのインポート時のエラー: {e}")


try: # module_Aを呼び出すプログラム．親ディレクトリを介してimportするため実行不可．
    import module_B
    module_B.hello_module_b()
except Exception as e:
    print(f"module_Bのインポート時のエラー: {e}")


try: # module_Aを呼び出すプログラム．同じディレクトリ内のフォルダにあるが，実行不可．
     # moduleではないフォルダを仲介するため．← この理由についてはあまり理解していない
    import module_C
    module_C.hello_module_c()
except Exception as e:
    print(f"module_Cのインポート時のエラー: {e}")


print("{:-^60s}".format(
    "以下utilファイルa,b,cとモジュールa,b,cのfrom importを試みる．"
))



try: # util_a.pyを呼び出すプログラム．同じディレクトリであるため実行可能．
     # いわゆる通常のimport
    from util_a import hello_util_a
    hello_util_a()
except Exception as e:
    print(f"util_A内の関数をfromにより直接インポートする時のエラー: {e}")


try: # util_b.pyを呼び出すプログラム．親ディレクトリを介してimportするため実行不可．
     # 一見directory_Bの前に`..`などを含むと良さそうだが，
     # import文に相対パスを含むことはシンタックスエラーである．
    from ..directory_B.util_b import hello_util_b
    hello_util_b()
except Exception as e:
    print(f"util_B内の関数をfromにより直接インポートする時のエラー: {e}")


try: # util_c.pyを呼び出すプログラム．
     # 関数ファイルをまとめる目的により子ディレクトリであれど実行可能．(わかんないけど多分．
    from directory_C.util_c import hello_util_c
    hello_util_c()
except Exception as e:
    print(f"util_C内の関数をfromにより直接インポートする時のエラー: {e}")


try: # module_Aのcoreファイルからhello_a関数を直接呼び出すプログラム．
     # 子ディレクトリは問題なくインポート可能．
    from module_A.core import hello_module_a
    hello_module_a()
except Exception as e:
    print(f"module_A内のファイルの関数をfromにより直接インポートする時のエラー: {e}")


try: # module_Bのcoreファイルからhello_b関数を直接呼び出すプログラム．
     # Aと同様実行可能．
    from ..directory_B.module_B.core import hello_module_b
    hello_module_b()
except Exception as e:
    print(f"module_B内のファイルの関数をfromにより直接インポートする時のエラー: {e}")


try: # module_Cのcoreファイルからhello_c関数を直接呼び出すプログラム．
     # sys.pathに含まれない親ディレクトリを参照することは仕様で禁止されている．
     # よって実行不可．
    from directory_C.module_C.core import hello_module_c
    hello_module_c()
except Exception as e:
    print(f"module_C内のファイルの関数をfromにより直接インポートする時のエラー: {e}")

