def winPossibilitiesCounter(p,r):
    totalPossibilities = fight(p, 0, 0, p, r)
    return totalPossibilities % (10 ^ 9 + 7)
def fight(aryaWins,sansaWins,possibilities,p, r):
    if (aryaWins < sansaWins * p):
        return possibilities

    if (aryaWins + sansaWins == r):
        possibilities += 1
        return possibilities
    return fight(aryaWins + 1, sansaWins, possibilities, p, r) + fight(aryaWins, sansaWins + 1, possibilities, p, r)

def main():
    n = int(input())
    for _ in range(n):
        input_list = list(map(int,input().strip().split()))[:2]
        p = input_list[1]
        r = input_list[0]
        print(winPossibilitiesCounter(p,r))

main()

