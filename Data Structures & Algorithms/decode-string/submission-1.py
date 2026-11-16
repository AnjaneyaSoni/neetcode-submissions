
class Solution:
    def decodeString(self, s: str) -> str:
        parts = []

        for i, c in enumerate(s):
            prev = s[i-1] if i else ''

            if c == '[':
                parts.append('*(')
            elif c == ']':
                parts.append(')')
            elif c.isalpha():
                if prev == ']':
                    parts.append(f"+'{c}'")
                else:
                    parts.append(f"'{c}'")
            elif c.isdigit():
                if prev.isalpha() or prev == ']':
                    parts.append('+' + c)
                else:
                    parts.append(c)

        return eval(''.join(parts))
