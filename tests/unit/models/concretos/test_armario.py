"""
Pruebas unitarias para la clase Armario.
"""
import pytest
from models.concretos.armario import Armario


class TestArmario:
    @pytest.fixture
    def armario_basico(self):
        return Armario("Armario Básico", "Madera", "Café", 400)

    @pytest.fixture
    def armario_completo(self):
        return Armario("Armario Premium", "Madera", "Blanco", 600,
                       num_puertas=4, num_cajones=3, tiene_espejos=True)

    def test_instanciacion_correcta(self, armario_basico):
        assert armario_basico.nombre == "Armario Básico"
        assert armario_basico.material == "Madera"
        assert armario_basico.precio_base == 400

    def test_puertas_por_defecto(self, armario_basico):
        assert armario_basico.num_puertas == 2

    def test_cajones_por_defecto(self, armario_basico):
        assert armario_basico.num_cajones == 0

    def test_espejos_por_defecto(self, armario_basico):
        assert armario_basico.tiene_espejos is False

    def test_calcular_precio_basico(self, armario_basico):
        assert armario_basico.calcular_precio() == 500

    def test_calcular_precio_completo(self, armario_completo):
        assert armario_completo.calcular_precio() == 990

    def test_obtener_descripcion(self, armario_basico):
        desc = armario_basico.obtener_descripcion()
        assert "Armario Básico" in desc
        assert "Madera" in desc