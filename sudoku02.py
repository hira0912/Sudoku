def lambda_handler(event, context):
    
    # 問題盤面（及び答え）の設定
    panel_question = ['x91x65x7x','xx6xx48x1','xx5817x26','xxxxxxxxx','162x89xx4','4xx1xx68x','25xxx819x','6xxx513x2','xxx472xxx']
    panel_question_ans = ['891265473','726394851','345817926','538746219','162589734','479123685','254638197','687951342','913472568']
    panel_difficult = ['8xxxxxxxx','xx36xxxxx','x7xx9x2xx','x5xxx7xxx','xxxx457xx','xxx1xxx3x','xx1xxxx68','xx85xxx1x','x9xxxx4xx']
    panel_diffucult_ans = ['812753649','943682175','675491283','154237896','369845721','287169534','521974368','438526917','796318452']

    
    # 盤面の計算
    panel_str = ''.join(panel_question)
    ret,panel_ans_str = calc_panel(panel_str,0)
    
    # 計算結果の表示
    panel_ans = []
    for i in range(0,81,9):
        panel_ans.append(panel_ans_str[i:i+9])
    return panel_ans

# 計算ルーチン
def calc_panel(panel,position):
    # セルが最終セルの場合
    if(position>80):
        return check_panel(panel),panel

    # 変数の定義
    ret = False
    panel_ans = []

    # セルが空欄の場合
    if(panel[position]=='x'):
        possibility = calc_possibility(panel,position) # possibility = [1,2,3,4,5,6,7,8,9]
        
        while len(possibility)>0 :
            # 答え導出完了の為の終了条件
            if ret:
                return ret,panel_ans
            # セルに一つ埋めて渡す
            panel_mod = setval(panel,position,possibility.pop(0))
            ret,panel_ans = calc_panel(panel_mod,position+1)
        return ret,panel_ans

    # セルが既に埋まっている場合は下のセルに継ぐ
    else:
        ret,panel_ans = calc_panel(panel,position+1)
        return ret,panel_ans

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

# パネル全体のチェック
def check_panel(panel):
    # 各行の調査    
    for row in range(0,81,9):
        ans = []
        for col in range(9):
            ans.append(panel[row+col])
        if not check_ans(ans):
            return False
    
    # 各列の調査
    for col in range(9):
        ans = []
        for row in range(0,81,9):
            ans.append(panel[row+col])
        if not check_ans(ans):
            return False
    
    # 各ブロックの調査
    for block in range(9):
        row = block // 3
        col = block % 3
        ans = []
        for pos in range(9):
            x = pos // 3
            y = pos % 3
            ans.append(panel[(3*row + x)*9+(3*col + y)])
        if not check_ans(ans):
            return False
    return True
    
# 特定9文字配列の確認
def check_ans(ans):
    checker = '123456789'
    ans.sort()
    ans_join = ''.join(ans)
    if(ans_join != checker):
        return False
    return True