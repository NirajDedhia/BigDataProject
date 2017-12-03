import java.io.BufferedReader;
import java.io.FileReader;
import java.util.*;

import weka.classifiers.Evaluation;
import weka.classifiers.trees.J48;
import weka.core.Instances;
import weka.core.Instance;
import weka.core.neighboursearch.*;

// Download weka-3.7.3.jar
// javac -cp weka-3.7.3.jar wekaJava.java 
// java -cp weka-3.7.3.jar: wekaJava

public class wekaJava {
	
    public static void main(String[] args) throws Exception {

        // Reading Cluster file
        BufferedReader br = new BufferedReader(new FileReader("cluster.arff"));
        Instances trainInstance = new Instances(br);
        int attributeCount = trainInstance.numAttributes() - 1;
        trainInstance.setClassIndex(attributeCount);
        br.close();

        // Building Classifier Model
        J48 nb = new J48();
        nb.buildClassifier(trainInstance);
        Evaluation eval = new Evaluation(trainInstance);
        eval.crossValidateModel(nb, trainInstance, 10, new Random(1));

        // Creating dictionary which stores movie name and Instance ID
        HashMap<String, Integer> movies = new HashMap<String, Integer>();
        for (int i = 0; i < trainInstance.size(); i++) {
			movies.put(trainInstance.get(i).toString(2), i);
		}

        // User Input
        Scanner in = new Scanner(System.in);
		//System.out.println("Enter your favorite movie name: ");
		// String movieName = in.nextLine();
        String movieName = "'Harry Potter and the Goblet of Fire'";
		int numberOfRecommendations = 10;
  
        // Provide Preferences
        int instanceId = Integer.parseInt( movies.get(movieName).toString() );
        displayRecommendations(trainInstance, instanceId, numberOfRecommendations);  
    }

    public static void displayRecommendations(Instances trained, int iId, int recom) throws Exception {
        LinearNNSearch linearNNSearch = new LinearNNSearch();
		linearNNSearch.setInstances(trained);
		Instance instance = trained.instance(iId);
        Instances recommendedInstances = linearNNSearch.kNearestNeighbours(instance, recom);
        for (int i = 0; i < recom; i++) {

			System.out.println(recommendedInstances.instance(i).stringValue(2));
        }
    }
}