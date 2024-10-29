import random 

# defining constants
TOTAL_NUMBERS:int = 10
MIN_LIMIT:int = 1
MAX_LIMIT:int = 100

def main():
    # Adding loop in the range of total number 
    for i in range(TOTAL_NUMBERS):
        number = random.randint(MIN_LIMIT, MAX_LIMIT) # generating random number
        print(f'Number {i+1}: {number}') # printing that number

if __name__ == '__main__':
    main()