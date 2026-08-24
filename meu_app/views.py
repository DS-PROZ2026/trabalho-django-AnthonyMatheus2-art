from django.shortcuts import get_object_or_404, redirect, render

from .forms import EquipamentoForm
from .models import Equipamento


def painel_dashboard(request):
    equipamentos = Equipamento.objects.all().order_by("id")
    return render(
        request,
        "meu_app/dashboard.html",
        {"equipamentos": equipamentos, "total": equipamentos.count()},
    )


def detalhe_equipamento(request, id):
    equipamento = get_object_or_404(Equipamento, id=id)
    return render(request, "meu_app/detalhe_equipamento.html", {"equipamento": equipamento})


def cadastrar_equipamento(request):
    if request.method == "POST":
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = EquipamentoForm()

    return render(request, "meu_app/cadastrar_equipamento.html", {"form": form})


def editar_equipamento(request, id):
    equipamento = get_object_or_404(Equipamento, id=id)

    if request.method == "POST":
        form = EquipamentoForm(request.POST, instance=equipamento)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = EquipamentoForm(instance=equipamento)

    return render(request, "meu_app/cadastrar_equipamento.html", {"form": form})


def deletar_equipamento(request, id):
    equipamento = get_object_or_404(Equipamento, id=id)

    if request.method == "POST":
        equipamento.delete()

    return redirect("dashboard")
