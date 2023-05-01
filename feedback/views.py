from django.shortcuts import render
from multiprocessing import context
from django.shortcuts import redirect, render
from .forms import feedbackForms
from .models import Feedback
from django.views.generic import ListView, DetailView

# Create your views here.
def feedback_list(request):
    feedbacks = Feedback.objects.all()
    context = {
        'feedback_list':feedbacks
        }
    return render(request,'feedback/feedback_list.html',context)


def feedback_success(request):
    return render(request, 'feedback/feedback_success.html')

def feedback_form(request, id=0):
    if request.method == "GET":
        if id==0:
            form = feedbackForms()
        else:
            feedback = Feedback.objects.get(pk=id)
            form = feedbackForms(instance=feedback)
        return render(request, 'feedback/feedback_form.html', {'form':form})
    else:
        if id==0:
            form = feedbackForms(request.POST)
        else:
            feedback = Feedback.objects.get(pk=id)
            form = feedbackForms(request.POST,instance=feedback)
        if form.is_valid():
            form.save()
        return redirect('/feedbacks/success')

def feedback_delete(request,id):
    feedback = Feedback.objects.get(pk=id)
    feedback.delete()
    return redirect('feedbacks/list')