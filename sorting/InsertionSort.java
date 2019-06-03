/*
  Simple insertion sort algorithm. This will sort
  an array of objects that extend from the Comparable interface

  The sorting logic is a minor derivative of the traditional
  insertion sort algorithm typically taught in CS courses but essentially
  does the exact same thing.

  methods: sort_asc()
           sort_dsc()

  author: Manish Suthar
*/
import java.util.Arrays;

public final class InsertionSort{

  public <K extends Comparable<K>> void sort_asc(K[] toSort){

    for (int i = 0; i < toSort.length-1; i++){
      int j = i + 1;

      while (j > 0 && ( toSort[j].compareTo(toSort[j-1]) < 0) ) {

        K temp = toSort[j];
        toSort[j] = toSort[j-1];
        toSort[j-1] = temp;
        j--;

      }
    }
  }

  public <K extends Comparable<K>> void sort_dsc(K[] toSort){

    for (int i = 0; i < toSort.length-1; i++){
      int j = i + 1;

      while (j > 0 && ( toSort[j].compareTo(toSort[j-1]) > 0) ) {

        K temp = toSort[j];
        toSort[j] = toSort[j-1];
        toSort[j-1] = temp;
        j--;

      }
    }
  }

  public static void main(String[] args){

    InsertionSort is = new InsertionSort();
    Integer[] data = new Integer[]{50,-2,1,4,3};
    System.out.println("\nUnsorted: " + Arrays.toString(data));
    is.sort_asc(data);
    System.out.println("Ascending: " + Arrays.toString(data));
    is.sort_dsc(data);
    System.out.println("Descending: " + Arrays.toString(data) + "\n");
    
  }
}
