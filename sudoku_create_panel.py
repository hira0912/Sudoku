import random
from collections import deque

def lambda_handler(event, context):
    # 計算及び結果の表示
    panel_ans = create_panel()
    return panel_ans

# パネルの生成
def create_panel():
    panel = ''

    # 最初の1行分(0-8)を生成
    possibility = ['1','2','3','4','5','6','7','8','9']
    panel += ''.join(random.sample(possibility,9))
    # 残りはxで埋めておく
    panel += 'x'*72 

    # 残りの行をdfsにて生成
    ret,panel_ans_str,cnt = dfs(panel,10,0)

    # 計算結果の表示
    panel_ans = []
    for i in range(0,81,9):
        panel_ans.append(panel_ans_str[i:i+9])
    return panel_ans,cnt

# 計算ルーチン
def dfs(panel,position,cnt):
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
    possibility_ready = calc_possibility(panel,position)
    possibility = deque(random.sample(possibility_ready,len(possibility_ready))) # possibility = [1,2,3,4,5,6,7,8,9]
    
    while len(possibility)>0 :
        # 答え導出完了による早期終了条件
        if ret:
            return ret,panel_ans,cnt
        # セルに一つ埋めて渡す
        # 計算カウント数に1を足す
        cnt += 1
        panel_mod = setval(panel,position,possibility.popleft())
        ret,panel_ans,cnt = dfs(panel_mod,next_position(panel_mod,position),cnt)
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