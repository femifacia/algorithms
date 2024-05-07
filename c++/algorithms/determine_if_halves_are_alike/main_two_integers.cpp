#include <iostream>
#include <unordered_set>

class Solution {
public:
    bool halvesAreAlike(std::string s) {
        std::unordered_set<char> set {'a', 'e', 'i', 'o', 'u', 'A', 'E','I','O', 'U'};
        int i = 0;
        int j = s.length() - 1;
        int voy = 0;
        while (i <= j) {
            if (set.find(s[i]) != set.end()) {
                voy+=1;
            }
            if (set.find(s[j]) != set.end()) {
                voy-=1;
            }
            i+=1;
            j-=1;
        }
        return voy == 0;
    }
};