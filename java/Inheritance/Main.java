/* Inheritance
 * https://stackoverflow.com/questions/51632152/what-does-possible-lossy-conversion-mean-and-how-do-i-fix-it
 */

interface Vehicle {
  void changeGear (byte newGear);
  void speedUp (int incrementFactor);
  void applyBrakes (int decrementFactor);
}

class Bicycle implements Vehicle {

  private int speed;
  private byte gear;

  public void changeGear(byte newGear) {
    System.out.println("Changing the gear!");
    gear = newGear;
  }

  public void speedUp(int incrementFactor) {
    speed = speed + incrementFactor;
  }

  public void applyBrakes(int decrementFactor) {
    speed = speed - decrementFactor;
  }

  public void printStates() {
    System.out.println("Speed: " + speed + " Gear: " + gear);
  }

}

class YetiBikes extends Bicycle {
  /* Add attributes and behavior specific to yetibikes */
}

public class Main {
  public static void main(String[] args) {
    YetiBikes bike1 = new YetiBikes();

    /* Checking Instances */
    // System.out.println(bike1 instanceof YetiBikes);
    // System.out.println(bike1 instanceof YetiBikes);
    // System.out.println(bike1 instanceof YetiBikes);

    /* Initial sate */
    System.out.println("Initial States:");
    bike1.printStates();

    /* Use interface */ 
    bike1.changeGear(1);
    bike1.speedUp(4);
    bike1.printStates();
  }
}
