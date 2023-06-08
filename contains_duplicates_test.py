from contains_duplicates import duplicates

def main():
    print("For array nums: [1,2,3,1], there are duplicates is " + str(duplicates([1,2,3,1])))
    print("For array nums: [] there are duplicates is " + str(duplicates([])))
    print("For array nums: [1] there are duplicates is " + str(duplicates([1])))
    print("For array nums: ['f','f','g',k'] there are duplicates is " + str(duplicates(['f','f','g','k'])))
    print("For array nums: ['f','r','g',k'] there are duplicates is " + str(duplicates(['f','r','g','k'])))
    print("For array nums: [1,1,1,3,3,4,3,2,4,2] there are duplicates is " + str(duplicates([1,1,1,3,3,4,3,2,4,2])))

main()