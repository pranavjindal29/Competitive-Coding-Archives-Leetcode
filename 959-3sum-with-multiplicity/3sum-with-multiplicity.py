class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        arr.sort()
        n = len(arr)
        MOD = 1000000007

        result = 0
        for i in range(n-2):
            j = i+1
            k = n-1
            while j < k:
                total = arr[i] + arr[j] + arr[k]
                if total < target:
                    j +=1
                elif total > target:
                    k -=1
                else:
                    if arr[j] != arr[k]:
                        left_count, right_count = 1, 1
                        while j+1 < k and arr[j] == arr[j+1]:
                            left_count += 1
                            j+=1
                        while k-1 > j and arr[k] == arr[k-1]:
                            right_count += 1
                            k-=1
                        result += left_count * right_count 
                        j +=1
                        k -=1
                        
                    else:
                        count = k-j+1
                        result += count*(count - 1)//2 
                        break
                    
        return result% MOD
        