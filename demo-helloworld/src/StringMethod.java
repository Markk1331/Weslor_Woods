public class StringMethod {
  public static void main(String[] args){

    // .lenth() method
    String ab = "Hi";
    ab = ab + " " + "I am Mark";
    System.out.println(ab);

    System.out.println(ab.length());

    System.out.println("a+a:" + ab.length());


    //.equals() method

    int a0 = 5 + 5;
    String a1 = String.valueOf(a0);
    String a2 = "10"; 

    
    boolean a1a2 = a1.equals(a2);

    System.out.println(a1a2);

    //.charAt() method

    String eee = "abcdefg";

    System.out.println(eee.charAt(2));





  }
}
