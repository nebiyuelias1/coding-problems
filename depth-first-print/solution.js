const depthFirstPrintRec = (graph, node) => {
    console.log(node);

    graph[node].forEach(element => {
        depthFirstPrintRec(graph, element)
    });
}

const depthFirstPrint = (graph, node) => {
    const stack = [node];

    while(stack.length > 0) {
        const current = stack.pop();
        console.log(current);
        graph[current].forEach(element => {
            stack.push(element);
        });
    }
}

const breadthFirstPrint = (graph, node) => {
    const queue = [node];

    while (queue.length > 0) {
        const current = queue.shift();
        console.log(current);
        graph[current].forEach(element => {
            queue.push(element);
        });
    }
}

const graph = {
    a: ['b', 'c'],
    b: ['d'],
    c: ['e'],
    d: ['f'],
    e: [],
    f: [],
}

// depthFirstPrintRec(graph, 'a');
// depthFirstPrint(graph, 'a');
breadthFirstPrint(graph, 'a');