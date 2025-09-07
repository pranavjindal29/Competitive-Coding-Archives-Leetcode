class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        userToLang = {u:{*langs} for u,langs in enumerate(languages, 1)}
        muteUsers = {u for f in friendships if not userToLang[f[0]]&userToLang[f[1]] for u in f}
        langCntr = Counter(lang for u in muteUsers for lang in userToLang[u])

        return len(muteUsers) - (langCntr and langCntr.most_common(1)[0][1] or 0)