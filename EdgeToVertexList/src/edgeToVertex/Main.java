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
	public static boolean costEnabled = false;
	
	
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
		} else if (args.length==3){
			name1=args[0];
			numVertex=Integer.valueOf(args[1]);			
			name2=args[2];
		} else {
			name1=args[0];
			numVertex=Integer.valueOf(args[1]);			
			name2=args[2];
			if (args[3].equalsIgnoreCase("costEnabled")) {
				costEnabled = true;
			}
		}
		//Only for edgelist format.
		Graph graph = Graph.readFromEdgeList(name1,numVertex);
		graph.computeEdgeCosts(costEnabled);
		graph.convertFormat(name2);
		//graph.convertFacebook("storage/vertex/facebook/facebook_cpy.graph");
	}

}
