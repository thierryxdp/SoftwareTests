def banco(c, l):
    caixas = [0] * c
    t_ultima_chegada = [0] * c
    resultado = 0
    for t,d in l:
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
    return resultado







# c_qtd_caixas, n_clientes = tuple(map(int, input().split()))
# caixas = [0] * c_qtd_caixas
# qtd_atrasos = 0

# for i in range(n_clientes):
#     t_fila, d_servico = tuple(map(int, input().split()))
    
#     #if 0 in caixas or t_fila > min(caixas): # se há algum caixa vazio
#     indice = caixas.index(min(caixas))
#     tempo_espera = min(caixas) - t_fila
#     caixas[indice] += d_servico - tempo_espera
    
#     if tempo_espera > 20:
#         qtd_atrasos += 1
        
# print(qtd_atrasos)
    