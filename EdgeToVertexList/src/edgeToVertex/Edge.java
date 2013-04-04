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
		return (v1.index-1) + " " + (v2.index-1);
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
	
	@Override
	public boolean equals(Object o) {
		Edge e = (Edge) o;
		if (this.v1== e.v1 && this.v2 == e.v2) {
			return true;
		} else if (this.v2 == e.v1 && this.v1 == e.v2) {
			return true;
		} else {
			return false;
		}
	}
	
	@Override
	public int hashCode() {
		return (int)(v1.index+v2.index);
	}	
}
