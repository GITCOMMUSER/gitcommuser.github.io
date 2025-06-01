def gcd(p,q):
    #علیرضا شیخ ممو 4031531023
    if q==0: return p
    return gcd(q,p%q)