import java.util.HashMap;

public class LRUCache {

    private class Node {
        int key;
        int val;
        Node prev;
        Node next;

        Node(int key, int val) {
            this.key = key;
            this.val = val;
        }
    }

    private Node head;
    private Node tail;
    private int currentSize;
    HashMap<Integer, Node> cacheHash;

    public LRUCache(int capacity) {

        currentSize = 0;
        cacheHash = new HashMap<>();
    }

    public int get(int key) {
        if (cacheHash.containsKey(key)) {
            return cacheHash.get(key).val;
        } else {
            return -1;
        }
    }

    public void put(int key, int value) {
        if (cacheHash.containsKey(key)) {
            cacheHash.get(key).val = value;
        } else {

        }
    }
}
