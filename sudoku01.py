def lambda_handler(event, context):
    
    # 盤面の設定
    panel_first = ['x91x65x7x','xx6xx48x1','xx5817x26','xxxxxxxxx','162x89xx4','4xx1xx68x','25xxx819x','6xxx513x2','xxx472xxx']
    panel_last = ['891265473','726394851','345817926','538746219','162589734','479123685','254638197','687951342','913472568']
    
    # 盤面の計算
    panel_ans = panel_calc(panel_first,0)
    return panel_ans

# 計算ルーチン
def panel_calc(panel,position):
    if(setcheck(panel,position)):
        possibility = setpossibility(panel,position) #[1,2,3,4,5,6,7,8,9]
        while len(possibility)>0 :
            panel_mod = setval(panel,position,possibility.pop(0))
            if(position==80):
                if(check_panel(panel_mod)):
                    return panel_mod
                    
                

# 対象の枠が埋まっているかどうかの判定
def setcheck(panel,position):
    if(panel[position//9][position%9]!='x'):
        return False
    else:
        return True
        
# 配置可能性の計算
def setpossibility(panel,position):
    possibility = [1,2,3,4,5,6,7,8,9]
    return possibility

# パネルに数値追加
def setval(panel,position,value):
    panel[position//9][position%9] = value
    return panel

# パネル全体のチェック
def check_panel(panel):
    # 各行の調査    
    for i in range(9):
        ans = []
        for j in range(9):
            ans.append(panel[i][j])
        if(check_ans(ans)==False):
            return False
    
    # 各列の調査
    for j in range(9):
        ans = []
        for i in range(9):
            ans.append(panel[i][j])
        if(check_ans(ans)==False):
            return False
    
    # 各ブロックの調査
    for k in range(9):
        row = k // 3
        col = k % 3
        ans = []
        for l in range(9):
            x = l // 3
            y = l % 3
            ans.append(panel[3*row + x][3*col + y])
        if(check_ans(ans)==False):
            return False
    
# 特定9文字配列の確認
def check_ans(ans):
    checker = '123456789'
    ans.sort()
    ans_join = ''.join(ans)
    if(ans_join != checker):
        return False
    return True