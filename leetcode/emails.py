emails = ["j+ezsorqlmc@rfpycgjuf.com","j+k+ri+rigt.ad@rfpycgjuf.com","hfmeqzk.isx+i@fiidmdrsu.com","j+p+h+d+d+p+z.j.k.g@rfpycgjuf.com","zygekdy.l.w+s@snh.owpyu.com","j+m.l+ia+qdgv+w@rfpycgjuf.com","r+hwbjwefkp@wcjaki.n.com","zygekdy.l.w+d@snh.owpyu.com","bizdm+sz.f.a.k@il.cjjlp.com","hfmeqzk.isx+t@fiidmdrsu.com","hfmeqzk.isx+i@fiidmdrsu.com","bizdm+f+j+m.l.l@il.cjjlp.com","zygekdy.l.w+g@snh.owpyu.com","r+evgvxmksf@wcjaki.n.com","hfmeqzk.isx+h@fiidmdrsu.com","bizdm+lov+cy@il.cjjlp.com","hfmeqzk.isx+o@fiidmdrsu.com","bizdm+hs+qao@il.cjjlp.com","r+v+z+rcuznrj@wcjaki.n.com","j+r.kn+h.w.a.h+bh@rfpycgjuf.com","hfmeqzk.isx+t@fiidmdrsu.com","hfmeqzk.isx+a@fiidmdrsu.com","zygekdy.l.w+o@snh.owpyu.com","zygekdy.l.w+i@snh.owpyu.com","r+vy.u.y+f.er+aw@wcjaki.n.com","zygekdy.l.w+c@snh.owpyu.com","bizdm+wztzg@il.cjjlp.com","j+h.fwbsr+chp@rfpycgjuf.com","zygekdy.l.w+s@snh.owpyu.com","zygekdy.l.w+d@snh.owpyu.com","bizdm+qq.o.q+p@il.cjjlp.com","zygekdy.l.w+o@snh.owpyu.com","j+c+zqbq+h.dyt@rfpycgjuf.com","r+hl.b.i+fz.hz.t@wcjaki.n.com","r+cbabpf.k+w+e@wcjaki.n.com"]
adress = []
setmail = set(adress)

for line in range(len(emails)):
    
#make all mail one peace:
    piece = emails[line]

#find the place of "@" and "+" :
    loc = piece.index("@")
    clean = piece[:loc]
    piece_2 = piece[loc:]
    if "+" in clean:
        plus = piece.index("+")
        clean = clean.replace(clean[plus:],'')

#clean "." :
                
    if "." in clean:
        replace = clean.replace(".",'')
                
    else:
        replace = clean
#get them one peace again:
    adress = replace+piece_2

#make a new list:
    setmail.add(adress)
print(len(setmail))
print(setmail)