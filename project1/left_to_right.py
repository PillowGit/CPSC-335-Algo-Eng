
def left_to_right(disks):
    n = len(disks) // 2
    print(disks)
    for passes in range(n):
        for i in range(n*2-1):
            if disks[i] == 'X' and disks[i+1] == 'O':
                disks[i], disks[i+1] = disks[i+1], disks[i]
        print(disks)
    return disks

def run():
    disks = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O']
    left_to_right(disks)

if __name__ == '__main__':
    run()
