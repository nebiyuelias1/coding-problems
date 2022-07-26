#include <bits/stdc++.h>

using namespace std;

class Solution {
    public:
    void breadthFirstTraversal(unordered_map<int, vector<int>> graph, int root) {
        vector<int> queue {root};
        set<int> visited;
        
        while(!queue.empty()) {
            int node = queue[0];
            queue.erase(queue.begin());
        

            if (visited.find(node) != visited.end()) {
                continue;
            }
            
            cout << node << endl;
            visited.insert(node);
            
            for (int i = 0; i < graph[node].size(); i++)
            {
                int newNode = graph[node][i];
                queue.push_back(newNode);
            }
        }
    }
};

int main(int argc, char const *argv[])
{
    unordered_map<int, vector<int>> v {
        {5, {8, 1, 12}},
        {8, {5, 12, 14, 4}},
        {12, {5, 8, 14}},
        {14, {8, 12, 4}},
        {4, {8, 14}},
        {1, {5, 7}},
        {7, {1, 16}},
        {16, {7}}
    };

    Solution s;
    s.breadthFirstTraversal(v, 5);
    return 0;
}
