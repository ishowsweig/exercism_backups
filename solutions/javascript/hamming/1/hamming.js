//
// This is only a SKELETON file for the 'Hamming' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const compute = (a, b) => {
  if (a.length !== b.length) {
    throw new Error("strands must be of equal length")
  }
  let distance = 0
  for (let i = 0; i < a.length; i++) {
    if (a[i] !== b[i]) {
      distance++
    }
  }
  return distance
};
