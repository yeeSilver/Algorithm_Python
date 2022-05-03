function mulNum(num) {
  if (num === 1) {
    return 1;
  }
  return num * mulNum(num - 1);
}

// console.log(5 * 4 * 3 * 2 * 1);
console.log(mulNum(5));

//왜 에러지 ...
