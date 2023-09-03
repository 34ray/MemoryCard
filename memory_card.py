#подключение библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle, randint

#прописываем класс
class Question():
    def __init__(self, lb_quetion, right_answer, wrong1, wrong2, wrong3):
        self.lb_quetion = lb_quetion
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

#создаём список
questions_list = []
questions_list.append(Question("Государственный язык Бразилии", "Португальский", "Испанский", "Бразильский", "Итальянский"))
questions_list.append(Question("Какой национальности не существует?", "Смурфы", "Энцы", "Алеуты", "Чулымцы"))
questions_list.append(Question("Сквозь землю провалился значит...", "Бесследно исчез", "Сильно испугался", "Допустил серьёзную ошибку", "Провалился сквозь землю"))
questions_list.append(Question("Дата крещения Руси", "988", "998", "888", "999"))
questions_list.append(Question("С какой книгой сравнивались учёные средневековья?", "Библия", "Теория права и государства", "Большая медицинская энциклопедия", "Ни с какой, сравнивали со знаниями других учёных"))
questions_list.append(Question("Сколько строчек кода Тимофей украл у меня?", "2", "3", "4", "Он ничего не крал"))
questions_list.append(Question("По какой координате надо ходить в незере в Майнкрафт, чтобы найти адскую крепость?", "Z", "Y", "X", "Что такое майнкрафт?"))
questions_list.append(Question("Где снимался Billy Herington?", "Гачимучи", "Терминатор", "Чебурашка 2023", "Пётр I"))
questions_list.append(Question("Самый лучший фильм в индустрии Dungeons Masters это", "Покорённый", "50 оттенков серого", "Терминатор", "Чебурашка"))

#функции обработки нажатия на кнопку Ответить/Следующий вопрос
#функция отображение результата
def show_result():
    RadioGroupBox.hide()
    RadioGroupBox2.show()
    downbutton.setText("Следующий вопрос")

#функция отображение
def show_quetion():
    RadioGroupBox2.hide()
    RadioGroupBox.show()
    downbutton.setText("Ответить")
    #сброс переключателей
    RadioGroup.setExclusive(False)
    radiobtn1.setChecked(False)
    radiobtn2.setChecked(False)
    radiobtn3.setChecked(False)
    radiobtn4.setChecked(False)
    RadioGroup.setExclusive(True)

#функция "show_result или show_quetion"
def click_ok():
    if downbutton.text() == "Ответить":
        check_answer()
    else:
        next_quetion()
def ask(q: Question):
    
    tright_answer.setText(q.right_answer)
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.lb_quetion)
    show_quetion()

def check_answer():
    ans_correct = "Правильно                          "
    ans_wrong = "Неправильно                        "
    ans_miss = "Почему не выбрал?                 "

    if answers[0].isChecked():
        show_correct(ans_correct)
        main.score += 1
    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct(ans_wrong)
    else:
        show_correct(ans_miss)

def show_correct(res):
    declab.setText(res)
    #отображение статистики в терминале
    print("Статистика")
    print("Всего вопросов:", main.total)
    print("Всего правильных ответов:", main.score)
    print("Рейтинг:", int(main.score/main.total*100),"%")
    show_result()

#переход к следующему вопросу       
def next_quetion():
    '''main.cur_question +=1
    if main.cur_question >= len(questions_list):
        main.cur_question = 0'''
    cur_question = randint(0, len(questions_list)-1)
    ask(questions_list[cur_question])
    main.total += 1

#создание приложения и главного окна
app = QApplication([])
main = QWidget()
main.setWindowTitle("Memory Card")

#создание виджетов №1(окно с вопросом)
question = QLabel("Сложный вопрос")
RadioGroupBox = QGroupBox("Варианты ответа:")
RadioGroupBox2 = QGroupBox("Результат теста")
radiobtn1 = QRadioButton("Вариант 1")
radiobtn2 = QRadioButton("Вариант 2")
radiobtn3 = QRadioButton("Вариант 3")
radiobtn4 = QRadioButton("Вариант 4")
answers = [radiobtn1, radiobtn2, radiobtn3, radiobtn4]
downbutton = QPushButton("Ответить")

#создание виджетов №2(окно с результатом)
declab = QLabel("Правильно/Неправильно                                              ")
tright_answer = QLabel("Правильный ответ")

#создание лэйаутов группы RadioGroupBox
layout_groupansV1 = QVBoxLayout()
layout_groupansV2 = QVBoxLayout()
layout_groupansH = QHBoxLayout()

#прикрепление виджетов к вертикальным линиям
layout_groupansV1.addWidget(radiobtn1)
layout_groupansV1.addWidget(radiobtn2)

layout_groupansV2.addWidget(radiobtn3)
layout_groupansV2.addWidget(radiobtn4)

#закрепление вертикальных к основной горизонтальной
layout_groupansH.addLayout(layout_groupansV1)
layout_groupansH.addLayout(layout_groupansV2)

#отображение лэйаутов в группе RadioGroupBox
RadioGroupBox.setLayout(layout_groupansH)



#создание лэйаутов основного окна
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()
layoutV = QVBoxLayout()

#прикрепление виджетов к горизонтальным линиям
layoutH1.addWidget(question, alignment = Qt.AlignCenter)
layoutH2.addWidget(RadioGroupBox, alignment = Qt.AlignCenter)
layoutH3.addWidget(downbutton, alignment = Qt.AlignCenter)

#прикрепление горизонтальных к основной вертикальной
layoutV.addLayout(layoutH1)
layoutV.addLayout(layoutH2)
layoutV.addLayout(layoutH3)

#отображение лэйаутов в основном окне
main.setLayout(layoutV)




#создание лэйаутов второй группы
layout_groupresH1 = QHBoxLayout()
layout_groupresH2 = QHBoxLayout()
layout_groupresV = QVBoxLayout()

#прикрепление виджетов к горизонтальной
layout_groupresH1.addWidget(declab, alignment = Qt.AlignVCenter)
layout_groupresH2.addWidget(tright_answer, alignment = Qt.AlignCenter)

#прикрепление горизонтальных к основной вертикальной
layout_groupresV.addLayout(layout_groupresH1)
layout_groupresV.addLayout(layout_groupresH2)

#отображение лэйаутов во второй группе
RadioGroupBox2.setLayout(layout_groupresV)

#прикрепление второй группы к основному окну(RadioGroupBox2)
layoutH2.addWidget(RadioGroupBox2, alignment = Qt.AlignCenter)
RadioGroupBox2.hide()

#создание специальной группы(для последующего сброса в функции show_question)
RadioGroup = QButtonGroup()
RadioGroup.addButton(radiobtn1)
RadioGroup.addButton(radiobtn2)
RadioGroup.addButton(radiobtn3)
RadioGroup.addButton(radiobtn4)

#Создание счётчиков для статистики
main.score = 0
main.total = 0

#создание вопроса и ответов
next_quetion()
#обработка нажатия на кнопку Ответить/Следующий вопрос
downbutton.clicked.connect(click_ok)


#изменение размера окна
main.resize(500,400)

#отображение приложения
main.show()
app.exec_()





