import random

from fpdf import FPDF, XPos, YPos

import question_generators

font_attr = ("times", 10)


question_gens = [question_generators.TimeDifferenceGen(), question_generators.QuadraticZerosGen(), question_generators.IntersectingLinesGen()]

pdf = FPDF()
pdf.add_page()
pdf.set_font(font_attr[0], '', font_attr[1])
questionNumber = 1


def addQuestion(question):
    global questionNumber
    # Adjust cell width to fit your content
    cell_width = 190
    answers = question.answer_choice_list

    # Add the first block of text and answer choices
    pdf.multi_cell(cell_width, 5, f'({questionNumber})          {question.question}', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(cell_width, 10,
             f'A) {answers[0]}     B) {answers[1]}     C) {answers[2]}     D) {answers[3]}     E) {answers[4]}',
             align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(cell_width, 10, f'', align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    print(question.correct_index)
    questionNumber += 1


for i in range(1, 25):
    addQuestion(random.choice(question_gens).generate_question())

pdf.output('pdf_1.pdf')
