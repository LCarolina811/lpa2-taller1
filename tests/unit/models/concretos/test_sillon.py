"""
Pruebas unitarias para la clase Sillon.
"""
import pytest
from models.concretos.sillon import Sillon


class TestSillon:
    @pytest.fixture
    def sillon_basico(self):
        return Sillon("Sillón Básico", "Tela", "Café", 300)

    @pytest.fixture
    def sillon_completo(self):
        return Sillon("Sillón Premium", "Cuero", "Negro", 500,
                      material_tapizado="Cuero", tiene_brazos=True,
                      es_reclinable=True, tiene_reposapiés=True)

    def test_instanciacion_correcta(self, sillon_basico):
        assert sillon_basico.nombre == "Sillón Básico"
        assert sillon_basico.material == "Tela"
        assert sillon_basico.color == "Café"
        assert sillon_basico.precio_base == 300

    def test_capacidad_por_defecto(self, sillon_basico):
        assert sillon_basico.capacidad_personas == 2

    def test_calcular_precio_basico(self, sillon_basico):
        precio = sillon_basico.calcular_precio()
        assert precio > 300

    def test_calcular_precio_completo(self, sillon_completo):
        precio = sillon_completo.calcular_precio()
        assert precio > 500

    def test_calcular_precio_con_brazos(self, sillon_basico):
        precio = sillon_basico.calcular_precio()
        assert precio == 400

    def test_es_reclinable_false_por_defecto(self, sillon_basico):
        assert sillon_basico.es_reclinable is False

    def test_tiene_reposapiés_false_por_defecto(self, sillon_basico):
        assert sillon_basico.tiene_reposapiés is False

    def test_obtener_descripcion(self, sillon_basico):
        desc = sillon_basico.obtener_descripcion()
        assert "Sillón Básico" in desc
        assert "Tela" in desc