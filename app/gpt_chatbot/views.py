from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.utils import timezone
import openai

from .models import Chat

openai_api_key = "my_secret_key"
openai.api_key = openai_api_key

def ask_openai(prompt):
    response = openai.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [{"role" : "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

# Create your views here.

def chatbot(request):
    if request.method == "POST":
        message = request.POST.get("message")
        response = ask_openai(message)

        chat = Chat(message = message,
                    response = response,
                    created_at = timezone.now)

        return JsonResponse({"message": message,
                             "response": response})

    return render(request, "chatbot.html")