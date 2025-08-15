from django.shortcuts import render,redirect
from .models import Todo
from django.contrib.auth.models import User
from datetime import date



def home_view(request):
    # user=User.objects.get(username=request.user)
    # todos=Todo.objects.filter(user=user).order_by("-created_at")
    # context={"todos":todos,"highPriorityCount": todos.filter(priority="high").count(),"mediumPriorityCount": todos.filter(priority="medium").count(),"lowPriorityCount": todos.filter(priority="low").count(),"username":request.user}
    # return render(request,"Home/homePage.html",context)
    todos = Todo.objects.filter(user=request.user).order_by("-created_at") 
    context = { 
        "todos": todos,
        "allTodosCount":todos.all().count(),
        "todayTodosCount":todos.filter(created_at__date=date.today()).count(),
        "highPriorityCount":todos.filter(priority__iexact="high").count(),
        "mediumPriorityCount": todos.filter(priority__iexact="medium").count(),
        "lowPriorityCount": todos.filter(priority__iexact="low").count(),
        "completedTods": todos.filter(is_completed=True).count(),
        "username": request.user.username
    }
    print(context["highPriorityCount"])
    return render(request, "Home/homePage.html", context)




def addTodo_view(request):
    if request.method=="POST":
        title=request.POST.get("title")
        descp=request.POST.get("descp")
        priority=request.POST.get("priority") or "low"
        is_completed=request.POST.get("is_completed")
        user=User.objects.get(username=request.user)
        Todo.objects.create(user=request.user,title=title,descp=descp,priority=priority,is_completed=is_completed)
        return redirect("home")
    return render(request,"Home/addTodo.html")



def isCompleted_view(request,id):
    todo=Todo.objects.get(id=id)
    todo.is_completed=True
    todo.save()
    return redirect("home")


def updateTodo_view(request,id):
    todo=Todo.objects.get(id=id)
    if request.method=="POST":
        descp=request.POST.get("descp")
        priority=request.POST.get("priority")
        is_completed=request.POST.get("is_completed")
        todo.descp=descp
        todo.priority=priority
        todo.is_completed=is_completed
        todo.save()
        return redirect("home")
    context={"todo":todo}
    return render(request,"Home/updateTodo.html",context) 





def  deleteTodo_view(request,id):
    todo=Todo.objects.get(id=id)
    todo.delete()
    return redirect("home")
        
    


def priority_view(request,priority):
    UserTodos=Todo.objects.filter(user=request.user)
    todos=UserTodos.filter(priority__iexact=priority).order_by("-created_at")
    context={
            "todos":todos,
            "todayTodosCount":UserTodos.filter(created_at__date=date.today()).count(),
             "allTodosCount":UserTodos.all().count(),
             "highPriorityCount": UserTodos.filter(priority__iexact="high").count(),
             "mediumPriorityCount": UserTodos.filter(priority__iexact="medium").count(),
             "lowPriorityCount": UserTodos.filter(priority__iexact="low").count(),
             "completedTods": UserTodos.filter(is_completed=True).count(),
             "username":request.user
             }
    return render(request,"Home/homePage.html",context)


# context={"todos":todos,"highPriority": Todo.objects.filter(priority="high"),"mediumPriority": Todo.objects.filter(priority="medium"),"lowPriority": Todo.objects.filter(priority="low"),"highPriorityCount": Todo.objects.filter(priority="high").count(),"mediumPriorityCount": Todo.objects.filter(priority="medium").count(),"lowPriorityCount": Todo.objects.filter(priority="low").count(),}