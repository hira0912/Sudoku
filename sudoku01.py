def lambda_handler(event, context):
    
    # 盤面の設定
    panel_first = ['x91x65x7x','xx6xx48x1','xx5817x26','xxxxxxxxx','162x89xx4','4xx1xx68x','25xxx819x','6xxx513x2','xxx472xxx']
    panel_difficult = ['8xxxxxxxx','xx36xxxxx','x7xx9x2xx','x5xxx7xxx','xxxx457xx','xxx1xxx3x','xx1xxxx68','xx85xxx1x','x9xxxx4xx']
    #panel_last = ['891265473','726394851','345817926','538746219','162589734','479123685','254638197','687951342','913472568']
    
    # 盤面の計算
    panel_str = ''.join(panel_first)
    panel_ans_str = calc_panel(panel_str)
    
    # 計算結果の表示
    panel_ans = []
    for i in range(0,81,9):
        panel_ans.append(panel_ans_str[i:i+9])
    return panel_ans

# 計算ルーチン
## 各セルの配置可能性を算出し、配置可能性から確定した場合はパネルに格納する
## 配置可能性からこれ以上進展がしない段階になったらパネルを確定させる
def calc_panel(panel):
    flag = True
    
    while flag:
        # 内部変数の初期化
        flag = False
        possibility = []
        
        # 空きセルはpossibilityを計算（埋まっているセルはFalseとする)
        for position in range(len(panel)):
            if panel[position]!='x':
                possibility.append(False)
            else:
                possibility.append(calc_possibility(panel,position))
                if(len(possibility[position])==1):
                    panel = setval(panel,position,possibility[position][0])
                    flag = True

    return panel
        
# セル単位の配置可能性の計算
def calc_possibility(panel,position):
    possibility = ['1','2','3','4','5','6','7','8','9']
    col = position%9
    row = position//9
    
    #同じ行のチェック
    for i in range(row*9,(row+1)*9):
        if i!=position and panel[i]!='x':
            if panel[i] in possibility:
                possibility.remove(panel[i])

    #同じ列のチェック
    for i in range(col,col+9*9,9):
        if i!=position and panel[i]!='x':
            if panel[i] in possibility:
                possibility.remove(panel[i])
    
    #同じブロックのチェック
    block_row = row // 3
    block_col = col // 3
    block_start = (block_row * 3 * 9) + (block_col * 3)

    for i in range(block_start, block_start + 21, 9):
        for j in range(i, i + 3):
            if 0 <= j < len(panel) and j != position and panel[j] != 'x':
                if panel[j] in possibility:
                    possibility.remove(panel[j])

    return possibility

# パネルに数値追加
def setval(panel,position,value):
    panel = panel[:position] + value + panel[position+1:]
    return panel