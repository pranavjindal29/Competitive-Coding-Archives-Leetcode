class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        ans = []
        left, right = 0, len(products) - 1

        for i in range(len(searchWord)):
            c = searchWord[i]
            res = []

            while left <= right and (len(products[left]) <= i or products[left][i] < c):
                left += 1
            while left <= right and (len(products[right]) <= i or products[right][i] > c):
                right -= 1

            for j in range(3):
                if left + j <= right:
                    res.append(products[left + j])
            ans.append(res)

        return ans