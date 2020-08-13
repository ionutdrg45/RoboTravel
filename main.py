import math

A = [[0 for x in range(50)] for y in range(50)]
D = [[0 for x in range(50)] for y in range(50)]
T = [[0 for x in range(50)] for y in range(50)]
n = 0
reach = 0
d = 0
TR = [0]*50
b = 0
PInfinit = 1.e20


def read(file_name):
    global n
    f = open(file_name, "r")
    n = int(f.readline())
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                A[i][j] = 0
            else:
                A[i][j] = PInfinit
    for line in f:
        values = line.split()
        v1 = int(values[0])
        v2 = int(values[1])
        v3 = int(values[2])
        A[v1][v2] = v3
    f.close()


def road(i, j):
    global d
    k = 1
    found = 0
    while k <= n and found == 0:
        if i != k and j != k and A[i][j] == A[i][k] + A[k][j]:
            road(i, k)
            road(k, j)
            found = 1
        k += 1
    if found == 0:
        d = d + 1
        TR[d] = j


def write_road(ni, nf):
    global d
    global reach
    if A[ni][nf] < PInfinit:
        d = d + 1
        TR[d] = ni
        road(ni, nf)
        print("The robot can reach in zone marked with " + str(nf) + " with distance " + str(A[ni][nf]) + " with route ")
        reach = 1
    else:
        print("The robot cannot reach the zone marked with " + str(nf))


def roads_len():
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if A[i][j] > A[i][k] + A[k][j]:
                    A[i][j] = A[i][k] + A[k][j]


def show_dir():
    global reach
    if reach == 1:
        for i in range(1, d):
            if i == 1:
                print(str(TR[i]) + "--------|" + str(A[TR[i]][TR[i+1]]) + "|--------->" + str(TR[i+1]))
            else:
                print("--------|" + str(A[TR[i]][TR[i+1]]) + "|--------->" + str(TR[i+1]))


def create_space():
    k: int = 0
    for i in range(1, int(math.sqrt(n))+1):
        for j in range(1, int(math.sqrt(n))+1):
            k += 1
            T[i][j] = k


def move_robot(bz):
    global b
    global d
    if bz != d:
        b += 1
        for x in range(20):
            print()
        for i in range(1, int(math.sqrt(n)) + 1):
            for j in range(1, int(math.sqrt(n)) + 1):
                if T[i][j] == TR[b]:
                    print("R  ", end = " ")
                else:
                    print("*  ", end = " ")
            print()
        if b == d:
            print("The robot reached the zone " + str(TR[d]))
    else:
        print("The robot cannot move.")


nodf = input("Which zone do you want to reach?: ")

read("Traiectorie.txt")
roads_len()
write_road(1, int(nodf))
show_dir()
create_space()


while True:
    command = input("Type y to move the robot and any key to exit: ")
    if command == "y":
        move_robot(b)
    else:
        break