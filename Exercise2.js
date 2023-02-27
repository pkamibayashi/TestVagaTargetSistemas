function verificaFibonacci(num) {
  let a = 0;
  let b = 1;
  let c = 0;

  while (c < num) {
    c = a + b;
    a = b;
    b = c;
  }

  if (c === num) {
    console.log(`${num} pertence à sequência de Fibonacci.`);
  } else {
    console.log(`${num} não pertence à sequência de Fibonacci.`);
  }
}
