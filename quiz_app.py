questions = [
    ("What is the capital of Japan?", ["A. Beijing", "B. Tokyo", "C. Seoul", "D. Bangkok"], "B"),
    ("Who wrote Romeo and Juliet?", ["A. Charles Dickens", "B. William Shakespeare", "C. Jane Austen", "D. Mark Twain"], "B"),
    ("Which planet is known as the Red Planet?", ["A. Venus", "B. Jupiter", "C. Mars", "D. Mercury"], "C"),
    ("What is the largest mammal in the world?", ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Hippopotamus"], "B"),
    ("In which year did World War II end?", ["A. 1942", "B. 1945", "C. 1939", "D. 1950"], "B"),
    ("Which element has the chemical symbol 'O'?", ["A. Gold", "B. Oxygen", "C. Osmium", "D. Silver"], "B"),
    ("Who is known as the Father of Computers?", ["A. Charles Babbage", "B. Alan Turing", "C. John von Neumann", "D. Bill Gates"], "A"),
    ("What is the national sport of Japan?", ["A. Judo", "B. Karate", "C. Sumo Wrestling", "D. Baseball"], "C"),
    ("Which continent is the Sahara Desert located in?", ["A. Asia", "B. Africa", "C. Australia", "D. South America"], "B"),
    ("What is the currency of Germany?", ["A. Pound", "B. Dollar", "C. Euro", "D. Franc"], "C"),
    ("Who painted the Mona Lisa?", ["A. Vincent van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Michelangelo"], "C"),
    ("Which is the longest river in the world?", ["A. Amazon", "B. Nile", "C. Yangtze", "D. Mississippi"], "B"),
    ("Who was the first person to step on the Moon?", ["A. Buzz Aldrin", "B. Neil Armstrong", "C. Yuri Gagarin", "D. Michael Collins"], "B"),
    ("Which organ in the human body purifies blood?", ["A. Heart", "B. Liver", "C. Kidney", "D. Lungs"], "C"),
    ("In which country were the Olympic Games first held?", ["A. Italy", "B. Greece", "C. France", "D. China"], "B"),
    ("Which is the tallest mountain in the world?", ["A. K2", "B. Mount Everest", "C. Kangchenjunga", "D. Lhotse"], "B"),
    ("Who invented the telephone?", ["A. Alexander Graham Bell", "B. Thomas Edison", "C. Nikola Tesla", "D. Guglielmo Marconi"], "A"),
    ("Which gas do plants absorb during photosynthesis?", ["A. Nitrogen", "B. Oxygen", "C. Carbon Dioxide", "D. Hydrogen"], "C"),
    ("What is the smallest prime number?", ["A. 0", "B. 1", "C. 2", "D. 3"], "C"),
    ("Which country is called the 'Land of the Rising Sun'?", ["A. China", "B. Japan", "C. Thailand", "D. South Korea"], "B")
]


attempted = set()
points = 0


def show_question(points,i):
    if i in attempted:
        print("You already attempted this question!")
    else:
        attempted.add(i)
        print(f"Q{i+1}. {questions[i][0]} \n")
        for option in questions[i][1]:
            print(option)

        answer = input("Your answer: ")
        if answer.strip().upper() == questions[i][2]:
            print("Correct")
            points += 1
        else:
            print("Incorrect")
            points -= 1
    return points

for i in range(len(questions)):
    points=show_question(points,i)

print(f"You got {points} points.")
input("Press any button to continue.")
