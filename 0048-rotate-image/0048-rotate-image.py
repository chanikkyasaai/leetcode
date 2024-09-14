class Solution:
    def rotate(self, List: List[List[int]]) -> None:
        # first we need to transpose the matrix

        for i in range(len(List)):
            for  j in range(len(List[0])):
                if i<j:
                    List[i][j], List[j][i] = List[j][i], List[i][j]
        
        for i in range(len(List)):
            for j in range(len(List[0]) // 2):
                ln = len(List[0])

                List[i][j], List[i][ln-j-1] = List[i][ln-j-1], List[i][j]

        