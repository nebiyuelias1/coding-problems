const exploreGraph = (grid, visited, row, column) => {
  if (row < 0 || row >= grid.length) {
    return;
  }
  if (column < 0 || column >= grid[0].length) {
    return;
  }

  if (grid[row][column] !== "L") {
    return;
  }

  const key = `${row},${column}`;
  if (visited.has(key)) {
    return;
  }

  visited.add(key);

  exploreGraph(grid, visited, row - 1, column);
  exploreGraph(grid, visited, row + 1, column);
  exploreGraph(grid, visited, row, column - 1);
  exploreGraph(grid, visited, row, column + 1);
};

const islandCount = (grid) => {
  const visited = new Set();
  let islandCount = 0;

  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[i].length; j++) {
        const key = `${i},${j}`;
      if (grid[i][j] == "L" && !visited.has(key)) {
        exploreGraph(grid, visited, i, j);
        islandCount += 1;
      }
    }
  }

  return islandCount;
};

const grid = [
  ["L", "W", "W", "L", "W"],
  ["L", "W", "W", "L", "L"],
  ["W", "L", "W", "L", "W"],
  ["W", "W", "W", "W", "W"],
  ["W", "W", "L", "L", "L"],
];

const count = islandCount(grid);

console.log(count);
