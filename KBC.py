
import random
import time

questionList = [
     {"question": "Who is the father of nation?",
     "option": ["A. Rabindra Nath Tagore", "B. Sharukh Khan", "C. Mahatma Gandhi", "D. GopalDas Ji"],
     "ans": "C"},   #1
  
    {"question": "National animal of India?",
     "option": ["A. Peacock", "B. Tiger", "C. Lion", "D. Hippo"],
     "ans": "B"},   #2

     {"question": "Which aircraft carrier was formerly known as Admiral Gorshkov?",
     "option": ["A. INS Vikrant", "B. INS Viraat", "C. INS Vikramaditya", "D. INS Vishal"],
     "ans": "C"},  #3

     {"question": "Who was the first woman to successfully climb K2, the world’s second highest mountain?",
     "option": ["A. Junko Tabei", "B. Chhurim Sherpa", "C. Wanda Rutkiewicz", "D. Edurne Pasaban"],
     "ans": "C"},  #4

     {"question": "Where in Singapore can you find the statue of a lion with the body of a fish?",
     "option": ["A. Sentosa Island", "B. Singapore Zoo", "C. Marina Bay", "D. Merlion Park"],
     "ans": "D"},  #5

     {"question": "Who is the first female officer in the Indian Navy to be posted as the Defence Attache at an Indian mission abroad?",
     "option": ["A. Pooja Sahay", "B. Shanti Pathak", "C. Pooja Thakur", "D. None of the above"],
     "ans": "D"},  #6

     {"question": "In India, what is the maximum permissible length of a train including the engine?",
     "option": ["A. 2.5 km", "B. 3.6 km", "C. 5.0 km", "D. 4.2 km"],
     "ans": "B"},] #7                                          


#Question for Flip Lifeline
Flip_Question={"question": "Which of these states has had the most number of its governors become Presidents of India?",
     "option": ["A. Bihar", "B. Maharashtra", "C. Uttar Pradesh", "D. West Bengal"],
     "ans": "A"}



amount = [10000, 50000 , 70000 , 120000 , 200000 , 500000 , 750000  ]   #list[1]

def lifeline_menu(lifeline_used):
    print("\nAvailable Lifelines:")
    if not lifeline_used["50:50"]:
        print("1. 50:50")
    if not lifeline_used["audience"]:
        print("2. Audience Poll")
    if not lifeline_used["flip"]:
        print("3. Flip the Question")

        choice = input("Enter lifeline number (or press Enter to skip): ").strip()
        return choice
    
    
def audience_poll(correct_option):
    print("\nAudience Poll Results:")
    correct_index = ["A", "B", "C", "D"].index(correct_option)
    percentages = [random.randint(10, 30) for _ in range(4)]
    percentages[correct_index] = random.randint(40, 80)
    total = sum(percentages)
    percentages = [int(p * 100 / total) for p in percentages]
    for i, option in enumerate(["A", "B", "C", "D"]):
        print(f"{option}: {percentages[i]}%")

def play_kbc():
    print("Deviyon aur sajjano, welcome to Kaun Banega Crorepati!\n")
    total_amount = 0
    lifeline_used ={"50:50": False, "audience": False, "flip": False}   # one use of lifeline
    player_name = input("Enter your name: ")

    for i, ques in enumerate(questionList):
        current_question = questionList[i]
        print(f"\nHere is Question {i + 1} for amount{amount[i]}")
        print(ques["question"])
        for j in ques["option"]:
            print(j)


      

         #Lifelines 
        use_life = input("Do you want to use Lifelines (Y/N): ").upper()
        if use_life == "Y":
            choice = lifeline_menu(lifeline_used)

            if choice == "1":
                if not lifeline_used["50:50"]:
                    lifeline_used["50:50"] = True
                    correct = ques["ans"]
                    correct_option = [opt for opt in ques["option"] if opt.startswith(correct)]
                    wrong_options = [opt for opt in ques["option"] if not opt.startswith(correct)]
                    print("Options after 50:50 Lifeline:")
                    print(correct_option[0])
                    print(wrong_options[0])
                else:
                    print("You've already used the 50:50 lifeline!")

            elif choice == "2":
                if not lifeline_used["audience"]:
                    audience_poll(ques["ans"])
                    lifeline_used["audience"] = True
                else:
                    print("You've already used the Audience Poll lifeline!")

            elif choice == "3":
                if not lifeline_used["flip"]:
                    lifeline_used["flip"] = True
                    print("Flipping question!")
                    ques = Flip_Question
                    print(f"\nNew Question:\n{ques['question']}")
                    for j in ques["option"]:
                        print(j)
                else:
                    print("You've already used the Flip the Question lifeline!")

       
         
            
          

         # Input Validation
        valid_options = ["A", "B", "C", "D"]
        while True:
         user_input = input("Enter your option (A/B/C/D): ").strip().upper()
         if user_input in valid_options:
            break
         else:
             print("Invalid input Please enter A, B, C, or D: ")
        

         #Main Logic
        if user_input == ques["ans"]:
            total_amount += amount[i]
            print(f"Sahi jawab! You won {total_amount}")
        else:
            total_amount = 0
            print("Galat jawab! Game Over." ,total_amount)
            break

    print(f"\nAapka total amount hai: {total_amount}")

   
    #For saving score
with open("kbc_scores.txt", "a") as file:
 file.write(f"Player won: total_amount\n")


#For Restart
while True:
    play_kbc()
    retry = input("\nDo you want to play again? (Yes/No): ").strip().lower()
    if retry not in ["yes", "y"]:
        print("Thank you for playing Kaun Banega Crorepati!")
        break       
    











  
