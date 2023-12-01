
input_file = 'Day2.dat'



def part_one():
    return

def part_two():         
    return 


def main():
    with open('./inputs/' + input_file,'r') as f:
        f = f.read()
        data = [pair.replace('X', 'A').replace('Y','B').replace('Z','C').split(' ') for pair in f.split('\n')]

        print(part_one(data))
        print(part_two(data))


if __name__=="__main__":
    main()