def f(x):
    return [len(x),-len([j for j in x if j.isupper()]),[ord(j) for j in x]]

def left(a,n):
    l,r=0,len(a)
    while r-l>1:
        m=(r+l)//2
        if f(a[m])<f(n):
            l=m
        else:
            r=m
    return l+1

def index_of(w,t):
    if w[0]==t:
        return 0
    return left(w,t)


print(index_of(['IO', 'Io', 'iO', 'io', 'SHQ', 'sHQ', 'Shq', 'shq', 'PYKNKL', 'PYKnKl', 'pykNkL', 'pyknkl', 'SGWJIUO', 'SGwJiUO', 'sgWjIuo', 'sgwjiuo', 'EFQDWDXS', 'EFQDwdXS', 'efqdWDxs', 'efqdwdxs', 'EYLFSKVHF', 'eyLFSkVHf', 'EYlfsKvhF', 'eylfskvhf', 'DUUROOAEWU', 'LDTQMQCVQC', 'dUUROOAEwU', 'LdTqmQCvQc', 'lDtQMqcVqC', 'DuurooaeWu', 'duurooaewu', 'ldtqmqcvqc'],'IO'))
print(index_of(['GQ', 'LC', 'Gq', 'Lc', 'gQ', 'lC', 'gq', 'lc', 'DNJ', 'HMS', 'IRL', 'UFX', 'XDO', 'HMs', 'dNJ', 'iRL', 'uFX', 'xDO', 'Dnj', 'Irl', 'Ufx', 'Xdo', 'hmS', 'dnj', 'hms', 'irl', 'ufx', 'xdo', 'FCMU', 'JDCL', 'RGEE', 'SCWQ', 'TAGL', 'TAPI', 'ZPGU', 'RGeE', 'ZPGu', 'JDcl', 'ScwQ', 'TAgl', 'jdCL', 'sCWq', 'taGL', 'rgEe', 'zpgU', 'fcmu', 'jdcl', 'rgee', 'scwq', 'tagl', 'tapi', 'zpgu', 'AFQXN', 'CXECX', 'HSYTZ', 'JQRGC', 'YJKGC', 'HSYtZ', 'JQRGc', 'YJkGC', 'afQXN', 'AFqxn', 'hsyTz', 'jqrgC', 'yjKgc', 'afqxn', 'cxecx', 'hsytz', 'jqrgc', 'yjkgc', 'BVOXXT', 'TUYPZO', 'VPUGDC', 'TuYPZO', 'bVOxXT', 'vPUGDc', 'BvoXxt', 'VpugdC', 'tUypzo', 'bvoxxt', 'tuypzo', 'vpugdc', 'FKDQEHF', 'FSROWOQ', 'PATXJDY', 'FKdQeHf', 'FSrOwoQ', 'PaTxJDy', 'fkDqEhF', 'fsRoWOq', 'pAtXjdY', 'fkdqehf', 'fsrowoq', 'patxjdy', 'FOKMYLSM', 'YIUSUMRT', 'YIUSUMrt', 'FokMYLsM', 'fOKmylSm', 'yiusumRT', 'fokmylsm', 'yiusumrt', 'FSQHLHXDD', 'GLXORXMXX', 'HWHIIUGPX', 'IPLYZLCID', 'SQMFVYCDX', 'WFPWONEYH', 'fSQHLhXDD', 'WfpWONEyH', 'glXOrXMXX', 'hWHIIUgPx', 'iPLyZlcID', 'sqMFVycDX', 'IplYzLCid', 'SQmfvYCdx', 'GLxoRxmxx', 'HwhiiuGpX', 'wFPwoneYh', 'FsqhlHxdd', 'fsqhlhxdd', 'glxorxmxx', 'hwhiiugpx', 'iplyzlcid', 'sqmfvycdx', 'wfpwoneyh', 'GFMVTIJYBI', 'HLUXXSWVVH', 'GFmVtIJYBI', 'HLuxxSWvVH', 'hlUXXswVvh', 'gfMvTijybi', 'gfmvtijybi', 'hluxxswvvh'],'DNJ'))
print(index_of(['cP', 'rE', 'sZ', 'am', 'bt', 'ev', 'hq', 'rx', 'yi', 'akC', 'nrcVpx', 'iKMVqsj'], 'akC'))
print(index_of(['JaCk', 'Jack', 'jack', 'jackk', 'COdewars', 'codeWars', 'abcdefgh', 'codewars', 'codewarsss'], 'codewars'))