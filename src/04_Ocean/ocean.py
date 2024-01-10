import sys
from typing import List
from collections import defaultdict

class Ocean:
    state: List[List[int]]

    def __init__(self, init_state: List[List[int]]):
        self.state = init_state

    def __str__(self) -> str:
        return "\n".join(["".join(str(el) for el in row) for row in self.state])

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.state!r})"

    def gen_next_quantum(self) -> "Ocean":
        nstate=[[0 for i in range(len(self.state[0]))] for j in range(len(self.state))]
        zeros=[0 for i in range(len(self.state[0])+2)]
        for i in self.state:
            i.append(0)
            i.insert(0,0)
        self.state.insert(0,zeros)
        self.state.append(zeros)
        def zero():
            return 0
        
        print(self.state)
        for i in range(1,len(self.state)-1):
            for j in range(1,len(self.state[0])-1):
                count=defaultdict(zero)
                for ii in (i-1,i,i+1):
                    for jj in (j-1,j,j+1):
                        if ii!=i or jj!=j:
                            count[self.state[ii][jj]]+=1
        
                if self.state[i][j]==0:
                    if count[2]==3:
                        nstate[i-1][j-1]=2
                    elif count[3]==3:
                        nstate[i-1][j-1]=3
                elif self.state[i][j]==2:
                    if count[2]==2 or count[2]==3:
                        nstate[i-1][j-1]=2
                    else:
                        nstate[i-1][j-1]=0
                elif self.state[i][j]==1:
                    nstate[i-1][j-1]=1
                elif self.state[i][j]==3:
                    if count[3]==2 or count[3]==3:
                        nstate[i-1][j-1]=3
                    else:
                        nstate[i-1][j-1]=0

        return Ocean(nstate)


if __name__ == "__main__":
    n_quantums = int(sys.stdin.readline())
    n_rows, n_clms = (int(i) for i in sys.stdin.readline().split())
    init_state = []
    for i in range(n_rows):
        line = [int(i) for i in sys.stdin.readline().split()]
        init_state.append(line)

    ocean = Ocean(init_state=init_state)
    for _ in range(n_quantums):
        ocean = ocean.gen_next_quantum()
    print(ocean)