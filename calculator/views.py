from django.shortcuts import render

def index(request):
    context = {}

    if request.method == "POST":
        num1 = request.POST.get("num1", "").strip()
        num2 = request.POST.get("num2", "").strip()

        if not num1 or not num2:
            context["error"] = "Both numbers must be non-empty."
        else:
            try:
                num1 = int(num1)
                num2 = int(num2)
                if num1 == 0 or num2 == 0:
                    context["error"] = "Both numbers must be non-zero."
                else:
                    mysum = num1 + num2
                    context = {"sum": mysum}
            except ValueError:
                context["error"] = "Both numbers must be valid integers."

    return render(request, 'index.html', context)