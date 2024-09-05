def lambda_handler(event, context):
    
    # 問題盤面（及び答え）の記載
    panel_question1 = ['x91x65x7x','xx6xx48x1','xx5817x26','xxxxxxxxx','162x89xx4','4xx1xx68x','25xxx819x','6xxx513x2','xxx472xxx'] # 空きセル43個
    panel_question1_ans = ['891265473','726394851','345817926','538746219','162589734','479123685','254638197','687951342','913472568']
    panel_question2 = ['8xxxxxxxx','xx36xxxxx','x7xx9x2xx','x5xxx7xxx','xxxx457xx','xxx1xxx3x','xx1xxxx68','xx85xxx1x','x9xxxx4xx'] # 空きセル60個
    panel_question2_ans = ['812753649','943682175','675491283','154237896','369845721','287169534','521974368','438526917','796318452']

    # 盤面の計算
    panel_str = ''.join(panel_question1)
    ret,panel_ans_str,cnt = calc_panel(panel_str,0,0)
    
    # 計算結果の表示
    panel_ans = []
    for i in range(0,81,9):
        panel_ans.append(panel_ans_str[i:i+9])
    return panel_ans,cnt

# 計算ルーチン
def calc_panel(panel,position,cnt):
    # セルが最終セルの場合
    if(position>80):
        return check_panel(panel),panel,cnt

    # 変数の定義
    ret = False
    panel_ans = []

    # セルが空欄の場合
    if(panel[position]=='x'):
        possibility = ['1','2','3','4','5','6','7','8','9']
        
        while len(possibility)>0 :
            # 答え導出完了による早期終了条件
            if ret:
                return ret,panel_ans,cnt
            # セルに一つ埋めて渡す
            # 計算カウント数に1を足す
            cnt += 1
            panel_mod = setval(panel,position,possibility.pop(0))
            ret,panel_ans,cnt = calc_panel(panel_mod,position+1,cnt)
        return ret,panel_ans,cnt

    # セルが既に埋まっている場合は下のセルに継ぐ
    else:
        ret,panel_ans,cnt = calc_panel(panel,position+1,cnt)
        return ret,panel_ans,cnt

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