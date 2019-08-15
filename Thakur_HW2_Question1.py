#Rupin Singh Thakur
#1001651167

def cal_average(score1,score2,score3,score4,score5):
    average=(score1+score2+score3+score4+score5)/5
    return average

def determine_grade(score):
    if(score>=90):
        return 'A'
    elif(score>=80 and score<90):
        return 'B'
    elif(score>=70 and score<80):
        return 'C'
    elif(score>=60 and score<70):
        return 'D'
    else:
        return 'F'
def main():
    print("Enter the five scores")
    score1 = float(input(" Kindly Enter the first Score: "))
    score2 = float(input(" Kindly Enter the second Score: "))
    score3 = float(input(" Kindly Enter the third Score: "))
    score4 = float(input(" KIndly Enter the fourth Score: "))
    score5 = float(input(" KindlyEnter the fifth Score: "))

    avg_score=cal_average(score1,score2,score3,score4,score5)
    print("The average score is %.2f" %avg_score)

    for score in [score1,score2,score3,score4,score5]:
        print("The grade for %.2f is %s" %(score,determine_grade(score)))

main()


