//2257C

#include <iostream>
#include <vector>
#include <unordered_set>

class Solution {
    int vertices;
    std::vector<std::vector<int>> nei;
    int damNodes;
    std::unordered_set<int> dams;

    std::vector<int> res;
public:
    void initialize() {
        std::cin >> vertices;
        nei = std::vector<std::vector<int>>(vertices);
        
        for (int i = 0; i < vertices - 1; ++i) {
            int parent;
            std::cin >> parent;
            nei[parent - 1].push_back(i + 1);
        }

        std::cin >> damNodes;
        dams.clear();

        for (int i = 0; i < damNodes; ++i) {
            int damVertex;
            std::cin >> damVertex;
            --damVertex;
            dams.insert(damVertex);
        }
    }


    bool dfs(int vertex) {
        bool hasDam = dams.find(vertex) != dams.end();
        std::vector<int> neighbors = nei[vertex];

        for (int i = 0; i < neighbors.size(); ++i) {
            if (!dfs(neighbors[i])) {
                continue;
            }
            
            if (!hasDam) {
                hasDam = true;
            } else {
                res.push_back(neighbors[i] + 1);
            }
        }

        return hasDam;
    }
    void solve() {
        res.clear();
        dfs(0);

        std::cout << res.size();
        for (int i: res) {
            std::cout << " " << i;
        }
        std::cout << std::endl;
    }
};

int main() {
    int n;
    std::cin >> n;
    Solution solution;
    for (int i = 0; i < n; ++i) {
        solution.initialize();
        solution.solve();
    }
    return 0;
}