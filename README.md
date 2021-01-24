# python_pachinko_simulation
パチンコシミュレーションコードをPythonで初心者が作ってみた

ファイルが2つある理由は、一般的な確変機とST機の双方のバージョンをシミュレーションしてみたかった為です。
グローバル変数ばかり使っている件については、ごめんなさい、許して

単純にパチンコをシミュレーションするプログラムを作ってみて、期待値収支がどのくらいになるのかを作り、
例えば1000円当たりの回転数によって7日間の収支がどの程度変化するのかを、あくまで”シミュレーション上”で理解できます。

基本的なアルゴリズムは出来てある為、台の入力データ（下記参照部分）のみを変更すれば、それっぽい収支結果が算出されます。
あくまでシミュレーション（しかも微妙なアルゴリズムで、ラウンド別の確変等の細かい調整や厳正な抽選ではなく、それっぽい抽選アルゴリズム）なので
本気にしないでください。

###########【台入力データ】#######################
#大当たり確率
atariKakuritsu: int = 
#ST中大当たり確率
STatariKakuritsu: int = 
#ST突入率
STtotsunyuritsu: int = 
#ST回数
STkaisu: int = 
#時短回数
jitanKaisu: int = 
#総回転数
kaitensuuSum: int = 
#1000円辺りの回転率
senenKaitensuu: int = 
#大当たり一回辺りの出玉数
ikaiOatariDedama: int = 
#日数分のシミュレーション
simulationDay: int = 
###########################################
