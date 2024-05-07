#include <iostream>
#include <unordered_set>

class Solution {
public:
    bool halvesAreAlike(std::string s) {
        std::unordered_set<char> set {'a', 'e', 'i', 'o', 'u', 'A', 'E','I','O', 'U'};
        int mid = s.length() / 2;
        int voy = 0;
        for (int i = 0; i < mid; i++) {
            if (set.find(s[i]) != set.end()) {
                voy+=1;
            }
            if (set.find(s[i + mid]) != set.end()) {
                voy-=1;
            }
        }
        return voy == 0;
    }
};