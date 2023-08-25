

def main():
    infile = open('United_States_COVID-19_Cases_and_Deaths_by_State_over_Time.csv', 'r')
    lines = infile.readlines()
    infile.close()
    for line in lines:
        print(line.rstrip())

main()
