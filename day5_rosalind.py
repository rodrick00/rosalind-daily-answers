def main():
    with open("rosalind_hamm.txt") as file:
        lines = file.read().strip().split("\n")
    s = lines[0]
    t = lines[1]
    print(hamm_dist(s,t))
def hamm_dist(s,t):
    count = 0 
    for a,b in zip(s,t):
        if a != b:
            count += 1
    return count
if __name__ == "__main__":
      main()