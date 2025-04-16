def main():
    # solve_puzzle(2, 'L', 'R', 'M')
    solve_puzzle(4, 'L', 'R', 'M')
def solve_puzzle(n, start_tower, destination_tower, other_tower):
    # n is the number of rings
    # Example: solve_puzzle(3, 'L', 'R', 'M')
    # should print out instructions to move three rings
    # from the left tower to the right tower. 
    # solve_puzzle(3, 'M', 'L', 'R')
    # tells you how to move three rings from middle tower
    # to the left tower.
    
    if n == 1:
        print(start_tower, 'to', destination_tower)
    else:
        solve_puzzle(n-1, start_tower, other_tower, destination_tower)
        print(start_tower, 'to', destination_tower)
        solve_puzzle(n-1, other_tower, destination_tower, start_tower)
        
if __name__ == "__main__": 
    main()