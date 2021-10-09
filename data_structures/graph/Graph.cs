using System.Collections.Generic;

public class Graph {

    private List<List<Node>> _adjList;
    public Graph(){
        this._adjList = new List<List<Node>>();
    }

    public void AddNode(Node node){
        this._adjList.Add(new List<Node>(){node});
    }
}


class Node {

}