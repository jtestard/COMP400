#Run
for i in {1000..20000..1000};   do      java -jar jar/convertE2V.jar storage/edgelist/sparse/sparse$i.graph $i storage/vertex/sparse/sparse$i.graph;  done