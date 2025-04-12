class Solution:
    def factorial(self, number):
        chakra = 1
        for i in range(1, number + 1):
            chakra *= i
        return chakra

    def generatePalindromes(self, cloneID, index, validPalindromes, k):
        if index >= (len(cloneID) + 1) // 2:
            if int(cloneID) % k == 0:
                validPalindromes.append(cloneID)
            return

        if index != 0:
            temp = cloneID
            temp = temp[:index] + '0' + temp[index+1:]
            temp = temp[:len(temp) - index - 1] + '0' + temp[len(temp) - index:]
            self.generatePalindromes(temp, index + 1, validPalindromes, k)

        for digit in range(1, 10):
            temp = cloneID
            temp = temp[:index] + str(digit) + temp[index+1:]
            temp = temp[:len(temp) - index - 1] + str(digit) + temp[len(temp) - index:]
            self.generatePalindromes(temp, index + 1, validPalindromes, k)

    def countGoodIntegers(self, n, k):
        validPalindromes = []
        baseForm = "0" * n
        self.generatePalindromes(baseForm, 0, validPalindromes, k)
        
        chakraPatterns = set()

        for shadowClone in validPalindromes:
            frequency = ['0'] * 10
            for chakra in shadowClone:
                idx = int(chakra)
                if frequency[idx] == '9':
                    frequency[idx] = 'A'  # beyond 9 digits (special case)
                else:
                    frequency[idx] = str(int(frequency[idx]) + 1)
            chakraPatterns.add(''.join(frequency))

        basePermutations = self.factorial(n)
        totalCount = 0

        for pattern in chakraPatterns:
            permutation = basePermutations
            for freq in pattern:
                divisor = 10 if freq == 'A' else int(freq)
                permutation //= self.factorial(divisor)

            if pattern[0] != '0':
                zeroCount = int(pattern[0]) - 1
                zeroRestrictedPerm = self.factorial(n - 1)
                for freq in pattern[1:]:
                    divisor = 10 if freq == 'A' else int(freq)
                    zeroRestrictedPerm //= self.factorial(divisor)
                zeroRestrictedPerm //= self.factorial(zeroCount)
                permutation -= zeroRestrictedPerm

            totalCount += permutation

        return int(totalCount)