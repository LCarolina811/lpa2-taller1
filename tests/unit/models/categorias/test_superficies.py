"""
Pruebas unitarias para la clase abstracta Superficie.
"""
import pytest
from abc import ABC
from models.categorias.superficies import Superficie


class SuperficieConcrета(Superficie):
    def calcular_precio(self): return self.precio_base
    def obtener_descripcion(self): return self.nombre


class TestSuperficie:
    @pytest.fixture
    def superficie(self):
        return SuperficieConcrета("Mesa Test", "Madera", "Café", 100.0, 120.0, 80.0, 75.0)

    def test_es_clase_abstracta(self):
        with pytest.raises(TypeError):
            Superficie("Mesa", "Madera", "Café", 100.0, 120.0, 80.0, 75.0)

    def test_hereda_de_abc(self):
        assert issubclass(Superficie, ABC)

    def test_instanciacion_correcta(self, superficie):
        assert superficie.nombre == "Mesa Test"
        assert superficie.largo == 120.0
        assert superficie.ancho == 80.0
        assert superficie.altura == 75.0

    def test_largo_invalido(self, superficie):
        with pytest.raises(ValueError):
            superficie.largo = 0

    def test_ancho_invalido(self, superficie):
        with pytest.raises(ValueError):
            superficie.ancho = -5

    def test_altura_invalida(self, superficie):
        with pytest.raises(ValueError):
            superficie.altura = 0

    def test_calcular_area(self, superficie):
        assert superficie.calcular_area() == 120.0 * 80.0

    def test_calcular_factor_tamaño(self, superficie):
        factor = superficie.calcular_factor_tamaño()
        assert factor > 1.0

    def test_obtener_info_superficie(self, superficie):
        info = superficie.obtener_info_superficie()
        assert "120" in info
        assert "80" in info
        assert "75" in info