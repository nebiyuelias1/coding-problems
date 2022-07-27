#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool isValid(string s) {
        vector<char> stk;

        for (int i = 0; i < s.size(); i++)
        {
            char c = s[i];
            if (c == '(' || c == '[' || c == '{') {
                stk.push_back(c);
            } else {
                if (stk.size() <= 0) {
                    return false;
                }

                char stack_c = stk[stk.size() - 1];
                stk.pop_back();

                if (c == ')') {
                    if (stack_c != '(') {
                        return false;
                    }
                }

                if (c == ']') {
                    if ( stack_c != '[') {
                        return false;
                    };
                }

                if (c == '}') {
                    if ( stack_c != '{') {
                        return false;
                    }
                }
            }
        }

        return stk.size() == 0;
    }
};

int main(int argc, char const *argv[])
{
    Solution s;
    s.isValid("(){}}{");
    return 0;
}