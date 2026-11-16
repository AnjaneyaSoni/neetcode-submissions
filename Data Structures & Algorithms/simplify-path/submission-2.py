
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for word in path.split('/'):
            if word == '..':
                if stack:
                    stack.pop()
            elif word not in ('', '.'):
                stack.append(word)

        return '/' + '/'.join(stack)
