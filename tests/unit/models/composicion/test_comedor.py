"""
Pruebas unitarias para la clase Comedor (composición).
"""
import pytest
from models.composicion.comedor import Comedor
from models.concretos.mesa import Mesa
from models.concretos.silla import Silla


class TestComedor:
    @pytest.fixture
    def mesa(self):
        return Mesa("Mesa Comedor", "Roble", "Café", 200.0)

    @pytest.fixture
    def sillas(self):
        return [Silla(f"Silla {i}", "Roble", "Café", 50.0) for i in range(4)]

    @pytest.fixture
    def comedor_basico(self, mesa):
        return Comedor("Comedor Familiar", mesa)

    @pytest.fixture
    def comedor_completo(self, mesa, sillas):
        return Comedor("Comedor Completo", mesa, sillas)

    def test_instanciacion_correcta(self, comedor_basico, mesa):
        assert comedor_basico.nombre == "Comedor Familiar"
        assert comedor_basico.mesa is mesa

    def test_sillas_vacias_por_defecto(self, comedor_basico):
        assert len(comedor_basico.sillas) == 0

    def test_composicion_con_sillas(self, comedor_completo):
        assert len(comedor_completo.sillas) == 4

    def test_agregar_silla(self, comedor_basico):
        silla = Silla("Silla Nueva", "Roble", "Café", 50.0)
        comedor_basico.agregar_silla(silla)
        assert len(comedor_basico.sillas) == 1

    def test_quitar_silla(self, comedor_completo):
        resultado = comedor_completo.quitar_silla()
        assert "removida" in resultado.lower()

    def test_quitar_silla_sin_sillas(self, comedor_basico):
        resultado = comedor_basico.quitar_silla()
        assert "no hay" in resultado.lower()

    def test_calcular_precio_total_sin_descuento(self, comedor_basico, mesa):
        precio = comedor_basico.calcular_precio_total()
        assert precio == mesa.calcular_precio()

    def test_calcular_precio_total_con_descuento(self, comedor_completo):
        precio = comedor_completo.calcular_precio_total()
        assert precio > 0

    def test_obtener_resumen(self, comedor_completo):
        resumen = comedor_completo.obtener_resumen()
        assert "nombre" in resumen
        assert "precio_total" in resumen
        assert "capacidad_personas" in resumen

    def test_obtener_descripcion_completa(self, comedor_completo):
        desc = comedor_completo.obtener_descripcion_completa()
        assert "COMEDOR" in desc
        assert "MESA" in desc
        assert "SILLAS" in desc

    def test_len_comedor(self, comedor_completo):
        assert len(comedor_completo) == 5

    def test_str_comedor(self, comedor_basico):
        assert "Comedor" in str(comedor_basico)