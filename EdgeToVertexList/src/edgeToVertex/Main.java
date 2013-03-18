/**
 * 
 */
package edgeToVertex;

/**
 * @author julestestard
 *
 */
public class Main {
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		String name1 = System.getProperty("user.dir") + "/data/" + "default.txt";
		String name2 = System.getProperty("user.dir") + "/data/" + "partitions.graph";
		if (args.length==0) {
		} else if (args.length==1) {
			name1=args[0];
		} else {
			name1=args[0];
			name2=args[1];			
		}
		Graph graph = Graph.readFromEdgeList(name1);
		graph.convertFormat(name2);
	}

}
