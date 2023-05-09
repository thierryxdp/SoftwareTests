def TipoTriangulo(a,b,c):
    # bsr
    if (
        a # abs, uoi/uod, svr
        <= 0 # ror, uoi na expressão lógica
        or # cor
        b # abs, uoi/uod, svr
        <= 0 # ror
        or # cor
        c # abs, uoi/uod, svr
        <= 0): # ror
        return "invalido" # bsr
	
    # bsr
    if (
        a+b # abs, uoi/uod, svr, aor
        >= # ror
        c # abs, uoi/uod, svr
        and # cor
        a+c # abs, uoi/uod, svr, aor
        >= # ror
        b # abs, uoi/uod, svr
        and # cor
        b+c # abs, uoi/uod, svr, aor
        >= # ror
        a): # abs, uoi/uod, svr
        
        # bsr
        
        if (
            a # abs, uoi/uod, svr
            == # ror
            b # abs, uoi/uod, svr
            and # cor
            b # abs, uoi/uod, svr
            == # ror
            c): # abs, uoi/uod, svr
            return "equilatero" #bsr
        
        #bsr
        
        if (
            a # abs, uoi/uod, svr
            == # ror
            b # abs, uoi/uod, svr
            or # cor
            a # abs, uoi/uod, svr
            == # ror
            c # abs, uoi/uod, svr
            or # cor
            b # abs, uoi/uod, svr
            == # ror
            c): # abs, uoi/uod, svr
            return "isosceles" #bsr
        return "escaleno" #bsr
    return "invalido" #bsr