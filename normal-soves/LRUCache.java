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
    private int capacity;
    HashMap<Integer, Node> cacheHash;

    public LRUCache(int capacity) {
        head = new Node(-1, 0);
        tail = new Node(-2, 0);
        head.next = tail;
        tail.prev = head;

        this.capacity = capacity;
        currentSize = 0;
        cacheHash = new HashMap<>();
    }

    public int get(int key) {
        if (cacheHash.containsKey(key)) {
            Node node = cacheHash.get(key);

            node.prev.next = node.next;
            node.next.prev = node.prev;

            node.prev = head;
            node.next = head.next;
            head.next.prev = node;
            head.next = node;
            return node.val;
        } else {
            return -1;
        }
    }

    public void put(int key, int value) {
        if (cacheHash.containsKey(key)) {
            Node node = cacheHash.get(key);
            node.val = value;

            node.prev.next = node.next;
            node.next.prev = node.prev;

            node.prev = head;
            node.next = head.next;
            head.next.prev = node;
            head.next = node;

        } else {
            Node node = new Node(key, value);

            node.prev = head;
            node.next = head.next;
            head.next.prev = node;
            head.next = node;

            cacheHash.put(key, node);

            if (cacheHash.size() > this.capacity) {
                int tailKey = tail.prev.key;
                tail.prev.prev.next = tail.prev.next;
                tail.prev.next.prev = tail.prev.prev;

                cacheHash.remove(tailKey);
            }
        }

    }

}
