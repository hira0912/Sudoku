from collections import deque

def lambda_handler(event, context):
    
    # 問題盤面（及び答え）の記載
    panel_question1 = ['x91x65x7x','xx6xx48x1','xx5817x26','xxxxxxxxx','162x89xx4','4xx1xx68x','25xxx819x','6xxx513x2','xxx472xxx'] # 空きセル43個
    panel_question1_ans = ['891265473','726394851','345817926','538746219','162589734','479123685','254638197','687951342','913472568']
    panel_question2 = ['8xxxxxxxx','xx36xxxxx','x7xx9x2xx','x5xxx7xxx','xxxx457xx','xxx1xxx3x','xx1xxxx68','xx85xxx1x','x9xxxx4xx'] # 空きセル60個
    panel_question2_ans = ['812753649','943682175','675491283','154237896','369845721','287169534','521974368','438526917','796318452']

    
    # 盤面の計算
    panel_str = ''.join(panel_question2)
    ret,panel_ans_str,cnt = calc_panel(panel_str,0,0)
    
    # 計算結果の表示
    panel_ans = []
    for i in range(0,81,9):
        panel_ans.append(panel_ans_str[i:i+9])
    return panel_ans,cnt,panel_str.count('x')

# 計算ルーチン
def calc_panel(panel,position,cnt):
    # セルが最終セルの場合
    if(position>80):
        return True,panel,cnt
        
    # パネル整理
    org_ret,panel,cnt = organize_panel(panel,cnt)
    # パネル整理の結果エラーが見付かった場合
    if not org_ret:
        return False,[],cnt

    # 変数の定義
    ret = False
    panel_ans = []

    # セルが空欄の場合
    if(panel[position]=='x'):
        possibility = deque(calc_possibility(panel,position)) # possibility = [1,2,3,4,5,6,7,8,9]
        
        while len(possibility)>0 :
            # 答え導出完了による早期終了条件
            if ret:
                return ret,panel_ans,cnt
            # セルに一つ埋めて渡す
            # 計算カウント数に1を足す
            cnt += 1
            panel_mod = setval(panel,position,possibility.popleft())
            ret,panel_ans,cnt = calc_panel(panel_mod,next_position(panel_mod,position),cnt)
        return ret,panel_ans,cnt

    # セルが既に埋まっている場合は下のセルに継ぐ
    else:
        ret,panel_ans,cnt = calc_panel(panel,next_position(panel,position),cnt)
        return ret,panel_ans,cnt

# 盤面整理
def organize_panel(panel,cnt):
    flag = True
    org_ret = True
    
    while flag:
        # 内部変数の初期化
        flag = False
        possibility = []

        # 空きセルはpossibilityを計算（埋まっているセルはFalseとする)
        for position in range(len(panel)):
            if panel[position]!='x':
                possibility.append(False)
            else:
                tmp_possibility = calc_possibility(panel,position)
                if(len(tmp_possibility)==0):
                    org_ret = False
                    break
                if(len(tmp_possibility)==1):
                    panel = setval(panel,position,tmp_possibility[0])
                    cnt += 1
                    flag = True
                    break
                possibility.append(tmp_possibility)
    return org_ret,panel,cnt
    
# 次のパネル
def next_position(panel,position):
    for i in range(position+1,81):
        if panel[i]=='x':
            return i
    return 81

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