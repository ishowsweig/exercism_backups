//
// This is only a SKELETON file for the 'Triangle' exercise. It's been provided as a
// convenience to get you started writing code faster.
//


export class Triangle {

  constructor(...sides) {
    let [a, b, c] = sides
    this.a = a
    this.b = b
    this.c = c
  }

  isTriangle() {
    return (this.a > 0 && this.b > 0 && this.c > 0) && (this.a + this.b >= this.c && this.a + this.c >= this.b && this.b + this.c >= this.a)
  }
  
  get isEquilateral() {
    return this.isTriangle() && (this.a === this.b && this.b === this.c && this.a === this.c)
  }

  get isIsosceles() {
    return this.isTriangle() && (this.a === this.b || this.a === this.c || this.b === this.c)
  }

  get isScalene() {
    return this.isTriangle() && (this.a !== this.b && this.a !== this.c && this.b !== this.c)
  }
}
