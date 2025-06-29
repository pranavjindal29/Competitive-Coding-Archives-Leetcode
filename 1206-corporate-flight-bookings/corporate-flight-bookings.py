class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        arr=[0]*(n+2)
        for i,j,k in bookings:
            arr[i]+=k
            arr[j+1]-=k
        for i in range(1,len(arr)):
            arr[i]+=arr[i-1]
        return arr[1:n+1]
        