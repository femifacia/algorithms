#!/usr/bin/env python

# I didn't code this solution. I found it from this url https://leetcode.com/problems/maximum-score-after-splitting-a-string/solutions/4438390/beats-100-explained-with-video-c-java-python-js-single-pass-visualized/
# It is really interesting because the Space complexity is O(1)
# This guy just count


class Solution(object):
    def maxScore(self, s):
        length = len(s)
        ones = 0
        tmpScore = 1 if s[0] == '0' else 0
        score = tmpScore
        
        for i in range(1, length - 1):
            if s[i] == '0':
                tmpScore += 1
            else:
                ones += 1
                tmpScore -= 1

            if tmpScore > score:
                score = tmpScore
        
        ones += 1 if s[length - 1] == '1' else 0

        return ones + score