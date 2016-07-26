public class TimeHashMap<Key, Time, Value> {

  private HashMap<Key, TreeMap<Time, Value>> map = new HashMap<Key, TreeMap<Time, Value>>();

  public Value get(Key key, Time time) {
    final TreeMap<Time, Value> redBlackBST = map.get(key);
    if (redBlackBST == null) return null;
    final Time floorKey = redBlackBST.floorKey(time);
    return floorKey == null ? null : redBlackBST.get(floorKey);
  }

  public void put(Key key, Time time, Value value) {
    if (!map.containsKey(key)) {
      map.put(key, new TreeMap<Time, Value>());
    }
    map.get(key).put(time, value);
  }

  public static void main(String args[]){
    TimeHashMap<String, Double, String> data = new TimeHashMap<String, Double, String>();
    data.put("K",1.0,"K1");
    data.put("K",2.0,"K2");
    System.out.println(data.get("K",0.9));
    System.out.println(data.get("K",1.0));
    System.out.println(data.get("K",1.5));
    System.out.println(data.get("K",2.0));
    System.out.println(data.get("K",2.2));
  }
}