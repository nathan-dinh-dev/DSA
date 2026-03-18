class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        order = ["electronics", "grocery", "pharmacy", "restaurant"]
        rank = {b: i for i, b in enumerate(order)}

        def valid_code(s: str) -> bool:
            if not s:
                return False
            for ch in s:
                if not (ch.isalnum() or ch == "_"):
                    return False
            return True
        
        valid = []

        for c, b, a in zip(code, businessLine, isActive):
            if a and b in rank and valid_code(c):
                valid.append((rank[b], c))

        valid.sort(key=lambda x: (x[0], x[1]))
        return [c for _, c in valid]