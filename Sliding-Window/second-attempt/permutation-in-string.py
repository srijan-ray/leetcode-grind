class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_alpha_dist = [0] * 26
        s2_alpha_dist = [0] * 26

        for i in range(len(s1)):
            s1_alpha_dist[ord(s1[i]) - ord('a')] += 1
            s2_alpha_dist[ord(s2[i]) - ord('a')] += 1

        if s1_alpha_dist == s2_alpha_dist:
            return True

        prev = 0
        for i in range(len(s1), len(s2)):
            prev_char_idx = ord(s2[prev]) - ord('a')
            s2_alpha_dist[prev_char_idx] -= 1

            obs_char_idx = ord(s2[i]) - ord('a')
            s2_alpha_dist[obs_char_idx] += 1

            if s1_alpha_dist == s2_alpha_dist:
                return True

            prev += 1

        return False
