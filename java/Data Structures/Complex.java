package datastructures.util;

public class Complex {
  private int a, b;

  public Complex(int a, int b){
    this.a = a;
    this.b = b;
  }

  public Complex(int a) {
    this(a, a);
  }

  public Complex () {
    this(0);
  }

  public String toString() {
    return this.a + "+" + this.b + "i";
  }
}
