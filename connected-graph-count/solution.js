const connectedComponentsCount = (graph) => {
  visited = new Set();
  count = 0;
  for (let key of Object.keys(graph)) {
    intKey = Number.parseInt(key);
    if (visited.has(intKey)) continue;

    stk = [intKey];
    while (stk.length > 0) {
      const current = stk.pop();
      if (visited.has(current)) continue;

      visited.add(current);
      for (neighbor of graph[current]) {
        stk.push(neighbor);
      }
    }
    count++;
  }
  return count;
};

count = connectedComponentsCount({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2],
});
console.log(count);
