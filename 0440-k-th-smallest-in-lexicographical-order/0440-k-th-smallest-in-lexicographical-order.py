class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_prefix(curr, n):
            """Counts how many numbers are between `curr` and `curr + 1` lexicographically."""
            count = 0
            next_prefix = curr + 1
            while curr <= n:
                count += min(n + 1, next_prefix) - curr
                curr *= 10
                next_prefix *= 10
            return count

        curr = 1
        k -= 1  # We start from 1, so reduce k by 1 to use it as zero-based index

        while k > 0:
            count = count_prefix(curr, n)
            if k >= count:
                # Skip this entire subtree, move to the next sibling
                curr += 1
                k -= count
            else:
                # Go deeper into the subtree
                curr *= 10
                k -= 1  # We move to the next level, so decrease k by 1

        return curr
