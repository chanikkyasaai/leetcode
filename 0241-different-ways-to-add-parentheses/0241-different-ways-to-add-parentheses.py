class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        memo = {}

        def compute(expression):
            # If the result for this expression is already computed, return it
            if expression in memo:
                return memo[expression]

            results = []

            # Try every operator in the expression
            for i in range(len(expression)):
                char = expression[i]
                if char in "+-*":
                    # Recursively compute results for left and right sub-expressions
                    left = compute(expression[:i])
                    right = compute(expression[i+1:])

                    # Combine the results from left and right using the current operator
                    for l in left:
                        for r in right:
                            if char == '+':
                                results.append(l + r)
                            elif char == '-':
                                results.append(l - r)
                            elif char == '*':
                                results.append(l * r)

            # If no operator is found, it means the expression is just a number
            if not results:
                results.append(int(expression))

            # Store the result in memoization cache
            memo[expression] = results
            return results

        # Start computing for the full expression
        return compute(expression)