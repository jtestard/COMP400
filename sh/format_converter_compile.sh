#Compile
#javac -cp ../EdgeToVertexList/src ../EdgeToVertexList/src/edgeToVertex/Main.java

#Run
for i in {1000..20000..1000};   do      java -jar ../jar/convertE2V.jar ../storage/sparse/sparse$i.graph ../storage/vertex/sparse/sparse$i.graph;  done