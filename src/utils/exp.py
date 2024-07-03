import csv
import glob


def get_questions():
    test_question_path = "./docs/test_question.csv"
    filter_question = []

    with open(test_question_path) as question_file:
        rows = csv.reader(question_file)
        exist_document = set([path.split("/")[-1] for path in glob.glob("./testdata/*.md")])
        for row in rows:
            if row[-1] in exist_document:
                filter_question.append(row)

    print(f"There are {len(filter_question)} testing questions.")
    return filter_question


def write_ans(results):
    with open("./exp/exp.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(
            [
                "No.",
                " Questions",
                "Reference Answer",
                "The source documents'" "title",
                "rag_ans",
            ]
        )
        writer.writerows(results)
    print("done!")


def parse_answer(answer, metadata):
    content = f"{answer}\n Source: \n"

    for source in metadata[:3]:
        content += f"{source}\n"
    return content
