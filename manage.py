class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
    
        triangle = []


        if numRows < 1:
            return triangle

        trangle.append([1])

        i = 1
        while i < numRows:
            row = []

            row.append([1])

            x = 1

            while x <= i-1:

                row.append(triangle[i-1][x-1]+triangle[i-1][x])
                x += 1

            row.append(1)

            




         triangle.append(row)
            i+=1

        return triangle
