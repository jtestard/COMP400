package edgeToVertex;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;

public class Graph {
	public HashMap<Long, Vertex> vertices;
	public ArrayList<Edge> edges;	

	public Graph() {
		vertices = new HashMap<Long, Vertex>();
		edges = new ArrayList<Edge>();
	}

	public void convertFormat(String filename) {
		try {
			BufferedWriter writer = new BufferedWriter(new FileWriter(filename));
			writer.write("%This is " + filename + "\n");
			System.out.println("Writing to file " + filename + "...");
			writer.write("\t"+vertices.size()+" "+edges.size()+"\n");
			for (Vertex v : vertices.values()) {
				String line = "";
				for (Edge e : v.edges) {
					line += "\t"+e.otherVertex(v).index;
				}
				writer.write(line + "\n");
			}
			writer.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	/**
	 * This method creates a graph from the given edge list.
	 * 
	 * @param filename
	 * @return
	 */
	public static Graph readFromEdgeList(String filename) {
		Graph graph = new Graph();
		try {
			BufferedReader reader = new BufferedReader(new FileReader(filename));
			String line;
			while ((line = reader.readLine()) != null) {
				String[] edgeLine = line.split(" ");
				if (edgeLine.length < 2) {
                                    continue;
                                }
                                if (edgeLine.length > 2) {
					throw new FormatException();
				}
				long n1 = Long.parseLong(edgeLine[0]);//edgeLine[0]
				long n2 = Long.parseLong(edgeLine[1]);
				// Add vertex to graph that is not already in vertices
				if (!graph.vertices.containsKey(n1)) {
					graph.vertices.put(n1, new Vertex(n1));
				}
				if (!graph.vertices.containsKey(n2)) {
					graph.vertices.put(n2, new Vertex(n2));
				}
				Edge edge = new Edge(graph.vertices.get(n1),
						graph.vertices.get(n2), 0);
				edge.v1.edges.add(edge);
				edge.v2.edges.add(edge);
				graph.edges.add(edge);
			}
			reader.close();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (FormatException e) {
			e.printStackTrace();
		} catch (NumberFormatException e) {
			e.printStackTrace();
		}
		return graph;
	}
}
