from http.client import responses
import random
import time
import os


#clears the screen
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    running = True
    while running:
        cls()
        print("Magic 8-Ball\nType [q] to quit\n")
        question = input("Ask the Magic 8-Ball anything: ").lower()
        if question == "q":
            running = False
            quit()
        else:
            questions_asked = 0
            cls()
            print("Magic 8-Ball is processing your question...")
            time.sleep(3)
            cls()
            print("Almost there...")
            time.sleep(1)
            cls()
            if questions_asked < 10:
                response = random.choice(open('responses.txt').readlines())
                questions_asked += 1
            if questions_asked >= 10 and questions_asked < 19:
                response = random.choice(open('irritated_responses.txt').readlines())
                questions_asked += 1
            if questions_asked == 19:
                response = random.choice(open('last_warning.txt').readlines())
            if questions_asked >= 20 and questions_asked < 25:
                response = random.choice(open('angry_responses.txt').readlines())
                questions_asked += 1
            if questions_asked >= 25:
                break
            print(response)
            time.sleep(4)
            main()

main()
