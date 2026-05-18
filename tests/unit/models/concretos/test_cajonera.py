"""
Pruebas unitarias para la clase Cajonera.
"""
import pytest
from models.concretos.cajonera import Cajonera


class TestCajonera:
    @pytest.fixture
    def cajonera_basica(self):
        return Cajonera("Cajonera Básica", "Madera", "Café", 150)

    @pytest.fixture
    def cajonera_completa(self):
        return Cajonera("Cajonera Premium", "Metal", "Negro", 200,
                        num_cajones=5, tiene_ruedas=True)

    def test_instanciacion_correcta(self, cajonera_basica):
        assert cajonera_basica.nombre == "Cajonera Básica"
        assert cajonera_basica.material == "Madera"
        assert cajonera_basica.precio_base == 150

    def test_cajones_por_defecto(self, cajonera_basica):
        assert cajonera_basica.num_cajones == 3

    def test_ruedas_por_defecto(self, cajonera_basica):
        assert cajonera_basica.tiene_ruedas is False

    def test_calcular_precio_basico(self, cajonera_basica):
        assert cajonera_basica.calcular_precio() == 210

    def test_calcular_precio_completo(self, cajonera_completa):
        assert cajonera_completa.calcular_precio() == 330

    def test_obtener_descripcion(self, cajonera_basica):
        desc = cajonera_basica.obtener_descripcion()
        assert "Cajonera Básica" in desc
        assert "Madera" in desc