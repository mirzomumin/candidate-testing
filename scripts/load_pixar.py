from testing.models import Test, Question, Option
import csv


def run():
    with open('apps/testing/data/test.csv') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            try:
                test, created = Test.objects.get_or_create(
                    title=row[1],
                    description=row[2],
                    duration_time=int(row[3]))

                question, created = Question.objects.get_or_create(
                    title=row[4],
                    point=int(row[5]),
                    difficulty=row[6],
                    test=test)

                option = Option(
                    title=row[7],
                    is_correct=bool(row[8]),
                    question=question
                )
                option.save()
            except Exception as e:
                print(e)