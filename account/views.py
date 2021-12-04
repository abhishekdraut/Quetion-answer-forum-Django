from django.conf.urls import url
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from category.models import Category
from question_answer.models import Question
from question_answer.models import Answer
from user_profile.models import  user_profile
from comment.models import Comment



""" Home page view function """
def homePage(request):
    categories=Category.objects.filter(status=True).order_by('id')[:5]
    
    allcategories=Category.objects.filter(status=True).order_by('id')
    Home_questions=Question.objects.filter(status=True).order_by('-id')[:8]

    return render(request,'home.html',{'categories':categories,'all':allcategories,'home_questions':Home_questions})


def category_questions(request, cat_id):
    categories=Category.objects.filter(status=True).order_by('id')[:5]
    allcategories=Category.objects.filter(status=True).order_by('id')
   
    category_question=Question.objects.filter(category_id=cat_id)
    
    return render(request,'category_questions.html',{'categories':categories,'all':allcategories,'category_question':category_question})

def questions(request,que_id):
    categories=Category.objects.filter(status=True).order_by('id')[:5]
    
    question=Question.objects.filter(id=que_id)
    answer=Answer.objects.filter(question_id=que_id)

    comments= Comment.objects.all()
    answers={}
    for key, each_answer in enumerate(answer):
        
        user_profileobject=user_profile.objects.get(user=each_answer.user)

        answers[key]={
            'answer1':each_answer,'user_profile':user_profileobject
        }
    
    

    answers=list(answers.values())
    
    
    return render(request, 'question.html',{'categories':categories,'question':question,'answer':answers,'comment':comments})


def comment_save(request):
    comment=request.POST.get('comment')
    user_id=request.POST.get('user_id')
    answer_id=request.POST.get('answer_id')
    question_id=request.POST.get('que_id')
    image=request.POST.get('image')
    if comment:
        comment1=Comment.objects.create(
            answer_id=answer_id,
            user_id=user_id,
            comments=comment,
            image=image
            
        )
        comment1.save()
    else:
        return redirect("questions_ref",que_id=question_id)


    return redirect("questions_ref",que_id=question_id )