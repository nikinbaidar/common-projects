/* Problem Set 1: Query
 * ====================
 * Assumptions:
 * ------------
 * 1. 'heap' follows level property as well as partial order property.
 * 2. 'heap' may or may not have (internal) leaf nodes. 
 * 3. 'heap' is a max heap.
 * 4. All nodes in 'heap' have unique elements.
 *
 * **NOTE:** Nodes that do not have any offsprings are termed leaf nodes. So
 * all the nodes at the bottom most level are leaf nodes. But the assumption 2
 * suggests that there might be internal leaf nodes as well.
 *
 * Problems:
 * ---------
 * P1.1 [X] Given a binary heap with the write a method to return the total
 *          number of levels in the heap.
 *
 * P1.2 [X] Write a method that prints the elements in each level of the heap,
 *          also list all the leaf nodes in the heap.
 *
 * P1.3 [ ] Given an index number (key) find it's 
 *       - [X] level
 *       - [X] parent
 *       - [X] right child,
 *       - [X] left child,
 *       - [X] siblings 
 *       - [o] cousions: parent's sibling's child
 *       - [X] left sub-branch
 *       - [X] right sub-branch
 *       - [X] value
 *
 *
 * Problem Set 2: Insertion
 * ========================
 *
 * P2.1 [X] Count the number of leaf nodes in a heap.
 *
 * P2.2 [X] Build a MaxHeap from an heap that does not follow partial order.
 *
 *
 * Problem Set 3: Construction
 * ===========================
 *
 * P3.1 [X] Perform Heap sort. i.e. transform a heap into a Min-heap.
 * P3.2 [ ] Floyd's Variation.
 */

package datastructures.queues;

import java.util.Arrays;
import java.util.ArrayList;
import datastructures.util.Maths;


class Main {
  public static void main(String[] args) {
    // int [] x = { 100, 19, 36, 17, 12, 25, 5, 9, 15, 6, 11, 13, 8, 1, 4 };  
    int [] y = { 19, 36, 17, 12, 25, 100, 5, 9, 15, 30, 6, 11, 13, 8, 1 };  
    Heaps heap = new Heaps(y);
    heap.printHeap();
    heap.HeapSort();
  }
}

public class Heaps {

  static int [] heap;
  static int depth;

  Heaps(int [] heap) {
    this.heap = Arrays.copyOfRange(heap, 0, heap.length);
    depth = getNumLevels();
  }

  private int getNumLevels() {
    return Maths.ceil(Maths.log2(heap.length));
  }

  private static int iLevel(int key) {
    return Maths.floor(Maths.log2(key + 1));
  }

  private static int iParent(int key) {
    /* Root node does not have a parent. */
    if (key != 0) {
      return (key - 1) / 2;
    }
    return -1;
  }

  private static int iLeftChild(int key) {
    if ((2*key + 1) < heap.length)
      return (2*key + 1);
    return -1;
  }


  private static int iRightChild(int key) {
    if ((2*key + 2) < heap.length)
      return (2*key + 2);
    return -1;
  }


  private static int iSibling(int key) {
    if (key != 0) {
      if (Maths.isEven(key) && (key-1) < heap.length) { return (key-1); }
      if (Maths.isOdd(key)  && (key+1) < heap.length) { return (key+1); }
    }
    return -1;
  }


  private static boolean isLeafNode(int key) {
    return (iLeftChild(key) == iRightChild(key));
  }


  private static int[] getLeafNodes() {
    int leaf_count = Maths.ceil((heap.length + 1) / 2);
    return Arrays.copyOfRange(heap, (heap.length - leaf_count), heap.length);
  }


  private static void iSwap(int i, int j) {
    heap[i] = heap[i] - heap[j];
    heap[j] = heap[i] + heap[j];
    heap[i] = heap[j] - heap[i];
  }


 private static void buildMaxHeap() {
   for (int i = iParent(heap.length - 1); i >= 0; i--) {
     /* Repair the sub-heap whose root is at index "i". */
     siftDown(i);
   }
 }


 private static boolean exists(int node) {
   return node != -1;
 }


 protected static void siftDown(int root) {
     int parent, leftChild;

     while (exists(iLeftChild(root))) {
       /* Assume root node is the parent node. */
       parent = root;
       leftChild = iLeftChild(root);

       if (heap[parent] < heap[leftChild])
         parent = leftChild;

       if (exists(iRightChild(root)))
         if( heap[parent] < heap[leftChild + 1] )
           parent = leftChild + 1;

       if (parent == root)
         return;
       else 
         iSwap(root, parent);

       /* Whatever is swapped with the root becomes the new root. */
       root = parent;
     }
   }


 protected static void buildMaxHeap(int pseudoLength) {
   for (int i = iParent(pseudoLength - 1); i>=0; i--) {

     /* Siftdown. But now, if the root node contains a leftchild we also check
      * if its index is less than the "lastNode" in the Heap. This extra
      * condition opts for heap sorting where the heaps max element is shifted
      * with the lastNode. This lastNode may or may not be the true last node
      * of the heap and is sort of a hack that gives an impression that the max
      * element of the heap has been removed.
      */

     siftDown(i, pseudoLength - 1);

   }
 }


 public static boolean exists(int node, int lastNode) {
   return (exists(node) && node <= lastNode);
 }


 protected static void siftDown(int root, int pseudoLength) {
     int parent, leftChild;

     while (exists(iLeftChild(root), pseudoLength)) {
       /* Assume root node is the parent node. */
       parent = root;
       leftChild = iLeftChild(root);

       if (heap[parent] < heap[leftChild])
         parent = leftChild;

     if (exists(iRightChild(root), pseudoLength)) 
         if( heap[parent] < heap[leftChild + 1] )
           parent = leftChild + 1;

       if (parent == root)
         return;
       else 
         iSwap(root, parent);

       /* Whatever is swapped with the root becomes the new root. */
       root = parent;
     }
   }

  protected static void HeapSort() {

    int pseudoLength = heap.length;

    /* Print the input */
    System.out.println(Arrays.toString(heap));


    while(pseudoLength > 0) {
      buildMaxHeap(pseudoLength);
      iSwap(0, pseudoLength - 1);
      pseudoLength--;
    }

    /* Output */
    System.out.println(Arrays.toString(heap));
  }


  protected static void printHeap() {
    /* (i) We can find the number of nodes in each level of a binary tree by
     * raising 2 to the power of level#. (ii) The index of the left most node
     * on a particular level of the heap is obtained by subtracting one from
     * the #nodes, and (iii) the index of the right most node on a particular
     * level of the heap is obtained by doubling the index of the left most
     * node on that level.
     * For example, 
     * 
     * | Level# | #nodes | start | end |
     * |--------|--------|-------|-----|
     * | 0      | 1      | 0     | 0   |
     * | 1      | 2      | 1     | 2   |
     * | 2      | 4      | 3     | 6   |
     * | 3      | 8      | 7     | 14  |
     * | 4      | 16     | 15    | 30  |
     *
     * Approach 1:
     * -----------
     * One way to do this is to use a nested loop as follows:
      
     * for (int level=0; level < depth; level++) {
     *   leftmost_node = (int) Math.pow(2, level) - 1;
     *   rightmost_node = 2 * leftmost_node;
     *   for(int current_node = leftmost_node; 
     *       current_node <= rightmost_node; current_node++) {
     *     System.out.print(heap[current_node] + " ");
     *   }
     *   System.out.println();
     * }
     *
     * > This approach fails when the heap has internal leaf nodes.
     *
     * Instead of printing from start to end of a level, we keep priting
     * until a new level has been reached. 
     * This approach uses just a sinlge loop and a single loop is always better
     * than two. Thre are two approaches to do this:
     *
     * Approach 2:
     * -----------
     * Basically what we do is, rather than looking at the current level we
     * look at the level below. The leftmost node in the level below is given
     * by the (#nodes in the level below - 1).
     * If current_node = leftmost_node_below a new level has been attained.
     *
     *
     *  while (current_level < depth) {
     *    leftmost_node_below = (int) Math.pow(2, current_level+1) - 1;

     *    if (current_node < leftmost_node_below 
     *       && current_node < heap.length) { 
     *      // Level's rightmost node has not been reached yet. 
     *      System.out.print(heap[current_node] + " ");
     *      current_node++;
     *    }
     *    else{
     *      System.out.println();
     *      current_level++;
     *    }
     *  }
     *  System.out.println();
     */

    int current_level = 0;
    for (int current_node = 0; current_node < heap.length; current_node++) {
      if (iLevel(current_node) > current_level) {
        System.out.println();
        current_level++;
      }
      System.out.print(heap[current_node] + " ");
    }
    System.out.println('\n');
  }

  protected static void printLeaves() {
    System.out.println("LEAF NODES: " + Arrays.toString(getLeafNodes()) + "\n");
  }


  protected static void printRelatives(int key) {
    String [] relations = {
      "Current Node",
      "Parent",
      "Sibling",
      "Left Child",
      "Right Child"
    };

    int [] relatives = {
      key,
      iParent(key),
      iSibling(key),
      iLeftChild(key),
      iRightChild(key)
    };

    System.out.printf("| %12s | %5s | %5s | \n", "Relation", "Index", "Value");
    System.out.println("|--------------|-------|-------|");
    for(int i=0 ; i<relatives.length; i++) {
      System.out.printf("| %12s | %5d ", relations[i], relatives[i]);
      if (relatives[i] != -1)
        System.out.printf("| %5d |\n",  heap[relatives[i]]);
      else
        System.out.printf("| %5s |\n",  "None");
    }
    System.out.printf("\n");
  }


  protected static void printLeftSubTree(int key) {
    ArrayList<Integer> lsubtree = new ArrayList<Integer>();
    int left_child;
    lsubtree.add(heap[key]);
    while (true) {
      left_child = iLeftChild(key);
      if (left_child != -1) {
        lsubtree.add(heap[left_child]);
        key = left_child;
      }
      else
        break;
    }
    System.out.printf("%16s", "Left Sub Tree: ");
    System.out.println(lsubtree);
  }

  protected static void printRightSubTree(int key) {
    ArrayList<Integer> rsubtree = new ArrayList<Integer>();
    int right_child;
    rsubtree.add(heap[key]);
    while (true) {
      right_child = iRightChild(key);
      if (right_child != -1) {
        rsubtree.add(heap[right_child]);
        key = right_child;
      }
      else
        break;
    }
    System.out.println("Right Sub Tree: " + rsubtree);
  }






} 
