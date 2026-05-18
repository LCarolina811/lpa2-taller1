"""
Pruebas unitarias para la clase Sofa.
"""
import pytest
from models.concretos.sofa import Sofa


class TestSofa:
    @pytest.fixture
    def sofa_basico(self):
        return Sofa("Sofá Básico", "Tela", "Gris", 400.0)

    @pytest.fixture
    def sofa_completo(self):
        return Sofa("Sofá Premium", "Cuero", "Negro", 800.0,
                    capacidad_personas=4, tiene_respaldo=True,
                    material_tapizado="Cuero", tiene_brazos=True,
                    es_modular=True, incluye_cojines=True)

    def test_instanciacion_correcta(self, sofa_basico):
        assert sofa_basico.nombre == "Sofá Básico"
        assert sofa_basico.material == "Tela"
        assert sofa_basico.color == "Gris"
        assert sofa_basico.precio_base == 400.0

    def test_capacidad_por_defecto(self, sofa_basico):
        assert sofa_basico.capacidad_personas == 3

    def test_calcular_precio_basico(self, sofa_basico):
        precio = sofa_basico.calcular_precio()
        assert precio > 400.0

    def test_calcular_precio_completo(self, sofa_completo):
        precio = sofa_completo.calcular_precio()
        assert precio > 800.0

    def test_tiene_brazos_por_defecto(self, sofa_basico):
        assert sofa_basico.tiene_brazos is True

    def test_es_modular_false_por_defecto(self, sofa_basico):
        assert sofa_basico.es_modular is False

    def test_incluye_cojines_false_por_defecto(self, sofa_basico):
        assert sofa_basico.incluye_cojines is False

    def test_obtener_descripcion(self, sofa_basico):
        desc = sofa_basico.obtener_descripcion()
        assert "Sofá Básico" in desc
        assert "Tela" in desc

    def test_precio_negativo_lanza_error(self):
        with pytest.raises(ValueError):
            sofa = Sofa("Sofá", "Tela", "Gris", 400.0)
            sofa.precio_base = -10