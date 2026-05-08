//
// This is only a SKELETON file for the 'Perfect Numbers' exercise. It's been provided as a
// convenience to get you started writing code faster.
//
const aliquot = (n) => {
  let sum = 0
  for (let i = 1; i < n; i++) {
    if (n % i === 0) {
      sum += i
    }
  }
  return sum
}
export const classify = (n) => {
  if (n <= 0) {
    throw new Error('Classification is only possible for natural numbers.')
  }
  const asum = aliquot(n)
  if (asum === n) {
    return 'perfect'
  }
  if (asum > n) {
    return 'abundant'
  } else {
    return 'deficient'
  }
};
