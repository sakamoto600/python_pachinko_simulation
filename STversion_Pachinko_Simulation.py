import random

###########【台入力データ】#######################
# 大当たり確率
atariKakuritsu: int = 320
# ST中大当たり確率
STatariKakuritsu: int = 100
# ST突入率
STtotsunyuritsu: int = 33
# ST回数
STkaisu: int = 160
#時短回数
jitanKaisu: int = 160
# 総回転数
kaitensuuSum: int = 3000
# 1000円辺りの回転率
senenKaitensuu: int = 12
#大当たり一回辺りの出玉数
ikaiOatariDedama: int = 1500
#日数分のシミュレーション
simulationDay: int = 7
###########################################

########データ収集##########
# ハマり回数
hamariKaisu: int = 0
# 最大ハマり回数
saidaiHamari: int = 0
# 確変中連チャン回数
renchanKaisu: int = 0
# 最大連チャン回数
saidaiRenchanKaisu: int = 0
# 確変突入率回数
kakuhenTotsunyuKaisu: int = 0
# 確変突入出来なかった回数
kakuhenNGKaisu: int = 0
# 初当たり確率
hatsuatariKakuritsu: int = 0
#外れ回数
hazureKaisu: int = 0
#当たり回数
atariKaisu: int = 0
# 最大当たり回数
saidaiAtariKaisu: int = 0
# 確変回数
kakuhenKaisu: int = 0
# 最大確変回数
saidaiKakuhenKaisu: int = 0
# 総大当たり回数
atariKaisuSum: int = 0
# 総大当たり回数
kakuhenKaisuSum: int = 0
##########################

# 現在のパチンコの状態：0＝通常時、1＝大当たり時かつ確変中
pachinkoStatus = 0

# パチンコシミュレーション1回転分
def pachinko1KaitenSimulation():
    global atariKakurits
    global STatariKakuritsu
    global STkaisu
    global STtotsunyuritsu
    global kaitensuuSum
    global jitanKaisu
    global senenKaitensuu
    global ikaiOatariDedama
    global simulationDay

    global hamariKaisu
    global saidaiHamari
    global renchanKaisu
    global saidaiRenchanKaisu
    global kakuhenTotsunyuKaisu
    global kakuhenNGKaisu
    global hatsuatariKakuritsu
    global hazureKaisu
    global atariKaisu
    global saidaiAtariKaisu
    global kakuhenKaisu
    global saidaiKakuhenKaisu
    global atariKaisuSum
    global kakuhenKaisuSum

    global pachinkoStatus

    ##ユーザーの方が入力した数字をrandomで乱数を引き出すコード
    #通常時+時短時の当たり乱数
    atariKakuritsuUser = random.randint(1, atariKakuritsu)
    hamariKaisu += 1

    #ST中の当たり乱数
    STTotsunyuritsuUser = random.randint(1, 100)
    STatariKakuritsuUser = random.randint(1, STatariKakuritsu)

    ##通常時パターン
    if pachinkoStatus == 0:
        ##通常時から大当たり処理
        if atariKakuritsuUser == 1:
            atariKaisu += 1
            print("★★★★★大当たり★★★★★")
            print(hamariKaisu, "回転目で", atariKaisu, "回目の大当たり！")
            hamariKaisu = 0

            ##ST突入判定
            if STTotsunyuritsuUser <= STtotsunyuritsu:
                kakuhenTotsunyuKaisu += 1
                pachinkoStatus = 2
                print(kakuhenTotsunyuKaisu, "回目、ST突入！")

            ##ST突入せず時短へ
            else:
                kakuhenNGKaisu += 1
                print(kakuhenNGKaisu, "回目、ST突入ならず、時短へ")
                pachinkoStatus = 1
        # 通常時から外れ処理
        else:
            hazureKaisu += 1
            #最大ハマり数
            if (hamariKaisu > saidaiHamari):
                saidaiHamari = hamariKaisu


    ##時短中処理
    elif pachinkoStatus == 1:
            #時短中大当たり&ST突入
            if atariKakuritsuUser == 1 & STTotsunyuritsuUser <= STtotsunyuritsu:
                atariKaisu += 1
                print("★★★時短中大当たり★★★")
                print(hamariKaisu, "回転目で", atariKaisu, "回目の大当たり！")
                pachinkoStatus = 2
                kakuhenTotsunyuKaisu += 1
                print(kakuhenTotsunyuKaisu, "回目、ST突入!")
                hamariKaisu = 0

            #時短中大当たり&ST突入せず
            elif atariKakuritsuUser == 1 & STTotsunyuritsuUser > STtotsunyuritsu:
                atariKaisu += 1
                kakuhenNGKaisu += 1
                print("★★★時短中大当たり★★★")
                print(hamariKaisu, "回転目で", atariKaisu, "回目の大当たり！")
                print(kakuhenNGKaisu, "回目、ST突入ならず、時短へ")
                print("===================")
                hamariKaisu = 0

            #時短終了
            elif hamariKaisu == jitanKaisu:
                print("時短終了、通常時へ転落")
                print("===================")
                pachinkoStatus = 0


    ##ST中パターン
    elif pachinkoStatus == 2:

            #ST中大当たり
            if STatariKakuritsuUser == 1:
                kakuhenKaisu += 1
                renchanKaisu += 1
                print((renchanKaisu + 1), "連チャン！(ST中)")
                hamariKaisu = 0

            #ST中駆け抜け
            elif STkaisu == hamariKaisu:
                print("残念！通常モードへ転落！")
                print("===================")
                if renchanKaisu > saidaiRenchanKaisu:
                    renchanKaisu += 1
                    saidaiRenchanKaisu = renchanKaisu
                renchanKaisu = 0
                pachinkoStatus = 0

# 日数シミュレーション
saidaiKachigaku: int = 0
saidaiMakegaku: int = 0
goukeiShushi: int = 0
heikinShushi: int = 0
ichinichiShushi: int = 0
daily_count: int = 0
max_saidaihamari: int = 0

#日数分の収支データ(出玉計測 / 日 + 最大データ算出 + その日の当たり・確変回数のリセット)
def pachinkoDailySimulation():
    global atariKakurits
    global STatariKakuritsu
    global STkaisu
    global STtotsunyuritsu
    global kaitensuuSum
    global jitanKaisu
    global senenKaitensuu
    global ikaiOatariDedama
    global simulationDay

    global hamariKaisu
    global saidaiHamari
    global renchanKaisu
    global saidaiRenchanKaisu
    global kakuhenTotsunyuKaisu
    global kakuhenNGKaisu
    global hatsuatariKakuritsu
    global hazureKaisu
    global atariKaisu
    global saidaiAtariKaisu
    global kakuhenKaisu
    global saidaiKakuhenKaisu
    global atariKaisuSum
    global kakuhenKaisuSum
    global pachinkoStatus

    ##日数シミュレーションのグローバル変数宣言
    global saidaiKachigaku
    global saidaiMakegaku
    global saidaiHamari
    global max_saidaihamari
    global goukeiShushi
    global heikinShushi
    global ichinichiShushi

    #【決めた回転数分回す】入っているデータ：大当たり回数(確変突入 / 非突入含む)・確変回数
    for _ in range(1, kaitensuuSum):
            pachinko1KaitenSimulation()

    ##出玉計測
    hazureDedama = ((250 / senenKaitensuu) * hazureKaisu)
    atariDedama = ((atariKaisu + kakuhenKaisu) * ikaiOatariDedama)
    ichinichiDedamaSum = (atariDedama) - (hazureDedama)

    ##出玉分を4円に換算
    ichinichiShushi = (ichinichiDedamaSum * 4)

    ##合計収支に加算
    goukeiShushi += ichinichiShushi

    ##一日における最大勝ち額・最大負け額の算出
    if ichinichiShushi > 0 and saidaiKachigaku < ichinichiShushi:
        saidaiKachigaku = ichinichiShushi
    elif ichinichiShushi < 0 and saidaiMakegaku > ichinichiShushi:
        saidaiMakegaku = ichinichiShushi

    ##一日における各種(総大当たり回数・総確変回数・ 最大大当たり回数・ 最大確変数・最大ハマり数）
    #総大当たり回数
    atariKaisuSum += atariKaisu

    #総確変回数
    kakuhenKaisuSum += kakuhenKaisu

    #最大大当たり回数
    if atariKaisu > saidaiAtariKaisu:
        saidaiAtariKaisu = atariKaisu

    #最大確変回数
    if kakuhenKaisu > saidaiKakuhenKaisu:
        saidaiKakuhenKaisu = kakuhenKaisu

    #最大ハマり回数の集計
    if saidaiHamari > max_saidaihamari:
        max_saidaihamari = saidaiHamari

# パチンコシミュレーター処理回数
for _ in range(1, (simulationDay + 1)):
    pachinkoDailySimulation()
    daily_count += 1
    print("")
    print("======【", daily_count, "日の結果です 】======")
    print(daily_count, "日目の収支結果は", int(ichinichiShushi), "円")
    print(daily_count, "日目の大当たり回数：　", atariKaisu, "回")
    print(daily_count, "日目の総ST回数：　", kakuhenKaisu, "回")
    print(daily_count, "日目の最大ハマり回数：　", saidaiHamari, "回")
    print("==============================")
    print("")
    ##出玉リセット(ハマり回数・確変突入回数・確変突入しなかった回数・初当たり回数・外れ回数・当たり回数・確変回数)
    hamariKaisu = 0
    kakuhenTotsunyuKaisu = 0
    kakuhenNGKaisu = 0
    hatsuatariKakuritsu = 0
    hazureKaisu = 0
    atariKaisu = 0
    kakuhenKaisu = 0
    saidaiHamari = 0

#= == == データ収集結果出力 == == = //
print("")
print("")
print("====今回のシミュレーション結果です====")

#= == =日数シミュレーションの結果表示 == == =
# 何日シミュレーションしたのか
print(simulationDay, "日分のシミュレーションをしました")
# 総回転数
print("総回転数：　", int(kaitensuuSum * simulationDay), "回転")
# 総収支金額
print(simulationDay, "日分の総収支金額：　", int(goukeiShushi), "円")
# 平均収支
print(simulationDay, "日における1日辺りの平均収支額：　", int(goukeiShushi / simulationDay), "円")
# 最大勝ち額
print(simulationDay, "日の中での最大勝ち額：　", int(saidaiKachigaku), "円")
# 最大負け額
print(simulationDay, "日の中での最大負け額：　", int(saidaiMakegaku), "円")
# 総大当たり回数
print(simulationDay, "日の中での総大当たり回数：　", atariKaisuSum, "回")
# 総確変回数
print(simulationDay, "日の中での総ST回数：　", kakuhenKaisuSum, "回")
# 最大大当たり回数
print(simulationDay, "日の中での最大大当たり回数：　", saidaiAtariKaisu, "回")
# 最大確変回数
print(simulationDay, "日の中での一日の最大ST回数：　", saidaiKakuhenKaisu, "回")
# 最大連チャン回数
print(simulationDay, "日の中での一回での最大ST連チャン回数：　", saidaiRenchanKaisu, "回")
# 最大ハマり回数
print(simulationDay, "日の中での最大ハマり回数：　", max_saidaihamari, "回")