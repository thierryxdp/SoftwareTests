c, n = tuple(map(int, input().split()))
caixas = [0] * c
t_ultima_chegada = [0] * c
resultado = 0

for i in range(n):
    t,d = tuple(map(int, input().split()))
    valor_melhor_caixa = min(caixas)
    pos_melhor_caixa = caixas.index(valor_melhor_caixa)
    #print(t - t_ultima_chegada[pos_melhor_caixa])
    caixas[pos_melhor_caixa] -= (t - t_ultima_chegada[pos_melhor_caixa])
    valor_melhor_caixa = caixas[pos_melhor_caixa]
    if (valor_melhor_caixa > 20):
        resultado += 1
    caixas[pos_melhor_caixa] += d
    t_ultima_chegada[pos_melhor_caixa] = t
    #print(caixas[pos_melhor_caixa])
    
print(resultado)