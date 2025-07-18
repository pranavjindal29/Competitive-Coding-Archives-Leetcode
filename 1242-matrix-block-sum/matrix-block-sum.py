class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
            
        h, w = len(mat), len( mat[0])
        integral_image = [ [ 0 for y in range(w) ] for x in range(h) ]
        

        for y in range(0, h):
            summation = 0
            
            for x in range(0, w):
                summation += mat[y][x]
                integral_image[y][x] = summation
                
                if y > 0:
                    integral_image[y][x] += integral_image[y-1][x]
        
        
        output_image = [ [ 0 for y in range(w) ] for x in range(h) ]
        
        for y in range(h):
            for x in range(w):
                
                min_row, max_row = max( 0, y-K), min( h-1, y+K)
                min_col, max_col = max( 0, x-K), min( w-1, x+K)
                
                output_image[y][x] = integral_image[max_row][max_col]
                
                if min_row > 0:
                    output_image[y][x] -= integral_image[min_row-1][max_col]
                
                if min_col > 0:
                    output_image[y][x] -= integral_image[max_row][min_col-1]
                    
                if min_col > 0 and min_row > 0:
                    output_image[y][x] += integral_image[min_row-1][min_col-1]
                
        return output_image