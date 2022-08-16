#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
    bool existRec(vector<vector<char>> &board, string word, int i, int j)
    {
        if (word.size() == 0)
        {
            return true;
        }

        if (i < 0 || j < 0 || i >= board.size() || j >= board[0].size())
        {
            return false;
        }

        if (board[i][j] == '#')
        {
            return false;
        }

        char temp = board[i][j];
        if (board[i][j] == word[0])
        {
            board[i][j] = '#';
            bool hasSolution = this->existRec(board, word.substr(1), i + 1, j) ||
                               this->existRec(board, word.substr(1), i - 1, j) ||
                               this->existRec(board, word.substr(1), i, j + 1) ||
                               this->existRec(board, word.substr(1), i, j - 1);
            
            if (hasSolution) {
                return true;
            }
        }

        board[i][j] = temp;
        return false;
    }
    bool exist(vector<vector<char>> &board, string word)
    {
        int m = board.size();
        int n = board[0].size();

        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (board[i][j] == word[0] && this->existRec(board, word, i, j))
                {
                    return true;
                }
            }
        }
        return false;
    }
};

int main(int argc, char const *argv[])
{

    return 0;
}