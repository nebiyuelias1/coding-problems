const exploreGraph = (grid, visited, row, column) => {
  if (row < 0 || row >= grid.length) {
    return 0;
  }
  if (column < 0 || column >= grid[0].length) {
    return 0;
  }

  if (grid[row][column] !== "L") {
    return 0;
  }

  const key = `${row},${column}`;
  if (visited.has(key)) {
    return 0;
  }

  visited.add(key);

  return (
    1 +
    exploreGraph(grid, visited, row - 1, column) +
    exploreGraph(grid, visited, row + 1, column) +
    exploreGraph(grid, visited, row, column - 1) +
    exploreGraph(grid, visited, row, column + 1)
  );
};

const minimumIsland = (grid) => {
  const visited = new Set();
  let minimumIslandCount = Number.MAX_SAFE_INTEGER;

  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[i].length; j++) {
      const key = `${i},${j}`;
      if (grid[i][j] == "L" && !visited.has(key)) {
        const count = exploreGraph(grid, visited, i, j);
        if (count < minimumIslandCount) {
            minimumIslandCount = count;
        }
      }
    }
  }

  return minimumIslandCount;
};

const grid = [
  ["W", "L", "W", "W", "W"],
  ["W", "L", "W", "W", "W"],
  ["W", "W", "W", "L", "W"],
  ["W", "W", "L", "L", "W"],
  ["L", "W", "W", "L", "L"],
  ["L", "L", "W", "W", "W"],
];

const answer = minimumIsland(grid); // -> 2

console.log(answer);
