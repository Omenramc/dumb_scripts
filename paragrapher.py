def paragrapher(s_:str,plen_:int) -> str: 
    p_ = ""
    for i in range(0,len(s_),plen_):
        new_ = s_[i:i+plen_]
        p_ = p_ + "\n" + new_
    return p_

def paragrapher_2(s_:str,ren_:int) -> str: 
    p_ = ""
    s_ = s_ + " "
    indx = 0
    while len(p_)<len(s_):
        
        cut = indx
        for i in range(indx,len(s_)):
            if s_[i]==" " and i <= ren_+indx:
                cut = i
            elif i > ren_+indx and ren_+indx-cut > i-ren_-indx:
                cut = i
            elif i > ren_+indx+cut and cut>indx:
                break
        p_ = p_ + "\n" + s_[indx:cut]
        indx = cut + 1

    return p_
