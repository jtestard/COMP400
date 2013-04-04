#Run
if [[ -z $1 ]]
then
	"You should add an argument for the type of graph you want, i.e. barabasi, sparse, dense, metric or random."
else
	for i in {1000..41000..10000};   do      java -jar jar/convertE2V.jar storage/edgelist/$1/$1$i.graph $i storage/vertex/$1/$1$i.graph;  done
	for i in {1000..41000..10000};   do      java -jar jar/convertE2V.jar storage/edgelist/$1/$1$i.graph $i storage/vertexEdgeCosts/$1/$1$i.graph costEnabled;  done
fi
