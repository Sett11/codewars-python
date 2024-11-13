from collections import Counter

def get_key_length(s,n):
    r,m={},0
    for i in range(2,n+1):
        t=[]
        for j in range(i+1):
            x=s[j::i]
            c=Counter(x)
            t.append(sum(c[k]*(c[k]-1)/(len(x)*(len(x)-1)) for k in x))
        y=sum(t)/len(t)
        r[y]=i
        m=max(m,y)
    return r[m]

t='+vzf>=xsIzP/bqDKF/I8BvG\\vrfvi`vDPOy|zCIfD]I8wzG\\x8zSA/GHDJL+CzTfQ|ICIB\x0cU%COzBUrIOCM`boIyi[rHCzK+KwxDy\\bQCvP@vGf\'S|NwyBCUUCyBQ]E8{\'C zGfXy`ICGG UtoGGC.bHCzijzuzIC`v8xDN<vFfPL,IsvFy,CsfDLUywNfp)nmfKG/tsf`<<v8VGN<rpzOi0zDCzPubwIfyUtvDGB`vB`Ni[ruvUG\\v`f$LUinms\rU*qDzL|ztDxi\x0bDsMDA+E8yzQ-IwwzBUKvzf>=xsIzP/bqDKF/I8vNiuzAKJQ{zpGzi]w8OMy\\JzvOG]E?\n/F=J8MzN}KoODM\\bKvNi\\FHfyC{vFQzBBbQCvP@vGfWy,soBzi=J8FIM E8OJi<rJzfz`FyzIi+bJvMG+EHfJDUKvzfA=GvzMi+J8zvP@P8vNi"pjp\x0ci<FKzQC`{8Czi.zrI`RUGIwGG{y8CDQUNCMF\x0c8rGDNI=bsIOG`vzTfz`FyzfR<v8xDN<vFfvL.bDPwJ=Jvzyi|ysfOC-yBDLS/bwIfR<v8muR<bqzIR}IM\nf#~vBfwC:FFzfR<zG fR<FIBC\rUJCHzi{BwGGC.bqMTN|rBvGW{KGfxM}CrfJA-rGDJL+CzTfz`voFfR<v8xDN<vFfDLUKvzfp\'KvfxC\\KIMT~kzyDKC.zo|'
print(get_key_length(t,10))