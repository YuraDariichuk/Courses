from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm
from .models import questionnaireAnswers, questionnaireData, lection
from django.contrib.auth.models import User


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Имя пользователя или пароль введены неверно')
    context = {}
    return render(request, 'login.html', context)


def regist(request):
    form = CreateUserForm
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form': form}
    return render(request, 'register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def index(request):
    if request.user.is_authenticated:
        questionnaire_list = lection.objects.all()
        return render(request, 'index.html', {'questionnaire_list': questionnaire_list})
    else:
        return redirect('login')


def lection_page(request, lec_id):
    lection_l = lection.objects.filter(lection_name = lec_id)
    return render(request, 'lection_page.html', {'lection': lection_l[0]})


def questionnaire_page(request, name):
    questionnaireCurr = questionnaireData.objects.get(questionnaire_name=name)
    questName = questionnaireCurr.questionnaire_name
    questions = questionnaireCurr.questions_text.split('/')
    tempAns = questionnaireCurr.questions_answers.split('/')
    tempQA = []
    for i in range(len(questions)):
        tempQA.append(questions[i] + '*' + tempAns[i])

    quest_ans = []
    for i in range(len(tempQA)):
        quest_ans.append(tempQA[i].split('*'))

    answers = []
    if request.method == 'POST':
        for i in range(1, len(quest_ans) + 1):
            answers.append(request.POST.get('quest' + str(i)))
        addAnswersToDB(answers, questName, request)
        return redirect('index')
    return render(request, 'questionnaire_page.html', {'questName': questName, 'quest_ans': quest_ans})


def addAnswersToDB(answers, name, req):
    quest = questionnaireData.objects.get(questionnaire_name=name)
    strAnsw = ""
    for str in answers:
        strAnsw += str + "\n"
    answ = questionnaireAnswers(questionnaire_name_fk=quest, user=req.user, answers=strAnsw)
    answ.save()

