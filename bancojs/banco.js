// const c = 1;
// const l = [
//   [0, 10],
//   [0, 10],
//   [1, 15],
//   [2, 10],
//   [30, 10]
// ];

function banco(c, l) {
    let caixas = Array(c).fill(0);
    let t_ultima_chegada = Array(c).fill(0);
    let resultado = 0;
    for (let i = 0; i < l.length; i++) {
      let [t, d] = l[i];
      let valor_melhor_caixa = Math.min(...caixas);
      let pos_melhor_caixa = caixas.indexOf(valor_melhor_caixa);
      caixas[pos_melhor_caixa] -= (t - t_ultima_chegada[pos_melhor_caixa]);
      valor_melhor_caixa = caixas[pos_melhor_caixa];
      if (valor_melhor_caixa > 20) {
        resultado += 1;
      }
      caixas[pos_melhor_caixa] += d;
      t_ultima_chegada[pos_melhor_caixa] = t;
    }
    return resultado;
}

module.exports = banco;