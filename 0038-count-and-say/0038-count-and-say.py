Solution=type('',(),{'countAndSay':lambda _,n:reduce(lambda s,_:''.join(str(len([*x]))+_ for _,x in groupby(s)),range(n-1),'1')})
        