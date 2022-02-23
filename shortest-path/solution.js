const buildAdjacencyList = (edges) => {
    const adjList = {};
    for (let edge of edges) {
        const nodeA = edge[0];
        const nodeB = edge[1];
        if (nodeA in adjList) {
            adjList[nodeA].push(nodeB);
        } else {
            adjList[nodeA] = [nodeB];
        }

        if (nodeB in adjList) {
            adjList[nodeB].push(nodeA);
        } else {
            adjList[nodeB] = [nodeA];
        }
    };

    return adjList
}

const edges = [
    ['w', 'x'],
    ['x', 'y'],
    ['z', 'y'],
    ['z', 'v'],
    ['w', 'v']
  ];


const shortestPath = (edges, nodeA, nodeB) => {
    const adjList = buildAdjacencyList(edges);
    const queue = [[nodeA, 0]];

    const visited = new Set();

    while (queue.length > 0) {
        const current = queue.shift();
        if (current[0] == nodeB) {
            return current[1];
        }
        visited.add(current[0]);

        adjList[current[0]].forEach(element => {
            if (!visited.has(element)) {
                queue.push([element, current[1] + 1]);
            }
        });
    }

    return -1;
};

const path = shortestPath(edges, 'y', 'x');
console.log(path);