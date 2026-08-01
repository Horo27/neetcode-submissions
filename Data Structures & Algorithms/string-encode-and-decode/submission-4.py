class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return 'none'
        return '.!.'.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == 'none':
            return []
        return s.split('.!.')