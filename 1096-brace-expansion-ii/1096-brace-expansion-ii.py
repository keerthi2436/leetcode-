class Solution:
    def braceExpansionII(self, expression):
        s = expression
        n = len(s)

        def union(a, b):
            return a | b

        def product(a, b):
            return {x + y for x in a for y in b}

        def parse_expr(i):
            res, i = parse_term(i)

            while i < n and s[i] == ',':
                cur, i = parse_term(i + 1)
                res = union(res, cur)

            return res, i

        def parse_term(i):
            res = {""}

            while i < n and s[i] not in '},':
                cur, i = parse_factor(i)
                res = product(res, cur)

            return res, i

        def parse_factor(i):
            if s[i] == '{':
                res, i = parse_expr(i + 1)
                return res, i + 1

            return {s[i]}, i + 1

        ans, _ = parse_expr(0)
        return sorted(ans)