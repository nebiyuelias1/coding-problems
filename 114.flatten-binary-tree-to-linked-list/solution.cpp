#include <bits/stdc++.h>

using namespace std;

struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode() : val(0), left(nullptr), right(nullptr) {}
     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    TreeNode* flattenRec(TreeNode* node) {
        if (node == nullptr) {
            return nullptr;
        }

        TreeNode* leftEnd = this->flattenRec(node->left);
        TreeNode* rightEnd = this->flattenRec(node->right);

        if (leftEnd == nullptr && rightEnd == nullptr) {
            return node;
        }

        if (leftEnd != nullptr && rightEnd != nullptr) {
            leftEnd->right = node->right;
            node->right = node->left;
            node->left = nullptr;
            return rightEnd;
        }

        if (leftEnd == nullptr) {
            return rightEnd;
        }

        if (rightEnd == nullptr) {
            node->right = node->left;
            node->left = nullptr;
            return leftEnd;
        }

        return nullptr;
    }
    
    void flatten(TreeNode* root) {
        this->flattenRec(root);
    }
};

int main(int argc, char const *argv[])
{
    TreeNode three {3};
    TreeNode four {4};
    TreeNode two {2, &three, &four};
    TreeNode six {6};
    TreeNode five {5, nullptr, &six};
    TreeNode one {1, &two, &five};

    Solution sol;
    sol.flatten(&one);
    return 0;
}