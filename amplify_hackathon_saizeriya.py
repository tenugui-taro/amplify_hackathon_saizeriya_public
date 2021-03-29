from amplify import gen_symbols, BinaryPoly, Solver, decode_solution
from amplify.client import FixstarsClient

# 2021/03/19 時点のサイゼリヤグランドメニュー
GRAND_MENU = [
    {"price":  350, "calorie":  161, "name": "ガーデンサラダ"},
    {"price":  500, "calorie":  243, "name": "ガーデンサラダ（Lサイズ）"},
    {"price":  350, "calorie":  188, "name": "チキンのシーザーサラダ"},
    {"price":  500, "calorie":  281, "name": "チキンのシーザーサラダ（Lサイズ）"},
    {"price":  350, "calorie":  126, "name": "小エビのサラダ"},
    {"price":  500, "calorie":  189, "name": "小エビのシーザーサラダ（Lサイズ）"},
    {"price":  300, "calorie":  223, "name": "リグーリア風ミネストローネ"},
    {"price":  300, "calorie":  294, "name": "田舎風やわらかキャベツのスープ"},
    {"price":  250, "calorie":  206, "name": "冷たいアスパラガスのスープ"},
    {"price":  150, "calorie":  146, "name": "コーンクリームスープ"},
    {"price":  150, "calorie":  189, "name": "ミニフィセル"},
    {"price":  200, "calorie":  245, "name": "ガーリックトースト"},
    {"price":  150, "calorie":  214, "name": "プチフォッカ"},
    {"price":  100, "calorie":  107, "name": "セットプチフォッカ"},
    {"price":  200, "calorie":  246, "name": "シナモンプチフォッカ"},
    {"price":  200, "calorie":   92, "name": "爽やかにんじんサラダ"},
    {"price":  300, "calorie":  195, "name": "フレッシュチーズとトマトのサラダ"},
    {"price":  600, "calorie":  390, "name": "フレッシュチーズとトマトのサラダ（Wサイズ）"},
    {"price":  400, "calorie":   55, "name": "プロシュート（パルマ産熟成生ハム）"},
    {"price":  800, "calorie":  110, "name": "プロシュート（パルマ産熟成生ハム）（Wサイズ）"},
    {"price":  300, "calorie":   95, "name": "熟成ミラノサラミ"},
    {"price":  600, "calorie":  190, "name": "熟成ミラノサラミ（Wサイズ）"},
    {"price":  350, "calorie":  188, "name": "イタリア風もつ煮込み"},
    {"price":  300, "calorie":  140, "name": "アスパラガスの温サラダ"},
    {"price":  200, "calorie":  214, "name": "柔らか青豆の温サラダ"},
    {"price":  200, "calorie":  142, "name": "ほうれん草のソテー"},
    {"price":  400, "calorie":  170, "name": "ムール貝のガーリック焼き"},
    {"price":  300, "calorie":  215, "name": "ポップコーンシュリンプ"},
    {"price":  250, "calorie":  376, "name": "カリッとポテト"},
    {"price":  400, "calorie":  420, "name": "チョリソー（辛味ソーセージ）"},
    {"price":  400, "calorie":  224, "name": "アロスティチーニ（ラムの串焼き、2本）"},
    {"price":  800, "calorie":  448, "name": "アロスティチーニ（ラムの串焼き、2本）（Wサイズ）"},
    {"price":  400, "calorie":  248, "name": "エスカルゴのオーブン焼き"},
    {"price":  300, "calorie":  369, "name": "辛味チキン"},
    {"price":  600, "calorie":  397, "name": "骨付きももの辛味チキン"},
    {"price":  400, "calorie":  461, "name": "アンチョビのフリコ"},
    {"price":  300, "calorie":  419, "name": "フリウリ風フリコ"},
    {"price":  400, "calorie":  530, "name": "エビクリームグラタン"},
    {"price":  400, "calorie":  529, "name": "ほうれん草のグラタン"},
    {"price":  400, "calorie":  759, "name": "ソーセージピザ"},
    {"price":  500, "calorie":  859, "name": "ソーセージピザ（Wチーズ）"},
    {"price":  400, "calorie":  557, "name": "マルゲリータピザ"},
    {"price":  500, "calorie":  657, "name": "マルゲリータピザ（Wチーズ）"},
    {"price":  500, "calorie":  566, "name": "バッファローモッツァレラのピザ"},
    {"price":  600, "calorie":  666, "name": "バッファローモッツァレラのピザ（Wチーズ）"},
    {"price":  400, "calorie":  635, "name": "パンチェッタのピザ"},
    {"price":  500, "calorie":  735, "name": "パンチェッタのピザ（Wチーズ）"},
    {"price":  400, "calorie":  539, "name": "野菜ときのこのピザ"},
    {"price":  500, "calorie":  639, "name": "野菜ときのこのピザ（Wチーズ）"},
    {"price":  400, "calorie":  669, "name": "たっぷりコーンのピザ"},
    {"price":  500, "calorie":  769, "name": "たっぷりコーンのピザ（Wチーズ）"},
    {"price":  400, "calorie":  568, "name": "アンチョビとルーコラのピザ"},
    {"price":  500, "calorie":  668, "name": "アンチョビとルーコラのピザ（Wチーズ）"},
    {"price":  400, "calorie":  551, "name": "タラコソースシシリー風"},
    {"price":  600, "calorie":  827, "name": "タラコソースシシリー風（大盛）"},
    {"price":  400, "calorie":  716, "name": "パルマ風スパゲッティ（トマト味）"},
    {"price":  600, "calorie": 1074, "name": "パルマ風スパゲッティ（トマト味）（大盛）"},
    {"price":  400, "calorie":  579, "name": "ミートソースボロニア風"},
    {"price":  600, "calorie":  869, "name": "ミートソースボロニア風（大盛）"},
    {"price":  450, "calorie":  662, "name": "半熟卵のミートソースボロニア風"},
    {"price":  300, "calorie":  535, "name": "ペペロンチーノ"},
    {"price":  450, "calorie":  803, "name": "ペペロンチーノ（大盛）"},
    {"price":  350, "calorie":  618, "name": "半熟卵のペペロンチーノ"},
    {"price":  500, "calorie":  883, "name": "半熟卵のペペロンチーノ（大盛）"},
    {"price":  300, "calorie":  534, "name": "アーリオ・オーリオ"},
    {"price":  450, "calorie":  801, "name": "アーリオ・オーリオ（大盛）"},
    {"price":  600, "calorie":  602, "name": "ラムのラグーススパゲッティ"},
    {"price":  800, "calorie":  803, "name": "ラムのラグーススパゲッティ（大盛）"},
    {"price":  500, "calorie":  714, "name": "ペストジェノベーゼ"},
    {"price":  700, "calorie": 1000, "name": "ペストジェノベーゼ（大盛）"},
    {"price":  500, "calorie":  668, "name": "エビとブロッコリーのオーロラソース"},
    {"price":  700, "calorie":  935, "name": "エビとブロッコリーのオーロラソース（大盛）"},
    {"price":  500, "calorie":  614, "name": "イカの墨入りスパゲッティ"},
    {"price":  700, "calorie":  860, "name": "イカの墨入りスパゲッティ（大盛）"},
    {"price":  500, "calorie":  731, "name": "カルボナーラ"},
    {"price":  700, "calorie": 1023, "name": "カルボナーラ（大盛）"},
    {"price":  400, "calorie":  629, "name": "アラビアータ"},
    {"price":  600, "calorie":  944, "name": "アラビアータ（大盛）"},
    {"price":  300, "calorie":  521, "name": "ミラノ風ドリア"},
    {"price":  400, "calorie":  628, "name": "セットプチフォッカ付きミラノ風ドリア"},
    {"price":  400, "calorie":  722, "name": "チーズたっぷりミラノ風ドリア"},
    {"price":  350, "calorie":  604, "name": "半熟卵のミラノ風ドリア"},
    {"price":  400, "calorie":  530, "name": "エビクリームグラタン"},
    {"price":  400, "calorie":  529, "name": "ほうれん草のグラタン"},
    {"price":  550, "calorie":  712, "name": "チョリソーとハンバーグの盛合せ"},
    {"price":  400, "calorie":  594, "name": "ハンバーグステーキ"},
    {"price":  500, "calorie":  666, "name": "ディアボラ風ハンバーグ"},
    {"price":  500, "calorie":  641, "name": "デミグラスソースのハンバーグ"},
    {"price":  500, "calorie":  705, "name": "イタリアンハンバーグ"},
    {"price":  100, "calorie":   78, "name": "ペコリーノ・ロマーノ"},
    {"price":   50, "calorie":   83, "name": "トッピング半熟卵"},
    {"price":  150, "calorie":  303, "name": "ライス"},
    {"price":  200, "calorie":  454, "name": "ラージライス"},
    {"price":  100, "calorie":  151, "name": "スモールライス"},
    {"price":  500, "calorie":  726, "name": "若鳥のディアボラ風"},
    {"price":  500, "calorie":  770, "name": "柔らかチキンのチーズ焼き"},
    {"price":  900, "calorie":  337, "name": "ラムのランプステーキ"},
    {"price": 1000, "calorie":  640, "name": "リブステーキ"},
    {"price":  100, "calorie":   72, "name": "野菜ペースト"},
    {"price":  300, "calorie":  229, "name": "ティラミス クラシコ"},
    {"price":  500, "calorie":  445, "name": "プリンとティラミス クラシコの盛合せ"},
    {"price":  400, "calorie":  284, "name": "とろけるティラミス＆コーヒーゼリー"},
    {"price":  400, "calorie":  186, "name": "カシスとブルーベリーのパンナコッタ"},
    {"price":  200, "calorie":  114, "name": "カプチーノ（アイスケーキ）"},
    {"price":  350, "calorie":  182, "name": "イタリアンジェラートのせコーヒーゼリー"},
    {"price":  250, "calorie":  121, "name": "イタリアンジェラート"},
    {"price":  200, "calorie":  127, "name": "すっきりレモンのシャーベット"},
    {"price":  250, "calorie":  216, "name": "イタリアンプリン"},
    {"price":  300, "calorie":  166, "name": "チョコレートケーキ"},
    {"price":  350, "calorie":  164, "name": "トリフアイスクリーム"},
    {"price":  100, "calorie":   40, "name": "フルーツソース（カシス＆ブルーベリー）"},
]

# 料理の名前リスト
GRAND_MENU_NAMES = []

# 料理の価格リスト
GRAND_MENU_PRICES = []

# 料理のカロリーリスト
GRAND_MENU_CALORIES = []

# 料理数
GRAND_MENU_NUM = len(GRAND_MENU)

# それぞれのリストに値を格納
for i in range(GRAND_MENU_NUM):
    GRAND_MENU_NAMES.append(GRAND_MENU[i]["name"])
    GRAND_MENU_PRICES.append(GRAND_MENU[i]["price"])
    GRAND_MENU_CALORIES.append(GRAND_MENU[i]["calorie"])

# 料理の数だけバイナリ変数を生成
q = gen_symbols(BinaryPoly, GRAND_MENU_NUM)

# 目指す合計金額
TOTAL_AMOUNT = 1000

# 目的関数の構築
f = BinaryPoly()

for i in range(GRAND_MENU_NUM):
    f += GRAND_MENU_PRICES[i] * q[i]

f = (TOTAL_AMOUNT - f) ** 2

# クライアントの設定
client = FixstarsClient()
client.parameters.timeout = 1000   # タイムアウト1秒
# client.token = "xxxxxxxxxxxxxxxxxxxxxxxxxx" # アカウントトークンに置換
client.parameters.outputs.duplicate = False  # 同じエネルギー値の解を列挙しない

solver = Solver(client)
result = solver.solve(f)

# 解が得られなかった場合、len(result) == 0
if len(result) == 0:
    raise RuntimeError("No solution was found")

energy = result[0].energy
values = result[0].values

solution = decode_solution(q, values)

# 注文する料理リスト
ORDER_GRAND_MENUS = []

# 注文する料理の価格合計
SUM_ORDER_GRAND_MENU_PRICES = 0

# 注文する料理のカロリー合計
SUM_ORDER_GRAND_MENU_CALORIES = 0

for i in range(len(solution)):
    if solution[i] == 1:
        ORDER_GRAND_MENUS.append(GRAND_MENU[i])
        SUM_ORDER_GRAND_MENU_PRICES += GRAND_MENU[i]["price"]
        SUM_ORDER_GRAND_MENU_CALORIES += GRAND_MENU[i]["calorie"]

print("\n----------------------------------------")
for i in range(len(ORDER_GRAND_MENUS)):
    print(("\\" + str(ORDER_GRAND_MENUS[i]["price"])).rjust(5) + str(
        ORDER_GRAND_MENUS[i]["calorie"]).rjust(5) + "kcal  " + str(ORDER_GRAND_MENUS[i]["name"]))

print("\n " + str(len(ORDER_GRAND_MENUS)) + "品でお会計は" +
      "計" + str(SUM_ORDER_GRAND_MENU_PRICES) + "円です。")
print(" 総カロリーは" + str(SUM_ORDER_GRAND_MENU_CALORIES) + "kcalです。")
print("----------------------------------------\n")
