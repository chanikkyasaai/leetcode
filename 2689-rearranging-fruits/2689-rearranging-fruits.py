class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        count = Counter()
        for x in basket1:
            count[x] += 1
        for x in basket2:
            count[x] -= 1

        # Check if solution is possible
        for diff in count.values():
            if diff % 2 != 0:
                return -1

        # Separate extras from both baskets
        extra1 = []
        extra2 = []

        for val, diff in count.items():
            if diff > 0:
                extra1.extend([val] * (diff // 2))
            elif diff < 0:
                extra2.extend([val] * (-diff // 2))

        # Sort for cheapest swaps
        extra1.sort()
        extra2.sort(reverse=True)  # reverse for greedy smallest + largest pairing

        # Minimum fruit value globally
        global_min = min(basket1 + basket2)

        total_cost = 0
        for a, b in zip(extra1, extra2):
            direct_swap = min(a, b)
            via_global = 2 * global_min
            total_cost += min(direct_swap, via_global)

        return total_cost