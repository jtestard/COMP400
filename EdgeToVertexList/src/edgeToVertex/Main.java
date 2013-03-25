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
		String name1 = System.getProperty("user.dir") + "/data/" + "edgelist.txt";
		String name2 = System.getProperty("user.dir") + "/data/" + "vertexList.graph";
		int numVertex =0;
		if (args.length==0) {
		} else if (args.length==1) {
			name1=args[0];
		} else if (args.length==2){
			name1=args[0];
			numVertex=Integer.valueOf(args[1]);			
		} else {
			name1=args[0];
			numVertex=Integer.valueOf(args[1]);			
			name2=args[2];
		}
		//Only for edgelist format.
		Graph graph = Graph.readFromEdgeList(name1,numVertex);
		graph.convertFormat(name2);
	}

}
