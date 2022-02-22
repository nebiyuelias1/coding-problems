const largestComponent = (graph) => {
  const visited = new Set();
  let largest = 1;
  for (let key of Object.keys(graph)) {
      const count = countNodes(graph, key, visited);
      if (count > largest) {
          largest = count;
      }
  }

  return largest;
};

const countNodes = (graph, current, visited) => {
    if (visited.has(String(current))) return 0;

    visited.add(String(current));

    let count = 0
    graph[current].forEach(element => {
       count += countNodes(graph, element, visited);
    });

    return 1 + count;
}

const answer = largestComponent({
  0: ["8", "1", "5"],
  1: ["0"],
  5: ["0", "8"],
  8: ["0", "5"],
  2: ["3", "4"],
  3: ["2", "4"],
  4: ["3", "2"],
}); // -> 4
console.log(answer);