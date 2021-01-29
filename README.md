## プログラム説明
パチンコシミュレーションプログラムをPythonで作ってみた

ファイルが2つある理由は、一般的な確変機とST機の双方のバージョンをシミュレーションしてみたかった為です。
グローバル変数ばかり使っている件については、ごめんなさい、許して

単純にパチンコをシミュレーションするプログラムを作ってみて、期待値収支がどのくらいになるのかを作り、
例えば1000円当たりの回転数によって7日間の収支がどの程度変化するのかを、あくまで”シミュレーション上”で理解できます。

## コード説明
中身としては2つの機能(関数)があり、
1.抽選一回転分(pachinko1kaitenSimulation)
2.回転数分抽選(pachinkoDailySimulation)
となり、それら2つを掛け合わせてシミュレーションしております。

基本的なアルゴリズムは出来てある為、台の入力データ（下記参照部分）のみを変更すれば、それっぽい収支結果が算出されます。
あくまでシミュレーション（しかも微妙なアルゴリズムで、ラウンド別の確変等の細かい調整や厳正な抽選ではなく、それっぽい抽選アルゴリズム）なので
本気にしないでください。

## 台入力データ
 - 大当たり確率(確率の分母を入力)
 - atariKakuritsu: int = 
 - ST中大当たり確率(確率の分母を入力)
 - STatariKakuritsu: int = 
 - ST突入率(％を入力 etc: 80)
 - STtotsunyuritsu: int = 
 - ST回数(STの最大回数を入力)
 - STkaisu: int = 
 - 時短回数(時短の最大回数を入力)
 - jitanKaisu: int = 
 - 総回転数(一日に回す回数を入力 ※これはST中の回数や時短回数も含まれます、おおよそ一日打っても2000～3000回転な気がします)
 - kaitensuuSum: int = 
 - 1000円辺りの回転率(これはその名の通り、釘調整が甘い台や辛い台をシミュレーション出来ます。これによって期待値収支も大きく変わりますｗ)
 - senenKaitensuu: int = 
 - 大当たり一回辺りの出玉数(ST中も含めた大当たりを出した時の出玉数を入力)
 - ikaiOatariDedama: int = 
 - 日数分のシミュレーション(シミュレーションする日数を入力します。これは総回転数と掛け合わせ、期待値収支に影響を及ぼします)
 - simulationDay: int = 
