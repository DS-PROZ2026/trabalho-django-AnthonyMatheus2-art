from django.test import TestCase
from django.urls import reverse

from .models import Equipamento


class EquipamentoTests(TestCase):
    def test_dashboard_loads(self):
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Painel de Controle")

    def test_cadastro(self):
        response = self.client.post(
            reverse("cadastrar_equipamento"),
            {
                "nome": "Notebook",
                "numero_patrimonio": 123,
                "tipo": "Informática",
                "em_uso": "on",
            },
        )
        self.assertRedirects(response, reverse("dashboard"))
        self.assertTrue(Equipamento.objects.filter(nome="Notebook").exists())

    def test_edicao(self):
        equipamento = Equipamento.objects.create(
            nome="Notebook", numero_patrimonio=123, tipo="Informática"
        )
        response = self.client.post(
            reverse("editar_equipamento", args=[equipamento.id]),
            {
                "nome": "Notebook atualizado",
                "numero_patrimonio": 456,
                "tipo": "Informática",
                "em_uso": "on",
            },
        )
        self.assertRedirects(response, reverse("dashboard"))
        equipamento.refresh_from_db()
        self.assertEqual(equipamento.nome, "Notebook atualizado")

    def test_exclusao_exige_post(self):
        equipamento = Equipamento.objects.create(
            nome="Notebook", numero_patrimonio=123, tipo="Informática"
        )
        response = self.client.get(
            reverse("deletar_equipamento", args=[equipamento.id])
        )
        self.assertRedirects(response, reverse("dashboard"))
        self.assertTrue(Equipamento.objects.filter(id=equipamento.id).exists())

        response = self.client.post(
            reverse("deletar_equipamento", args=[equipamento.id])
        )
        self.assertRedirects(response, reverse("dashboard"))
        self.assertFalse(Equipamento.objects.filter(id=equipamento.id).exists())
