#include <iostream>
#include <vector>
#include <map>

using namespace std;

class Solution
{
private:
    map<int, vector<int>> getAdjList(int n, vector<vector<int>> &edges)
    {
        map<int, vector<int>> adjList;
        for (int i = 0; i < n; i++)
        {
            vector<int> lst;
            adjList[i] = lst;
        }

        for (vector<int> &e : edges)
        {
            int node = e[0];
            adjList[e[0]].push_back(e[1]);
            adjList[e[1]].push_back(e[0]);
        }
        return adjList;
    }

    bool validPathRec(map<int, vector<int>> &adjList, int source, int destination)
    {
        if (source == destination) {
            return true;
        }

        vector<int> &neighbors = adjList[source];
        for(int i: neighbors) {
            if(validPathRec(adjList, i, destination)) {
                return true;
            }
        }
        
        return false;
    }

public:
    bool validPath(int n, vector<vector<int>> &edges, int source, int destination)
    {
        map<int, vector<int>> adjList = getAdjList(n, edges);
        return validPathRec(adjList, source, destination);
    }
};

int main()
{
    Solution sol;
    vector<vector<int>> v;
    v.push_back({0, 1});
    v.push_back({1, 2});
    v.push_back({2, 0});
    cout << sol.validPath(3, v, 0, 2) << endl;
    return 0;
}
