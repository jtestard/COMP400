/**
 * 
 */
package edgeToVertex;

import java.util.ArrayList;

/**
 * @author julestestard
 *
 */
public class Vertex {
	public ArrayList<Edge> edges;
	public long index;
	public long partition;
	
	public Vertex(long index) {
		this.index = index;
		this.edges = new ArrayList<Edge>();
		this.partition = 0;
	}
	
	public int degree() {
		return this.edges.size();
	}
}
