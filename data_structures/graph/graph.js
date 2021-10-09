class Graph {
    constructor(){
        this.vertices = [];
        this.edges = {};
        this.numberOfEdges = 0;
    }

    adVertex(vertex){
        this.vertices.push(vertex);        
        this.adEdges[vertex] = [];
    }

    removeVertex(vertext){
        const index = this.vertices.indexOf(vertext);
        this.vertices.splice(index, 1);
    }

    adEdges(vertex1, vertex2){        
        this.adEdges[vertex1].push([vertex1, vertex2]);
        this.adEdges[vertex2].push([vertex2, vertex1]);
        this.numberOfEdges++;
    }


    print(){
        console.log(this.vertices.map(x =>{
           return `${x} => ${this.adEdges[x].join(', ')}`; 
        }))
    }
}


(function test(){

    let grapth = new Graph();
    grapth.adVertex('Node1');
    grapth.adVertex('Node2');
    grapth.adVertex('Node3');
    grapth.adVertex('Node4');
    grapth.adVertex('Node5');

    grapth.adEdges('Node1', 'Node2');
    grapth.adEdges('Node1', 'Node3');
    grapth.adEdges('Node1', 'Node5');

    console.log(grapth);
    grapth.print();
})()