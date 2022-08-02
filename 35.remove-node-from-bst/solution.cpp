#include <bits/stdc++.h>

using namespace std;

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution
{
private:
    TreeNode *root;

public:
    TreeNode *removeNode(TreeNode *node, TreeNode *parentNode)
    {

        if (parentNode == nullptr)
        {
            if (node->left == nullptr && node->right == nullptr)
            {
                node = nullptr;
                this->root = nullptr;
                return nullptr;
            }

            if (node->right != nullptr && node->left != nullptr)
            {
                TreeNode *current = node->right;
                while (current->left != nullptr)
                {
                    current = current->left;
                }
                current->left = node->left;
                this->root = node->right;
                return node->right;
            }
            else if (node->left == nullptr)
            {
                this->root = node->right;
                return node->right;
            }
            else if (node->right == nullptr)
            {
                this->root = node->left;
                return node->left;
            }
        }

        bool childIsOnLeftSideOfParent = node->val < parentNode->val;

        if (node->left == nullptr && node->right == nullptr)
        {
            if (childIsOnLeftSideOfParent) {
                parentNode->left = nullptr;
            } else {
                parentNode->right = nullptr;
            }
        }


        if (childIsOnLeftSideOfParent)
        {
            if (node->right != nullptr)
            {
                parentNode->left = node->right;
                TreeNode *current = node->right;
                while (current->left != nullptr)
                {
                    current = current->left;
                }
                current->left = node->left;
            }
            else
            {
                parentNode->left = node->left;
            }
        }
        else
        {
            if (node->left != nullptr && node->right != nullptr)
            {
                parentNode->right = node->right;
                TreeNode *current = node->right;

                while (current->left != nullptr)
                {
                    current = current->left;
                }
                current->left = node->left;
            }
            else if (node->left == nullptr)
            {
                parentNode->right = node->right;
            } else {
                parentNode->right = node->left;
            }
        }

        return nullptr;
    }

    TreeNode *deleteNodeRec(TreeNode *node, TreeNode *parentNode, int key)
    {
        if (node == nullptr)
        {
            return nullptr;
        }

        if (node->val == key)
        {
            return this->removeNode(node, parentNode);
        }

        if (key > node->val)
        {
            return this->deleteNodeRec(node->right, node, key);
        }
        else
        {
            return this->deleteNodeRec(node->left, node, key);
        }
    }

    TreeNode *deleteNode(TreeNode *root, int key)
    {
        this->root = root;
        this->deleteNodeRec(root, nullptr, key);
        return this->root;
    }
};

int main(int argc, char const *argv[])
{

    return 0;
}