function largestPrime(n) {
  for (let i = n - 1; i > 0; i -= 1000) {
    console.log("Iterating : ", i);
    if (n % i == 0) {
      console.log("Testing : ", i);
      if (isPrime(i)) {
        return i;
      }
    }
  }
}

function isPrime(n) {
  if (n == 1) {
    return false;
  }
  if (n >= 2 && n <= 3) {
    return true;
  }

  for (let i = 2; i < n; i++) {
    if (n % i == 0) {
      return false;
    }
  }
  return true;
}

console.log(largestPrime(600851475));
