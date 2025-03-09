from question_model import Question


class QuizBrain:
    def __init__(self, questions: list[Question]):
        self.question_number = 0
        self.questions_list = questions
        self.score = 0

    def next_question(self) -> None:
        question = self.questions_list[self.question_number]
        self.question_number += 1
        answer = input(
            f"Q.{self.question_number}: {question.question} (True/False): "
        ).lower()
        self.check_answer(answer, question.correct_answer)

    def still_has_questions(self) -> bool:
        return self.question_number < len(self.questions_list)

    def check_answer(self, answer, correct_answer) -> None:
        if answer == correct_answer.lower():
            self.score += 1
            print("Correct!")
        else:
            print("Incorrect!")
        print(f"The correct answer was {correct_answer}.")
        print(f"Current score: {self.score}/{self.question_number}\n")

    def final_score(self) -> None:
        print("You've completed the quiz!")
        print(f"Your final score was: {self.score}/{self.question_number}")
