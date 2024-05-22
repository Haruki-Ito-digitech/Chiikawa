"""素数を判定しよう"""
#import
import math
import sys
args = sys.argv

#引数を変数に代入
num = int(args[1])

#素数判定処理
def Prime_judge(num):
    #2~numまで計算を繰り返す
    judge = "Prime"
    for i in range(2, num):
        #割り切れたら素数ではない
        if num % int(i) == 0:
            judge = "not"
            #素数ではないと分かった時点で処理終了
            break
    """
        else:
        #割り切れなければ素数の可能性あり
            judge = "Prime"
    """
    return judge

#メイン関数
def main():
    #1000未満かどうか判定
    if 1000 <= num:
        judge = "1000以上は判定できません"
    else:
        #素数判定
        judge = Prime_judge(num)
    
    print(judge, end="")

if __name__ == '__main__':
    main()
