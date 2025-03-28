import random

indian_capitals = {
    'Andaman and Nicobar Islands': 'Port Blair',
    'Andhra Pradesh': 'Amaravati',
    'Arunachal Pradesh': 'Itanagar',
    'Assam': 'Dispur',
    'Bihar': 'Patna',
    'Chandigarh': 'Chandigarh',
    'Chhattisgarh': 'Raipur',
    'Dadra and Nagar Haveli and Daman and Diu': 'Daman',
    'Delhi': 'New Delhi',
    'Goa': 'Panaji',
    'Gujarat': 'Gandhinagar',
    'Haryana': 'Chandigarh',
    'Himachal Pradesh': 'Shimla',
    'Jammu and Kashmir': 'Srinagar (Summer), Jammu (Winter)',
    'Jharkhand': 'Ranchi',
    'Karnataka': 'Bengaluru',
    'Kerala': 'Thiruvananthapuram',
    'Ladakh': 'Leh',
    'Lakshadweep': 'Kavaratti',
    'Madhya Pradesh': 'Bhopal',
    'Maharashtra': 'Mumbai',
    'Manipur': 'Imphal',
    'Meghalaya': 'Shillong',
    'Mizoram': 'Aizawl',
    'Nagaland': 'Kohima',
    'Odisha': 'Bhubaneswar',
    'Puducherry': 'Puducherry',
    'Punjab': 'Chandigarh',
    'Rajasthan': 'Jaipur',
    'Sikkim': 'Gangtok',
    'Tamil Nadu': 'Chennai',
    'Telangana': 'Hyderabad',
    'Tripura': 'Agartala',
    'Uttar Pradesh': 'Lucknow',
    'Uttarakhand': 'Dehradun',
    'West Bengal': 'Kolkata'
}

for quizNum in range(31):
    quizFile = open("capitalsQuiz%s.txt" %(quizNum+1), "w")
    answerKeyFile = open("capitalsQuizAnswers%s.txt" %(quizNum+1), "w")

    quizFile.write("Name:\n\nDate:\n\n")
    quizFile.write((" "*20) + "State and UTs Capitals Quiz (Form %s)" %(quizNum+1))
    quizFile.write("\n\n")

    statesUTs = list(indian_capitals.keys())
    random.shuffle(statesUTs)

    for questionNum in range(len(indian_capitals)):
        correctAnswer = indian_capitals[statesUTs[questionNum]]
        wrongAnswers = list(indian_capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers,3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        quizFile.write("%s. What is the capital of %s?\n" %(questionNum+1, statesUTs[questionNum]))
        for i in range(4):
            quizFile.write('    %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
    
    quizFile.close()
    answerKeyFile.close()
