package edgeToVertex;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.LinkedHashMap;

public class Graph {
	public int vertexSize;
	public int edgeSize;
	public Vertex[] vertices;

	public Graph() {
		edgeSize = 0;
		vertexSize = 0;
	}

	public void convertFormat(String filename) {

		// write to file
		try {
			BufferedWriter writer = new BufferedWriter(new FileWriter(filename));
			writer.write("%This is " + filename + "\n");
			System.out.println("Writing to file " + filename + "...");
			writer.write("\t" + vertexSize + " " + edgeSize + "\n");
			for (int i = 0 ; i < vertexSize ; i++) {
				Vertex v = vertices[i];
				String line = "";
				if (v!=null) {
					for (Edge e : v.edges) {
						line += "\t" + e.otherVertex(v).index;
					}
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
				if (edgeLine.length < 1 ) {
					continue;
				}
				if (edgeLine.length == 1) {
					graph.vertexSize = Integer.parseInt(edgeLine[0]);
					graph.vertices = new Vertex[graph.vertexSize];
					continue;
				}
				if (edgeLine.length > 2) {
					throw new FormatException();
				}
				int n1 = Integer.parseInt(edgeLine[0])+1;// edgeLine[0]
				int n2 = Integer.parseInt(edgeLine[1])+1;
				if (!graph.vertexAdded(n1)) {
					graph.vertices[n1-1]=new Vertex(n1);
				}
				if (!graph.vertexAdded(n2)) {
					graph.vertices[n2-1]=new Vertex(n2);
				}
				Edge edge = new Edge(graph.vertices[n1-1],graph.vertices[n2-1],0);
				graph.vertices[n1-1].edges.add(edge);
				graph.vertices[n2-1].edges.add(edge);
				graph.edgeSize++;
//				// Add vertex to graph that is not already in vertices
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
	
	private boolean vertexAdded(long index) {
		for (Vertex v : vertices) {
			if (v!=null)
				if (v.index==index)
					return true;
		}
		return false;
	}
}