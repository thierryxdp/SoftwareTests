const banco = require('./banco.js')

describe('banco', () => {
  it('teste do input 2', () => {
    const c = 3;
    const l = [
      [0 ,10],
      [0 ,10],
      [0 ,10],
      [3 ,10],
      [5 ,10],
      [7 ,10],
      [11, 10],
      [13, 10],
      [14, 10],
      [15, 10],
      [16, 10],
      [17, 10],
      [18, 3],
      [19, 10],
      [20, 10],
      [23, 3]
    ];
    const result = banco(c, l);
    expect(result).toEqual(2);
  });

  it('teste do input 1', () => {
    const c = 1;
    const l = [
      [0, 10],
      [0, 10],
      [1, 15],
      [2, 10],
      [30, 10]
    ];
    const result = banco(c, l);
    expect(result).toEqual(1);
  });
});