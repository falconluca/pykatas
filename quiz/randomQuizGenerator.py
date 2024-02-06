#! python3
# randomQuizGenerator.py - 生成随机的测验试卷文件

import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford',
            'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
            'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka',
            'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis',
            'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
            'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City',
            'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'NewMexico': 'Santa Fe', 'New York': 'Albany',
            'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
            'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City',
            'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}


if __name__ == '__main__':
    totalQuiz = 2
    for quizNum in range(totalQuiz):
        # STEP1: Create the quiz and answer key files.
        quizFileName = f'quiz{quizNum+1}.txt'
        quizFile = open(quizFileName, 'w')
        answerFileName = f'answers{quizNum + 1}'
        answerFile = open(answerFileName, 'w')

        # STEP2: Write out the header for the quiz.
        # Name:
        #
        # Date:
        #
        # Period:
        #
        #                     State Capitals Quiz (Form 1)
        #
        quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
        quizFile.write(f'{(" "*20)}State Capitals Quiz (Form {quizNum+1})\n\n')

        # STEP3: Shuffle the order of the states.
        states = list(capitals.keys())
        random.shuffle(states)

        # STEP4: Loop through all 50 states, making a question for each.
        totalQuestion = 50
        for questionNum in range(totalQuestion):
            # Get right and wrong answers.
            correctAnswer = capitals[states[questionNum]]

            wrongAnswers = list(capitals.values())
            del wrongAnswers[wrongAnswers.index(correctAnswer)]
            wrongAnswers = random.sample(wrongAnswers, 3)  # 从该列表中选择 3 个随机的值

            answerOptions = wrongAnswers + [correctAnswer]
            random.shuffle(answerOptions)

            # Write the question and answer options to the quiz file.
            quizFile.write(f'{questionNum+1}. What is the capital of {states[questionNum]}?\n')
            for i in range(4):
                quizFile.write(f'{("ABCD"[i])}. {answerOptions[i]}\n')
            quizFile.write('\n')

            # Write the answer key to a file.
            answerFile.write(f'{questionNum + 1}. {"ABCD"[answerOptions.index(correctAnswer)]}\n')  # 在随机排序的答案选项中，找到正确答案的整数下标

        quizFile.close()
        answerFile.close()


