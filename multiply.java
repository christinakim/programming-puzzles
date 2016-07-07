import java.io.*;
import java.util.*;

/*
 * To execute Java, please define "static void main" on a class
 * named Solution.
 *
 * If you need more classes, simply define them inline.
 */

class Solution {
  public static void main(String[] args) {
    int n = 10;
    int array[] = new int []{2,5};
    System.out.println(multiply(n, array));
  }
  
  public static int multiply(int n, int[] arr){
    HashSet<Integer> multiples = new HashSet<Integer>();
    for (int i = 0; i < arr.length; i++){
      int k = 0;
      while (k < n && arr[i]*k < n){
        multiples.add(arr[i]*k);
        k++;
      }

    }

    int total = n - multiples.size();
    return total;

  }
}
