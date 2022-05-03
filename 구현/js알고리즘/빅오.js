//Big O 표기법

function count(n) {
  console.log("올라간다");
  for (let i = 0; i < n; i++) {
    console.log(i);
  }
  console.log("내려간다");
  for (let j = n - 1; j >= n; j--) {
    console.log(j);
  }
}
function print(n) {
  for (const i = 0; i < n; i++) {
    for (const j = 0; j < n; j++) {
      console.log(i, j);
    }
  }
}
