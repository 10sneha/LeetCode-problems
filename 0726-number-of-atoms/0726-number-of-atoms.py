class Solution:
    def countOfAtoms(self, formula: str) -> str:
        matcher = re.findall(r"([A-Z][a-z]*)(\d*)|(\()|(\))(\d*)",formula)
        matcher.reverse()

        map = defaultdict(int)

        stack = [1]
        mul = 1

        for atom, count, left, right, multiplier in matcher:
            if atom:
                if count:
                    map[atom] += int(count) * mul
                else:
                    map[atom] += 1 * mul     
            
            elif right:
                if not multiplier:
                    multiplier = 1
                else:
                    multiplier = int(multiplier)
                mul *= multiplier
                stack.append(multiplier)
            
            elif left:
                mul //= stack.pop()

        map = dict(sorted(map.items()))

        ans = ""
        for atom in map:
            ans += atom
            if map[atom] > 1:
                ans += str(map[atom])
        
        return ans