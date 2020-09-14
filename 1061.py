d = input().split()[1]
h,m,s = input().split(' : ')
df = input().split()[1]
hf,mf,sf = input().split(' : ')

s = int(s)
sf = int(sf)
m = int(m)
mf = int(mf)
h = int(h)
hf = int(hf)
d = int(d)
df = int(df)

s = sf - s
m = mf - m
h = hf - h
d = df - d

if (s < 0) :
    s = s+60
    m=m-1


if (m < 0) :
    m = m+60
    h=h-1


if (h < 0) :
    h = h+24
    d=d-1
    
if(d>=0 and h>=0 and m>=1 and s>=0):
    print('{} dia(s)\n{} hora(s)\n{} minuto(s)\n{} segundo(s)'.format(d, h, m, s))