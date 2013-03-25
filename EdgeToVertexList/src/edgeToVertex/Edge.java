/**
 * 
 */
package edgeToVertex;

/**
 * @author julestestard
 *
 */
public class Edge {
	public Vertex v1;
	public Vertex v2;
	public int cost;
	/**
	 * @param v1
	 * @param v2
	 * @param cost
	 */
	public Edge(Vertex v1, Vertex v2, int cost) {
		this.v1 = v1;
		this.v2 = v2;
		this.cost = cost;
	}
	/* (non-Javadoc)
	 * @see java.lang.Object#toString()
	 */
	@Override
	public String toString() {
		return "Edge [v1=" + v1 + ", v2=" + v2 + ", cost=" + cost + "]";
	}
	
	public Vertex otherVertex(Vertex v) {
		if (v == v1) {
			return v2;
		} else if (v==v2) {
			return v1;
		} else {
			return null;
		}
	}
}
