from flask import request
import json
##########################
# GET Questions #
##########################

""" def get_questions_by_kc(name):
    kc = KC.objects(name=name).first()
    questions_obj = Question.objects(kc_list = kc)
    questions = [ques.question for ques in questions_obj ]
    correct_ans = [ques.correct_answer for ques in questions_obj ]
    options = [ques.options for ques in questions_obj]
    kc_object = [ques.kc_list for ques in questions_obj]

    kc_list = []
    for i in kc_object:
        kc = []
        for j in i:
            kc.append(j.name)
        kc_list.append(kc)

    kc_taxonomy = [ques.kc_taxonomy for ques in questions_obj]

    author_email = [ques.author_email for ques in questions_obj]
    QuestionType = [ques.QuestionType for ques in questions_obj]
    notes_teacher = [ques.notes_teacher for ques in questions_obj]
    notes_student = [ques.notes_student for ques in questions_obj]
    feedback_student = [ques.feedback_student for ques in questions_obj]
    question_disclosability = [
        ques.question_disclosability for ques in questions_obj]
    solution_disclosability = [
        ques.solution_disclosability for ques in questions_obj]



    return {"Questions" : questions, "answer": correct_ans, "Options": options, "kc" : kc_list, "kc_taxonomy" : kc_taxonomy, "author_email" : author_email,
            "QuestionType": QuestionType, "notes_teacher": notes_teacher, "notes_student" :notes_student, "feedback_student": feedback_student,
            "question_disclosability": question_disclosability, "solution_disclosability": solution_disclosability }

def get_questions_by_kc_taxonomy(level):
    taxonomy_level = level
    questions_obj = Question.objects(kc_taxonomy = taxonomy_level)
    questions = [ques.question for ques in questions_obj ]
    correct_ans = [ques.correct_answer for ques in questions_obj ]
    options = [ques.options for ques in questions_obj]

    return {"Questions" : questions, "answer": correct_ans, "Options": options}

def get_questions_by_course(name):
    course = Course.objects(name=name).first()
    questions_obj = Question.objects(course=course)
    questions = [ques.question for ques in questions_obj]
    correct_ans = [ques.correct_answer for ques in questions_obj]
    options = [ques.options for ques in questions_obj]

    return {"Questions": questions, "answer": correct_ans, "Options": options}
 """


class Download:
    def get_questions_by_selection(selections):
        for selection in selections:
            course = selection["course"]
            question = selection["question"]
            taxonomy = selection["taxonomy"]
            taxonomy_level = selection["taxonomy_level"]
            print(course, question, taxonomy, taxonomy_level)

