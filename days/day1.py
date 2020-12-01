from termcolor import cprint

example_input = [1721,979,366,299,675,1456]

def run(real_input):
    input = real_input 
    
    part1 = next(a*b for a in input for b in input if a+b==2020)
    part2 = next(a*b*c for a in input for b in input for c in input if a+b+c==2020)

    cprint(f"Part1: {part1}\nPart2: {part2}", 'white')
