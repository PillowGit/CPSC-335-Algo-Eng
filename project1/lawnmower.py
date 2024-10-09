
def lawnmower(disks):
    print(disks)
    n = len(disks) // 2
    for passes in range(n):
        if passes % 2 == 0: # Left to right
            for i in range(n*2-1):
                if disks[i] == 'X' and disks[i+1] == 'O':
                    disks[i], disks[i+1] = disks[i+1], disks[i]
        else: # Right to left
            for i in range(n*2-1, 0, -1):
                if disks[i] == 'O' and disks[i-1] == 'X':
                    disks[i], disks[i-1] = disks[i-1], disks[i]
        print(disks)
    return disks

def run():
    disks = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O']
    lawnmower(disks)

if __name__ == '__main__':
    run()
