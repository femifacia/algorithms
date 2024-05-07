#include <iostream>
#include <algorithm>

#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast", "inline", "ffast-math", "unroll-loops", "no-stack-protector")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,avx2,tune=native", "f16c")
static const auto UntieStream = []()
{ std::ios_base::sync_with_stdio(false); std::cin.tie(nullptr); std::cout.tie(nullptr); return 'c'; }();

class Solution {
public:
    int minSteps(std::string s, std::string t)
    {
        //uncomment the next line if you want speed at runtime but be carefull, it unite 0 and 1 fd. Check if
        // you don't know want this implie

        //UntieStream;
        int count[26] = {0};
        int ans = 0;

        for (int i = s.length() - 1; i >= 0; i--) {
            count[s[i] - 'a'] ++;
            count[t[i] - 'a']--;
        }
        for (int i = 0; i < 26; i++) {
            ans += std::max(count[i], 0);
        }
        return ans;
    }
};