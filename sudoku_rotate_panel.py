import random

def lambda_handler(event, context):
    
    # 問題盤面（及び答え）の記載
    panel_1 = ['891265473','726394851','345817926','538746219','162589734','479123685','254638197','687951342','913472568']
    panel_2 = ['812753649','943682175','675491283','154237896','369845721','287169534','521974368','438526917','796318452']

    # 盤面の計算
    panel_str = ''.join(panel_1)
    panel_ans_str = rotate_panel(panel_str)
    
    # 計算結果の表示
    panel_ans = []
    for i in range(0,81,9):
        panel_ans.append(panel_ans_str[i:i+9])
    return panel_ans

# パネルの数値入れ替え
def rotate_panel(panel):
    panel_ans = ''

    value_list = ['1','2','3','4','5','6','7','8','9']
    shuffle_value_list = random.sample(value_list,len(value_list))

    for i in range(81):
        for j in range(len(value_list)):
            if panel[i] == value_list[j]:
                panel_ans += shuffle_value_list[j]
                break

    return panel_ans