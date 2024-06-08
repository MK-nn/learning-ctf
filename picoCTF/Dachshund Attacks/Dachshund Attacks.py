e = 82545667395339820184882572769860423857172762211235962550009482386899846265287055787478742045036922034581625740794303196770228607525145129503016553149427165818918429903337218013572625798481606001622430216185912937195829845163095077154244760959140941590427550727160940652491057353490817635090813062814214345761
n = 120386274133710272569186131246158702703508029573542560222709872826440188617847747213687885926307921185792297361891164667145223063542333699280529774095953759847220488310250112170133177339176392340120957437501015055112775106237325073110640374058826362862617636711280759898657911279852790792502284799508304927207
c = 65627203233114168923407527238982903338058157372084123001026376216947338614758786689043525673068964941824060852125294573080318865067914639295994659403165675591220427542513132776670679759978666518328659308537839838257168064266376266603661282793517400526663069586109667449728007761934813147923473536340700693255

import gmpy2
from Crypto.Util.number import long_to_bytes

def WienersAttack(n, e):
    r0, r1 = e, n
    k0, k1 = 0, 1
    d0, d1 = 1, 0

    i = 0
    while r1 != 0:
        q = r0 // r1
        r0, r1 = r1, r0 % r1
        k0, k1 = k1, q*k1 + k0
        d0, d1 = d1, q*d1 + d0

        if i % 2 == 0:
            k = k1 + k0
            d = d1 + d0
        else:
            k = k1
            d = d1

        i += 1
        if k == 0 or (e * d - 1) % k != 0:
            continue
        s = n - (e * d - 1) // k + 1
        D = s*s - 4*n
        sD = gmpy2.isqrt(D)
        if D > 0 and sD * sD == D:
            return d
    return -1

d = WienersAttack(n, e)

print(long_to_bytes(pow(c, d, n)).decode().strip())