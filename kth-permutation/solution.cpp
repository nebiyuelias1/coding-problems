#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int factorial(int n)
    {
        return (n == 1 || n == 0) ? 1 : factorial(n - 1) * n;
    }

    string getPermutation(int n, int k) {
        vector<int> digits;
        string sequence = "";
        for (int i = 1; i <=n; i++) {
            digits.push_back(i);
        }

        while(n > 0) {
            int fact = factorial(n);
            int length = fact / n;
            int index = (k-1) / length;
            int digit = digits.at(index);
            sequence += to_string(digit);
            digits.erase(digits.begin() + index);
            k = k - (index * length);
            n--;
        }
        return sequence;
    }
};

int main(int argc, char const *argv[])
{
    /* code */
    Solution sol;
    cout << sol.getPermutation(4, 9) << endl;
    return 0;
}
