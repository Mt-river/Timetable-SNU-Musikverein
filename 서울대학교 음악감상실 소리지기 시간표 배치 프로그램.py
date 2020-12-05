import cvxpy as cp
import pandas as pd
import copy

def df_maker(col_num, ind_num, fill):
    col = []
    ind = []
    con = []
    for i in range(0,col_num):
        col.append(fill)
    for i in range(0,ind_num):
        ind.append(fill)
    for i in range(0,ind_num):
        con.append(col)
    return pd.DataFrame(con, columns=col, index=ind)

abc = ['a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k' ,'l' ,'m' ,'n',
       'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']
ABC = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
       'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X' , 'Y' , 'Z']
day = ['m1', 'm2', 'm3', 'm4', 'm5', 't1', 't2', 't3', 't4', 't5',
       'w1', 'w2', 'w3', 'w4', 'w5', 'th1', 'th2', 'th3', 'th4', 'th5',
       'f1', 'f2', 'f3', 'f4', 'f5']

time = []
variable = {}

print('서울대학교 음악감상실 소리지기')
print()
print('이 프로그램은 최대 25명을 한 시간표에 배치하는 프로그램입니다.')
print()
print('각 사람을 알파벳으로 표현하고, 가능한 요일(m, t, w, th, f)과 시간대(1, 2, 3, 4, 5)를 붙여서 값을 입력해주세요.')
print('예시1: 첫 번째 사람(의무타임이면 소문자)을 a라고 하고, 그 사람이 월요일 세 번째 시간과 다섯 번째 시간이 가능하다면 am1, am3를 한 번씩 입력하면 됩니다.')
print('예시2: 두 번째 사람(의무타임 대상자가 아니면 대문자)을 B라고 하고, 그 사람이 목요일 첫 번째 시간과 금요일 두 번째 시간이 가능하다면 Bth1, Bf2를 한 번씩 입력하면 됩니다.')
print()
print("=="*20)

while True:
    a = input('각 사람마다 선호하지 않는 타임 순으로 입력하세요(더 이상 입력하지 않으려면 Y를 입력): ') # 의사결정변수 입력
    if a == 'Y' or a == 'y':
        break
    else:
        time.append(a)

for i in time:
    if i[0] == 'a' and i[-2:] == 'm1':
        am1 = cp.Variable(boolean=True) # 입력 받은 값을 의사결정변수로 변환(binary) 
        variable['am1'] = am1
    
    if i[0] == 'a' and i[-2:] == 'm2':
        am2 = cp.Variable(boolean=True)
        variable['am2'] = am2

    if i[0] == 'a' and i[-2:] == 'm3':
        am3 = cp.Variable(boolean=True)
        variable['am3'] = am3

    if i[0] == 'a' and i[-2:] == 'm4':
        am4 = cp.Variable(boolean=True)
        variable['am4'] = am4

    if i[0] == 'a' and i[-2:] == 'm5':
        am5 = cp.Variable(boolean=True)
        variable['am5'] = am5

    if i[0] == 'a' and i[-2:] == 't1':
        at1 = cp.Variable(boolean=True)
        variable['at1'] = at1
    
    if i[0] == 'a' and i[-2:] == 't2':
        at2 = cp.Variable(boolean=True)
        variable['at2'] = at2

    if i[0] == 'a' and i[-2:] == 't3':
        at3 = cp.Variable(boolean=True)
        variable['at3'] = at3

    if i[0] == 'a' and i[-2:] == 't4':
        at4 = cp.Variable(boolean=True)
        variable['at4'] = at4

    if i[0] == 'a' and i[-2:] == 't5':
        at5 = cp.Variable(boolean=True)
        variable['at5'] = at5

    if i[0] == 'a' and i[-2:] == 'w1':
        aw1 = cp.Variable(boolean=True)
        variable['at1'] = aw1
    
    if i[0] == 'a' and i[-2:] == 'w2':
        aw2 = cp.Variable(boolean=True)
        variable['aw2'] = aw2

    if i[0] == 'a' and i[-2:] == 'w3':
        aw3 = cp.Variable(boolean=True)
        variable['aw3'] = aw3

    if i[0] == 'a' and i[-2:] == 'w4':
        aw4 = cp.Variable(boolean=True)
        variable['aw4'] = aw4

    if i[0] == 'a' and i[-2:] == 'w5':
        aw5 = cp.Variable(boolean=True)
        variable['aw5'] = aw5

    if i[0] == 'a' and i[-3:] == 'th1':
        ath1 = cp.Variable(boolean=True)
        variable['ath1'] = ath1
    
    if i[0] == 'a' and i[-3:] == 'th2':
        ath2 = cp.Variable(boolean=True)
        variable['ath2'] = ath2

    if i[0] == 'a' and i[-3:] == 'th3':
        ath3 = cp.Variable(boolean=True)
        variable['ath3'] = ath3

    if i[0] == 'a' and i[-3:] == 'th4':
        ath4 = cp.Variable(boolean=True)
        variable['ath4'] = ath4

    if i[0] == 'a' and i[-3:] == 'th5':
        ath5 = cp.Variable(boolean=True)
        variable['ath5'] = ath5

    if i[0] == 'a' and i[-2:] == 'f1':
        af1 = cp.Variable(boolean=True)
        variable['af1'] = af1
    
    if i[0] == 'a' and i[-2:] == 'f2':
        af2 = cp.Variable(boolean=True)
        variable['af2'] = af2

    if i[0] == 'a' and i[-2:] == 'f3':
        af3 = cp.Variable(boolean=True)
        variable['af3'] = af3

    if i[0] == 'a' and i[-2:] == 'f4':
        af4 = cp.Variable(boolean=True)
        variable['af4'] = af4

    if i[0] == 'a' and i[-2:] == 'f5':
        af5 = cp.Variable(boolean=True)
        variable['af5'] = af5

    if i[0] == 'b' and i[-2:] == 'm1':
        bm1 = cp.Variable(boolean=True)
        variable['bm1'] = bm1
    
    if i[0] == 'b' and i[-2:] == 'm2':
        bm2 = cp.Variable(boolean=True)
        variable['bm2'] = bm2

    if i[0] == 'b' and i[-2:] == 'm3':
        bm3 = cp.Variable(boolean=True)
        variable['bm3'] = bm3

    if i[0] == 'b' and i[-2:] == 'm4':
        bm4 = cp.Variable(boolean=True)
        variable['bm4'] = bm4

    if i[0] == 'b' and i[-2:] == 'm5':
        bm5 = cp.Variable(boolean=True)
        variable['bm5'] = bm5

    if i[0] == 'b' and i[-2:] == 't1':
        bt1 = cp.Variable(boolean=True)
        variable['bt1'] = bt1
    
    if i[0] == 'b' and i[-2:] == 't2':
        bt2 = cp.Variable(boolean=True)
        variable['bt2'] = bt2

    if i[0] == 'b' and i[-2:] == 't3':
        bt3 = cp.Variable(boolean=True)
        variable['bt3'] = bt3

    if i[0] == 'b' and i[-2:] == 't4':
        bt4 = cp.Variable(boolean=True)
        variable['bt4'] = bt4

    if i[0] == 'b' and i[-2:] == 't5':
        bt5 = cp.Variable(boolean=True)
        variable['bt5'] = bt5

    if i[0] == 'b' and i[-2:] == 'w1':
        bw1 = cp.Variable(boolean=True)
        variable['bw1'] = bw1
    
    if i[0] == 'b' and i[-2:] == 'w2':
        bw2 = cp.Variable(boolean=True)
        variable['bw2'] = bw2

    if i[0] == 'b' and i[-2:] == 'w3':
        bw3 = cp.Variable(boolean=True)
        variable['bw3'] = bw3

    if i[0] == 'b' and i[-2:] == 'w4':
        bw4 = cp.Variable(boolean=True)
        variable['bw4'] = bw4

    if i[0] == 'b' and i[-2:] == 'w5':
        bw5 = cp.Variable(boolean=True)
        variable['bw5'] = bw5

    if i[0] == 'b' and i[-3:] == 'th1':
        bth1 = cp.Variable(boolean=True)
        variable['bth1'] = bth1
    
    if i[0] == 'b' and i[-3:] == 'th2':
        bth2 = cp.Variable(boolean=True)
        variable['bth2'] = bth2

    if i[0] == 'b' and i[-3:] == 'th3':
        bth3 = cp.Variable(boolean=True)
        variable['bth3'] = bth3

    if i[0] == 'b' and i[-3:] == 'th4':
        bth4 = cp.Variable(boolean=True)
        variable['bth4'] = bth4

    if i[0] == 'b' and i[-3:] == 'th5':
        bth5 = cp.Variable(boolean=True)
        variable['bth5'] = bth5

    if i[0] == 'b' and i[-2:] == 'f1':
        bf1 = cp.Variable(boolean=True)
        variable['bf1'] = bf1
    
    if i[0] == 'b' and i[-2:] == 'f2':
        bf2 = cp.Variable(boolean=True)
        variable['bf2'] = bf2

    if i[0] == 'b' and i[-2:] == 'f3':
        bf3 = cp.Variable(boolean=True)
        variable['bf3'] = bf3

    if i[0] == 'b' and i[-2:] == 'f4':
        bf4 = cp.Variable(boolean=True)
        variable['bf4'] = bf4

    if i[0] == 'b' and i[-2:] == 'f5':
        bf5 = cp.Variable(boolean=True)
        variable['bf5'] = bf5

    if i[0] == 'c' and i[-2:] == 'm1':
        cm1 = cp.Variable(boolean=True)
        variable['cm1'] = cm1
    
    if i[0] == 'c' and i[-2:] == 'm2':
        cm2 = cp.Variable(boolean=True)
        variable['cm2'] = cm2

    if i[0] == 'c' and i[-2:] == 'm3':
        cm3 = cp.Variable(boolean=True)
        variable['cm3'] = cm3

    if i[0] == 'c' and i[-2:] == 'm4':
        cm4 = cp.Variable(boolean=True)
        variable['cm4'] = cm4

    if i[0] == 'c' and i[-2:] == 'm5':
        cm5 = cp.Variable(boolean=True)
        variable['cm5'] = cm5

    if i[0] == 'c' and i[-2:] == 't1':
        ct1 = cp.Variable(boolean=True)
        variable['ct1'] = ct1
    
    if i[0] == 'c' and i[-2:] == 't2':
        ct2 = cp.Variable(boolean=True)
        variable['ct2'] = ct2

    if i[0] == 'c' and i[-2:] == 't3':
        ct3 = cp.Variable(boolean=True)
        variable['ct3'] = ct3

    if i[0] == 'c' and i[-2:] == 't4':
        ct4 = cp.Variable(boolean=True)
        variable['ct4'] = ct4

    if i[0] == 'c' and i[-2:] == 't5':
        ct5 = cp.Variable(boolean=True)
        variable['ct5'] = ct5

    if i[0] == 'c' and i[-2:] == 'w1':
        cw1 = cp.Variable(boolean=True)
        variable['cw1'] = cw1
    
    if i[0] == 'c' and i[-2:] == 'w2':
        cw2 = cp.Variable(boolean=True)
        variable['cw2'] = cw2

    if i[0] == 'c' and i[-2:] == 'w3':
        cw3 = cp.Variable(boolean=True)
        variable['cw3'] = cw3

    if i[0] == 'c' and i[-2:] == 'w4':
        cw4 = cp.Variable(boolean=True)
        variable['cw4'] = cw4

    if i[0] == 'c' and i[-2:] == 'w5':
        cw5 = cp.Variable(boolean=True)
        variable['cw5'] = cw5

    if i[0] == 'c' and i[-3:] == 'th1':
        cth1 = cp.Variable(boolean=True)
        variable['cth1'] = cth1
    
    if i[0] == 'c' and i[-3:] == 'th2':
        cth2 = cp.Variable(boolean=True)
        variable['cth2'] = cth2

    if i[0] == 'c' and i[-3:] == 'th3':
        cth3 = cp.Variable(boolean=True)
        variable['cth3'] = cth3

    if i[0] == 'c' and i[-3:] == 'th4':
        cth4 = cp.Variable(boolean=True)
        variable['cth4'] = cth4

    if i[0] == 'c' and i[-3:] == 'th5':
        cth5 = cp.Variable(boolean=True)
        variable['cth5'] = cth5

    if i[0] == 'c' and i[-2:] == 'f1':
        cf1 = cp.Variable(boolean=True)
        variable['cf1'] = cf1
    
    if i[0] == 'c' and i[-2:] == 'f2':
        cf2 = cp.Variable(boolean=True)
        variable['cf2'] = cf2

    if i[0] == 'c' and i[-2:] == 'f3':
        cf3 = cp.Variable(boolean=True)
        variable['cf3'] = cf3

    if i[0] == 'c' and i[-2:] == 'f4':
        cf4 = cp.Variable(boolean=True)
        variable['cf4'] = cf4

    if i[0] == 'c' and i[-2:] == 'f5':
        cf5 = cp.Variable(boolean=True)
        variable['cf5'] = cf5

    if i[0] == 'd' and i[-2:] == 'm1':
        dm1 = cp.Variable(boolean=True)
        variable['dm1'] = dm1
    
    if i[0] == 'd' and i[-2:] == 'm2':
        dm2 = cp.Variable(boolean=True)
        variable['dm2'] = dm2

    if i[0] == 'd' and i[-2:] == 'm3':
        dm3 = cp.Variable(boolean=True)
        variable['dm3'] = dm3

    if i[0] == 'd' and i[-2:] == 'm4':
        dm4 = cp.Variable(boolean=True)
        variable['dm4'] = dm4

    if i[0] == 'd' and i[-2:] == 'm5':
        dm5 = cp.Variable(boolean=True)
        variable['dm5'] = dm5

    if i[0] == 'd' and i[-2:] == 't1':
        dt1 = cp.Variable(boolean=True)
        variable['dt1'] = dt1
    
    if i[0] == 'd' and i[-2:] == 't2':
        dt2 = cp.Variable(boolean=True)
        variable['dt2'] = dt2

    if i[0] == 'd' and i[-2:] == 't3':
        dt3 = cp.Variable(boolean=True)
        variable['dt3'] = dt3

    if i[0] == 'd' and i[-2:] == 't4':
        dt4 = cp.Variable(boolean=True)
        variable['dt4'] = dt4

    if i[0] == 'd' and i[-2:] == 't5':
        dt5 = cp.Variable(boolean=True)
        variable['dt5'] = dt5

    if i[0] == 'd' and i[-2:] == 'w1':
        dw1 = cp.Variable(boolean=True)
        variable['dw1'] = dw1
    
    if i[0] == 'd' and i[-2:] == 'w2':
        dw2 = cp.Variable(boolean=True)
        variable['dw2'] = dw2

    if i[0] == 'd' and i[-2:] == 'w3':
        dw3 = cp.Variable(boolean=True)
        variable['dw3'] = dw3

    if i[0] == 'd' and i[-2:] == 'w4':
        dw4 = cp.Variable(boolean=True)
        variable['dw4'] = dw4

    if i[0] == 'd' and i[-2:] == 'w5':
        dw5 = cp.Variable(boolean=True)
        variable['dw5'] = dw5

    if i[0] == 'd' and i[-3:] == 'th1':
        dth1 = cp.Variable(boolean=True)
        variable['dth1'] = dth1
    
    if i[0] == 'd' and i[-3:] == 'th2':
        dth2 = cp.Variable(boolean=True)
        variable['dth2'] = dth2

    if i[0] == 'd' and i[-3:] == 'th3':
        dth3 = cp.Variable(boolean=True)
        variable['dth3'] = dth3

    if i[0] == 'd' and i[-3:] == 'th4':
        dth4 = cp.Variable(boolean=True)
        variable['dth4'] = dth4

    if i[0] == 'd' and i[-3:] == 'th5':
        dth5 = cp.Variable(boolean=True)
        variable['dth5'] = dth5

    if i[0] == 'd' and i[-2:] == 'f1':
        df1 = cp.Variable(boolean=True)
        variable['df1'] = df1
    
    if i[0] == 'd' and i[-2:] == 'f2':
        df2 = cp.Variable(boolean=True)
        variable['df2'] = df2

    if i[0] == 'd' and i[-2:] == 'f3':
        df3 = cp.Variable(boolean=True)
        variable['df3'] = df3

    if i[0] == 'd' and i[-2:] == 'f4':
        df4 = cp.Variable(boolean=True)
        variable['df4'] = df4

    if i[0] == 'd' and i[-2:] == 'f5':
        df5 = cp.Variable(boolean=True)
        variable['df5'] = df5

    if i[0] == 'e' and i[-2:] == 'm1':
        em1 = cp.Variable(boolean=True)
        variable['em1'] = em1
    
    if i[0] == 'e' and i[-2:] == 'm2':
        em2 = cp.Variable(boolean=True)
        variable['em2'] = em2

    if i[0] == 'e' and i[-2:] == 'm3':
        em3 = cp.Variable(boolean=True)
        variable['em3'] = em3

    if i[0] == 'e' and i[-2:] == 'm4':
        em4 = cp.Variable(boolean=True)
        variable['em4'] = em4

    if i[0] == 'e' and i[-2:] == 'm5':
        em5 = cp.Variable(boolean=True)
        variable['em5'] = em5

    if i[0] == 'e' and i[-2:] == 't1':
        et1 = cp.Variable(boolean=True)
        variable['et1'] = et1
    
    if i[0] == 'e' and i[-2:] == 't2':
        et2 = cp.Variable(boolean=True)
        variable['et2'] = et2

    if i[0] == 'e' and i[-2:] == 't3':
        et3 = cp.Variable(boolean=True)
        variable['et3'] = et3

    if i[0] == 'e' and i[-2:] == 't4':
        et4 = cp.Variable(boolean=True)
        variable['et4'] = et4

    if i[0] == 'e' and i[-2:] == 't5':
        et5 = cp.Variable(boolean=True)
        variable['et5'] = et5

    if i[0] == 'e' and i[-2:] == 'w1':
        ew1 = cp.Variable(boolean=True)
        variable['dw1'] = dw1
    
    if i[0] == 'e' and i[-2:] == 'w2':
        ew2 = cp.Variable(boolean=True)
        variable['ew2'] = ew2

    if i[0] == 'e' and i[-2:] == 'w3':
        ew3 = cp.Variable(boolean=True)
        variable['ew3'] = ew3

    if i[0] == 'e' and i[-2:] == 'w4':
        ew4 = cp.Variable(boolean=True)
        variable['ew4'] = ew4

    if i[0] == 'e' and i[-2:] == 'w5':
        ew5 = cp.Variable(boolean=True)
        variable['ew5'] = ew5

    if i[0] == 'e' and i[-3:] == 'th1':
        eth1 = cp.Variable(boolean=True)
        variable['eth1'] = eth1
    
    if i[0] == 'e' and i[-3:] == 'th2':
        eth2 = cp.Variable(boolean=True)
        variable['eth2'] = eth2

    if i[0] == 'e' and i[-3:] == 'th3':
        eth3 = cp.Variable(boolean=True)
        variable['eth3'] = eth3

    if i[0] == 'd' and i[-3:] == 'th4':
        dth4 = cp.Variable(boolean=True)
        variable['dth4'] = dth4

    if i[0] == 'e' and i[-3:] == 'th5':
        eth5 = cp.Variable(boolean=True)
        variable['eth5'] = eth5

    if i[0] == 'd' and i[-2:] == 'f1':
        df1 = cp.Variable(boolean=True)
        variable['df1'] = df1
    
    if i[0] == 'e' and i[-2:] == 'f2':
        ef2 = cp.Variable(boolean=True)
        variable['ef2'] = ef2

    if i[0] == 'e' and i[-2:] == 'f3':
        ef3 = cp.Variable(boolean=True)
        variable['ef3'] = ef3

    if i[0] == 'e' and i[-2:] == 'f4':
        ef4 = cp.Variable(boolean=True)
        variable['ef4'] = ef4

    if i[0] == 'e' and i[-2:] == 'f5':
        ef5 = cp.Variable(boolean=True)
        variable['ef5'] = ef5

    if i[0] == 'f' and i[-2:] == 'm1':
        fm1 = cp.Variable(boolean=True)
        variable['fm1'] = fm1
    
    if i[0] == 'f' and i[-2:] == 'm2':
        fm2 = cp.Variable(boolean=True)
        variable['fm2'] = fm2

    if i[0] == 'f' and i[-2:] == 'm3':
        fm3 = cp.Variable(boolean=True)
        variable['fm3'] = fm3

    if i[0] == 'f' and i[-2:] == 'm4':
        fm4 = cp.Variable(boolean=True)
        variable['fm4'] = fm4

    if i[0] == 'f' and i[-2:] == 'm5':
        fm5 = cp.Variable(boolean=True)
        variable['fm5'] = fm5

    if i[0] == 'f' and i[-2:] == 't1':
        ft1 = cp.Variable(boolean=True)
        variable['ft1'] = ft1
    
    if i[0] == 'f' and i[-2:] == 't2':
        ft2 = cp.Variable(boolean=True)
        variable['ft2'] = ft2

    if i[0] == 'f' and i[-2:] == 't3':
        ft3 = cp.Variable(boolean=True)
        variable['ft3'] = ft3

    if i[0] == 'f' and i[-2:] == 't4':
        ft4 = cp.Variable(boolean=True)
        variable['ft4'] = ft4

    if i[0] == 'f' and i[-2:] == 't5':
        ft5 = cp.Variable(boolean=True)
        variable['ft5'] = ft5

    if i[0] == 'f' and i[-2:] == 'w1':
        fw1 = cp.Variable(boolean=True)
        variable['fw1'] = fw1
    
    if i[0] == 'f' and i[-2:] == 'w2':
        fw2 = cp.Variable(boolean=True)
        variable['fw2'] = fw2

    if i[0] == 'f' and i[-2:] == 'w3':
        fw3 = cp.Variable(boolean=True)
        variable['fw3'] = fw3

    if i[0] == 'f' and i[-2:] == 'w4':
        fw4 = cp.Variable(boolean=True)
        variable['fw4'] = fw4

    if i[0] == 'f' and i[-2:] == 'w5':
        fw5 = cp.Variable(boolean=True)
        variable['fw5'] = fw5

    if i[0] == 'f' and i[-3:] == 'th1':
        fth1 = cp.Variable(boolean=True)
        variable['fth1'] = fth1
    
    if i[0] == 'f' and i[-3:] == 'th2':
        fth2 = cp.Variable(boolean=True)
        variable['fth2'] = fth2

    if i[0] == 'f' and i[-3:] == 'th3':
        fth3 = cp.Variable(boolean=True)
        variable['fth3'] = fth3

    if i[0] == 'f' and i[-3:] == 'th4':
        fth4 = cp.Variable(boolean=True)
        variable['fth4'] = fth4

    if i[0] == 'f' and i[-3:] == 'th5':
        fth5 = cp.Variable(boolean=True)
        variable['fth5'] = fth5

    if i[0] == 'f' and i[-2:] == 'f1':
        ff1 = cp.Variable(boolean=True)
        variable['ff1'] = ff1
    
    if i[0] == 'f' and i[-2:] == 'f2':
        ff2 = cp.Variable(boolean=True)
        variable['ff2'] = ff2

    if i[0] == 'f' and i[-2:] == 'f3':
        ff3 = cp.Variable(boolean=True)
        variable['ff3'] = ff3

    if i[0] == 'f' and i[-2:] == 'f4':
        ff4 = cp.Variable(boolean=True)
        variable['ff4'] = ff4

    if i[0] == 'f' and i[-2:] == 'f5':
        ff5 = cp.Variable(boolean=True)
        variable['ff5'] = ff5

    if i[0] == 'g' and i[-2:] == 'm1':
        gm1 = cp.Variable(boolean=True)
        variable['gm1'] = gm1
    
    if i[0] == 'g' and i[-2:] == 'm2':
        gm2 = cp.Variable(boolean=True)
        variable['gm2'] = gm2

    if i[0] == 'g' and i[-2:] == 'm3':
        gm3 = cp.Variable(boolean=True)
        variable['gm3'] = gm3

    if i[0] == 'g' and i[-2:] == 'm4':
        gm4 = cp.Variable(boolean=True)
        variable['gm4'] = gm4

    if i[0] == 'g' and i[-2:] == 'm5':
        gm5 = cp.Variable(boolean=True)
        variable['gm5'] = gm5

    if i[0] == 'g' and i[-2:] == 't1':
        gt1 = cp.Variable(boolean=True)
        variable['gt1'] = gt1
    
    if i[0] == 'g' and i[-2:] == 't2':
        gt2 = cp.Variable(boolean=True)
        variable['gt2'] = gt2

    if i[0] == 'g' and i[-2:] == 't3':
        gt3 = cp.Variable(boolean=True)
        variable['gt3'] = gt3

    if i[0] == 'g' and i[-2:] == 't4':
        gt4 = cp.Variable(boolean=True)
        variable['gt4'] = gt4

    if i[0] == 'g' and i[-2:] == 't5':
        gt5 = cp.Variable(boolean=True)
        variable['gt5'] = gt5

    if i[0] == 'g' and i[-2:] == 'w1':
        gw1 = cp.Variable(boolean=True)
        variable['gw1'] = gw1
    
    if i[0] == 'g' and i[-2:] == 'w2':
        gw2 = cp.Variable(boolean=True)
        variable['gw2'] = gw2

    if i[0] == 'g' and i[-2:] == 'w3':
        gw3 = cp.Variable(boolean=True)
        variable['gw3'] = gw3

    if i[0] == 'g' and i[-2:] == 'w4':
        gw4 = cp.Variable(boolean=True)
        variable['gw4'] = gw4

    if i[0] == 'g' and i[-2:] == 'w5':
        gw5 = cp.Variable(boolean=True)
        variable['gw5'] = gw5

    if i[0] == 'g' and i[-3:] == 'th1':
        gth1 = cp.Variable(boolean=True)
        variable['gth1'] = gth1
    
    if i[0] == 'g' and i[-3:] == 'th2':
        gth2 = cp.Variable(boolean=True)
        variable['gth2'] = gth2

    if i[0] == 'g' and i[-3:] == 'th3':
        gth3 = cp.Variable(boolean=True)
        variable['gth3'] = gth3

    if i[0] == 'g' and i[-3:] == 'th4':
        gth4 = cp.Variable(boolean=True)
        variable['gth4'] = gth4

    if i[0] == 'g' and i[-3:] == 'th5':
        gth5 = cp.Variable(boolean=True)
        variable['gth5'] = gth5

    if i[0] == 'g' and i[-2:] == 'f1':
        gf1 = cp.Variable(boolean=True)
        variable['gf1'] = gf1
    
    if i[0] == 'g' and i[-2:] == 'f2':
        gf2 = cp.Variable(boolean=True)
        variable['gf2'] = gf2

    if i[0] == 'g' and i[-2:] == 'f3':
        gf3 = cp.Variable(boolean=True)
        variable['gf3'] = gf3

    if i[0] == 'g' and i[-2:] == 'f4':
        gf4 = cp.Variable(boolean=True)
        variable['gf4'] = gf4

    if i[0] == 'g' and i[-2:] == 'f5':
        gf5 = cp.Variable(boolean=True)
        variable['gf5'] = gf5

    if i[0] == 'h' and i[-2:] == 'm1':
        hm1 = cp.Variable(boolean=True)
        variable['hm1'] = hm1
    
    if i[0] == 'h' and i[-2:] == 'm2':
        hm2 = cp.Variable(boolean=True)
        variable['hm2'] = hm2

    if i[0] == 'h' and i[-2:] == 'm3':
        hm3 = cp.Variable(boolean=True)
        variable['hm3'] = hm3

    if i[0] == 'h' and i[-2:] == 'm4':
        hm4 = cp.Variable(boolean=True)
        variable['hm4'] = hm4

    if i[0] == 'h' and i[-2:] == 'm5':
        hm5 = cp.Variable(boolean=True)
        variable['hm5'] = hm5

    if i[0] == 'h' and i[-2:] == 't1':
        ht1 = cp.Variable(boolean=True)
        variable['ht1'] = ht1
    
    if i[0] == 'h' and i[-2:] == 't2':
        ht2 = cp.Variable(boolean=True)
        variable['ht2'] = ht2

    if i[0] == 'h' and i[-2:] == 't3':
        ht3 = cp.Variable(boolean=True)
        variable['ht3'] = ht3

    if i[0] == 'h' and i[-2:] == 't4':
        ht4 = cp.Variable(boolean=True)
        variable['ht4'] = ht4

    if i[0] == 'h' and i[-2:] == 't5':
        ht5 = cp.Variable(boolean=True)
        variable['ht5'] = ht5

    if i[0] == 'h' and i[-2:] == 'w1':
        hw1 = cp.Variable(boolean=True)
        variable['hw1'] = hw1
    
    if i[0] == 'h' and i[-2:] == 'w2':
        hw2 = cp.Variable(boolean=True)
        variable['hw2'] = hw2

    if i[0] == 'h' and i[-2:] == 'w3':
        hw3 = cp.Variable(boolean=True)
        variable['hw3'] = hw3

    if i[0] == 'h' and i[-2:] == 'w4':
        hw4 = cp.Variable(boolean=True)
        variable['hw4'] = hw4

    if i[0] == 'h' and i[-2:] == 'w5':
        hw5 = cp.Variable(boolean=True)
        variable['hw5'] = hw5

    if i[0] == 'h' and i[-3:] == 'th1':
        hth1 = cp.Variable(boolean=True)
        variable['hth1'] = hth1
    
    if i[0] == 'h' and i[-3:] == 'th2':
        hth2 = cp.Variable(boolean=True)
        variable['hth2'] = hth2

    if i[0] == 'h' and i[-3:] == 'th3':
        hth3 = cp.Variable(boolean=True)
        variable['hth3'] = hth3

    if i[0] == 'h' and i[-3:] == 'th4':
        hth4 = cp.Variable(boolean=True)
        variable['hth4'] = hth4

    if i[0] == 'h' and i[-3:] == 'th5':
        hth5 = cp.Variable(boolean=True)
        variable['hth5'] = hth5

    if i[0] == 'h' and i[-2:] == 'f1':
        hf1 = cp.Variable(boolean=True)
        variable['hf1'] = hf1
    
    if i[0] == 'h' and i[-2:] == 'f2':
        hf2 = cp.Variable(boolean=True)
        variable['hf2'] = hf2

    if i[0] == 'h' and i[-2:] == 'f3':
        hf3 = cp.Variable(boolean=True)
        variable['hf3'] = hf3

    if i[0] == 'h' and i[-2:] == 'f4':
        hf4 = cp.Variable(boolean=True)
        variable['hf4'] = hf4

    if i[0] == 'h' and i[-2:] == 'f5':
        hf5 = cp.Variable(boolean=True)
        variable['hf5'] = hf5

    if i[0] == 'i' and i[-2:] == 'm1':
        im1 = cp.Variable(boolean=True)
        variable['im1'] = im1
    
    if i[0] == 'i' and i[-2:] == 'm2':
        im2 = cp.Variable(boolean=True)
        variable['im2'] = im2

    if i[0] == 'i' and i[-2:] == 'm3':
        im3 = cp.Variable(boolean=True)
        variable['im3'] = im3

    if i[0] == 'i' and i[-2:] == 'm4':
        im4 = cp.Variable(boolean=True)
        variable['im4'] = im4

    if i[0] == 'i' and i[-2:] == 'm5':
        im5 = cp.Variable(boolean=True)
        variable['im5'] = im5

    if i[0] == 'i' and i[-2:] == 't1':
        it1 = cp.Variable(boolean=True)
        variable['it1'] = it1
    
    if i[0] == 'i' and i[-2:] == 't2':
        it2 = cp.Variable(boolean=True)
        variable['it2'] = it2

    if i[0] == 'i' and i[-2:] == 't3':
        it3 = cp.Variable(boolean=True)
        variable['it3'] = it3

    if i[0] == 'i' and i[-2:] == 't4':
        it4 = cp.Variable(boolean=True)
        variable['it4'] = it4

    if i[0] == 'i' and i[-2:] == 't5':
        it5 = cp.Variable(boolean=True)
        variable['it5'] = it5

    if i[0] == 'i' and i[-2:] == 'w1':
        iw1 = cp.Variable(boolean=True)
        variable['iw1'] = iw1
    
    if i[0] == 'i' and i[-2:] == 'w2':
        iw2 = cp.Variable(boolean=True)
        variable['iw2'] = iw2

    if i[0] == 'i' and i[-2:] == 'w3':
        iw3 = cp.Variable(boolean=True)
        variable['iw3'] = iw3

    if i[0] == 'i' and i[-2:] == 'w4':
        iw4 = cp.Variable(boolean=True)
        variable['iw4'] = iw4

    if i[0] == 'i' and i[-2:] == 'w5':
        iw5 = cp.Variable(boolean=True)
        variable['iw5'] = iw5

    if i[0] == 'i' and i[-3:] == 'th1':
        ith1 = cp.Variable(boolean=True)
        variable['ith1'] = ith1
    
    if i[0] == 'i' and i[-3:] == 'th2':
        ith2 = cp.Variable(boolean=True)
        variable['ith2'] = ith2

    if i[0] == 'i' and i[-3:] == 'th3':
        ith3 = cp.Variable(boolean=True)
        variable['ith3'] = ith3

    if i[0] == 'i' and i[-3:] == 'th4':
        ith4 = cp.Variable(boolean=True)
        variable['ith4'] = ith4

    if i[0] == 'i' and i[-3:] == 'th5':
        ith5 = cp.Variable(boolean=True)
        variable['ith5'] = ith5

    if i[0] == 'i' and i[-2:] == 'f1':
        if1 = cp.Variable(boolean=True)
        variable['if1'] = if1
    
    if i[0] == 'i' and i[-2:] == 'f2':
        if2 = cp.Variable(boolean=True)
        variable['if2'] = if2

    if i[0] == 'i' and i[-2:] == 'f3':
        if3 = cp.Variable(boolean=True)
        variable['if3'] = if3

    if i[0] == 'i' and i[-2:] == 'f4':
        if4 = cp.Variable(boolean=True)
        variable['if4'] = if4

    if i[0] == 'i' and i[-2:] == 'f5':
        if5 = cp.Variable(boolean=True)
        variable['if5'] = if5

    if i[0] == 'j' and i[-2:] == 'm1':
        jm1 = cp.Variable(boolean=True)
        variable['jm1'] = jm1
    
    if i[0] == 'j' and i[-2:] == 'm2':
        jm2 = cp.Variable(boolean=True)
        variable['jm2'] = jm2

    if i[0] == 'j' and i[-2:] == 'm3':
        jm3 = cp.Variable(boolean=True)
        variable['jm3'] = jm3

    if i[0] == 'j' and i[-2:] == 'm4':
        jm4 = cp.Variable(boolean=True)
        variable['jm4'] = jm4

    if i[0] == 'j' and i[-2:] == 'm5':
        jm5 = cp.Variable(boolean=True)
        variable['jm5'] = jm5

    if i[0] == 'j' and i[-2:] == 't1':
        jt1 = cp.Variable(boolean=True)
        variable['jt1'] = jt1
    
    if i[0] == 'j' and i[-2:] == 't2':
        jt2 = cp.Variable(boolean=True)
        variable['jt2'] = jt2

    if i[0] == 'j' and i[-2:] == 't3':
        jt3 = cp.Variable(boolean=True)
        variable['jt3'] = jt3

    if i[0] == 'j' and i[-2:] == 't4':
        jt4 = cp.Variable(boolean=True)
        variable['jt4'] = jt4

    if i[0] == 'j' and i[-2:] == 't5':
        jt5 = cp.Variable(boolean=True)
        variable['jt5'] = jt5

    if i[0] == 'j' and i[-2:] == 'w1':
        jw1 = cp.Variable(boolean=True)
        variable['jw1'] = jw1
    
    if i[0] == 'j' and i[-2:] == 'w2':
        jw2 = cp.Variable(boolean=True)
        variable['jw2'] = jw2

    if i[0] == 'j' and i[-2:] == 'w3':
        jw3 = cp.Variable(boolean=True)
        variable['jw3'] = jw3

    if i[0] == 'j' and i[-2:] == 'w4':
        jw4 = cp.Variable(boolean=True)
        variable['jw4'] = jw4

    if i[0] == 'j' and i[-2:] == 'w5':
        jw5 = cp.Variable(boolean=True)
        variable['jw5'] = jw5

    if i[0] == 'j' and i[-3:] == 'th1':
        jth1 = cp.Variable(boolean=True)
        variable['jth1'] = jth1
    
    if i[0] == 'j' and i[-3:] == 'th2':
        jth2 = cp.Variable(boolean=True)
        variable['jth2'] = jth2

    if i[0] == 'j' and i[-3:] == 'th3':
        jth3 = cp.Variable(boolean=True)
        variable['jth3'] = jth3

    if i[0] == 'j' and i[-3:] == 'th4':
        jth4 = cp.Variable(boolean=True)
        variable['jth4'] = jth4

    if i[0] == 'j' and i[-3:] == 'th5':
        jth5 = cp.Variable(boolean=True)
        variable['jth5'] = jth5

    if i[0] == 'j' and i[-2:] == 'f1':
        jf1 = cp.Variable(boolean=True)
        variable['jf1'] = jf1
    
    if i[0] == 'j' and i[-2:] == 'f2':
        jf2 = cp.Variable(boolean=True)
        variable['jf2'] = jf2

    if i[0] == 'j' and i[-2:] == 'f3':
        jf3 = cp.Variable(boolean=True)
        variable['jf3'] = jf3

    if i[0] == 'j' and i[-2:] == 'f4':
        jf4 = cp.Variable(boolean=True)
        variable['jf4'] = jf4

    if i[0] == 'j' and i[-2:] == 'f5':
        jf5 = cp.Variable(boolean=True)
        variable['jf5'] = jf5

    if i[0] == 'k' and i[-2:] == 'm1':
        km1 = cp.Variable(boolean=True)
        variable['km1'] = km1
    
    if i[0] == 'k' and i[-2:] == 'm2':
        km2 = cp.Variable(boolean=True)
        variable['km2'] = km2

    if i[0] == 'k' and i[-2:] == 'm3':
        km3 = cp.Variable(boolean=True)
        variable['km3'] = km3

    if i[0] == 'k' and i[-2:] == 'm4':
        km4 = cp.Variable(boolean=True)
        variable['km4'] = km4

    if i[0] == 'k' and i[-2:] == 'm5':
        km5 = cp.Variable(boolean=True)
        variable['km5'] = km5

    if i[0] == 'k' and i[-2:] == 't1':
        kt1 = cp.Variable(boolean=True)
        variable['kt1'] = kt1
    
    if i[0] == 'k' and i[-2:] == 't2':
        kt2 = cp.Variable(boolean=True)
        variable['kt2'] = kt2

    if i[0] == 'k' and i[-2:] == 't3':
        kt3 = cp.Variable(boolean=True)
        variable['kt3'] = kt3

    if i[0] == 'k' and i[-2:] == 't4':
        kt4 = cp.Variable(boolean=True)
        variable['kt4'] = kt4

    if i[0] == 'k' and i[-2:] == 't5':
        kt5 = cp.Variable(boolean=True)
        variable['kt5'] = kt5

    if i[0] == 'k' and i[-2:] == 'w1':
        kw1 = cp.Variable(boolean=True)
        variable['kw1'] = kw1
    
    if i[0] == 'k' and i[-2:] == 'w2':
        kw2 = cp.Variable(boolean=True)
        variable['kw2'] = kw2

    if i[0] == 'k' and i[-2:] == 'w3':
        kw3 = cp.Variable(boolean=True)
        variable['kw3'] = kw3

    if i[0] == 'k' and i[-2:] == 'w4':
        kw4 = cp.Variable(boolean=True)
        variable['kw4'] = kw4

    if i[0] == 'k' and i[-2:] == 'w5':
        kw5 = cp.Variable(boolean=True)
        variable['kw5'] = kw5

    if i[0] == 'k' and i[-3:] == 'th1':
        kth1 = cp.Variable(boolean=True)
        variable['kth1'] = kth1
    
    if i[0] == 'k' and i[-3:] == 'th2':
        kth2 = cp.Variable(boolean=True)
        variable['kth2'] = kth2

    if i[0] == 'k' and i[-3:] == 'th3':
        kth3 = cp.Variable(boolean=True)
        variable['kth3'] = kth3

    if i[0] == 'k' and i[-3:] == 'th4':
        kth4 = cp.Variable(boolean=True)
        variable['kth4'] = kth4

    if i[0] == 'k' and i[-3:] == 'th5':
        kth5 = cp.Variable(boolean=True)
        variable['kth5'] = kth5

    if i[0] == 'k' and i[-2:] == 'f1':
        kf1 = cp.Variable(boolean=True)
        variable['kf1'] = kf1
    
    if i[0] == 'k' and i[-2:] == 'f2':
        kf2 = cp.Variable(boolean=True)
        variable['kf2'] = kf2

    if i[0] == 'k' and i[-2:] == 'f3':
        kf3 = cp.Variable(boolean=True)
        variable['kf3'] = kf3

    if i[0] == 'k' and i[-2:] == 'f4':
        kf4 = cp.Variable(boolean=True)
        variable['kf4'] = kf4

    if i[0] == 'k' and i[-2:] == 'f5':
        kf5 = cp.Variable(boolean=True)
        variable['kf5'] = kf5

    if i[0] == 'l' and i[-2:] == 'm1':
        lm1 = cp.Variable(boolean=True)
        variable['lm1'] = lm1
    
    if i[0] == 'l' and i[-2:] == 'm2':
        lm2 = cp.Variable(boolean=True)
        variable['lm2'] = lm2

    if i[0] == 'l' and i[-2:] == 'm3':
        lm3 = cp.Variable(boolean=True)
        variable['lm3'] = lm3

    if i[0] == 'l' and i[-2:] == 'm4':
        lm4 = cp.Variable(boolean=True)
        variable['lm4'] = lm4

    if i[0] == 'l' and i[-2:] == 'm5':
        lm5 = cp.Variable(boolean=True)
        variable['lm5'] = lm5

    if i[0] == 'l' and i[-2:] == 't1':
        lt1 = cp.Variable(boolean=True)
        variable['lt1'] = lt1
    
    if i[0] == 'l' and i[-2:] == 't2':
        lt2 = cp.Variable(boolean=True)
        variable['lt2'] = lt2

    if i[0] == 'l' and i[-2:] == 't3':
        lt3 = cp.Variable(boolean=True)
        variable['lt3'] = lt3

    if i[0] == 'l' and i[-2:] == 't4':
        lt4 = cp.Variable(boolean=True)
        variable['lt4'] = lt4

    if i[0] == 'l' and i[-2:] == 't5':
        lt5 = cp.Variable(boolean=True)
        variable['lt5'] = lt5

    if i[0] == 'l' and i[-2:] == 'w1':
        lw1 = cp.Variable(boolean=True)
        variable['lw1'] = lw1
    
    if i[0] == 'l' and i[-2:] == 'w2':
        lw2 = cp.Variable(boolean=True)
        variable['lw2'] = lw2

    if i[0] == 'l' and i[-2:] == 'w3':
        lw3 = cp.Variable(boolean=True)
        variable['lw3'] = lw3

    if i[0] == 'l' and i[-2:] == 'w4':
        lw4 = cp.Variable(boolean=True)
        variable['lw4'] = lw4

    if i[0] == 'l' and i[-2:] == 'w5':
        lw5 = cp.Variable(boolean=True)
        variable['lw5'] = lw5

    if i[0] == 'l' and i[-3:] == 'th1':
        lth1 = cp.Variable(boolean=True)
        variable['lth1'] = lth1
    
    if i[0] == 'l' and i[-3:] == 'th2':
        lth2 = cp.Variable(boolean=True)
        variable['lth2'] = lth2

    if i[0] == 'l' and i[-3:] == 'th3':
        lth3 = cp.Variable(boolean=True)
        variable['lth3'] = lth3

    if i[0] == 'l' and i[-3:] == 'th4':
        lth4 = cp.Variable(boolean=True)
        variable['lth4'] = lth4

    if i[0] == 'l' and i[-3:] == 'th5':
        lth5 = cp.Variable(boolean=True)
        variable['lth5'] = lth5

    if i[0] == 'l' and i[-2:] == 'f1':
        lf1 = cp.Variable(boolean=True)
        variable['lf1'] = lf1
    
    if i[0] == 'l' and i[-2:] == 'f2':
        lf2 = cp.Variable(boolean=True)
        variable['lf2'] = lf2

    if i[0] == 'l' and i[-2:] == 'f3':
        lf3 = cp.Variable(boolean=True)
        variable['lf3'] = lf3

    if i[0] == 'l' and i[-2:] == 'f4':
        lf4 = cp.Variable(boolean=True)
        variable['lf4'] = lf4

    if i[0] == 'l' and i[-2:] == 'f5':
        lf5 = cp.Variable(boolean=True)
        variable['lf5'] = lf5
        
    if i[0] == 'm' and i[-2:] == 'm1':
        mm1 = cp.Variable(boolean=True)
        variable['mm1'] = mm1
    
    if i[0] == 'm' and i[-2:] == 'm2':
        mm2 = cp.Variable(boolean=True)
        variable['mm2'] = mm2

    if i[0] == 'm' and i[-2:] == 'm3':
        mm3 = cp.Variable(boolean=True)
        variable['mm3'] = mm3

    if i[0] == 'm' and i[-2:] == 'm4':
        mm4 = cp.Variable(boolean=True)
        variable['mm4'] = mm4

    if i[0] == 'm' and i[-2:] == 'm5':
        mm5 = cp.Variable(boolean=True)
        variable['mm5'] = mm5

    if i[0] == 'm' and i[-2:] == 't1':
        mt1 = cp.Variable(boolean=True)
        variable['mt1'] = mt1
    
    if i[0] == 'm' and i[-2:] == 't2':
        mt2 = cp.Variable(boolean=True)
        variable['mt2'] = mt2

    if i[0] == 'm' and i[-2:] == 't3':
        mt3 = cp.Variable(boolean=True)
        variable['mt3'] = mt3

    if i[0] == 'm' and i[-2:] == 't4':
        mt4 = cp.Variable(boolean=True)
        variable['mt4'] = mt4

    if i[0] == 'm' and i[-2:] == 't5':
        mt5 = cp.Variable(boolean=True)
        variable['mt5'] = mt5

    if i[0] == 'm' and i[-2:] == 'w1':
        mw1 = cp.Variable(boolean=True)
        variable['mw1'] = mw1
    
    if i[0] == 'm' and i[-2:] == 'w2':
        mw2 = cp.Variable(boolean=True)
        variable['mw2'] = mw2

    if i[0] == 'm' and i[-2:] == 'w3':
        mw3 = cp.Variable(boolean=True)
        variable['mw3'] = mw3

    if i[0] == 'm' and i[-2:] == 'w4':
        mw4 = cp.Variable(boolean=True)
        variable['mw4'] = mw4

    if i[0] == 'm' and i[-2:] == 'w5':
        mw5 = cp.Variable(boolean=True)
        variable['mw5'] = mw5

    if i[0] == 'm' and i[-3:] == 'th1':
        mth1 = cp.Variable(boolean=True)
        variable['mth1'] = mth1
    
    if i[0] == 'm' and i[-3:] == 'th2':
        mth2 = cp.Variable(boolean=True)
        variable['mth2'] = mth2

    if i[0] == 'm' and i[-3:] == 'th3':
        mth3 = cp.Variable(boolean=True)
        variable['mth3'] = mth3

    if i[0] == 'm' and i[-3:] == 'th4':
        mth4 = cp.Variable(boolean=True)
        variable['mth4'] = mth4

    if i[0] == 'm' and i[-3:] == 'th5':
        mth5 = cp.Variable(boolean=True)
        variable['mth5'] = mth5

    if i[0] == 'm' and i[-2:] == 'f1':
        mf1 = cp.Variable(boolean=True)
        variable['mf1'] = mf1
    
    if i[0] == 'm' and i[-2:] == 'f2':
        mf2 = cp.Variable(boolean=True)
        variable['mf2'] = mf2

    if i[0] == 'm' and i[-2:] == 'f3':
        mf3 = cp.Variable(boolean=True)
        variable['mf3'] = mf3

    if i[0] == 'm' and i[-2:] == 'f4':
        mf4 = cp.Variable(boolean=True)
        variable['mf4'] = mf4

    if i[0] == 'm' and i[-2:] == 'f5':
        mf5 = cp.Variable(boolean=True)
        variable['mf5'] = mf5

    if i[0] == 'n' and i[-2:] == 'm1':
        nm1 = cp.Variable(boolean=True)
        variable['nm1'] = nm1
    
    if i[0] == 'n' and i[-2:] == 'm2':
        nm2 = cp.Variable(boolean=True)
        variable['nm2'] = nm2

    if i[0] == 'n' and i[-2:] == 'm3':
        nm3 = cp.Variable(boolean=True)
        variable['nm3'] = nm3

    if i[0] == 'n' and i[-2:] == 'm4':
        nm4 = cp.Variable(boolean=True)
        variable['nm4'] = nm4

    if i[0] == 'n' and i[-2:] == 'm5':
        nm5 = cp.Variable(boolean=True)
        variable['nm5'] = nm5

    if i[0] == 'n' and i[-2:] == 't1':
        nt1 = cp.Variable(boolean=True)
        variable['nt1'] = nt1
    
    if i[0] == 'n' and i[-2:] == 't2':
        nt2 = cp.Variable(boolean=True)
        variable['nt2'] = nt2

    if i[0] == 'n' and i[-2:] == 't3':
        nt3 = cp.Variable(boolean=True)
        variable['nt3'] = nt3

    if i[0] == 'n' and i[-2:] == 't4':
        nt4 = cp.Variable(boolean=True)
        variable['nt4'] = nt4

    if i[0] == 'n' and i[-2:] == 't5':
        nt5 = cp.Variable(boolean=True)
        variable['nt5'] = nt5

    if i[0] == 'n' and i[-2:] == 'w1':
        nw1 = cp.Variable(boolean=True)
        variable['nw1'] = nw1
    
    if i[0] == 'n' and i[-2:] == 'w2':
        nw2 = cp.Variable(boolean=True)
        variable['nw2'] = nw2

    if i[0] == 'n' and i[-2:] == 'w3':
        nw3 = cp.Variable(boolean=True)
        variable['nw3'] = nw3

    if i[0] == 'n' and i[-2:] == 'w4':
        nw4 = cp.Variable(boolean=True)
        variable['nw4'] = nw4

    if i[0] == 'n' and i[-2:] == 'w5':
        nw5 = cp.Variable(boolean=True)
        variable['nw5'] = nw5

    if i[0] == 'n' and i[-3:] == 'th1':
        nth1 = cp.Variable(boolean=True)
        variable['nth1'] = nth1
    
    if i[0] == 'n' and i[-3:] == 'th2':
        nth2 = cp.Variable(boolean=True)
        variable['nth2'] = nth2

    if i[0] == 'n' and i[-3:] == 'th3':
        nth3 = cp.Variable(boolean=True)
        variable['nth3'] = nth3

    if i[0] == 'n' and i[-3:] == 'th4':
        nth4 = cp.Variable(boolean=True)
        variable['nth4'] = nth4

    if i[0] == 'n' and i[-3:] == 'th5':
        nth5 = cp.Variable(boolean=True)
        variable['nth5'] = nth5

    if i[0] == 'n' and i[-2:] == 'f1':
        nf1 = cp.Variable(boolean=True)
        variable['nf1'] = nf1
    
    if i[0] == 'n' and i[-2:] == 'f2':
        nf2 = cp.Variable(boolean=True)
        variable['nf2'] = nf2

    if i[0] == 'n' and i[-2:] == 'f3':
        nf3 = cp.Variable(boolean=True)
        variable['nf3'] = nf3

    if i[0] == 'n' and i[-2:] == 'f4':
        nf4 = cp.Variable(boolean=True)
        variable['nf4'] = nf4

    if i[0] == 'n' and i[-2:] == 'f5':
        nf5 = cp.Variable(boolean=True)
        variable['nf5'] = nf5

    if i[0] == 'n' and i[-2:] == 'm1':
        nm1 = cp.Variable(boolean=True)
        variable['nm1'] = nm1
    
    if i[0] == 'n' and i[-2:] == 'm2':
        nm2 = cp.Variable(boolean=True)
        variable['nm2'] = nm2

    if i[0] == 'n' and i[-2:] == 'm3':
        nm3 = cp.Variable(boolean=True)
        variable['nm3'] = nm3

    if i[0] == 'n' and i[-2:] == 'm4':
        nm4 = cp.Variable(boolean=True)
        variable['nm4'] = nm4

    if i[0] == 'n' and i[-2:] == 'm5':
        nm5 = cp.Variable(boolean=True)
        variable['nm5'] = nm5

    if i[0] == 'n' and i[-2:] == 't1':
        nt1 = cp.Variable(boolean=True)
        variable['nt1'] = nt1
    
    if i[0] == 'n' and i[-2:] == 't2':
        nt2 = cp.Variable(boolean=True)
        variable['nt2'] = nt2

    if i[0] == 'n' and i[-2:] == 't3':
        nt3 = cp.Variable(boolean=True)
        variable['nt3'] = nt3

    if i[0] == 'n' and i[-2:] == 't4':
        nt4 = cp.Variable(boolean=True)
        variable['nt4'] = nt4

    if i[0] == 'n' and i[-2:] == 't5':
        nt5 = cp.Variable(boolean=True)
        variable['nt5'] = nt5

    if i[0] == 'n' and i[-2:] == 'w1':
        nw1 = cp.Variable(boolean=True)
        variable['nw1'] = nw1
    
    if i[0] == 'n' and i[-2:] == 'w2':
        nw2 = cp.Variable(boolean=True)
        variable['nw2'] = nw2

    if i[0] == 'n' and i[-2:] == 'w3':
        nw3 = cp.Variable(boolean=True)
        variable['nw3'] = nw3

    if i[0] == 'n' and i[-2:] == 'w4':
        nw4 = cp.Variable(boolean=True)
        variable['nw4'] = nw4

    if i[0] == 'n' and i[-2:] == 'w5':
        nw5 = cp.Variable(boolean=True)
        variable['nw5'] = nw5

    if i[0] == 'n' and i[-3:] == 'th1':
        nth1 = cp.Variable(boolean=True)
        variable['nth1'] = nth1
    
    if i[0] == 'n' and i[-3:] == 'th2':
        nth2 = cp.Variable(boolean=True)
        variable['nth2'] = nth2

    if i[0] == 'n' and i[-3:] == 'th3':
        nth3 = cp.Variable(boolean=True)
        variable['nth3'] = nth3

    if i[0] == 'n' and i[-3:] == 'th4':
        nth4 = cp.Variable(boolean=True)
        variable['nth4'] = nth4

    if i[0] == 'n' and i[-3:] == 'th5':
        nth5 = cp.Variable(boolean=True)
        variable['nth5'] = nth5

    if i[0] == 'n' and i[-2:] == 'f1':
        nf1 = cp.Variable(boolean=True)
        variable['nf1'] = nf1
    
    if i[0] == 'n' and i[-2:] == 'f2':
        nf2 = cp.Variable(boolean=True)
        variable['nf2'] = nf2

    if i[0] == 'n' and i[-2:] == 'f3':
        nf3 = cp.Variable(boolean=True)
        variable['nf3'] = nf3

    if i[0] == 'n' and i[-2:] == 'f4':
        nf4 = cp.Variable(boolean=True)
        variable['nf4'] = nf4

    if i[0] == 'n' and i[-2:] == 'f5':
        nf5 = cp.Variable(boolean=True)
        variable['nf5'] = nf5

    if i[0] == 'o' and i[-2:] == 'm1':
        om1 = cp.Variable(boolean=True)
        variable['om1'] = om1
    
    if i[0] == 'o' and i[-2:] == 'm2':
        om2 = cp.Variable(boolean=True)
        variable['om2'] = om2

    if i[0] == 'o' and i[-2:] == 'm3':
        om3 = cp.Variable(boolean=True)
        variable['om3'] = om3

    if i[0] == 'o' and i[-2:] == 'm4':
        om4 = cp.Variable(boolean=True)
        variable['om4'] = om4

    if i[0] == 'o' and i[-2:] == 'm5':
        om5 = cp.Variable(boolean=True)
        variable['om5'] = om5

    if i[0] == 'o' and i[-2:] == 't1':
        ot1 = cp.Variable(boolean=True)
        variable['ot1'] = ot1
    
    if i[0] == 'o' and i[-2:] == 't2':
        ot2 = cp.Variable(boolean=True)
        variable['ot2'] = ot2

    if i[0] == 'o' and i[-2:] == 't3':
        ot3 = cp.Variable(boolean=True)
        variable['ot3'] = ot3

    if i[0] == 'o' and i[-2:] == 't4':
        ot4 = cp.Variable(boolean=True)
        variable['ot4'] = ot4

    if i[0] == 'o' and i[-2:] == 't5':
        ot5 = cp.Variable(boolean=True)
        variable['ot5'] = ot5

    if i[0] == 'o' and i[-2:] == 'w1':
        ow1 = cp.Variable(boolean=True)
        variable['ow1'] = ow1
    
    if i[0] == 'o' and i[-2:] == 'w2':
        ow2 = cp.Variable(boolean=True)
        variable['ow2'] = ow2

    if i[0] == 'o' and i[-2:] == 'w3':
        ow3 = cp.Variable(boolean=True)
        variable['ow3'] = ow3

    if i[0] == 'o' and i[-2:] == 'w4':
        ow4 = cp.Variable(boolean=True)
        variable['ow4'] = ow4

    if i[0] == 'o' and i[-2:] == 'w5':
        ow5 = cp.Variable(boolean=True)
        variable['ow5'] = ow5

    if i[0] == 'o' and i[-3:] == 'th1':
        oth1 = cp.Variable(boolean=True)
        variable['oth1'] = oth1
    
    if i[0] == 'o' and i[-3:] == 'th2':
        oth2 = cp.Variable(boolean=True)
        variable['oth2'] = oth2

    if i[0] == 'o' and i[-3:] == 'th3':
        oth3 = cp.Variable(boolean=True)
        variable['oth3'] = oth3

    if i[0] == 'o' and i[-3:] == 'th4':
        oth4 = cp.Variable(boolean=True)
        variable['oth4'] = oth4

    if i[0] == 'o' and i[-3:] == 'th5':
        oth5 = cp.Variable(boolean=True)
        variable['oth5'] = oth5

    if i[0] == 'o' and i[-2:] == 'f1':
        of1 = cp.Variable(boolean=True)
        variable['of1'] = of1
    
    if i[0] == 'o' and i[-2:] == 'f2':
        of2 = cp.Variable(boolean=True)
        variable['of2'] = of2

    if i[0] == 'o' and i[-2:] == 'f3':
        of3 = cp.Variable(boolean=True)
        variable['of3'] = of3

    if i[0] == 'o' and i[-2:] == 'f4':
        of4 = cp.Variable(boolean=True)
        variable['of4'] = of4

    if i[0] == 'o' and i[-2:] == 'f5':
        of5 = cp.Variable(boolean=True)
        variable['of5'] = of5

    if i[0] == 'p' and i[-2:] == 'm1':
        pm1 = cp.Variable(boolean=True)
        variable['pm1'] = pm1
    
    if i[0] == 'p' and i[-2:] == 'm2':
        pm2 = cp.Variable(boolean=True)
        variable['pm2'] = pm2

    if i[0] == 'p' and i[-2:] == 'm3':
        pm3 = cp.Variable(boolean=True)
        variable['pm3'] = pm3

    if i[0] == 'p' and i[-2:] == 'm4':
        pm4 = cp.Variable(boolean=True)
        variable['pm4'] = pm4

    if i[0] == 'p' and i[-2:] == 'm5':
        pm5 = cp.Variable(boolean=True)
        variable['pm5'] = pm5

    if i[0] == 'p' and i[-2:] == 't1':
        pt1 = cp.Variable(boolean=True)
        variable['pt1'] = pt1
    
    if i[0] == 'p' and i[-2:] == 't2':
        pt2 = cp.Variable(boolean=True)
        variable['pt2'] = pt2

    if i[0] == 'p' and i[-2:] == 't3':
        pt3 = cp.Variable(boolean=True)
        variable['pt3'] = pt3

    if i[0] == 'p' and i[-2:] == 't4':
        pt4 = cp.Variable(boolean=True)
        variable['pt4'] = pt4

    if i[0] == 'p' and i[-2:] == 't5':
        pt5 = cp.Variable(boolean=True)
        variable['pt5'] = pt5

    if i[0] == 'p' and i[-2:] == 'w1':
        pw1 = cp.Variable(boolean=True)
        variable['pw1'] = pw1
    
    if i[0] == 'p' and i[-2:] == 'w2':
        pw2 = cp.Variable(boolean=True)
        variable['pw2'] = pw2

    if i[0] == 'p' and i[-2:] == 'w3':
        pw3 = cp.Variable(boolean=True)
        variable['pw3'] = pw3

    if i[0] == 'p' and i[-2:] == 'w4':
        pw4 = cp.Variable(boolean=True)
        variable['pw4'] = pw4

    if i[0] == 'p' and i[-2:] == 'w5':
        pw5 = cp.Variable(boolean=True)
        variable['pw5'] = pw5

    if i[0] == 'p' and i[-3:] == 'th1':
        pth1 = cp.Variable(boolean=True)
        variable['pth1'] = pth1
    
    if i[0] == 'p' and i[-3:] == 'th2':
        pth2 = cp.Variable(boolean=True)
        variable['pth2'] = pth2

    if i[0] == 'p' and i[-3:] == 'th3':
        pth3 = cp.Variable(boolean=True)
        variable['pth3'] = pth3

    if i[0] == 'p' and i[-3:] == 'th4':
        pth4 = cp.Variable(boolean=True)
        variable['pth4'] = pth4

    if i[0] == 'p' and i[-3:] == 'th5':
        pth5 = cp.Variable(boolean=True)
        variable['pth5'] = pth5

    if i[0] == 'p' and i[-2:] == 'f1':
        pf1 = cp.Variable(boolean=True)
        variable['pf1'] = pf1
    
    if i[0] == 'p' and i[-2:] == 'f2':
        pf2 = cp.Variable(boolean=True)
        variable['pf2'] = pf2

    if i[0] == 'p' and i[-2:] == 'f3':
        pf3 = cp.Variable(boolean=True)
        variable['pf3'] = pf3

    if i[0] == 'p' and i[-2:] == 'f4':
        pf4 = cp.Variable(boolean=True)
        variable['pf4'] = pf4

    if i[0] == 'p' and i[-2:] == 'f5':
        pf5 = cp.Variable(boolean=True)
        variable['pf5'] = pf5

    if i[0] == 'p' and i[-2:] == 'm1':
        pm1 = cp.Variable(boolean=True)
        variable['pm1'] = pm1
    
    if i[0] == 'p' and i[-2:] == 'm2':
        pm2 = cp.Variable(boolean=True)
        variable['pm2'] = pm2

    if i[0] == 'p' and i[-2:] == 'm3':
        pm3 = cp.Variable(boolean=True)
        variable['pm3'] = pm3

    if i[0] == 'p' and i[-2:] == 'm4':
        pm4 = cp.Variable(boolean=True)
        variable['pm4'] = pm4

    if i[0] == 'p' and i[-2:] == 'm5':
        pm5 = cp.Variable(boolean=True)
        variable['pm5'] = pm5

    if i[0] == 'p' and i[-2:] == 't1':
        pt1 = cp.Variable(boolean=True)
        variable['pt1'] = pt1
    
    if i[0] == 'p' and i[-2:] == 't2':
        pt2 = cp.Variable(boolean=True)
        variable['pt2'] = pt2

    if i[0] == 'p' and i[-2:] == 't3':
        pt3 = cp.Variable(boolean=True)
        variable['pt3'] = pt3

    if i[0] == 'p' and i[-2:] == 't4':
        pt4 = cp.Variable(boolean=True)
        variable['pt4'] = pt4

    if i[0] == 'p' and i[-2:] == 't5':
        pt5 = cp.Variable(boolean=True)
        variable['pt5'] = pt5

    if i[0] == 'p' and i[-2:] == 'w1':
        pw1 = cp.Variable(boolean=True)
        variable['pw1'] = pw1
    
    if i[0] == 'p' and i[-2:] == 'w2':
        pw2 = cp.Variable(boolean=True)
        variable['pw2'] = pw2

    if i[0] == 'p' and i[-2:] == 'w3':
        pw3 = cp.Variable(boolean=True)
        variable['pw3'] = pw3

    if i[0] == 'p' and i[-2:] == 'w4':
        pw4 = cp.Variable(boolean=True)
        variable['pw4'] = pw4

    if i[0] == 'p' and i[-2:] == 'w5':
        pw5 = cp.Variable(boolean=True)
        variable['pw5'] = pw5

    if i[0] == 'p' and i[-3:] == 'th1':
        pth1 = cp.Variable(boolean=True)
        variable['pth1'] = pth1
    
    if i[0] == 'p' and i[-3:] == 'th2':
        pth2 = cp.Variable(boolean=True)
        variable['pth2'] = pth2

    if i[0] == 'p' and i[-3:] == 'th3':
        pth3 = cp.Variable(boolean=True)
        variable['pth3'] = pth3

    if i[0] == 'p' and i[-3:] == 'th4':
        pth4 = cp.Variable(boolean=True)
        variable['pth4'] = pth4

    if i[0] == 'p' and i[-3:] == 'th5':
        pth5 = cp.Variable(boolean=True)
        variable['pth5'] = pth5

    if i[0] == 'p' and i[-2:] == 'f1':
        pf1 = cp.Variable(boolean=True)
        variable['pf1'] = pf1
    
    if i[0] == 'p' and i[-2:] == 'f2':
        pf2 = cp.Variable(boolean=True)
        variable['pf2'] = pf2

    if i[0] == 'p' and i[-2:] == 'f3':
        pf3 = cp.Variable(boolean=True)
        variable['pf3'] = pf3

    if i[0] == 'p' and i[-2:] == 'f4':
        pf4 = cp.Variable(boolean=True)
        variable['pf4'] = pf4

    if i[0] == 'p' and i[-2:] == 'f5':
        pf5 = cp.Variable(boolean=True)
        variable['pf5'] = pf5

    if i[0] == 'q' and i[-2:] == 'm1':
        qm1 = cp.Variable(boolean=True)
        variable['qm1'] = qm1
    
    if i[0] == 'q' and i[-2:] == 'm2':
        qm2 = cp.Variable(boolean=True)
        variable['qm2'] = qm2

    if i[0] == 'q' and i[-2:] == 'm3':
        qm3 = cp.Variable(boolean=True)
        variable['qm3'] = qm3

    if i[0] == 'q' and i[-2:] == 'm4':
        qm4 = cp.Variable(boolean=True)
        variable['qm4'] = qm4

    if i[0] == 'q' and i[-2:] == 'm5':
        qm5 = cp.Variable(boolean=True)
        variable['qm5'] = qm5

    if i[0] == 'q' and i[-2:] == 't1':
        qt1 = cp.Variable(boolean=True)
        variable['qt1'] = qt1
    
    if i[0] == 'q' and i[-2:] == 't2':
        qt2 = cp.Variable(boolean=True)
        variable['qt2'] = qt2

    if i[0] == 'q' and i[-2:] == 't3':
        qt3 = cp.Variable(boolean=True)
        variable['qt3'] = qt3

    if i[0] == 'q' and i[-2:] == 't4':
        qt4 = cp.Variable(boolean=True)
        variable['qt4'] = qt4

    if i[0] == 'q' and i[-2:] == 't5':
        qt5 = cp.Variable(boolean=True)
        variable['qt5'] = qt5

    if i[0] == 'q' and i[-2:] == 'w1':
        qw1 = cp.Variable(boolean=True)
        variable['qw1'] = qw1
    
    if i[0] == 'q' and i[-2:] == 'w2':
        qw2 = cp.Variable(boolean=True)
        variable['qw2'] = qw2

    if i[0] == 'q' and i[-2:] == 'w3':
        qw3 = cp.Variable(boolean=True)
        variable['qw3'] = qw3

    if i[0] == 'q' and i[-2:] == 'w4':
        qw4 = cp.Variable(boolean=True)
        variable['qw4'] = qw4

    if i[0] == 'q' and i[-2:] == 'w5':
        qw5 = cp.Variable(boolean=True)
        variable['qw5'] = qw5

    if i[0] == 'q' and i[-3:] == 'th1':
        qth1 = cp.Variable(boolean=True)
        variable['qth1'] = qth1
    
    if i[0] == 'q' and i[-3:] == 'th2':
        qth2 = cp.Variable(boolean=True)
        variable['qth2'] = qth2

    if i[0] == 'q' and i[-3:] == 'th3':
        qth3 = cp.Variable(boolean=True)
        variable['qth3'] = qth3

    if i[0] == 'q' and i[-3:] == 'th4':
        qth4 = cp.Variable(boolean=True)
        variable['qth4'] = qth4

    if i[0] == 'q' and i[-3:] == 'th5':
        qth5 = cp.Variable(boolean=True)
        variable['qth5'] = qth5

    if i[0] == 'q' and i[-2:] == 'f1':
        qf1 = cp.Variable(boolean=True)
        variable['qf1'] = qf1
    
    if i[0] == 'q' and i[-2:] == 'f2':
        qf2 = cp.Variable(boolean=True)
        variable['qf2'] = qf2

    if i[0] == 'q' and i[-2:] == 'f3':
        qf3 = cp.Variable(boolean=True)
        variable['qf3'] = qf3

    if i[0] == 'q' and i[-2:] == 'f4':
        qf4 = cp.Variable(boolean=True)
        variable['qf4'] = qf4

    if i[0] == 'q' and i[-2:] == 'f5':
        qf5 = cp.Variable(boolean=True)
        variable['qf5'] = qf5

    if i[0] == 'r' and i[-2:] == 'm1':
        rm1 = cp.Variable(boolean=True)
        variable['rm1'] = rm1
    
    if i[0] == 'r' and i[-2:] == 'm2':
        rm2 = cp.Variable(boolean=True)
        variable['rm2'] = rm2

    if i[0] == 'r' and i[-2:] == 'm3':
        rm3 = cp.Variable(boolean=True)
        variable['rm3'] = rm3

    if i[0] == 'r' and i[-2:] == 'm4':
        rm4 = cp.Variable(boolean=True)
        variable['rm4'] = rm4

    if i[0] == 'r' and i[-2:] == 'm5':
        rm5 = cp.Variable(boolean=True)
        variable['rm5'] = rm5

    if i[0] == 'r' and i[-2:] == 't1':
        rt1 = cp.Variable(boolean=True)
        variable['rt1'] = rt1
    
    if i[0] == 'r' and i[-2:] == 't2':
        rt2 = cp.Variable(boolean=True)
        variable['rt2'] = rt2

    if i[0] == 'r' and i[-2:] == 't3':
        rt3 = cp.Variable(boolean=True)
        variable['rt3'] = rt3

    if i[0] == 'r' and i[-2:] == 't4':
        rt4 = cp.Variable(boolean=True)
        variable['rt4'] = rt4

    if i[0] == 'r' and i[-2:] == 't5':
        rt5 = cp.Variable(boolean=True)
        variable['rt5'] = rt5

    if i[0] == 'r' and i[-2:] == 'w1':
        rw1 = cp.Variable(boolean=True)
        variable['rw1'] = rw1
    
    if i[0] == 'r' and i[-2:] == 'w2':
        rw2 = cp.Variable(boolean=True)
        variable['rw2'] = rw2

    if i[0] == 'r' and i[-2:] == 'w3':
        rw3 = cp.Variable(boolean=True)
        variable['rw3'] = rw3

    if i[0] == 'r' and i[-2:] == 'w4':
        rw4 = cp.Variable(boolean=True)
        variable['rw4'] = rw4

    if i[0] == 'r' and i[-2:] == 'w5':
        rw5 = cp.Variable(boolean=True)
        variable['rw5'] = rw5

    if i[0] == 'r' and i[-3:] == 'th1':
        rth1 = cp.Variable(boolean=True)
        variable['rth1'] = rth1
    
    if i[0] == 'r' and i[-3:] == 'th2':
        rth2 = cp.Variable(boolean=True)
        variable['rth2'] = rth2

    if i[0] == 'r' and i[-3:] == 'th3':
        rth3 = cp.Variable(boolean=True)
        variable['rth3'] = rth3

    if i[0] == 'r' and i[-3:] == 'th4':
        rth4 = cp.Variable(boolean=True)
        variable['rth4'] = rth4

    if i[0] == 'r' and i[-3:] == 'th5':
        rth5 = cp.Variable(boolean=True)
        variable['rth5'] = rth5

    if i[0] == 'r' and i[-2:] == 'f1':
        rf1 = cp.Variable(boolean=True)
        variable['rf1'] = rf1
    
    if i[0] == 'r' and i[-2:] == 'f2':
        rf2 = cp.Variable(boolean=True)
        variable['rf2'] = rf2

    if i[0] == 'r' and i[-2:] == 'f3':
        rf3 = cp.Variable(boolean=True)
        variable['rf3'] = rf3

    if i[0] == 'r' and i[-2:] == 'f4':
        rf4 = cp.Variable(boolean=True)
        variable['rf4'] = rf4

    if i[0] == 'r' and i[-2:] == 'f5':
        rf5 = cp.Variable(boolean=True)
        variable['rf5'] = rf5

    if i[0] == 's' and i[-2:] == 'm1':
        sm1 = cp.Variable(boolean=True)
        variable['sm1'] = sm1
    
    if i[0] == 's' and i[-2:] == 'm2':
        sm2 = cp.Variable(boolean=True)
        variable['sm2'] = sm2

    if i[0] == 's' and i[-2:] == 'm3':
        sm3 = cp.Variable(boolean=True)
        variable['sm3'] = sm3

    if i[0] == 's' and i[-2:] == 'm4':
        sm4 = cp.Variable(boolean=True)
        variable['sm4'] = sm4

    if i[0] == 's' and i[-2:] == 'm5':
        sm5 = cp.Variable(boolean=True)
        variable['sm5'] = sm5

    if i[0] == 's' and i[-2:] == 't1':
        st1 = cp.Variable(boolean=True)
        variable['st1'] = st1
    
    if i[0] == 's' and i[-2:] == 't2':
        st2 = cp.Variable(boolean=True)
        variable['st2'] = st2

    if i[0] == 's' and i[-2:] == 't3':
        st3 = cp.Variable(boolean=True)
        variable['st3'] = st3

    if i[0] == 's' and i[-2:] == 't4':
        st4 = cp.Variable(boolean=True)
        variable['st4'] = st4

    if i[0] == 's' and i[-2:] == 't5':
        st5 = cp.Variable(boolean=True)
        variable['st5'] = st5

    if i[0] == 's' and i[-2:] == 'w1':
        sw1 = cp.Variable(boolean=True)
        variable['sw1'] = sw1
    
    if i[0] == 's' and i[-2:] == 'w2':
        sw2 = cp.Variable(boolean=True)
        variable['sw2'] = sw2

    if i[0] == 's' and i[-2:] == 'w3':
        sw3 = cp.Variable(boolean=True)
        variable['sw3'] = sw3

    if i[0] == 's' and i[-2:] == 'w4':
        sw4 = cp.Variable(boolean=True)
        variable['sw4'] = sw4

    if i[0] == 's' and i[-2:] == 'w5':
        sw5 = cp.Variable(boolean=True)
        variable['sw5'] = sw5

    if i[0] == 's' and i[-3:] == 'th1':
        sth1 = cp.Variable(boolean=True)
        variable['sth1'] = sth1
    
    if i[0] == 's' and i[-3:] == 'th2':
        sth2 = cp.Variable(boolean=True)
        variable['sth2'] = sth2

    if i[0] == 's' and i[-3:] == 'th3':
        sth3 = cp.Variable(boolean=True)
        variable['sth3'] = sth3

    if i[0] == 's' and i[-3:] == 'th4':
        sth4 = cp.Variable(boolean=True)
        variable['sth4'] = sth4

    if i[0] == 's' and i[-3:] == 'th5':
        sth5 = cp.Variable(boolean=True)
        variable['sth5'] = sth5

    if i[0] == 's' and i[-2:] == 'f1':
        sf1 = cp.Variable(boolean=True)
        variable['sf1'] = sf1
    
    if i[0] == 's' and i[-2:] == 'f2':
        sf2 = cp.Variable(boolean=True)
        variable['sf2'] = sf2

    if i[0] == 's' and i[-2:] == 'f3':
        sf3 = cp.Variable(boolean=True)
        variable['sf3'] = sf3

    if i[0] == 's' and i[-2:] == 'f4':
        sf4 = cp.Variable(boolean=True)
        variable['sf4'] = sf4

    if i[0] == 's' and i[-2:] == 'f5':
        sf5 = cp.Variable(boolean=True)
        variable['sf5'] = sf5

    if i[0] == 't' and i[-2:] == 'm1':
        tm1 = cp.Variable(boolean=True)
        variable['tm1'] = tm1
    
    if i[0] == 't' and i[-2:] == 'm2':
        tm2 = cp.Variable(boolean=True)
        variable['tm2'] = tm2

    if i[0] == 't' and i[-2:] == 'm3':
        tm3 = cp.Variable(boolean=True)
        variable['tm3'] = tm3

    if i[0] == 't' and i[-2:] == 'm4':
        tm4 = cp.Variable(boolean=True)
        variable['tm4'] = tm4

    if i[0] == 't' and i[-2:] == 'm5':
        tm5 = cp.Variable(boolean=True)
        variable['tm5'] = tm5

    if i[0] == 't' and i[-2:] == 't1':
        tt1 = cp.Variable(boolean=True)
        variable['tt1'] = tt1
    
    if i[0] == 't' and i[-2:] == 't2':
        tt2 = cp.Variable(boolean=True)
        variable['tt2'] = tt2

    if i[0] == 't' and i[-2:] == 't3':
        tt3 = cp.Variable(boolean=True)
        variable['tt3'] = tt3

    if i[0] == 't' and i[-2:] == 't4':
        tt4 = cp.Variable(boolean=True)
        variable['tt4'] = tt4

    if i[0] == 't' and i[-2:] == 't5':
        tt5 = cp.Variable(boolean=True)
        variable['tt5'] = tt5

    if i[0] == 't' and i[-2:] == 'w1':
        tw1 = cp.Variable(boolean=True)
        variable['tw1'] = tw1
    
    if i[0] == 't' and i[-2:] == 'w2':
        tw2 = cp.Variable(boolean=True)
        variable['tw2'] = tw2

    if i[0] == 't' and i[-2:] == 'w3':
        tw3 = cp.Variable(boolean=True)
        variable['tw3'] = tw3

    if i[0] == 't' and i[-2:] == 'w4':
        tw4 = cp.Variable(boolean=True)
        variable['tw4'] = tw4

    if i[0] == 't' and i[-2:] == 'w5':
        tw5 = cp.Variable(boolean=True)
        variable['tw5'] = tw5

    if i[0] == 't' and i[-3:] == 'th1':
        tth1 = cp.Variable(boolean=True)
        variable['tth1'] = tth1
    
    if i[0] == 't' and i[-3:] == 'th2':
        tth2 = cp.Variable(boolean=True)
        variable['tth2'] = tth2

    if i[0] == 't' and i[-3:] == 'th3':
        tth3 = cp.Variable(boolean=True)
        variable['tth3'] = tth3

    if i[0] == 't' and i[-3:] == 'th4':
        tth4 = cp.Variable(boolean=True)
        variable['tth4'] = tth4

    if i[0] == 't' and i[-3:] == 'th5':
        tth5 = cp.Variable(boolean=True)
        variable['tth5'] = tth5

    if i[0] == 't' and i[-2:] == 'f1':
        tf1 = cp.Variable(boolean=True)
        variable['tf1'] = tf1
    
    if i[0] == 't' and i[-2:] == 'f2':
        tf2 = cp.Variable(boolean=True)
        variable['tf2'] = tf2

    if i[0] == 't' and i[-2:] == 'f3':
        tf3 = cp.Variable(boolean=True)
        variable['tf3'] = tf3

    if i[0] == 't' and i[-2:] == 'f4':
        tf4 = cp.Variable(boolean=True)
        variable['tf4'] = tf4

    if i[0] == 't' and i[-2:] == 'f5':
        tf5 = cp.Variable(boolean=True)
        variable['tf5'] = tf5

    if i[0] == 'u' and i[-2:] == 'm1':
        um1 = cp.Variable(boolean=True)
        variable['um1'] = um1
    
    if i[0] == 'u' and i[-2:] == 'm2':
        um2 = cp.Variable(boolean=True)
        variable['um2'] = um2

    if i[0] == 'u' and i[-2:] == 'm3':
        um3 = cp.Variable(boolean=True)
        variable['um3'] = um3

    if i[0] == 'u' and i[-2:] == 'm4':
        um4 = cp.Variable(boolean=True)
        variable['um4'] = um4

    if i[0] == 'u' and i[-2:] == 'm5':
        um5 = cp.Variable(boolean=True)
        variable['um5'] = um5

    if i[0] == 'u' and i[-2:] == 't1':
        ut1 = cp.Variable(boolean=True)
        variable['ut1'] = ut1
    
    if i[0] == 'u' and i[-2:] == 't2':
        ut2 = cp.Variable(boolean=True)
        variable['ut2'] = ut2

    if i[0] == 'u' and i[-2:] == 't3':
        ut3 = cp.Variable(boolean=True)
        variable['ut3'] = ut3

    if i[0] == 'u' and i[-2:] == 't4':
        ut4 = cp.Variable(boolean=True)
        variable['ut4'] = ut4

    if i[0] == 'u' and i[-2:] == 't5':
        ut5 = cp.Variable(boolean=True)
        variable['ut5'] = ut5

    if i[0] == 'u' and i[-2:] == 'w1':
        uw1 = cp.Variable(boolean=True)
        variable['uw1'] = uw1
    
    if i[0] == 'u' and i[-2:] == 'w2':
        uw2 = cp.Variable(boolean=True)
        variable['uw2'] = uw2

    if i[0] == 'u' and i[-2:] == 'w3':
        uw3 = cp.Variable(boolean=True)
        variable['uw3'] = uw3

    if i[0] == 'u' and i[-2:] == 'w4':
        uw4 = cp.Variable(boolean=True)
        variable['uw4'] = uw4

    if i[0] == 'u' and i[-2:] == 'w5':
        uw5 = cp.Variable(boolean=True)
        variable['uw5'] = uw5

    if i[0] == 'u' and i[-3:] == 'th1':
        uth1 = cp.Variable(boolean=True)
        variable['uth1'] = uth1
    
    if i[0] == 'u' and i[-3:] == 'th2':
        uth2 = cp.Variable(boolean=True)
        variable['uth2'] = uth2

    if i[0] == 'u' and i[-3:] == 'th3':
        uth3 = cp.Variable(boolean=True)
        variable['uth3'] = uth3

    if i[0] == 'u' and i[-3:] == 'th4':
        uth4 = cp.Variable(boolean=True)
        variable['uth4'] = uth4

    if i[0] == 'u' and i[-3:] == 'th5':
        uth5 = cp.Variable(boolean=True)
        variable['uth5'] = uth5

    if i[0] == 'u' and i[-2:] == 'f1':
        uf1 = cp.Variable(boolean=True)
        variable['uf1'] = uf1
    
    if i[0] == 'u' and i[-2:] == 'f2':
        uf2 = cp.Variable(boolean=True)
        variable['uf2'] = uf2

    if i[0] == 'u' and i[-2:] == 'f3':
        uf3 = cp.Variable(boolean=True)
        variable['uf3'] = uf3

    if i[0] == 'u' and i[-2:] == 'f4':
        uf4 = cp.Variable(boolean=True)
        variable['uf4'] = uf4

    if i[0] == 'u' and i[-2:] == 'f5':
        uf5 = cp.Variable(boolean=True)
        variable['uf5'] = uf5

    if i[0] == 'v' and i[-2:] == 'm1':
        vm1 = cp.Variable(boolean=True)
        variable['vm1'] = vm1
    
    if i[0] == 'v' and i[-2:] == 'm2':
        vm2 = cp.Variable(boolean=True)
        variable['vm2'] = vm2

    if i[0] == 'v' and i[-2:] == 'm3':
        vm3 = cp.Variable(boolean=True)
        variable['vm3'] = vm3

    if i[0] == 'v' and i[-2:] == 'm4':
        vm4 = cp.Variable(boolean=True)
        variable['vm4'] = vm4

    if i[0] == 'v' and i[-2:] == 'm5':
        vm5 = cp.Variable(boolean=True)
        variable['vm5'] = vm5

    if i[0] == 'v' and i[-2:] == 't1':
        vt1 = cp.Variable(boolean=True)
        variable['vt1'] = vt1
    
    if i[0] == 'v' and i[-2:] == 't2':
        vt2 = cp.Variable(boolean=True)
        variable['vt2'] = vt2

    if i[0] == 'v' and i[-2:] == 't3':
        vt3 = cp.Variable(boolean=True)
        variable['vt3'] = vt3

    if i[0] == 'v' and i[-2:] == 't4':
        vt4 = cp.Variable(boolean=True)
        variable['vt4'] = vt4

    if i[0] == 'v' and i[-2:] == 't5':
        vt5 = cp.Variable(boolean=True)
        variable['vt5'] = vt5

    if i[0] == 'v' and i[-2:] == 'w1':
        vw1 = cp.Variable(boolean=True)
        variable['vw1'] = vw1
    
    if i[0] == 'v' and i[-2:] == 'w2':
        vw2 = cp.Variable(boolean=True)
        variable['vw2'] = vw2

    if i[0] == 'v' and i[-2:] == 'w3':
        vw3 = cp.Variable(boolean=True)
        variable['vw3'] = vw3

    if i[0] == 'v' and i[-2:] == 'w4':
        vw4 = cp.Variable(boolean=True)
        variable['vw4'] = vw4

    if i[0] == 'v' and i[-2:] == 'w5':
        vw5 = cp.Variable(boolean=True)
        variable['vw5'] = vw5

    if i[0] == 'v' and i[-3:] == 'th1':
        vth1 = cp.Variable(boolean=True)
        variable['vth1'] = vth1
    
    if i[0] == 'v' and i[-3:] == 'th2':
        vth2 = cp.Variable(boolean=True)
        variable['vth2'] = vth2

    if i[0] == 'v' and i[-3:] == 'th3':
        vth3 = cp.Variable(boolean=True)
        variable['vth3'] = vth3

    if i[0] == 'v' and i[-3:] == 'th4':
        vth4 = cp.Variable(boolean=True)
        variable['vth4'] = vth4

    if i[0] == 'v' and i[-3:] == 'th5':
        vth5 = cp.Variable(boolean=True)
        variable['vth5'] = vth5

    if i[0] == 'v' and i[-2:] == 'f1':
        vf1 = cp.Variable(boolean=True)
        variable['vf1'] = vf1
    
    if i[0] == 'v' and i[-2:] == 'f2':
        vf2 = cp.Variable(boolean=True)
        variable['vf2'] = vf2

    if i[0] == 'v' and i[-2:] == 'f3':
        vf3 = cp.Variable(boolean=True)
        variable['vf3'] = vf3

    if i[0] == 'v' and i[-2:] == 'f4':
        vf4 = cp.Variable(boolean=True)
        variable['vf4'] = vf4

    if i[0] == 'v' and i[-2:] == 'f5':
        vf5 = cp.Variable(boolean=True)
        variable['vf5'] = vf5

    if i[0] == 'w' and i[-2:] == 'm1':
        wm1 = cp.Variable(boolean=True)
        variable['wm1'] = wm1
    
    if i[0] == 'w' and i[-2:] == 'm2':
        wm2 = cp.Variable(boolean=True)
        variable['wm2'] = wm2

    if i[0] == 'w' and i[-2:] == 'm3':
        wm3 = cp.Variable(boolean=True)
        variable['wm3'] = wm3

    if i[0] == 'w' and i[-2:] == 'm4':
        wm4 = cp.Variable(boolean=True)
        variable['wm4'] = wm4

    if i[0] == 'w' and i[-2:] == 'm5':
        wm5 = cp.Variable(boolean=True)
        variable['wm5'] = wm5

    if i[0] == 'w' and i[-2:] == 't1':
        wt1 = cp.Variable(boolean=True)
        variable['wt1'] = wt1
    
    if i[0] == 'w' and i[-2:] == 't2':
        wt2 = cp.Variable(boolean=True)
        variable['wt2'] = wt2

    if i[0] == 'w' and i[-2:] == 't3':
        wt3 = cp.Variable(boolean=True)
        variable['wt3'] = wt3

    if i[0] == 'w' and i[-2:] == 't4':
        wt4 = cp.Variable(boolean=True)
        variable['wt4'] = wt4

    if i[0] == 'w' and i[-2:] == 't5':
        wt5 = cp.Variable(boolean=True)
        variable['wt5'] = wt5

    if i[0] == 'w' and i[-2:] == 'w1':
        ww1 = cp.Variable(boolean=True)
        variable['ww1'] = ww1
    
    if i[0] == 'w' and i[-2:] == 'w2':
        ww2 = cp.Variable(boolean=True)
        variable['ww2'] = ww2

    if i[0] == 'w' and i[-2:] == 'w3':
        ww3 = cp.Variable(boolean=True)
        variable['ww3'] = ww3

    if i[0] == 'w' and i[-2:] == 'w4':
        ww4 = cp.Variable(boolean=True)
        variable['ww4'] = ww4

    if i[0] == 'w' and i[-2:] == 'w5':
        ww5 = cp.Variable(boolean=True)
        variable['ww5'] = ww5

    if i[0] == 'w' and i[-3:] == 'th1':
        wth1 = cp.Variable(boolean=True)
        variable['wth1'] = wth1
    
    if i[0] == 'w' and i[-3:] == 'th2':
        wth2 = cp.Variable(boolean=True)
        variable['wth2'] = wth2

    if i[0] == 'w' and i[-3:] == 'th3':
        wth3 = cp.Variable(boolean=True)
        variable['wth3'] = wth3

    if i[0] == 'w' and i[-3:] == 'th4':
        wth4 = cp.Variable(boolean=True)
        variable['wth4'] = wth4

    if i[0] == 'w' and i[-3:] == 'th5':
        wth5 = cp.Variable(boolean=True)
        variable['wth5'] = wth5

    if i[0] == 'w' and i[-2:] == 'f1':
        wf1 = cp.Variable(boolean=True)
        variable['wf1'] = wf1
    
    if i[0] == 'w' and i[-2:] == 'f2':
        wf2 = cp.Variable(boolean=True)
        variable['wf2'] = wf2

    if i[0] == 'w' and i[-2:] == 'f3':
        wf3 = cp.Variable(boolean=True)
        variable['wf3'] = wf3

    if i[0] == 'w' and i[-2:] == 'f4':
        wf4 = cp.Variable(boolean=True)
        variable['wf4'] = wf4

    if i[0] == 'w' and i[-2:] == 'f5':
        wf5 = cp.Variable(boolean=True)
        variable['wf5'] = wf5

    if i[0] == 'x' and i[-2:] == 'm1':
        xm1 = cp.Variable(boolean=True)
        variable['xm1'] = xm1
    
    if i[0] == 'x' and i[-2:] == 'm2':
        xm2 = cp.Variable(boolean=True)
        variable['xm2'] = xm2

    if i[0] == 'x' and i[-2:] == 'm3':
        xm3 = cp.Variable(boolean=True)
        variable['xm3'] = xm3

    if i[0] == 'x' and i[-2:] == 'm4':
        xm4 = cp.Variable(boolean=True)
        variable['xm4'] = xm4

    if i[0] == 'x' and i[-2:] == 'm5':
        xm5 = cp.Variable(boolean=True)
        variable['xm5'] = xm5

    if i[0] == 'x' and i[-2:] == 't1':
        xt1 = cp.Variable(boolean=True)
        variable['xt1'] = xt1
    
    if i[0] == 'x' and i[-2:] == 't2':
        xt2 = cp.Variable(boolean=True)
        variable['xt2'] = xt2

    if i[0] == 'x' and i[-2:] == 't3':
        xt3 = cp.Variable(boolean=True)
        variable['xt3'] = xt3

    if i[0] == 'x' and i[-2:] == 't4':
        xt4 = cp.Variable(boolean=True)
        variable['xt4'] = xt4

    if i[0] == 'x' and i[-2:] == 't5':
        xt5 = cp.Variable(boolean=True)
        variable['xt5'] = xt5

    if i[0] == 'x' and i[-2:] == 'w1':
        xw1 = cp.Variable(boolean=True)
        variable['xw1'] = xw1
    
    if i[0] == 'x' and i[-2:] == 'w2':
        xw2 = cp.Variable(boolean=True)
        variable['xw2'] = xw2

    if i[0] == 'x' and i[-2:] == 'w3':
        xw3 = cp.Variable(boolean=True)
        variable['xw3'] = xw3

    if i[0] == 'x' and i[-2:] == 'w4':
        xw4 = cp.Variable(boolean=True)
        variable['xw4'] = xw4

    if i[0] == 'x' and i[-2:] == 'w5':
        xw5 = cp.Variable(boolean=True)
        variable['xw5'] = xw5

    if i[0] == 'x' and i[-3:] == 'th1':
        xth1 = cp.Variable(boolean=True)
        variable['xth1'] = xth1
    
    if i[0] == 'x' and i[-3:] == 'th2':
        xth2 = cp.Variable(boolean=True)
        variable['xth2'] = xth2

    if i[0] == 'x' and i[-3:] == 'th3':
        xth3 = cp.Variable(boolean=True)
        variable['xth3'] = xth3

    if i[0] == 'x' and i[-3:] == 'th4':
        xth4 = cp.Variable(boolean=True)
        variable['xth4'] = xth4

    if i[0] == 'x' and i[-3:] == 'th5':
        xth5 = cp.Variable(boolean=True)
        variable['xth5'] = xth5

    if i[0] == 'x' and i[-2:] == 'f1':
        xf1 = cp.Variable(boolean=True)
        variable['xf1'] = xf1
    
    if i[0] == 'x' and i[-2:] == 'f2':
        xf2 = cp.Variable(boolean=True)
        variable['xf2'] = xf2

    if i[0] == 'x' and i[-2:] == 'f3':
        xf3 = cp.Variable(boolean=True)
        variable['xf3'] = xf3

    if i[0] == 'x' and i[-2:] == 'f4':
        xf4 = cp.Variable(boolean=True)
        variable['xf4'] = xf4

    if i[0] == 'x' and i[-2:] == 'f5':
        xf5 = cp.Variable(boolean=True)
        variable['xf5'] = xf5

    if i[0] == 'y' and i[-2:] == 'm1':
        ym1 = cp.Variable(boolean=True)
        variable['ym1'] = ym1
    
    if i[0] == 'y' and i[-2:] == 'm2':
        ym2 = cp.Variable(boolean=True)
        variable['ym2'] = ym2

    if i[0] == 'y' and i[-2:] == 'm3':
        ym3 = cp.Variable(boolean=True)
        variable['ym3'] = ym3

    if i[0] == 'y' and i[-2:] == 'm4':
        ym4 = cp.Variable(boolean=True)
        variable['ym4'] = ym4

    if i[0] == 'y' and i[-2:] == 'm5':
        ym5 = cp.Variable(boolean=True)
        variable['ym5'] = ym5

    if i[0] == 'y' and i[-2:] == 't1':
        yt1 = cp.Variable(boolean=True)
        variable['yt1'] = yt1
    
    if i[0] == 'y' and i[-2:] == 't2':
        yt2 = cp.Variable(boolean=True)
        variable['yt2'] = yt2

    if i[0] == 'y' and i[-2:] == 't3':
        yt3 = cp.Variable(boolean=True)
        variable['yt3'] = yt3

    if i[0] == 'y' and i[-2:] == 't4':
        yt4 = cp.Variable(boolean=True)
        variable['yt4'] = yt4

    if i[0] == 'y' and i[-2:] == 't5':
        yt5 = cp.Variable(boolean=True)
        variable['yt5'] = yt5

    if i[0] == 'y' and i[-2:] == 'w1':
        yw1 = cp.Variable(boolean=True)
        variable['yw1'] = yw1
    
    if i[0] == 'y' and i[-2:] == 'w2':
        yw2 = cp.Variable(boolean=True)
        variable['yw2'] = yw2

    if i[0] == 'y' and i[-2:] == 'w3':
        yw3 = cp.Variable(boolean=True)
        variable['yw3'] = yw3

    if i[0] == 'y' and i[-2:] == 'w4':
        yw4 = cp.Variable(boolean=True)
        variable['yw4'] = yw4

    if i[0] == 'y' and i[-2:] == 'w5':
        yw5 = cp.Variable(boolean=True)
        variable['yw5'] = yw5

    if i[0] == 'y' and i[-3:] == 'th1':
        yth1 = cp.Variable(boolean=True)
        variable['yth1'] = yth1
    
    if i[0] == 'y' and i[-3:] == 'th2':
        yth2 = cp.Variable(boolean=True)
        variable['yth2'] = yth2

    if i[0] == 'y' and i[-3:] == 'th3':
        yth3 = cp.Variable(boolean=True)
        variable['yth3'] = yth3

    if i[0] == 'y' and i[-3:] == 'th4':
        yth4 = cp.Variable(boolean=True)
        variable['yth4'] = yth4

    if i[0] == 'y' and i[-3:] == 'th5':
        yth5 = cp.Variable(boolean=True)
        variable['yth5'] = yth5

    if i[0] == 'y' and i[-2:] == 'f1':
        yf1 = cp.Variable(boolean=True)
        variable['yf1'] = yf1
    
    if i[0] == 'y' and i[-2:] == 'f2':
        yf2 = cp.Variable(boolean=True)
        variable['yf2'] = yf2

    if i[0] == 'y' and i[-2:] == 'f3':
        yf3 = cp.Variable(boolean=True)
        variable['yf3'] = yf3

    if i[0] == 'y' and i[-2:] == 'f4':
        yf4 = cp.Variable(boolean=True)
        variable['yf4'] = yf4

    if i[0] == 'y' and i[-2:] == 'f5':
        yf5 = cp.Variable(boolean=True)
        variable['yf5'] = yf5

    if i[0] == 'A' and i[-2:] == 'm1':
        Am1 = cp.Variable(boolean=True)
        variable['Am1'] = Am1
    
    if i[0] == 'A' and i[-2:] == 'm2':
        Am2 = cp.Variable(boolean=True)
        variable['Am2'] = Am2

    if i[0] == 'A' and i[-2:] == 'm3':
        Am3 = cp.Variable(boolean=True)
        variable['Am3'] = Am3

    if i[0] == 'A' and i[-2:] == 'm4':
        Am4 = cp.Variable(boolean=True)
        variable['Am4'] = Am4

    if i[0] == 'A' and i[-2:] == 'm5':
        Am5 = cp.Variable(boolean=True)
        variable['Am5'] = Am5

    if i[0] == 'A' and i[-2:] == 't1':
        At1 = cp.Variable(boolean=True)
        variable['At1'] = At1
    
    if i[0] == 'A' and i[-2:] == 't2':
        At2 = cp.Variable(boolean=True)
        variable['At2'] = At2

    if i[0] == 'A' and i[-2:] == 't3':
        At3 = cp.Variable(boolean=True)
        variable['At3'] = At3

    if i[0] == 'A' and i[-2:] == 't4':
        At4 = cp.Variable(boolean=True)
        variable['At4'] = At4

    if i[0] == 'A' and i[-2:] == 't5':
        At5 = cp.Variable(boolean=True)
        variable['At5'] = At5

    if i[0] == 'A' and i[-2:] == 'w1':
        Aw1 = cp.Variable(boolean=True)
        variable['Aw1'] = Aw1
    
    if i[0] == 'A' and i[-2:] == 'w2':
        Aw2 = cp.Variable(boolean=True)
        variable['Aw2'] = Aw2

    if i[0] == 'A' and i[-2:] == 'w3':
        Aw3 = cp.Variable(boolean=True)
        variable['Aw3'] = Aw3

    if i[0] == 'A' and i[-2:] == 'w4':
        Aw4 = cp.Variable(boolean=True)
        variable['Aw4'] = Aw4

    if i[0] == 'A' and i[-2:] == 'w5':
        Aw5 = cp.Variable(boolean=True)
        variable['Aw5'] = Aw5

    if i[0] == 'A' and i[-3:] == 'th1':
        Ath1 = cp.Variable(boolean=True)
        variable['Ath1'] = Ath1
    
    if i[0] == 'A' and i[-3:] == 'th2':
        Ath2 = cp.Variable(boolean=True)
        variable['Ath2'] = Ath2

    if i[0] == 'A' and i[-3:] == 'th3':
        Ath3 = cp.Variable(boolean=True)
        variable['Ath3'] = Ath3

    if i[0] == 'A' and i[-3:] == 'th4':
        Ath4 = cp.Variable(boolean=True)
        variable['Ath4'] = Ath4

    if i[0] == 'A' and i[-3:] == 'th5':
        Ath5 = cp.Variable(boolean=True)
        variable['Ath5'] = Ath5

    if i[0] == 'A' and i[-2:] == 'f1':
        Af1 = cp.Variable(boolean=True)
        variable['Af1'] = Af1
    
    if i[0] == 'A' and i[-2:] == 'f2':
        Af2 = cp.Variable(boolean=True)
        variable['Af2'] = Af2

    if i[0] == 'A' and i[-2:] == 'f3':
        Af3 = cp.Variable(boolean=True)
        variable['Af3'] = Af3

    if i[0] == 'A' and i[-2:] == 'f4':
        Af4 = cp.Variable(boolean=True)
        variable['Af4'] = Af4

    if i[0] == 'A' and i[-2:] == 'f5':
        Af5 = cp.Variable(boolean=True)
        variable['Af5'] = Af5

    if i[0] == 'B' and i[-2:] == 'm1':
        Bm1 = cp.Variable(boolean=True)
        variable['Bm1'] = Bm1
    
    if i[0] == 'B' and i[-2:] == 'm2':
        Bm2 = cp.Variable(boolean=True)
        variable['Bm2'] = Bm2

    if i[0] == 'B' and i[-2:] == 'm3':
        Bm3 = cp.Variable(boolean=True)
        variable['Bm3'] = Bm3

    if i[0] == 'B' and i[-2:] == 'm4':
        Bm4 = cp.Variable(boolean=True)
        variable['Bm4'] = Bm4

    if i[0] == 'B' and i[-2:] == 'm5':
        Bm5 = cp.Variable(boolean=True)
        variable['Bm5'] = Bm5

    if i[0] == 'B' and i[-2:] == 't1':
        Bt1 = cp.Variable(boolean=True)
        variable['Bt1'] = Bt1
    
    if i[0] == 'B' and i[-2:] == 't2':
        Bt2 = cp.Variable(boolean=True)
        variable['Bt2'] = Bt2

    if i[0] == 'B' and i[-2:] == 't3':
        Bt3 = cp.Variable(boolean=True)
        variable['Bt3'] = Bt3

    if i[0] == 'B' and i[-2:] == 't4':
        Bt4 = cp.Variable(boolean=True)
        variable['Bt4'] = Bt4

    if i[0] == 'B' and i[-2:] == 't5':
        Bt5 = cp.Variable(boolean=True)
        variable['Bt5'] = Bt5

    if i[0] == 'B' and i[-2:] == 'w1':
        Bw1 = cp.Variable(boolean=True)
        variable['Bw1'] = Bw1
    
    if i[0] == 'B' and i[-2:] == 'w2':
        Bw2 = cp.Variable(boolean=True)
        variable['Bw2'] = Bw2

    if i[0] == 'B' and i[-2:] == 'w3':
        Bw3 = cp.Variable(boolean=True)
        variable['Bw3'] = Bw3

    if i[0] == 'B' and i[-2:] == 'w4':
        Bw4 = cp.Variable(boolean=True)
        variable['Bw4'] = Bw4

    if i[0] == 'B' and i[-2:] == 'w5':
        Bw5 = cp.Variable(boolean=True)
        variable['Bw5'] = Bw5

    if i[0] == 'B' and i[-3:] == 'th1':
        Bth1 = cp.Variable(boolean=True)
        variable['Bth1'] = Bth1
    
    if i[0] == 'B' and i[-3:] == 'th2':
        Bth2 = cp.Variable(boolean=True)
        variable['Bth2'] = Bth2

    if i[0] == 'B' and i[-3:] == 'th3':
        Bth3 = cp.Variable(boolean=True)
        variable['Bth3'] = Bth3

    if i[0] == 'B' and i[-3:] == 'th4':
        Bth4 = cp.Variable(boolean=True)
        variable['Bth4'] = Bth4

    if i[0] == 'B' and i[-3:] == 'th5':
        Bth5 = cp.Variable(boolean=True)
        variable['Bth5'] = Bth5

    if i[0] == 'B' and i[-2:] == 'f1':
        Bf1 = cp.Variable(boolean=True)
        variable['Bf1'] = Bf1
    
    if i[0] == 'B' and i[-2:] == 'f2':
        Bf2 = cp.Variable(boolean=True)
        variable['Bf2'] = Bf2

    if i[0] == 'B' and i[-2:] == 'f3':
        Bf3 = cp.Variable(boolean=True)
        variable['Bf3'] = Bf3

    if i[0] == 'B' and i[-2:] == 'f4':
        Bf4 = cp.Variable(boolean=True)
        variable['Bf4'] = Bf4

    if i[0] == 'B' and i[-2:] == 'f5':
        Bf5 = cp.Variable(boolean=True)
        variable['Bf5'] = Bf5

    if i[0] == 'C' and i[-2:] == 'm1':
        Cm1 = cp.Variable(boolean=True)
        variable['Cm1'] = Cm1
    
    if i[0] == 'C' and i[-2:] == 'm2':
        Cm2 = cp.Variable(boolean=True)
        variable['Cm2'] = Cm2

    if i[0] == 'C' and i[-2:] == 'm3':
        Cm3 = cp.Variable(boolean=True)
        variable['Cm3'] = Cm3

    if i[0] == 'C' and i[-2:] == 'm4':
        Cm4 = cp.Variable(boolean=True)
        variable['Cm4'] = Cm4

    if i[0] == 'C' and i[-2:] == 'm5':
        Cm5 = cp.Variable(boolean=True)
        variable['Cm5'] = Cm5

    if i[0] == 'C' and i[-2:] == 't1':
        Ct1 = cp.Variable(boolean=True)
        variable['Ct1'] = Ct1
    
    if i[0] == 'C' and i[-2:] == 't2':
        Ct2 = cp.Variable(boolean=True)
        variable['Ct2'] = Ct2

    if i[0] == 'C' and i[-2:] == 't3':
        Ct3 = cp.Variable(boolean=True)
        variable['Ct3'] = Ct3

    if i[0] == 'C' and i[-2:] == 't4':
        Ct4 = cp.Variable(boolean=True)
        variable['Ct4'] = Ct4

    if i[0] == 'C' and i[-2:] == 't5':
        Ct5 = cp.Variable(boolean=True)
        variable['Ct5'] = Ct5

    if i[0] == 'C' and i[-2:] == 'w1':
        Cw1 = cp.Variable(boolean=True)
        variable['Cw1'] = Cw1
    
    if i[0] == 'C' and i[-2:] == 'w2':
        Cw2 = cp.Variable(boolean=True)
        variable['Cw2'] = Cw2

    if i[0] == 'C' and i[-2:] == 'w3':
        Cw3 = cp.Variable(boolean=True)
        variable['Cw3'] = Cw3

    if i[0] == 'C' and i[-2:] == 'w4':
        Cw4 = cp.Variable(boolean=True)
        variable['Cw4'] = Cw4

    if i[0] == 'C' and i[-2:] == 'w5':
        Cw5 = cp.Variable(boolean=True)
        variable['Cw5'] = Cw5

    if i[0] == 'C' and i[-3:] == 'th1':
        Cth1 = cp.Variable(boolean=True)
        variable['Cth1'] = Cth1
    
    if i[0] == 'C' and i[-3:] == 'th2':
        Cth2 = cp.Variable(boolean=True)
        variable['Cth2'] = Cth2

    if i[0] == 'C' and i[-3:] == 'th3':
        Cth3 = cp.Variable(boolean=True)
        variable['Cth3'] = Cth3

    if i[0] == 'C' and i[-3:] == 'th4':
        Cth4 = cp.Variable(boolean=True)
        variable['Cth4'] = Cth4

    if i[0] == 'C' and i[-3:] == 'th5':
        Cth5 = cp.Variable(boolean=True)
        variable['Cth5'] = Cth5

    if i[0] == 'C' and i[-2:] == 'f1':
        Cf1 = cp.Variable(boolean=True)
        variable['Cf1'] = Cf1
    
    if i[0] == 'C' and i[-2:] == 'f2':
        Cf2 = cp.Variable(boolean=True)
        variable['Cf2'] = Cf2

    if i[0] == 'C' and i[-2:] == 'f3':
        Cf3 = cp.Variable(boolean=True)
        variable['Cf3'] = Cf3

    if i[0] == 'C' and i[-2:] == 'f4':
        Cf4 = cp.Variable(boolean=True)
        variable['Cf4'] = Cf4

    if i[0] == 'C' and i[-2:] == 'f5':
        Cf5 = cp.Variable(boolean=True)
        variable['Cf5'] = Cf5
        
    if i[0] == 'D' and i[-2:] == 'm1':
        Dm1 = cp.Variable(boolean=True)
        variable['Dm1'] = Dm1
    
    if i[0] == 'D' and i[-2:] == 'm2':
        Dm2 = cp.Variable(boolean=True)
        variable['Dm2'] = Dm2

    if i[0] == 'D' and i[-2:] == 'm3':
        Dm3 = cp.Variable(boolean=True)
        variable['Dm3'] = Dm3

    if i[0] == 'D' and i[-2:] == 'm4':
        Dm4 = cp.Variable(boolean=True)
        variable['Dm4'] = Dm4

    if i[0] == 'D' and i[-2:] == 'm5':
        Dm5 = cp.Variable(boolean=True)
        variable['Dm5'] = Dm5

    if i[0] == 'D' and i[-2:] == 't1':
        Dt1 = cp.Variable(boolean=True)
        variable['Dt1'] = Dt1
    
    if i[0] == 'D' and i[-2:] == 't2':
        Dt2 = cp.Variable(boolean=True)
        variable['Dt2'] = Dt2

    if i[0] == 'D' and i[-2:] == 't3':
        Dt3 = cp.Variable(boolean=True)
        variable['Dt3'] = Dt3

    if i[0] == 'D' and i[-2:] == 't4':
        Dt4 = cp.Variable(boolean=True)
        variable['Dt4'] = Dt4

    if i[0] == 'D' and i[-2:] == 't5':
        Dt5 = cp.Variable(boolean=True)
        variable['Dt5'] = Dt5

    if i[0] == 'D' and i[-2:] == 'w1':
        Dw1 = cp.Variable(boolean=True)
        variable['Dw1'] = Dw1
    
    if i[0] == 'D' and i[-2:] == 'w2':
        Dw2 = cp.Variable(boolean=True)
        variable['Dw2'] = Dw2

    if i[0] == 'D' and i[-2:] == 'w3':
        Dw3 = cp.Variable(boolean=True)
        variable['Dw3'] = Dw3

    if i[0] == 'D' and i[-2:] == 'w4':
        Dw4 = cp.Variable(boolean=True)
        variable['Dw4'] = Dw4

    if i[0] == 'D' and i[-2:] == 'w5':
        Dw5 = cp.Variable(boolean=True)
        variable['Dw5'] = Dw5

    if i[0] == 'D' and i[-3:] == 'th1':
        Dth1 = cp.Variable(boolean=True)
        variable['Dth1'] = Dth1
    
    if i[0] == 'D' and i[-3:] == 'th2':
        Dth2 = cp.Variable(boolean=True)
        variable['Dth2'] = Dth2

    if i[0] == 'D' and i[-3:] == 'th3':
        Dth3 = cp.Variable(boolean=True)
        variable['Dth3'] = Dth3

    if i[0] == 'D' and i[-3:] == 'th4':
        Dth4 = cp.Variable(boolean=True)
        variable['Dth4'] = Dth4

    if i[0] == 'D' and i[-3:] == 'th5':
        Dth5 = cp.Variable(boolean=True)
        variable['Dth5'] = Dth5

    if i[0] == 'D' and i[-2:] == 'f1':
        Df1 = cp.Variable(boolean=True)
        variable['Df1'] = Df1
    
    if i[0] == 'D' and i[-2:] == 'f2':
        Df2 = cp.Variable(boolean=True)
        variable['Df2'] = Df2

    if i[0] == 'D' and i[-2:] == 'f3':
        Df3 = cp.Variable(boolean=True)
        variable['Df3'] = Df3

    if i[0] == 'D' and i[-2:] == 'f4':
        Df4 = cp.Variable(boolean=True)
        variable['Df4'] = Df4

    if i[0] == 'D' and i[-2:] == 'f5':
        Df5 = cp.Variable(boolean=True)
        variable['Df5'] = Df5

    if i[0] == 'E' and i[-2:] == 'm1':
        Em1 = cp.Variable(boolean=True)
        variable['Em1'] = Em1
    
    if i[0] == 'E' and i[-2:] == 'm2':
        Em2 = cp.Variable(boolean=True)
        variable['Em2'] = Em2

    if i[0] == 'E' and i[-2:] == 'm3':
        Em3 = cp.Variable(boolean=True)
        variable['Em3'] = Em3

    if i[0] == 'E' and i[-2:] == 'm4':
        Em4 = cp.Variable(boolean=True)
        variable['Em4'] = Em4

    if i[0] == 'E' and i[-2:] == 'm5':
        Em5 = cp.Variable(boolean=True)
        variable['Em5'] = Em5

    if i[0] == 'E' and i[-2:] == 't1':
        Et1 = cp.Variable(boolean=True)
        variable['Et1'] = Et1
    
    if i[0] == 'E' and i[-2:] == 't2':
        Et2 = cp.Variable(boolean=True)
        variable['Et2'] = Et2

    if i[0] == 'E' and i[-2:] == 't3':
        Et3 = cp.Variable(boolean=True)
        variable['Et3'] = Et3

    if i[0] == 'E' and i[-2:] == 't4':
        Et4 = cp.Variable(boolean=True)
        variable['Et4'] = Et4

    if i[0] == 'E' and i[-2:] == 't5':
        Et5 = cp.Variable(boolean=True)
        variable['Et5'] = Et5

    if i[0] == 'E' and i[-2:] == 'w1':
        Ew1 = cp.Variable(boolean=True)
        variable['Ew1'] = Ew1
    
    if i[0] == 'E' and i[-2:] == 'w2':
        Ew2 = cp.Variable(boolean=True)
        variable['Ew2'] = Ew2

    if i[0] == 'E' and i[-2:] == 'w3':
        Ew3 = cp.Variable(boolean=True)
        variable['Ew3'] = Ew3

    if i[0] == 'E' and i[-2:] == 'w4':
        Ew4 = cp.Variable(boolean=True)
        variable['Ew4'] = Ew4

    if i[0] == 'E' and i[-2:] == 'w5':
        Ew5 = cp.Variable(boolean=True)
        variable['Ew5'] = Ew5

    if i[0] == 'E' and i[-3:] == 'th1':
        Eth1 = cp.Variable(boolean=True)
        variable['Eth1'] = Eth1
    
    if i[0] == 'E' and i[-3:] == 'th2':
        Eth2 = cp.Variable(boolean=True)
        variable['Eth2'] = Eth2

    if i[0] == 'E' and i[-3:] == 'th3':
        Eth3 = cp.Variable(boolean=True)
        variable['Eth3'] = Eth3

    if i[0] == 'E' and i[-3:] == 'th4':
        Eth4 = cp.Variable(boolean=True)
        variable['Eth4'] = Eth4

    if i[0] == 'E' and i[-3:] == 'th5':
        Eth5 = cp.Variable(boolean=True)
        variable['Eth5'] = Eth5

    if i[0] == 'E' and i[-2:] == 'f1':
        Ef1 = cp.Variable(boolean=True)
        variable['Ef1'] = Ef1
    
    if i[0] == 'E' and i[-2:] == 'f2':
        Ef2 = cp.Variable(boolean=True)
        variable['Ef2'] = Ef2

    if i[0] == 'E' and i[-2:] == 'f3':
        Ef3 = cp.Variable(boolean=True)
        variable['Ef3'] = Ef3

    if i[0] == 'E' and i[-2:] == 'f4':
        Ef4 = cp.Variable(boolean=True)
        variable['Ef4'] = Ef4

    if i[0] == 'E' and i[-2:] == 'f5':
        Ef5 = cp.Variable(boolean=True)
        variable['Ef5'] = Ef5

    if i[0] == 'F' and i[-2:] == 'm1':
        Fm1 = cp.Variable(boolean=True)
        variable['Fm1'] = Fm1
    
    if i[0] == 'F' and i[-2:] == 'm2':
        Fm2 = cp.Variable(boolean=True)
        variable['Fm2'] = Fm2

    if i[0] == 'F' and i[-2:] == 'm3':
        Fm3 = cp.Variable(boolean=True)
        variable['Fm3'] = Fm3

    if i[0] == 'F' and i[-2:] == 'm4':
        Fm4 = cp.Variable(boolean=True)
        variable['Fm4'] = Fm4

    if i[0] == 'F' and i[-2:] == 'm5':
        Fm5 = cp.Variable(boolean=True)
        variable['Fm5'] = Fm5

    if i[0] == 'F' and i[-2:] == 't1':
        Ft1 = cp.Variable(boolean=True)
        variable['Ft1'] = Ft1
    
    if i[0] == 'F' and i[-2:] == 't2':
        Ft2 = cp.Variable(boolean=True)
        variable['Ft2'] = Ft2

    if i[0] == 'F' and i[-2:] == 't3':
        Ft3 = cp.Variable(boolean=True)
        variable['Ft3'] = Ft3

    if i[0] == 'F' and i[-2:] == 't4':
        Ft4 = cp.Variable(boolean=True)
        variable['Ft4'] = Ft4

    if i[0] == 'F' and i[-2:] == 't5':
        Ft5 = cp.Variable(boolean=True)
        variable['Ft5'] = Ft5

    if i[0] == 'F' and i[-2:] == 'w1':
        Fw1 = cp.Variable(boolean=True)
        variable['Fw1'] = Fw1
    
    if i[0] == 'F' and i[-2:] == 'w2':
        Fw2 = cp.Variable(boolean=True)
        variable['Fw2'] = Fw2

    if i[0] == 'F' and i[-2:] == 'w3':
        Fw3 = cp.Variable(boolean=True)
        variable['Fw3'] = Fw3

    if i[0] == 'F' and i[-2:] == 'w4':
        Fw4 = cp.Variable(boolean=True)
        variable['Fw4'] = Fw4

    if i[0] == 'F' and i[-2:] == 'w5':
        Fw5 = cp.Variable(boolean=True)
        variable['Fw5'] = Fw5

    if i[0] == 'F' and i[-3:] == 'th1':
        Fth1 = cp.Variable(boolean=True)
        variable['Fth1'] = Fth1
    
    if i[0] == 'F' and i[-3:] == 'th2':
        Fth2 = cp.Variable(boolean=True)
        variable['Fth2'] = Fth2

    if i[0] == 'F' and i[-3:] == 'th3':
        Fth3 = cp.Variable(boolean=True)
        variable['Fth3'] = Fth3

    if i[0] == 'F' and i[-3:] == 'th4':
        Fth4 = cp.Variable(boolean=True)
        variable['Fth4'] = Fth4

    if i[0] == 'F' and i[-3:] == 'th5':
        Fth5 = cp.Variable(boolean=True)
        variable['Fth5'] = Fth5

    if i[0] == 'F' and i[-2:] == 'f1':
        Ff1 = cp.Variable(boolean=True)
        variable['Ff1'] = Ff1
    
    if i[0] == 'F' and i[-2:] == 'f2':
        Ff2 = cp.Variable(boolean=True)
        variable['Ff2'] = Ff2

    if i[0] == 'F' and i[-2:] == 'f3':
        Ff3 = cp.Variable(boolean=True)
        variable['Ff3'] = Ff3

    if i[0] == 'F' and i[-2:] == 'f4':
        Ff4 = cp.Variable(boolean=True)
        variable['Ff4'] = Ff4

    if i[0] == 'F' and i[-2:] == 'f5':
        Ff5 = cp.Variable(boolean=True)
        variable['Ff5'] = Ff5

    if i[0] == 'G' and i[-2:] == 'm1':
        Gm1 = cp.Variable(boolean=True)
        variable['Gm1'] = Gm1
    
    if i[0] == 'G' and i[-2:] == 'm2':
        Gm2 = cp.Variable(boolean=True)
        variable['Gm2'] = Gm2

    if i[0] == 'G' and i[-2:] == 'm3':
        Gm3 = cp.Variable(boolean=True)
        variable['Gm3'] = Gm3

    if i[0] == 'G' and i[-2:] == 'm4':
        Gm4 = cp.Variable(boolean=True)
        variable['Gm4'] = Gm4

    if i[0] == 'G' and i[-2:] == 'm5':
        Gm5 = cp.Variable(boolean=True)
        variable['Gm5'] = Gm5

    if i[0] == 'G' and i[-2:] == 't1':
        Gt1 = cp.Variable(boolean=True)
        variable['Gt1'] = Gt1
    
    if i[0] == 'G' and i[-2:] == 't2':
        Gt2 = cp.Variable(boolean=True)
        variable['Gt2'] = Gt2

    if i[0] == 'G' and i[-2:] == 't3':
        Gt3 = cp.Variable(boolean=True)
        variable['Gt3'] = Gt3

    if i[0] == 'G' and i[-2:] == 't4':
        Gt4 = cp.Variable(boolean=True)
        variable['Gt4'] = Gt4

    if i[0] == 'G' and i[-2:] == 't5':
        Gt5 = cp.Variable(boolean=True)
        variable['Gt5'] = Gt5

    if i[0] == 'G' and i[-2:] == 'w1':
        Gw1 = cp.Variable(boolean=True)
        variable['Gw1'] = Gw1
    
    if i[0] == 'G' and i[-2:] == 'w2':
        Gw2 = cp.Variable(boolean=True)
        variable['Gw2'] = Gw2

    if i[0] == 'G' and i[-2:] == 'w3':
        Gw3 = cp.Variable(boolean=True)
        variable['Gw3'] = Gw3

    if i[0] == 'G' and i[-2:] == 'w4':
        Gw4 = cp.Variable(boolean=True)
        variable['Gw4'] = Gw4

    if i[0] == 'G' and i[-2:] == 'w5':
        Gw5 = cp.Variable(boolean=True)
        variable['Gw5'] = Gw5

    if i[0] == 'G' and i[-3:] == 'th1':
        Gth1 = cp.Variable(boolean=True)
        variable['Gth1'] = Gth1
    
    if i[0] == 'G' and i[-3:] == 'th2':
        Gth2 = cp.Variable(boolean=True)
        variable['Gth2'] = Gth2

    if i[0] == 'G' and i[-3:] == 'th3':
        Gth3 = cp.Variable(boolean=True)
        variable['Gth3'] = Gth3

    if i[0] == 'G' and i[-3:] == 'th4':
        Gth4 = cp.Variable(boolean=True)
        variable['Gth4'] = Gth4

    if i[0] == 'G' and i[-3:] == 'th5':
        Gth5 = cp.Variable(boolean=True)
        variable['Gth5'] = Gth5

    if i[0] == 'G' and i[-2:] == 'f1':
        Gf1 = cp.Variable(boolean=True)
        variable['Gf1'] = Gf1
    
    if i[0] == 'G' and i[-2:] == 'f2':
        Gf2 = cp.Variable(boolean=True)
        variable['Gf2'] = Gf2

    if i[0] == 'G' and i[-2:] == 'f3':
        Gf3 = cp.Variable(boolean=True)
        variable['Gf3'] = Gf3

    if i[0] == 'G' and i[-2:] == 'f4':
        Gf4 = cp.Variable(boolean=True)
        variable['Gf4'] = Gf4

    if i[0] == 'G' and i[-2:] == 'f5':
        Gf5 = cp.Variable(boolean=True)
        variable['Gf5'] = Gf5

    if i[0] == 'H' and i[-2:] == 'm1':
        Hm1 = cp.Variable(boolean=True)
        variable['Hm1'] = Hm1
    
    if i[0] == 'H' and i[-2:] == 'm2':
        Hm2 = cp.Variable(boolean=True)
        variable['Hm2'] = Hm2

    if i[0] == 'H' and i[-2:] == 'm3':
        Hm3 = cp.Variable(boolean=True)
        variable['Hm3'] = Hm3

    if i[0] == 'H' and i[-2:] == 'm4':
        Hm4 = cp.Variable(boolean=True)
        variable['Hm4'] = Hm4

    if i[0] == 'H' and i[-2:] == 'm5':
        Hm5 = cp.Variable(boolean=True)
        variable['Hm5'] = Hm5

    if i[0] == 'H' and i[-2:] == 't1':
        Ht1 = cp.Variable(boolean=True)
        variable['Ht1'] = Ht1
    
    if i[0] == 'H' and i[-2:] == 't2':
        Ht2 = cp.Variable(boolean=True)
        variable['Ht2'] = Ht2

    if i[0] == 'H' and i[-2:] == 't3':
        Ht3 = cp.Variable(boolean=True)
        variable['Ht3'] = Ht3

    if i[0] == 'H' and i[-2:] == 't4':
        Ht4 = cp.Variable(boolean=True)
        variable['Ht4'] = Ht4

    if i[0] == 'H' and i[-2:] == 't5':
        Ht5 = cp.Variable(boolean=True)
        variable['Ht5'] = Ht5

    if i[0] == 'H' and i[-2:] == 'w1':
        Hw1 = cp.Variable(boolean=True)
        variable['Hw1'] = Hw1
    
    if i[0] == 'H' and i[-2:] == 'w2':
        Hw2 = cp.Variable(boolean=True)
        variable['Hw2'] = Hw2

    if i[0] == 'H' and i[-2:] == 'w3':
        Hw3 = cp.Variable(boolean=True)
        variable['Hw3'] = Hw3

    if i[0] == 'H' and i[-2:] == 'w4':
        Hw4 = cp.Variable(boolean=True)
        variable['Hw4'] = Hw4

    if i[0] == 'H' and i[-2:] == 'w5':
        Hw5 = cp.Variable(boolean=True)
        variable['Hw5'] = Hw5

    if i[0] == 'H' and i[-3:] == 'th1':
        Hth1 = cp.Variable(boolean=True)
        variable['Hth1'] = Hth1
    
    if i[0] == 'H' and i[-3:] == 'th2':
        Hth2 = cp.Variable(boolean=True)
        variable['Hth2'] = Hth2

    if i[0] == 'H' and i[-3:] == 'th3':
        Hth3 = cp.Variable(boolean=True)
        variable['Hth3'] = Hth3

    if i[0] == 'H' and i[-3:] == 'th4':
        Hth4 = cp.Variable(boolean=True)
        variable['Hth4'] = Hth4

    if i[0] == 'H' and i[-3:] == 'th5':
        Hth5 = cp.Variable(boolean=True)
        variable['Hth5'] = Hth5

    if i[0] == 'H' and i[-2:] == 'f1':
        Hf1 = cp.Variable(boolean=True)
        variable['Hf1'] = Hf1
    
    if i[0] == 'H' and i[-2:] == 'f2':
        Hf2 = cp.Variable(boolean=True)
        variable['Hf2'] = Hf2

    if i[0] == 'H' and i[-2:] == 'f3':
        Hf3 = cp.Variable(boolean=True)
        variable['Hf3'] = Hf3

    if i[0] == 'H' and i[-2:] == 'f4':
        Hf4 = cp.Variable(boolean=True)
        variable['Hf4'] = Hf4

    if i[0] == 'H' and i[-2:] == 'f5':
        Hf5 = cp.Variable(boolean=True)
        variable['Hf5'] = Hf5

    if i[0] == 'I' and i[-2:] == 'm1':
        Im1 = cp.Variable(boolean=True)
        variable['Im1'] = Im1
    
    if i[0] == 'I' and i[-2:] == 'm2':
        Im2 = cp.Variable(boolean=True)
        variable['Im2'] = Im2

    if i[0] == 'I' and i[-2:] == 'm3':
        Im3 = cp.Variable(boolean=True)
        variable['Im3'] = Im3

    if i[0] == 'I' and i[-2:] == 'm4':
        Im4 = cp.Variable(boolean=True)
        variable['Im4'] = Im4

    if i[0] == 'I' and i[-2:] == 'm5':
        Im5 = cp.Variable(boolean=True)
        variable['Im5'] = Im5

    if i[0] == 'I' and i[-2:] == 't1':
        It1 = cp.Variable(boolean=True)
        variable['It1'] = It1
    
    if i[0] == 'I' and i[-2:] == 't2':
        It2 = cp.Variable(boolean=True)
        variable['It2'] = It2

    if i[0] == 'I' and i[-2:] == 't3':
        It3 = cp.Variable(boolean=True)
        variable['It3'] = It3

    if i[0] == 'I' and i[-2:] == 't4':
        It4 = cp.Variable(boolean=True)
        variable['It4'] = It4

    if i[0] == 'I' and i[-2:] == 't5':
        It5 = cp.Variable(boolean=True)
        variable['It5'] = It5

    if i[0] == 'I' and i[-2:] == 'w1':
        Iw1 = cp.Variable(boolean=True)
        variable['Iw1'] = Iw1
    
    if i[0] == 'I' and i[-2:] == 'w2':
        Iw2 = cp.Variable(boolean=True)
        variable['Iw2'] = Iw2

    if i[0] == 'I' and i[-2:] == 'w3':
        Iw3 = cp.Variable(boolean=True)
        variable['Iw3'] = Iw3

    if i[0] == 'I' and i[-2:] == 'w4':
        Iw4 = cp.Variable(boolean=True)
        variable['Iw4'] = Iw4

    if i[0] == 'I' and i[-2:] == 'w5':
        Iw5 = cp.Variable(boolean=True)
        variable['Iw5'] = Iw5

    if i[0] == 'I' and i[-3:] == 'th1':
        Ith1 = cp.Variable(boolean=True)
        variable['Ith1'] = Ith1
    
    if i[0] == 'I' and i[-3:] == 'th2':
        Ith2 = cp.Variable(boolean=True)
        variable['Ith2'] = Ith2

    if i[0] == 'I' and i[-3:] == 'th3':
        Ith3 = cp.Variable(boolean=True)
        variable['Ith3'] = Ith3

    if i[0] == 'I' and i[-3:] == 'th4':
        Ith4 = cp.Variable(boolean=True)
        variable['Ith4'] = Ith4

    if i[0] == 'I' and i[-3:] == 'th5':
        Ith5 = cp.Variable(boolean=True)
        variable['Ith5'] = Ith5

    if i[0] == 'I' and i[-2:] == 'f1':
        If1 = cp.Variable(boolean=True)
        variable['If1'] = If1
    
    if i[0] == 'I' and i[-2:] == 'f2':
        If2 = cp.Variable(boolean=True)
        variable['If2'] = If2

    if i[0] == 'I' and i[-2:] == 'f3':
        If3 = cp.Variable(boolean=True)
        variable['If3'] = If3

    if i[0] == 'I' and i[-2:] == 'f4':
        If4 = cp.Variable(boolean=True)
        variable['If4'] = If4

    if i[0] == 'I' and i[-2:] == 'f5':
        If5 = cp.Variable(boolean=True)
        variable['If5'] = If5

    if i[0] == 'J' and i[-2:] == 'm1':
        Jm1 = cp.Variable(boolean=True)
        variable['Jm1'] = Jm1
    
    if i[0] == 'J' and i[-2:] == 'm2':
        Jm2 = cp.Variable(boolean=True)
        variable['Jm2'] = Jm2

    if i[0] == 'J' and i[-2:] == 'm3':
        Jm3 = cp.Variable(boolean=True)
        variable['Jm3'] = Jm3

    if i[0] == 'J' and i[-2:] == 'm4':
        Jm4 = cp.Variable(boolean=True)
        variable['Jm4'] = Jm4

    if i[0] == 'J' and i[-2:] == 'm5':
        Jm5 = cp.Variable(boolean=True)
        variable['Jm5'] = Jm5

    if i[0] == 'J' and i[-2:] == 't1':
        Jt1 = cp.Variable(boolean=True)
        variable['Jt1'] = Jt1
    
    if i[0] == 'J' and i[-2:] == 't2':
        Jt2 = cp.Variable(boolean=True)
        variable['Jt2'] = Jt2

    if i[0] == 'J' and i[-2:] == 't3':
        Jt3 = cp.Variable(boolean=True)
        variable['Jt3'] = Jt3

    if i[0] == 'J' and i[-2:] == 't4':
        Jt4 = cp.Variable(boolean=True)
        variable['Jt4'] = Jt4

    if i[0] == 'J' and i[-2:] == 't5':
        Jt5 = cp.Variable(boolean=True)
        variable['Jt5'] = Jt5

    if i[0] == 'J' and i[-2:] == 'w1':
        Jw1 = cp.Variable(boolean=True)
        variable['Jw1'] = Jw1
    
    if i[0] == 'J' and i[-2:] == 'w2':
        Jw2 = cp.Variable(boolean=True)
        variable['Jw2'] = Jw2

    if i[0] == 'J' and i[-2:] == 'w3':
        Jw3 = cp.Variable(boolean=True)
        variable['Jw3'] = Jw3

    if i[0] == 'J' and i[-2:] == 'w4':
        Jw4 = cp.Variable(boolean=True)
        variable['Jw4'] = Jw4

    if i[0] == 'J' and i[-2:] == 'w5':
        Jw5 = cp.Variable(boolean=True)
        variable['Jw5'] = Jw5

    if i[0] == 'J' and i[-3:] == 'th1':
        Jth1 = cp.Variable(boolean=True)
        variable['Jth1'] = Jth1
    
    if i[0] == 'J' and i[-3:] == 'th2':
        Jth2 = cp.Variable(boolean=True)
        variable['Jth2'] = Jth2

    if i[0] == 'J' and i[-3:] == 'th3':
        Jth3 = cp.Variable(boolean=True)
        variable['Jth3'] = Jth3

    if i[0] == 'J' and i[-3:] == 'th4':
        Jth4 = cp.Variable(boolean=True)
        variable['Jth4'] = Jth4

    if i[0] == 'J' and i[-3:] == 'th5':
        Jth5 = cp.Variable(boolean=True)
        variable['Jth5'] = Jth5

    if i[0] == 'J' and i[-2:] == 'f1':
        Jf1 = cp.Variable(boolean=True)
        variable['Jf1'] = Jf1
    
    if i[0] == 'J' and i[-2:] == 'f2':
        Jf2 = cp.Variable(boolean=True)
        variable['Jf2'] = Jf2

    if i[0] == 'J' and i[-2:] == 'f3':
        Jf3 = cp.Variable(boolean=True)
        variable['Jf3'] = Jf3

    if i[0] == 'J' and i[-2:] == 'f4':
        Jf4 = cp.Variable(boolean=True)
        variable['Jf4'] = Jf4

    if i[0] == 'J' and i[-2:] == 'f5':
        Jf5 = cp.Variable(boolean=True)
        variable['Jf5'] = Jf5

    if i[0] == 'K' and i[-2:] == 'm1':
        Km1 = cp.Variable(boolean=True)
        variable['Km1'] = Km1
    
    if i[0] == 'K' and i[-2:] == 'm2':
        Km2 = cp.Variable(boolean=True)
        variable['Km2'] = Km2

    if i[0] == 'K' and i[-2:] == 'm3':
        Km3 = cp.Variable(boolean=True)
        variable['Km3'] = Km3

    if i[0] == 'K' and i[-2:] == 'm4':
        Km4 = cp.Variable(boolean=True)
        variable['Km4'] = Km4

    if i[0] == 'K' and i[-2:] == 'm5':
        Km5 = cp.Variable(boolean=True)
        variable['Km5'] = Km5

    if i[0] == 'K' and i[-2:] == 't1':
        Kt1 = cp.Variable(boolean=True)
        variable['Kt1'] = Kt1
    
    if i[0] == 'K' and i[-2:] == 't2':
        Kt2 = cp.Variable(boolean=True)
        variable['Kt2'] = Kt2

    if i[0] == 'K' and i[-2:] == 't3':
        Kt3 = cp.Variable(boolean=True)
        variable['Kt3'] = Kt3

    if i[0] == 'K' and i[-2:] == 't4':
        Kt4 = cp.Variable(boolean=True)
        variable['Kt4'] = Kt4

    if i[0] == 'K' and i[-2:] == 't5':
        Kt5 = cp.Variable(boolean=True)
        variable['Kt5'] = Kt5

    if i[0] == 'K' and i[-2:] == 'w1':
        Kw1 = cp.Variable(boolean=True)
        variable['Kw1'] = Kw1
    
    if i[0] == 'K' and i[-2:] == 'w2':
        Kw2 = cp.Variable(boolean=True)
        variable['Kw2'] = Kw2

    if i[0] == 'K' and i[-2:] == 'w3':
        Kw3 = cp.Variable(boolean=True)
        variable['Kw3'] = Kw3

    if i[0] == 'K' and i[-2:] == 'w4':
        Kw4 = cp.Variable(boolean=True)
        variable['Kw4'] = Kw4

    if i[0] == 'K' and i[-2:] == 'w5':
        Kw5 = cp.Variable(boolean=True)
        variable['Kw5'] = Kw5

    if i[0] == 'K' and i[-3:] == 'th1':
        Kth1 = cp.Variable(boolean=True)
        variable['Kth1'] = Kth1
    
    if i[0] == 'K' and i[-3:] == 'th2':
        Kth2 = cp.Variable(boolean=True)
        variable['Kth2'] = Kth2

    if i[0] == 'K' and i[-3:] == 'th3':
        Kth3 = cp.Variable(boolean=True)
        variable['Kth3'] = Kth3

    if i[0] == 'K' and i[-3:] == 'th4':
        Kth4 = cp.Variable(boolean=True)
        variable['Kth4'] = Kth4

    if i[0] == 'K' and i[-3:] == 'th5':
        Kth5 = cp.Variable(boolean=True)
        variable['Kth5'] = Kth5

    if i[0] == 'K' and i[-2:] == 'f1':
        Kf1 = cp.Variable(boolean=True)
        variable['Kf1'] = Kf1
    
    if i[0] == 'K' and i[-2:] == 'f2':
        Kf2 = cp.Variable(boolean=True)
        variable['Kf2'] = Kf2

    if i[0] == 'K' and i[-2:] == 'f3':
        Kf3 = cp.Variable(boolean=True)
        variable['Kf3'] = Kf3

    if i[0] == 'K' and i[-2:] == 'f4':
        Kf4 = cp.Variable(boolean=True)
        variable['Kf4'] = Kf4

    if i[0] == 'K' and i[-2:] == 'f5':
        Kf5 = cp.Variable(boolean=True)
        variable['Kf5'] = Kf5

    if i[0] == 'L' and i[-2:] == 'm1':
        Lm1 = cp.Variable(boolean=True)
        variable['Lm1'] = Lm1
    
    if i[0] == 'L' and i[-2:] == 'm2':
        Lm2 = cp.Variable(boolean=True)
        variable['Lm2'] = Lm2

    if i[0] == 'L' and i[-2:] == 'm3':
        Lm3 = cp.Variable(boolean=True)
        variable['Lm3'] = Lm3

    if i[0] == 'L' and i[-2:] == 'm4':
        Lm4 = cp.Variable(boolean=True)
        variable['Lm4'] = Lm4

    if i[0] == 'L' and i[-2:] == 'm5':
        Lm5 = cp.Variable(boolean=True)
        variable['Lm5'] = Lm5

    if i[0] == 'L' and i[-2:] == 't1':
        Lt1 = cp.Variable(boolean=True)
        variable['Lt1'] = Lt1
    
    if i[0] == 'L' and i[-2:] == 't2':
        Lt2 = cp.Variable(boolean=True)
        variable['Lt2'] = Lt2

    if i[0] == 'L' and i[-2:] == 't3':
        Lt3 = cp.Variable(boolean=True)
        variable['Lt3'] = Lt3

    if i[0] == 'L' and i[-2:] == 't4':
        Lt4 = cp.Variable(boolean=True)
        variable['Lt4'] = Lt4

    if i[0] == 'L' and i[-2:] == 't5':
        Lt5 = cp.Variable(boolean=True)
        variable['Lt5'] = Lt5

    if i[0] == 'L' and i[-2:] == 'w1':
        Lw1 = cp.Variable(boolean=True)
        variable['Lw1'] = Lw1
    
    if i[0] == 'L' and i[-2:] == 'w2':
        Lw2 = cp.Variable(boolean=True)
        variable['Lw2'] = Lw2

    if i[0] == 'L' and i[-2:] == 'w3':
        Lw3 = cp.Variable(boolean=True)
        variable['Lw3'] = Lw3

    if i[0] == 'L' and i[-2:] == 'w4':
        Lw4 = cp.Variable(boolean=True)
        variable['Lw4'] = Lw4

    if i[0] == 'L' and i[-2:] == 'w5':
        Lw5 = cp.Variable(boolean=True)
        variable['Lw5'] = Lw5

    if i[0] == 'L' and i[-3:] == 'th1':
        Lth1 = cp.Variable(boolean=True)
        variable['Lth1'] = Lth1
    
    if i[0] == 'L' and i[-3:] == 'th2':
        Lth2 = cp.Variable(boolean=True)
        variable['Lth2'] = Lth2

    if i[0] == 'L' and i[-3:] == 'th3':
        Lth3 = cp.Variable(boolean=True)
        variable['Lth3'] = Lth3

    if i[0] == 'L' and i[-3:] == 'th4':
        Lth4 = cp.Variable(boolean=True)
        variable['Lth4'] = Lth4

    if i[0] == 'L' and i[-3:] == 'th5':
        Lth5 = cp.Variable(boolean=True)
        variable['Lth5'] = Lth5

    if i[0] == 'L' and i[-2:] == 'f1':
        Lf1 = cp.Variable(boolean=True)
        variable['Lf1'] = Lf1
    
    if i[0] == 'L' and i[-2:] == 'f2':
        Lf2 = cp.Variable(boolean=True)
        variable['Lf2'] = Lf2

    if i[0] == 'L' and i[-2:] == 'f3':
        Lf3 = cp.Variable(boolean=True)
        variable['Lf3'] = Lf3

    if i[0] == 'L' and i[-2:] == 'f4':
        Lf4 = cp.Variable(boolean=True)
        variable['Lf4'] = Lf4

    if i[0] == 'L' and i[-2:] == 'f5':
        Lf5 = cp.Variable(boolean=True)
        variable['Lf5'] = Lf5

    if i[0] == 'M' and i[-2:] == 'm1':
        Mm1 = cp.Variable(boolean=True)
        variable['Mm1'] = Mm1
    
    if i[0] == 'M' and i[-2:] == 'm2':
        Mm2 = cp.Variable(boolean=True)
        variable['Mm2'] = Mm2

    if i[0] == 'M' and i[-2:] == 'm3':
        Mm3 = cp.Variable(boolean=True)
        variable['Mm3'] = Mm3

    if i[0] == 'M' and i[-2:] == 'm4':
        Mm4 = cp.Variable(boolean=True)
        variable['Mm4'] = Mm4

    if i[0] == 'M' and i[-2:] == 'm5':
        Mm5 = cp.Variable(boolean=True)
        variable['Mm5'] = Mm5

    if i[0] == 'M' and i[-2:] == 't1':
        Mt1 = cp.Variable(boolean=True)
        variable['Mt1'] = Mt1
    
    if i[0] == 'M' and i[-2:] == 't2':
        Mt2 = cp.Variable(boolean=True)
        variable['Mt2'] = Mt2

    if i[0] == 'M' and i[-2:] == 't3':
        Mt3 = cp.Variable(boolean=True)
        variable['Mt3'] = Mt3

    if i[0] == 'M' and i[-2:] == 't4':
        Mt4 = cp.Variable(boolean=True)
        variable['Mt4'] = Mt4

    if i[0] == 'M' and i[-2:] == 't5':
        Mt5 = cp.Variable(boolean=True)
        variable['Mt5'] = Mt5

    if i[0] == 'M' and i[-2:] == 'w1':
        Mw1 = cp.Variable(boolean=True)
        variable['Mw1'] = Mw1
    
    if i[0] == 'M' and i[-2:] == 'w2':
        Mw2 = cp.Variable(boolean=True)
        variable['Mw2'] = Mw2

    if i[0] == 'M' and i[-2:] == 'w3':
        Mw3 = cp.Variable(boolean=True)
        variable['Mw3'] = Mw3

    if i[0] == 'M' and i[-2:] == 'w4':
        Mw4 = cp.Variable(boolean=True)
        variable['Mw4'] = Mw4

    if i[0] == 'M' and i[-2:] == 'w5':
        Mw5 = cp.Variable(boolean=True)
        variable['Mw5'] = Mw5

    if i[0] == 'M' and i[-3:] == 'th1':
        Mth1 = cp.Variable(boolean=True)
        variable['Mth1'] = Mth1
    
    if i[0] == 'M' and i[-3:] == 'th2':
        Mth2 = cp.Variable(boolean=True)
        variable['Mth2'] = Mth2

    if i[0] == 'M' and i[-3:] == 'th3':
        Mth3 = cp.Variable(boolean=True)
        variable['Mth3'] = Mth3

    if i[0] == 'M' and i[-3:] == 'th4':
        Mth4 = cp.Variable(boolean=True)
        variable['Mth4'] = Mth4

    if i[0] == 'M' and i[-3:] == 'th5':
        Mth5 = cp.Variable(boolean=True)
        variable['Mth5'] = Mth5

    if i[0] == 'M' and i[-2:] == 'f1':
        Mf1 = cp.Variable(boolean=True)
        variable['Mf1'] = Mf1
    
    if i[0] == 'M' and i[-2:] == 'f2':
        Mf2 = cp.Variable(boolean=True)
        variable['Mf2'] = Mf2

    if i[0] == 'M' and i[-2:] == 'f3':
        Mf3 = cp.Variable(boolean=True)
        variable['Mf3'] = Mf3

    if i[0] == 'M' and i[-2:] == 'f4':
        Mf4 = cp.Variable(boolean=True)
        variable['Mf4'] = Mf4

    if i[0] == 'M' and i[-2:] == 'f5':
        Mf5 = cp.Variable(boolean=True)
        variable['Mf5'] = Mf5

    if i[0] == 'N' and i[-2:] == 'm1':
        Nm1 = cp.Variable(boolean=True)
        variable['Nm1'] = Nm1
    
    if i[0] == 'N' and i[-2:] == 'm2':
        Nm2 = cp.Variable(boolean=True)
        variable['Nm2'] = Nm2

    if i[0] == 'N' and i[-2:] == 'm3':
        Nm3 = cp.Variable(boolean=True)
        variable['Nm3'] = Nm3

    if i[0] == 'N' and i[-2:] == 'm4':
        Nm4 = cp.Variable(boolean=True)
        variable['Nm4'] = Nm4

    if i[0] == 'N' and i[-2:] == 'm5':
        Nm5 = cp.Variable(boolean=True)
        variable['Nm5'] = Nm5

    if i[0] == 'N' and i[-2:] == 't1':
        Nt1 = cp.Variable(boolean=True)
        variable['Nt1'] = Nt1
    
    if i[0] == 'N' and i[-2:] == 't2':
        Nt2 = cp.Variable(boolean=True)
        variable['Nt2'] = Nt2

    if i[0] == 'N' and i[-2:] == 't3':
        Nt3 = cp.Variable(boolean=True)
        variable['Nt3'] = Nt3

    if i[0] == 'N' and i[-2:] == 't4':
        Nt4 = cp.Variable(boolean=True)
        variable['Nt4'] = Nt4

    if i[0] == 'N' and i[-2:] == 't5':
        Nt5 = cp.Variable(boolean=True)
        variable['Nt5'] = Nt5

    if i[0] == 'N' and i[-2:] == 'w1':
        Nw1 = cp.Variable(boolean=True)
        variable['Nw1'] = Nw1
    
    if i[0] == 'N' and i[-2:] == 'w2':
        Nw2 = cp.Variable(boolean=True)
        variable['Nw2'] = Nw2

    if i[0] == 'N' and i[-2:] == 'w3':
        Nw3 = cp.Variable(boolean=True)
        variable['Nw3'] = Nw3

    if i[0] == 'N' and i[-2:] == 'w4':
        Nw4 = cp.Variable(boolean=True)
        variable['Nw4'] = Nw4

    if i[0] == 'N' and i[-2:] == 'w5':
        Nw5 = cp.Variable(boolean=True)
        variable['Nw5'] = Nw5

    if i[0] == 'N' and i[-3:] == 'th1':
        Nth1 = cp.Variable(boolean=True)
        variable['Nth1'] = Nth1
    
    if i[0] == 'N' and i[-3:] == 'th2':
        Nth2 = cp.Variable(boolean=True)
        variable['Nth2'] = Nth2

    if i[0] == 'N' and i[-3:] == 'th3':
        Nth3 = cp.Variable(boolean=True)
        variable['Nth3'] = Nth3

    if i[0] == 'N' and i[-3:] == 'th4':
        Nth4 = cp.Variable(boolean=True)
        variable['Nth4'] = Nth4

    if i[0] == 'N' and i[-3:] == 'th5':
        Nth5 = cp.Variable(boolean=True)
        variable['Nth5'] = Nth5

    if i[0] == 'N' and i[-2:] == 'f1':
        Nf1 = cp.Variable(boolean=True)
        variable['Nf1'] = Nf1
    
    if i[0] == 'N' and i[-2:] == 'f2':
        Nf2 = cp.Variable(boolean=True)
        variable['Nf2'] = Nf2

    if i[0] == 'N' and i[-2:] == 'f3':
        Nf3 = cp.Variable(boolean=True)
        variable['Nf3'] = Nf3

    if i[0] == 'N' and i[-2:] == 'f4':
        Nf4 = cp.Variable(boolean=True)
        variable['Nf4'] = Nf4

    if i[0] == 'N' and i[-2:] == 'f5':
        Nf5 = cp.Variable(boolean=True)
        variable['Nf5'] = Nf5

    if i[0] == 'O' and i[-2:] == 'm1':
        Om1 = cp.Variable(boolean=True)
        variable['Om1'] = Om1
    
    if i[0] == 'O' and i[-2:] == 'm2':
        Om2 = cp.Variable(boolean=True)
        variable['Om2'] = Om2

    if i[0] == 'O' and i[-2:] == 'm3':
        Om3 = cp.Variable(boolean=True)
        variable['Om3'] = Om3

    if i[0] == 'O' and i[-2:] == 'm4':
        Om4 = cp.Variable(boolean=True)
        variable['Om4'] = Om4

    if i[0] == 'O' and i[-2:] == 'm5':
        Om5 = cp.Variable(boolean=True)
        variable['Om5'] = Om5

    if i[0] == 'O' and i[-2:] == 't1':
        Ot1 = cp.Variable(boolean=True)
        variable['Ot1'] = Ot1
    
    if i[0] == 'O' and i[-2:] == 't2':
        Ot2 = cp.Variable(boolean=True)
        variable['Ot2'] = Ot2

    if i[0] == 'O' and i[-2:] == 't3':
        Ot3 = cp.Variable(boolean=True)
        variable['Ot3'] = Ot3

    if i[0] == 'O' and i[-2:] == 't4':
        Ot4 = cp.Variable(boolean=True)
        variable['Ot4'] = Ot4

    if i[0] == 'O' and i[-2:] == 't5':
        Ot5 = cp.Variable(boolean=True)
        variable['Ot5'] = Ot5

    if i[0] == 'O' and i[-2:] == 'w1':
        Ow1 = cp.Variable(boolean=True)
        variable['Ow1'] = Ow1
    
    if i[0] == 'O' and i[-2:] == 'w2':
        Ow2 = cp.Variable(boolean=True)
        variable['Ow2'] = Ow2

    if i[0] == 'O' and i[-2:] == 'w3':
        Ow3 = cp.Variable(boolean=True)
        variable['Ow3'] = Ow3

    if i[0] == 'O' and i[-2:] == 'w4':
        Ow4 = cp.Variable(boolean=True)
        variable['Ow4'] = Ow4

    if i[0] == 'O' and i[-2:] == 'w5':
        Ow5 = cp.Variable(boolean=True)
        variable['Ow5'] = Ow5

    if i[0] == 'O' and i[-3:] == 'th1':
        Oth1 = cp.Variable(boolean=True)
        variable['Oth1'] = Oth1
    
    if i[0] == 'O' and i[-3:] == 'th2':
        Oth2 = cp.Variable(boolean=True)
        variable['Oth2'] = Oth2

    if i[0] == 'O' and i[-3:] == 'th3':
        Oth3 = cp.Variable(boolean=True)
        variable['Oth3'] = Oth3

    if i[0] == 'O' and i[-3:] == 'th4':
        Oth4 = cp.Variable(boolean=True)
        variable['Oth4'] = Oth4

    if i[0] == 'O' and i[-3:] == 'th5':
        Oth5 = cp.Variable(boolean=True)
        variable['Oth5'] = Oth5

    if i[0] == 'O' and i[-2:] == 'f1':
        Of1 = cp.Variable(boolean=True)
        variable['Of1'] = Of1
    
    if i[0] == 'O' and i[-2:] == 'f2':
        Of2 = cp.Variable(boolean=True)
        variable['Of2'] = Of2

    if i[0] == 'O' and i[-2:] == 'f3':
        Of3 = cp.Variable(boolean=True)
        variable['Of3'] = Of3

    if i[0] == 'O' and i[-2:] == 'f4':
        Of4 = cp.Variable(boolean=True)
        variable['Of4'] = Of4

    if i[0] == 'O' and i[-2:] == 'f5':
        Of5 = cp.Variable(boolean=True)
        variable['Of5'] = Of5

    if i[0] == 'P' and i[-2:] == 'm1':
        Pm1 = cp.Variable(boolean=True)
        variable['Pm1'] = Pm1
    
    if i[0] == 'P' and i[-2:] == 'm2':
        Pm2 = cp.Variable(boolean=True)
        variable['Pm2'] = Pm2

    if i[0] == 'P' and i[-2:] == 'm3':
        Pm3 = cp.Variable(boolean=True)
        variable['Pm3'] = Pm3

    if i[0] == 'P' and i[-2:] == 'm4':
        Pm4 = cp.Variable(boolean=True)
        variable['Pm4'] = Pm4

    if i[0] == 'P' and i[-2:] == 'm5':
        Pm5 = cp.Variable(boolean=True)
        variable['Pm5'] = Pm5

    if i[0] == 'P' and i[-2:] == 't1':
        Pt1 = cp.Variable(boolean=True)
        variable['Pt1'] = Pt1
    
    if i[0] == 'P' and i[-2:] == 't2':
        Pt2 = cp.Variable(boolean=True)
        variable['Pt2'] = Pt2

    if i[0] == 'P' and i[-2:] == 't3':
        Pt3 = cp.Variable(boolean=True)
        variable['Pt3'] = Pt3

    if i[0] == 'P' and i[-2:] == 't4':
        Pt4 = cp.Variable(boolean=True)
        variable['Pt4'] = Pt4

    if i[0] == 'P' and i[-2:] == 't5':
        Pt5 = cp.Variable(boolean=True)
        variable['Pt5'] = Pt5

    if i[0] == 'P' and i[-2:] == 'w1':
        Pw1 = cp.Variable(boolean=True)
        variable['Pw1'] = Pw1
    
    if i[0] == 'P' and i[-2:] == 'w2':
        Pw2 = cp.Variable(boolean=True)
        variable['Pw2'] = Pw2

    if i[0] == 'P' and i[-2:] == 'w3':
        Pw3 = cp.Variable(boolean=True)
        variable['Pw3'] = Pw3

    if i[0] == 'P' and i[-2:] == 'w4':
        Pw4 = cp.Variable(boolean=True)
        variable['Pw4'] = Pw4

    if i[0] == 'P' and i[-2:] == 'w5':
        Pw5 = cp.Variable(boolean=True)
        variable['Pw5'] = Pw5

    if i[0] == 'P' and i[-3:] == 'th1':
        Pth1 = cp.Variable(boolean=True)
        variable['Pth1'] = Pth1
    
    if i[0] == 'P' and i[-3:] == 'th2':
        Pth2 = cp.Variable(boolean=True)
        variable['Pth2'] = Pth2

    if i[0] == 'P' and i[-3:] == 'th3':
        Pth3 = cp.Variable(boolean=True)
        variable['Pth3'] = Pth3

    if i[0] == 'P' and i[-3:] == 'th4':
        Pth4 = cp.Variable(boolean=True)
        variable['Pth4'] = Pth4

    if i[0] == 'P' and i[-3:] == 'th5':
        Pth5 = cp.Variable(boolean=True)
        variable['Pth5'] = Pth5

    if i[0] == 'P' and i[-2:] == 'f1':
        Pf1 = cp.Variable(boolean=True)
        variable['Pf1'] = Pf1
    
    if i[0] == 'P' and i[-2:] == 'f2':
        Pf2 = cp.Variable(boolean=True)
        variable['Pf2'] = Pf2

    if i[0] == 'P' and i[-2:] == 'f3':
        Pf3 = cp.Variable(boolean=True)
        variable['Pf3'] = Pf3

    if i[0] == 'P' and i[-2:] == 'f4':
        Pf4 = cp.Variable(boolean=True)
        variable['Pf4'] = Pf4

    if i[0] == 'P' and i[-2:] == 'f5':
        Pf5 = cp.Variable(boolean=True)
        variable['Pf5'] = Pf5

    if i[0] == 'Q' and i[-2:] == 'm1':
        Qm1 = cp.Variable(boolean=True)
        variable['Qm1'] = Qm1
    
    if i[0] == 'Q' and i[-2:] == 'm2':
        Qm2 = cp.Variable(boolean=True)
        variable['Qm2'] = Qm2

    if i[0] == 'Q' and i[-2:] == 'm3':
        Qm3 = cp.Variable(boolean=True)
        variable['Qm3'] = Qm3

    if i[0] == 'Q' and i[-2:] == 'm4':
        Qm4 = cp.Variable(boolean=True)
        variable['Qm4'] = Qm4

    if i[0] == 'Q' and i[-2:] == 'm5':
        Qm5 = cp.Variable(boolean=True)
        variable['Qm5'] = Qm5

    if i[0] == 'Q' and i[-2:] == 't1':
        Qt1 = cp.Variable(boolean=True)
        variable['Qt1'] = Qt1
    
    if i[0] == 'Q' and i[-2:] == 't2':
        Qt2 = cp.Variable(boolean=True)
        variable['Qt2'] = Qt2

    if i[0] == 'Q' and i[-2:] == 't3':
        Qt3 = cp.Variable(boolean=True)
        variable['Qt3'] = Qt3

    if i[0] == 'Q' and i[-2:] == 't4':
        Qt4 = cp.Variable(boolean=True)
        variable['Qt4'] = Qt4

    if i[0] == 'Q' and i[-2:] == 't5':
        Qt5 = cp.Variable(boolean=True)
        variable['Qt5'] = Qt5

    if i[0] == 'Q' and i[-2:] == 'w1':
        Qw1 = cp.Variable(boolean=True)
        variable['Qw1'] = Qw1
    
    if i[0] == 'Q' and i[-2:] == 'w2':
        Qw2 = cp.Variable(boolean=True)
        variable['Qw2'] = Qw2

    if i[0] == 'Q' and i[-2:] == 'w3':
        Qw3 = cp.Variable(boolean=True)
        variable['Qw3'] = Qw3

    if i[0] == 'Q' and i[-2:] == 'w4':
        Qw4 = cp.Variable(boolean=True)
        variable['Qw4'] = Qw4

    if i[0] == 'Q' and i[-2:] == 'w5':
        Qw5 = cp.Variable(boolean=True)
        variable['Qw5'] = Qw5

    if i[0] == 'Q' and i[-3:] == 'th1':
        Qth1 = cp.Variable(boolean=True)
        variable['Qth1'] = Qth1
    
    if i[0] == 'Q' and i[-3:] == 'th2':
        Qth2 = cp.Variable(boolean=True)
        variable['Qth2'] = Qth2

    if i[0] == 'Q' and i[-3:] == 'th3':
        Qth3 = cp.Variable(boolean=True)
        variable['Qth3'] = Qth3

    if i[0] == 'Q' and i[-3:] == 'th4':
        Qth4 = cp.Variable(boolean=True)
        variable['Qth4'] = Qth4

    if i[0] == 'Q' and i[-3:] == 'th5':
        Qth5 = cp.Variable(boolean=True)
        variable['Qth5'] = Qth5

    if i[0] == 'Q' and i[-2:] == 'f1':
        Qf1 = cp.Variable(boolean=True)
        variable['Qf1'] = Qf1
    
    if i[0] == 'Q' and i[-2:] == 'f2':
        Qf2 = cp.Variable(boolean=True)
        variable['Qf2'] = Qf2

    if i[0] == 'Q' and i[-2:] == 'f3':
        Qf3 = cp.Variable(boolean=True)
        variable['Qf3'] = Qf3

    if i[0] == 'Q' and i[-2:] == 'f4':
        Qf4 = cp.Variable(boolean=True)
        variable['Qf4'] = Qf4

    if i[0] == 'Q' and i[-2:] == 'f5':
        Qf5 = cp.Variable(boolean=True)
        variable['Qf5'] = Qf5

    if i[0] == 'R' and i[-2:] == 'm1':
        Rm1 = cp.Variable(boolean=True)
        variable['Rm1'] = Rm1
    
    if i[0] == 'R' and i[-2:] == 'm2':
        Rm2 = cp.Variable(boolean=True)
        variable['Rm2'] = Rm2

    if i[0] == 'R' and i[-2:] == 'm3':
        Rm3 = cp.Variable(boolean=True)
        variable['Rm3'] = Rm3

    if i[0] == 'R' and i[-2:] == 'm4':
        Rm4 = cp.Variable(boolean=True)
        variable['Rm4'] = Rm4

    if i[0] == 'R' and i[-2:] == 'm5':
        Rm5 = cp.Variable(boolean=True)
        variable['Rm5'] = Rm5

    if i[0] == 'R' and i[-2:] == 't1':
        Rt1 = cp.Variable(boolean=True)
        variable['Rt1'] = Rt1
    
    if i[0] == 'R' and i[-2:] == 't2':
        Rt2 = cp.Variable(boolean=True)
        variable['Rt2'] = Rt2

    if i[0] == 'R' and i[-2:] == 't3':
        Rt3 = cp.Variable(boolean=True)
        variable['Rt3'] = Rt3

    if i[0] == 'R' and i[-2:] == 't4':
        Rt4 = cp.Variable(boolean=True)
        variable['Rt4'] = Rt4

    if i[0] == 'R' and i[-2:] == 't5':
        Rt5 = cp.Variable(boolean=True)
        variable['Rt5'] = Rt5

    if i[0] == 'R' and i[-2:] == 'w1':
        Rw1 = cp.Variable(boolean=True)
        variable['Rw1'] = Rw1
    
    if i[0] == 'R' and i[-2:] == 'w2':
        Rw2 = cp.Variable(boolean=True)
        variable['Rw2'] = Rw2

    if i[0] == 'R' and i[-2:] == 'w3':
        Rw3 = cp.Variable(boolean=True)
        variable['Rw3'] = Rw3

    if i[0] == 'R' and i[-2:] == 'w4':
        Rw4 = cp.Variable(boolean=True)
        variable['Rw4'] = Rw4

    if i[0] == 'R' and i[-2:] == 'w5':
        Rw5 = cp.Variable(boolean=True)
        variable['Rw5'] = Rw5

    if i[0] == 'R' and i[-3:] == 'th1':
        Rth1 = cp.Variable(boolean=True)
        variable['Rth1'] = Rth1
    
    if i[0] == 'R' and i[-3:] == 'th2':
        Rth2 = cp.Variable(boolean=True)
        variable['Rth2'] = Rth2

    if i[0] == 'R' and i[-3:] == 'th3':
        Rth3 = cp.Variable(boolean=True)
        variable['Rth3'] = Rth3

    if i[0] == 'R' and i[-3:] == 'th4':
        Rth4 = cp.Variable(boolean=True)
        variable['Rth4'] = Rth4

    if i[0] == 'R' and i[-3:] == 'th5':
        Rth5 = cp.Variable(boolean=True)
        variable['Rth5'] = Rth5

    if i[0] == 'R' and i[-2:] == 'f1':
        Rf1 = cp.Variable(boolean=True)
        variable['Rf1'] = Rf1
    
    if i[0] == 'R' and i[-2:] == 'f2':
        Rf2 = cp.Variable(boolean=True)
        variable['Rf2'] = Rf2

    if i[0] == 'R' and i[-2:] == 'f3':
        Rf3 = cp.Variable(boolean=True)
        variable['Rf3'] = Rf3

    if i[0] == 'R' and i[-2:] == 'f4':
        Rf4 = cp.Variable(boolean=True)
        variable['Rf4'] = Rf4

    if i[0] == 'R' and i[-2:] == 'f5':
        Rf5 = cp.Variable(boolean=True)
        variable['Rf5'] = Rf5

    if i[0] == 'S' and i[-2:] == 'm1':
        Sm1 = cp.Variable(boolean=True)
        variable['Sm1'] = Sm1
    
    if i[0] == 'S' and i[-2:] == 'm2':
        Sm2 = cp.Variable(boolean=True)
        variable['Sm2'] = Sm2

    if i[0] == 'S' and i[-2:] == 'm3':
        Sm3 = cp.Variable(boolean=True)
        variable['Sm3'] = Sm3

    if i[0] == 'S' and i[-2:] == 'm4':
        Sm4 = cp.Variable(boolean=True)
        variable['Sm4'] = Sm4

    if i[0] == 'S' and i[-2:] == 'm5':
        Sm5 = cp.Variable(boolean=True)
        variable['Sm5'] = Sm5

    if i[0] == 'S' and i[-2:] == 't1':
        St1 = cp.Variable(boolean=True)
        variable['St1'] = St1
    
    if i[0] == 'S' and i[-2:] == 't2':
        St2 = cp.Variable(boolean=True)
        variable['St2'] = St2

    if i[0] == 'S' and i[-2:] == 't3':
        St3 = cp.Variable(boolean=True)
        variable['St3'] = St3

    if i[0] == 'S' and i[-2:] == 't4':
        St4 = cp.Variable(boolean=True)
        variable['St4'] = St4

    if i[0] == 'S' and i[-2:] == 't5':
        St5 = cp.Variable(boolean=True)
        variable['St5'] = St5

    if i[0] == 'S' and i[-2:] == 'w1':
        Sw1 = cp.Variable(boolean=True)
        variable['Sw1'] = Sw1
    
    if i[0] == 'S' and i[-2:] == 'w2':
        Sw2 = cp.Variable(boolean=True)
        variable['Sw2'] = Sw2

    if i[0] == 'S' and i[-2:] == 'w3':
        Sw3 = cp.Variable(boolean=True)
        variable['Sw3'] = Sw3

    if i[0] == 'S' and i[-2:] == 'w4':
        Sw4 = cp.Variable(boolean=True)
        variable['Sw4'] = Sw4

    if i[0] == 'S' and i[-2:] == 'w5':
        Sw5 = cp.Variable(boolean=True)
        variable['Sw5'] = Sw5

    if i[0] == 'S' and i[-3:] == 'th1':
        Sth1 = cp.Variable(boolean=True)
        variable['Sth1'] = Sth1
    
    if i[0] == 'S' and i[-3:] == 'th2':
        Sth2 = cp.Variable(boolean=True)
        variable['Sth2'] = Sth2

    if i[0] == 'S' and i[-3:] == 'th3':
        Sth3 = cp.Variable(boolean=True)
        variable['Sth3'] = Sth3

    if i[0] == 'S' and i[-3:] == 'th4':
        Sth4 = cp.Variable(boolean=True)
        variable['Sth4'] = Sth4

    if i[0] == 'S' and i[-3:] == 'th5':
        Sth5 = cp.Variable(boolean=True)
        variable['Sth5'] = Sth5

    if i[0] == 'S' and i[-2:] == 'f1':
        Sf1 = cp.Variable(boolean=True)
        variable['Sf1'] = Sf1
    
    if i[0] == 'S' and i[-2:] == 'f2':
        Sf2 = cp.Variable(boolean=True)
        variable['Sf2'] = Sf2

    if i[0] == 'S' and i[-2:] == 'f3':
        Sf3 = cp.Variable(boolean=True)
        variable['Sf3'] = Sf3

    if i[0] == 'S' and i[-2:] == 'f4':
        Sf4 = cp.Variable(boolean=True)
        variable['Sf4'] = Sf4

    if i[0] == 'S' and i[-2:] == 'f5':
        Sf5 = cp.Variable(boolean=True)
        variable['Sf5'] = Sf5

    if i[0] == 'T' and i[-2:] == 'm1':
        Tm1 = cp.Variable(boolean=True)
        variable['Tm1'] = Tm1
    
    if i[0] == 'T' and i[-2:] == 'm2':
        Tm2 = cp.Variable(boolean=True)
        variable['Tm2'] = Tm2

    if i[0] == 'T' and i[-2:] == 'm3':
        Tm3 = cp.Variable(boolean=True)
        variable['Tm3'] = Tm3

    if i[0] == 'T' and i[-2:] == 'm4':
        Tm4 = cp.Variable(boolean=True)
        variable['Tm4'] = Tm4

    if i[0] == 'T' and i[-2:] == 'm5':
        Tm5 = cp.Variable(boolean=True)
        variable['Tm5'] = Tm5

    if i[0] == 'T' and i[-2:] == 't1':
        Tt1 = cp.Variable(boolean=True)
        variable['Tt1'] = Tt1
    
    if i[0] == 'T' and i[-2:] == 't2':
        Tt2 = cp.Variable(boolean=True)
        variable['Tt2'] = Tt2

    if i[0] == 'T' and i[-2:] == 't3':
        Tt3 = cp.Variable(boolean=True)
        variable['Tt3'] = Tt3

    if i[0] == 'T' and i[-2:] == 't4':
        Tt4 = cp.Variable(boolean=True)
        variable['Tt4'] = Tt4

    if i[0] == 'T' and i[-2:] == 't5':
        Tt5 = cp.Variable(boolean=True)
        variable['Tt5'] = Tt5

    if i[0] == 'T' and i[-2:] == 'w1':
        Tw1 = cp.Variable(boolean=True)
        variable['Tw1'] = Tw1
    
    if i[0] == 'T' and i[-2:] == 'w2':
        Tw2 = cp.Variable(boolean=True)
        variable['Tw2'] = Tw2

    if i[0] == 'T' and i[-2:] == 'w3':
        Tw3 = cp.Variable(boolean=True)
        variable['Tw3'] = Tw3

    if i[0] == 'T' and i[-2:] == 'w4':
        Tw4 = cp.Variable(boolean=True)
        variable['Tw4'] = Tw4

    if i[0] == 'T' and i[-2:] == 'w5':
        Tw5 = cp.Variable(boolean=True)
        variable['Tw5'] = Tw5

    if i[0] == 'T' and i[-3:] == 'th1':
        Tth1 = cp.Variable(boolean=True)
        variable['Tth1'] = Tth1
    
    if i[0] == 'T' and i[-3:] == 'th2':
        Tth2 = cp.Variable(boolean=True)
        variable['Tth2'] = Tth2

    if i[0] == 'T' and i[-3:] == 'th3':
        Tth3 = cp.Variable(boolean=True)
        variable['Tth3'] = Tth3

    if i[0] == 'T' and i[-3:] == 'th4':
        Tth4 = cp.Variable(boolean=True)
        variable['Tth4'] = Tth4

    if i[0] == 'T' and i[-3:] == 'th5':
        Tth5 = cp.Variable(boolean=True)
        variable['Tth5'] = Tth5

    if i[0] == 'T' and i[-2:] == 'f1':
        Tf1 = cp.Variable(boolean=True)
        variable['Tf1'] = Tf1
    
    if i[0] == 'T' and i[-2:] == 'f2':
        Tf2 = cp.Variable(boolean=True)
        variable['Tf2'] = Tf2

    if i[0] == 'T' and i[-2:] == 'f3':
        Tf3 = cp.Variable(boolean=True)
        variable['Tf3'] = Tf3

    if i[0] == 'T' and i[-2:] == 'f4':
        Tf4 = cp.Variable(boolean=True)
        variable['Tf4'] = Tf4

    if i[0] == 'T' and i[-2:] == 'f5':
        Tf5 = cp.Variable(boolean=True)
        variable['Tf5'] = Tf5

    if i[0] == 'U' and i[-2:] == 'm1':
        Um1 = cp.Variable(boolean=True)
        variable['Um1'] = Um1
    
    if i[0] == 'U' and i[-2:] == 'm2':
        Um2 = cp.Variable(boolean=True)
        variable['Um2'] = Um2

    if i[0] == 'U' and i[-2:] == 'm3':
        Um3 = cp.Variable(boolean=True)
        variable['Um3'] = Um3

    if i[0] == 'U' and i[-2:] == 'm4':
        Um4 = cp.Variable(boolean=True)
        variable['Um4'] = Um4

    if i[0] == 'U' and i[-2:] == 'm5':
        Um5 = cp.Variable(boolean=True)
        variable['Um5'] = Um5

    if i[0] == 'U' and i[-2:] == 't1':
        Ut1 = cp.Variable(boolean=True)
        variable['Ut1'] = Ut1
    
    if i[0] == 'U' and i[-2:] == 't2':
        Ut2 = cp.Variable(boolean=True)
        variable['Ut2'] = Ut2

    if i[0] == 'U' and i[-2:] == 't3':
        Ut3 = cp.Variable(boolean=True)
        variable['Ut3'] = Ut3

    if i[0] == 'U' and i[-2:] == 't4':
        Ut4 = cp.Variable(boolean=True)
        variable['Ut4'] = Ut4

    if i[0] == 'U' and i[-2:] == 't5':
        Ut5 = cp.Variable(boolean=True)
        variable['Ut5'] = Ut5

    if i[0] == 'U' and i[-2:] == 'w1':
        Uw1 = cp.Variable(boolean=True)
        variable['Uw1'] = Uw1
    
    if i[0] == 'U' and i[-2:] == 'w2':
        Uw2 = cp.Variable(boolean=True)
        variable['Uw2'] = Uw2

    if i[0] == 'U' and i[-2:] == 'w3':
        Uw3 = cp.Variable(boolean=True)
        variable['Uw3'] = Uw3

    if i[0] == 'U' and i[-2:] == 'w4':
        Uw4 = cp.Variable(boolean=True)
        variable['Uw4'] = Uw4

    if i[0] == 'U' and i[-2:] == 'w5':
        Uw5 = cp.Variable(boolean=True)
        variable['Uw5'] = Uw5

    if i[0] == 'U' and i[-3:] == 'th1':
        Uth1 = cp.Variable(boolean=True)
        variable['Uth1'] = Uth1
    
    if i[0] == 'U' and i[-3:] == 'th2':
        Uth2 = cp.Variable(boolean=True)
        variable['Uth2'] = Uth2

    if i[0] == 'U' and i[-3:] == 'th3':
        Uth3 = cp.Variable(boolean=True)
        variable['Uth3'] = Uth3

    if i[0] == 'U' and i[-3:] == 'th4':
        Uth4 = cp.Variable(boolean=True)
        variable['Uth4'] = Uth4

    if i[0] == 'U' and i[-3:] == 'th5':
        Uth5 = cp.Variable(boolean=True)
        variable['Uth5'] = Uth5

    if i[0] == 'U' and i[-2:] == 'f1':
        Uf1 = cp.Variable(boolean=True)
        variable['Uf1'] = Uf1
    
    if i[0] == 'U' and i[-2:] == 'f2':
        Uf2 = cp.Variable(boolean=True)
        variable['Uf2'] = Uf2

    if i[0] == 'U' and i[-2:] == 'f3':
        Uf3 = cp.Variable(boolean=True)
        variable['Uf3'] = Uf3

    if i[0] == 'U' and i[-2:] == 'f4':
        Uf4 = cp.Variable(boolean=True)
        variable['Uf4'] = Uf4

    if i[0] == 'U' and i[-2:] == 'f5':
        Uf5 = cp.Variable(boolean=True)
        variable['Uf5'] = Uf5

    if i[0] == 'V' and i[-2:] == 'm1':
        Vm1 = cp.Variable(boolean=True)
        variable['Vm1'] = Vm1
    
    if i[0] == 'V' and i[-2:] == 'm2':
        Vm2 = cp.Variable(boolean=True)
        variable['Vm2'] = Vm2

    if i[0] == 'V' and i[-2:] == 'm3':
        Vm3 = cp.Variable(boolean=True)
        variable['Vm3'] = Vm3

    if i[0] == 'V' and i[-2:] == 'm4':
        Vm4 = cp.Variable(boolean=True)
        variable['Vm4'] = Vm4

    if i[0] == 'V' and i[-2:] == 'm5':
        Vm5 = cp.Variable(boolean=True)
        variable['Vm5'] = Vm5

    if i[0] == 'V' and i[-2:] == 't1':
        Vt1 = cp.Variable(boolean=True)
        variable['Vt1'] = Vt1
    
    if i[0] == 'V' and i[-2:] == 't2':
        Vt2 = cp.Variable(boolean=True)
        variable['Vt2'] = Vt2

    if i[0] == 'V' and i[-2:] == 't3':
        Vt3 = cp.Variable(boolean=True)
        variable['Vt3'] = Vt3

    if i[0] == 'V' and i[-2:] == 't4':
        Vt4 = cp.Variable(boolean=True)
        variable['Vt4'] = Vt4

    if i[0] == 'V' and i[-2:] == 't5':
        Vt5 = cp.Variable(boolean=True)
        variable['Vt5'] = Vt5

    if i[0] == 'V' and i[-2:] == 'w1':
        Vw1 = cp.Variable(boolean=True)
        variable['Vw1'] = Vw1
    
    if i[0] == 'V' and i[-2:] == 'w2':
        Vw2 = cp.Variable(boolean=True)
        variable['Vw2'] = Vw2

    if i[0] == 'V' and i[-2:] == 'w3':
        Vw3 = cp.Variable(boolean=True)
        variable['Vw3'] = Vw3

    if i[0] == 'V' and i[-2:] == 'w4':
        Vw4 = cp.Variable(boolean=True)
        variable['Vw4'] = Vw4

    if i[0] == 'V' and i[-2:] == 'w5':
        Vw5 = cp.Variable(boolean=True)
        variable['Vw5'] = Vw5

    if i[0] == 'V' and i[-3:] == 'th1':
        Vth1 = cp.Variable(boolean=True)
        variable['Vth1'] = Vth1
    
    if i[0] == 'V' and i[-3:] == 'th2':
        Vth2 = cp.Variable(boolean=True)
        variable['Vth2'] = Vth2

    if i[0] == 'V' and i[-3:] == 'th3':
        Vth3 = cp.Variable(boolean=True)
        variable['Vth3'] = Vth3

    if i[0] == 'V' and i[-3:] == 'th4':
        Vth4 = cp.Variable(boolean=True)
        variable['Vth4'] = Vth4

    if i[0] == 'V' and i[-3:] == 'th5':
        Vth5 = cp.Variable(boolean=True)
        variable['Vth5'] = Vth5

    if i[0] == 'V' and i[-2:] == 'f1':
        Vf1 = cp.Variable(boolean=True)
        variable['Vf1'] = Vf1
    
    if i[0] == 'V' and i[-2:] == 'f2':
        Vf2 = cp.Variable(boolean=True)
        variable['Vf2'] = Vf2

    if i[0] == 'V' and i[-2:] == 'f3':
        Vf3 = cp.Variable(boolean=True)
        variable['Vf3'] = Vf3

    if i[0] == 'V' and i[-2:] == 'f4':
        Vf4 = cp.Variable(boolean=True)
        variable['Vf4'] = Vf4

    if i[0] == 'V' and i[-2:] == 'f5':
        Vf5 = cp.Variable(boolean=True)
        variable['Vf5'] = Vf5

    if i[0] == 'W' and i[-2:] == 'm1':
        Wm1 = cp.Variable(boolean=True)
        variable['Wm1'] = Wm1
    
    if i[0] == 'W' and i[-2:] == 'm2':
        Wm2 = cp.Variable(boolean=True)
        variable['Wm2'] = Wm2

    if i[0] == 'W' and i[-2:] == 'm3':
        Wm3 = cp.Variable(boolean=True)
        variable['Wm3'] = Wm3

    if i[0] == 'W' and i[-2:] == 'm4':
        Wm4 = cp.Variable(boolean=True)
        variable['Wm4'] = Wm4

    if i[0] == 'W' and i[-2:] == 'm5':
        Wm5 = cp.Variable(boolean=True)
        variable['Wm5'] = Wm5

    if i[0] == 'W' and i[-2:] == 't1':
        Wt1 = cp.Variable(boolean=True)
        variable['Wt1'] = Wt1
    
    if i[0] == 'W' and i[-2:] == 't2':
        Wt2 = cp.Variable(boolean=True)
        variable['Wt2'] = Wt2

    if i[0] == 'W' and i[-2:] == 't3':
        Wt3 = cp.Variable(boolean=True)
        variable['Wt3'] = Wt3

    if i[0] == 'W' and i[-2:] == 't4':
        Wt4 = cp.Variable(boolean=True)
        variable['Wt4'] = Wt4

    if i[0] == 'W' and i[-2:] == 't5':
        Wt5 = cp.Variable(boolean=True)
        variable['Wt5'] = Wt5

    if i[0] == 'W' and i[-2:] == 'w1':
        Ww1 = cp.Variable(boolean=True)
        variable['Ww1'] = Ww1
    
    if i[0] == 'W' and i[-2:] == 'w2':
        Ww2 = cp.Variable(boolean=True)
        variable['Ww2'] = Ww2

    if i[0] == 'W' and i[-2:] == 'w3':
        Ww3 = cp.Variable(boolean=True)
        variable['Ww3'] = Ww3

    if i[0] == 'W' and i[-2:] == 'w4':
        Ww4 = cp.Variable(boolean=True)
        variable['Ww4'] = Ww4

    if i[0] == 'W' and i[-2:] == 'w5':
        Ww5 = cp.Variable(boolean=True)
        variable['Ww5'] = Ww5

    if i[0] == 'W' and i[-3:] == 'th1':
        Wth1 = cp.Variable(boolean=True)
        variable['Wth1'] = Wth1
    
    if i[0] == 'W' and i[-3:] == 'th2':
        Wth2 = cp.Variable(boolean=True)
        variable['Wth2'] = Wth2

    if i[0] == 'W' and i[-3:] == 'th3':
        Wth3 = cp.Variable(boolean=True)
        variable['Wth3'] = Wth3

    if i[0] == 'W' and i[-3:] == 'th4':
        Wth4 = cp.Variable(boolean=True)
        variable['Wth4'] = Wth4

    if i[0] == 'W' and i[-3:] == 'th5':
        Wth5 = cp.Variable(boolean=True)
        variable['Wth5'] = Wth5

    if i[0] == 'W' and i[-2:] == 'f1':
        Wf1 = cp.Variable(boolean=True)
        variable['Wf1'] = Wf1
    
    if i[0] == 'W' and i[-2:] == 'f2':
        Wf2 = cp.Variable(boolean=True)
        variable['Wf2'] = Wf2

    if i[0] == 'W' and i[-2:] == 'f3':
        Wf3 = cp.Variable(boolean=True)
        variable['Wf3'] = Wf3

    if i[0] == 'W' and i[-2:] == 'f4':
        Wf4 = cp.Variable(boolean=True)
        variable['Wf4'] = Wf4

    if i[0] == 'W' and i[-2:] == 'f5':
        Wf5 = cp.Variable(boolean=True)
        variable['Wf5'] = Wf5

    if i[0] == 'X' and i[-2:] == 'm1':
        Xm1 = cp.Variable(boolean=True)
        variable['Xm1'] = Xm1
    
    if i[0] == 'X' and i[-2:] == 'm2':
        Xm2 = cp.Variable(boolean=True)
        variable['Xm2'] = Xm2

    if i[0] == 'X' and i[-2:] == 'm3':
        Xm3 = cp.Variable(boolean=True)
        variable['Xm3'] = Xm3

    if i[0] == 'X' and i[-2:] == 'm4':
        Xm4 = cp.Variable(boolean=True)
        variable['Xm4'] = Xm4

    if i[0] == 'X' and i[-2:] == 'm5':
        Xm5 = cp.Variable(boolean=True)
        variable['Xm5'] = Xm5

    if i[0] == 'X' and i[-2:] == 't1':
        Xt1 = cp.Variable(boolean=True)
        variable['Xt1'] = Xt1
    
    if i[0] == 'X' and i[-2:] == 't2':
        Xt2 = cp.Variable(boolean=True)
        variable['Xt2'] = Xt2

    if i[0] == 'X' and i[-2:] == 't3':
        Xt3 = cp.Variable(boolean=True)
        variable['Xt3'] = Xt3

    if i[0] == 'X' and i[-2:] == 't4':
        Xt4 = cp.Variable(boolean=True)
        variable['Xt4'] = Xt4

    if i[0] == 'X' and i[-2:] == 't5':
        Xt5 = cp.Variable(boolean=True)
        variable['Xt5'] = Xt5

    if i[0] == 'X' and i[-2:] == 'w1':
        Xw1 = cp.Variable(boolean=True)
        variable['Xw1'] = Xw1
    
    if i[0] == 'X' and i[-2:] == 'w2':
        Xw2 = cp.Variable(boolean=True)
        variable['Xw2'] = Xw2

    if i[0] == 'X' and i[-2:] == 'w3':
        Xw3 = cp.Variable(boolean=True)
        variable['Xw3'] = Xw3

    if i[0] == 'X' and i[-2:] == 'w4':
        Xw4 = cp.Variable(boolean=True)
        variable['Xw4'] = Xw4

    if i[0] == 'X' and i[-2:] == 'w5':
        Xw5 = cp.Variable(boolean=True)
        variable['Xw5'] = Xw5

    if i[0] == 'X' and i[-3:] == 'th1':
        Xth1 = cp.Variable(boolean=True)
        variable['Xth1'] = Xth1
    
    if i[0] == 'X' and i[-3:] == 'th2':
        Xth2 = cp.Variable(boolean=True)
        variable['Xth2'] = Xth2

    if i[0] == 'X' and i[-3:] == 'th3':
        Xth3 = cp.Variable(boolean=True)
        variable['Xth3'] = Xth3

    if i[0] == 'X' and i[-3:] == 'th4':
        Xth4 = cp.Variable(boolean=True)
        variable['Xth4'] = Xth4

    if i[0] == 'X' and i[-3:] == 'th5':
        Xth5 = cp.Variable(boolean=True)
        variable['Xth5'] = Xth5

    if i[0] == 'X' and i[-2:] == 'f1':
        Xf1 = cp.Variable(boolean=True)
        variable['Xf1'] = Xf1
    
    if i[0] == 'X' and i[-2:] == 'f2':
        Xf2 = cp.Variable(boolean=True)
        variable['Xf2'] = Xf2

    if i[0] == 'X' and i[-2:] == 'f3':
        Xf3 = cp.Variable(boolean=True)
        variable['Xf3'] = Xf3

    if i[0] == 'X' and i[-2:] == 'f4':
        Xf4 = cp.Variable(boolean=True)
        variable['Xf4'] = Xf4

    if i[0] == 'X' and i[-2:] == 'f5':
        Xf5 = cp.Variable(boolean=True)
        variable['Xf5'] = Xf5

    if i[0] == 'Y' and i[-2:] == 'm1':
        Ym1 = cp.Variable(boolean=True)
        variable['Ym1'] = Ym1
    
    if i[0] == 'Y' and i[-2:] == 'm2':
        Ym2 = cp.Variable(boolean=True)
        variable['Ym2'] = Ym2

    if i[0] == 'Y' and i[-2:] == 'm3':
        Ym3 = cp.Variable(boolean=True)
        variable['Ym3'] = Ym3

    if i[0] == 'Y' and i[-2:] == 'm4':
        Ym4 = cp.Variable(boolean=True)
        variable['Ym4'] = Ym4

    if i[0] == 'Y' and i[-2:] == 'm5':
        Ym5 = cp.Variable(boolean=True)
        variable['Ym5'] = Ym5

    if i[0] == 'Y' and i[-2:] == 't1':
        Yt1 = cp.Variable(boolean=True)
        variable['Yt1'] = Yt1
    
    if i[0] == 'Y' and i[-2:] == 't2':
        Yt2 = cp.Variable(boolean=True)
        variable['Yt2'] = Yt2

    if i[0] == 'Y' and i[-2:] == 't3':
        Yt3 = cp.Variable(boolean=True)
        variable['Yt3'] = Yt3

    if i[0] == 'Y' and i[-2:] == 't4':
        Yt4 = cp.Variable(boolean=True)
        variable['Yt4'] = Yt4

    if i[0] == 'Y' and i[-2:] == 't5':
        Yt5 = cp.Variable(boolean=True)
        variable['Yt5'] = Yt5

    if i[0] == 'Y' and i[-2:] == 'w1':
        Yw1 = cp.Variable(boolean=True)
        variable['Yw1'] = Yw1
    
    if i[0] == 'Y' and i[-2:] == 'w2':
        Yw2 = cp.Variable(boolean=True)
        variable['Yw2'] = Yw2

    if i[0] == 'Y' and i[-2:] == 'w3':
        Yw3 = cp.Variable(boolean=True)
        variable['Yw3'] = Yw3

    if i[0] == 'Y' and i[-2:] == 'w4':
        Yw4 = cp.Variable(boolean=True)
        variable['Yw4'] = Yw4

    if i[0] == 'Y' and i[-2:] == 'w5':
        Yw5 = cp.Variable(boolean=True)
        variable['Yw5'] = Yw5

    if i[0] == 'Y' and i[-3:] == 'th1':
        Yth1 = cp.Variable(boolean=True)
        variable['Yth1'] = Yth1
    
    if i[0] == 'Y' and i[-3:] == 'th2':
        Yth2 = cp.Variable(boolean=True)
        variable['Yth2'] = Yth2

    if i[0] == 'Y' and i[-3:] == 'th3':
        Yth3 = cp.Variable(boolean=True)
        variable['Yth3'] = Yth3

    if i[0] == 'Y' and i[-3:] == 'th4':
        Yth4 = cp.Variable(boolean=True)
        variable['Yth4'] = Yth4

    if i[0] == 'Y' and i[-3:] == 'th5':
        Yth5 = cp.Variable(boolean=True)
        variable['Yth5'] = Yth5

    if i[0] == 'Y' and i[-2:] == 'f1':
        Yf1 = cp.Variable(boolean=True)
        variable['Yf1'] = Yf1
    
    if i[0] == 'Y' and i[-2:] == 'f2':
        Yf2 = cp.Variable(boolean=True)
        variable['Yf2'] = Yf2

    if i[0] == 'Y' and i[-2:] == 'f3':
        Yf3 = cp.Variable(boolean=True)
        variable['Yf3'] = Yf3

    if i[0] == 'Y' and i[-2:] == 'f4':
        Yf4 = cp.Variable(boolean=True)
        variable['Yf4'] = Yf4

    if i[0] == 'Y' and i[-2:] == 'f5':
        Yf5 = cp.Variable(boolean=True)
        variable['Yf5'] = Yf5

variable1 = variable.copy()
expr = []
ex = []

for i in ABC:
    for k in variable1:
        if i == k[0]:
            ex.append(variable1[k])
    b = sum(ex)
    expr.append(b <= 1)
    ex = [] # OB 사람 제약식

for i in abc:
    for k in variable1:
        if i == k[0]:
            ex.append(variable1[k])
    b = sum(ex)       
    expr.append(b <= 1)
    ex = [] # 의무 사람 제약식 

for i in day:
    for k in variable1:
        if i == k[-2:]:
            ex.append(variable1[k])
        if i == k[-3:]:
            ex.append(variable1[k])
    b = sum(ex)       
    expr.append(b <= 1)
    ex = [] # 타임 제약식

for i in range(len(expr)):
    if True in expr:
        expr.remove(True)

for i in range(len(expr)):
    if False in expr:
        expr.remove(False)

obj_f = 0

for i in variable1:
    obj_f += variable1[i] # 목적함수 

obj = cp.Maximize(obj_f) # 균등 배치 최대화 문제 정의
prob1 = cp.Problem(obj, expr)
prob1.solve() # 균등 배치 최대화 문제 풀기

count = 0

a = list(variable1.values())

for i in range(len(a)):
    if a[i].value != 0:
        count += 1
        
one = []

print()
print()
print("=="*20)
if prob1.status=='optimal':
    print(f"균등 배치 status: {prob1.status}")
    print()
    print("optimal", count)
    print("optimal var")
    for i, j in zip(time, variable1.values()):
        if j.value != 0:
            one.append(i)
            print(f'{i}')
            
else:
    print(f"균등 배치 Wrong status: {prob1.status}")
print("=="*20)

table1 = df_maker(5, 5, '#')
col = ['M', 'T', 'W', 'Th', 'F']
ind = [1, 2, 3, 4, 5]
table1.columns = col
table1.index = ind

for i in variable1:
    if variable1[i].value != 0 and variable1[i].value != None:
        if i[-2:] == 'm1':
            table1.loc[1, 'M'] = i[0]
        if i[-2:] == 'm2':
            table1.loc[2, 'M'] = i[0]
        if i[-2:] == 'm3':
            table1.loc[3, 'M'] = i[0]
        if i[-2:] == 'm4':
            table1.loc[4, 'M'] = i[0]
        if i[-2:] == 'm5':
            table1.loc[5, 'M'] = i[0]
        if i[-2:] == 't1':
            table1.loc[1, 'T'] = i[0]
        if i[-2:] == 't2':
            table1.loc[2, 'T'] = i[0]
        if i[-2:] == 't3':
            table1.loc[3, 'T'] = i[0]
        if i[-2:] == 't4':
            table1.loc[4, 'T'] = i[0]
        if i[-2:] == 't5':
            table1.loc[5, 'T'] = i[0]
        if i[-2:] == 'w1':
            table1.loc[1, 'W'] = i[0]
        if i[-2:] == 'w2':
            table1.loc[2, 'W'] = i[0]
        if i[-2:] == 'w3':
            table1.loc[3, 'W'] = i[0]
        if i[-2:] == 'w4':
            table1.loc[4, 'W'] = i[0]
        if i[-2:] == 'w5':
            table1.loc[5, 'W'] = i[0]
        if i[-3:] == 'th1':
            table1.loc[1, 'Th'] = i[0]
        if i[-3:] == 'th2':
            table1.loc[2, 'Th'] = i[0]
        if i[-3:] == 'th3':
            table1.loc[3, 'Th'] = i[0]
        if i[-3:] == 'th4':
            table1.loc[4, 'Th'] = i[0]
        if i[-3:] == 'th5':
            table1.loc[5, 'Th'] = i[0]
        if i[-2:] == 'f1':
            table1.loc[1, 'F'] = i[0]
        if i[-2:] == 'f2':
            table1.loc[2, 'F'] = i[0]
        if i[-2:] == 'f3':
            table1.loc[3, 'F'] = i[0]
        if i[-2:] == 'f4':
            table1.loc[4, 'F'] = i[0]
        if i[-2:] == 'f5':
            table1.loc[5, 'F'] = i[0]

inp = []
on = []

for i in time:
    inp.append(i[0])
for i in one:
    on.append(i[0])

inpu = set(inp)
onne = set(on)
io = inpu - onne

print(table1) # 균등 배치 시간표 출력
print()
if len(io) != 0: print(f'미배치: {io}') 

variable2 = variable.copy()
expr = []
ex = []

for i in ABC:
    for k in variable2:
        if i == k[0]:
            ex.append(variable2[k])
    b = sum(ex)
    expr.append(b <= 1)
    ex = [] # ob 개인 제약식

for i in abc:
    for k in variable2:
        if i == k[0]:
            ex.append(variable2[k])
    b = sum(ex)       
    expr.append(b <= 1)
    ex = [] # 의무 개인 제약식 

for i in day:
    for k in variable2:
        if i == k[-2:]:
            ex.append(variable2[k])
        if i == k[-3:]:
            ex.append(variable2[k])
    b = sum(ex)       
    expr.append(b <= 1)
    ex = [] # 시간 제약식

for i in range(len(expr)):
    if True in expr:
        expr.remove(True)

for i in range(len(expr)):
    if False in expr:
        expr.remove(False)

obj_f = 0

for i in abc:
    parameter = 1
    for j in variable2:
        if i == j[0]:
            variable2[j] = parameter*variable2[j]
            parameter += 1 # 목적함수 계수 가중치

for i in ABC:
    parameter = 1
    for j in variable2:
        if i == j[0]:
            variable2[j] = parameter*variable2[j]
            parameter += 1 # 목적함수 계수 가중치
            
for i in variable2:
    obj_f += variable2[i] # 목적함수 

obj = cp.Maximize(obj_f) # 가중치 배치 최대화 문제 정의
prob2 = cp.Problem(obj, expr)
prob2.solve() # 가중치 배치 최대화 문제 풀기

count = 0

a = list(variable2.values())

for i in range(len(a)):
    if a[i].value != 0:
        count += 1

one = []  

print()
print()
print("=="*20)
if prob2.status=='optimal':
    print(f"가중치 배치 status: {prob2.status}")
    print()
    print("optimal", count)
    print("optimal var")
    for i, j in zip(time, variable2.values()):
        if j.value != 0:
            one.append(i)
            print(f'{i}') # 값이 1인 의사결정변수 출력
            
else:
    print(f"가중치 배치 Wrong status: {prob2.status}")
print("=="*20)

table2 = df_maker(5, 5, '#')
table2.columns = col
table2.index = ind

for i in variable2:
    if variable2[i].value != 0 and variable2[i].value != None:
        if i[-2:] == 'm1':
            table2.loc[1, 'M'] = i[0]
        if i[-2:] == 'm2':
            table2.loc[2, 'M'] = i[0]
        if i[-2:] == 'm3':
            table2.loc[3, 'M'] = i[0]
        if i[-2:] == 'm4':
            table2.loc[4, 'M'] = i[0]
        if i[-2:] == 'm5':
            table2.loc[5, 'M'] = i[0]
        if i[-2:] == 't1':
            table2.loc[1, 'T'] = i[0]
        if i[-2:] == 't2':
            table2.loc[2, 'T'] = i[0]
        if i[-2:] == 't3':
            table2.loc[3, 'T'] = i[0]
        if i[-2:] == 't4':
            table2.loc[4, 'T'] = i[0]
        if i[-2:] == 't5':
            table2.loc[5, 'T'] = i[0]
        if i[-2:] == 'w1':
            table2.loc[1, 'W'] = i[0]
        if i[-2:] == 'w2':
            table2.loc[2, 'W'] = i[0]
        if i[-2:] == 'w3':
            table2.loc[3, 'W'] = i[0]
        if i[-2:] == 'w4':
            table2.loc[4, 'W'] = i[0]
        if i[-2:] == 'w5':
            table2.loc[5, 'W'] = i[0]
        if i[-3:] == 'th1':
            table2.loc[1, 'Th'] = i[0]
        if i[-3:] == 'th2':
            table2.loc[2, 'Th'] = i[0]
        if i[-3:] == 'th3':
            table2.loc[3, 'Th'] = i[0]
        if i[-3:] == 'th4':
            table2.loc[4, 'Th'] = i[0]
        if i[-3:] == 'th5':
            table2.loc[5, 'Th'] = i[0]
        if i[-2:] == 'f1':
            table2.loc[1, 'F'] = i[0]
        if i[-2:] == 'f2':
            table2.loc[2, 'F'] = i[0]
        if i[-2:] == 'f3':
            table2.loc[3, 'F'] = i[0]
        if i[-2:] == 'f4':
            table2.loc[4, 'F'] = i[0]
        if i[-2:] == 'f5':
            table2.loc[5, 'F'] = i[0]

inp = []
on = []

for i in time:
    inp.append(i[0])
for i in one:
    on.append(i[0])

inpu = set(inp)
onne = set(on)
io = inpu - onne

print(table2) # 가중치 배치 시간표 출력
print()
if len(io) != 0: print(f'미배치: {io}') 

variable3 = variable.copy()
expr = []
ex = []

for i in ABC:
    for k in variable3:
        if i == k[0]:
            ex.append(variable3[k])
    b = sum(ex)
    expr.append(b <= 1)
    ex = [] # ob 개인 제약식

for i in abc:
    for k in variable3:
        if i == k[0]:
            ex.append(variable3[k])
    b = sum(ex)       
    expr.append(b == 1)
    ex = [] # 의무 개인 제약식 

for i in day:
    for k in variable3:
        if i == k[-2:]:
            ex.append(variable3[k])
        if i == k[-3:]:
            ex.append(variable3[k])
    b = sum(ex)       
    expr.append(b <= 1)
    ex = [] # 시간 제약식

for i in range(len(expr)):
    if True in expr:
        expr.remove(True)

for i in range(len(expr)):
    if False in expr:
        expr.remove(False)

obj_f = 0

for i in abc:
    parameter = 1
    for j in variable3:
        if i == j[0]:
            variable3[j] = parameter*variable3[j]
            parameter += 1 # 목적함수 계수 가중치

for i in ABC:
    parameter = 1
    for j in variable3:
        if i == j[0]:
            variable3[j] = parameter*variable3[j]
            parameter += 1 # 목적함수 계수 가중치
            
for i in variable3:
    obj_f += variable3[i] # 목적함수 

obj = cp.Maximize(obj_f) # 의무 우선 가중치 배치 최대화 문제 정의
prob3 = cp.Problem(obj, expr)
prob3.solve() # 의무 우선 가중치 배치 최대화 문제 풀기

count = 0

a = list(variable3.values())

for i in range(len(a)):
    if a[i].value != 0:
        count += 1

one = []  

print()
print()
print("=="*20)
if prob3.status=='optimal':
    print(f"의무 우선 가중치 배치 status: {prob3.status}")
    print()
    print("optimal", count)
    print("optimal var")
    for i, j in zip(time, variable3.values()):
        if j.value != 0:
            one.append(i)
            print(f'{i}') # 값이 1인 의사결정변수 출력
            
else:
    print(f"의무 우선 가중치 배치 Wrong status: {prob3.status}")
print("=="*20)

table3 = df_maker(5, 5, '#')
table3.columns = col
table3.index = ind

for i in variable3:
    if variable3[i].value != 0 and variable3[i].value != None:
        if i[-2:] == 'm1':
            table3.loc[1, 'M'] = i[0]
        if i[-2:] == 'm2':
            table3.loc[2, 'M'] = i[0]
        if i[-2:] == 'm3':
            table3.loc[3, 'M'] = i[0]
        if i[-2:] == 'm4':
            table3.loc[4, 'M'] = i[0]
        if i[-2:] == 'm5':
            table3.loc[5, 'M'] = i[0]
        if i[-2:] == 't1':
            table3.loc[1, 'T'] = i[0]
        if i[-2:] == 't2':
            table3.loc[2, 'T'] = i[0]
        if i[-2:] == 't3':
            table3.loc[3, 'T'] = i[0]
        if i[-2:] == 't4':
            table3.loc[4, 'T'] = i[0]
        if i[-2:] == 't5':
            table3.loc[5, 'T'] = i[0]
        if i[-2:] == 'w1':
            table3.loc[1, 'W'] = i[0]
        if i[-2:] == 'w2':
            table3.loc[2, 'W'] = i[0]
        if i[-2:] == 'w3':
            table3.loc[3, 'W'] = i[0]
        if i[-2:] == 'w4':
            table3.loc[4, 'W'] = i[0]
        if i[-2:] == 'w5':
            table3.loc[5, 'W'] = i[0]
        if i[-3:] == 'th1':
            table3.loc[1, 'Th'] = i[0]
        if i[-3:] == 'th2':
            table3.loc[2, 'Th'] = i[0]
        if i[-3:] == 'th3':
            table3.loc[3, 'Th'] = i[0]
        if i[-3:] == 'th4':
            table3.loc[4, 'Th'] = i[0]
        if i[-3:] == 'th5':
            table3.loc[5, 'Th'] = i[0]
        if i[-2:] == 'f1':
            table3.loc[1, 'F'] = i[0]
        if i[-2:] == 'f2':
            table3.loc[2, 'F'] = i[0]
        if i[-2:] == 'f3':
            table3.loc[3, 'F'] = i[0]
        if i[-2:] == 'f4':
            table3.loc[4, 'F'] = i[0]
        if i[-2:] == 'f5':
            table3.loc[5, 'F'] = i[0]

inp = []
on = []

for i in time:
    inp.append(i[0])
for i in one:
    on.append(i[0])

inpu = set(inp)
onne = set(on)
io = inpu - onne

print(table3) # 의무 우선 가중치 배치 시간표 출력
print()
if len(io) != 0: print(f'미배치: {io}') 

print()        
k=input("press close to exit")
