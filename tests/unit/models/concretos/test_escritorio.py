"""
Pruebas unitarias para la clase Escritorio.
"""
import pytest
from models.concretos.escritorio import Escritorio


class TestEscritorio:
    @pytest.fixture
    def escritorio_basico(self):
        return Escritorio("Escritorio Básico", "Madera", "Café", 300)

    @pytest.fixture
    def escritorio_completo(self):
        return Escritorio("Escritorio Premium", "Madera", "Blanco", 400,
                          forma="en L", tiene_cajones=True, num_cajones=3,
                          largo=1.8, tiene_iluminacion=True)

    def test_instanciacion_correcta(self, escritorio_basico):
        assert escritorio_basico.nombre == "Escritorio Básico"
        assert escritorio_basico.material == "Madera"
        assert escritorio_basico.precio_base == 300

    def test_forma_por_defecto(self, escritorio_basico):
        assert escritorio_basico.forma == "rectangular"

    def test_cajones_por_defecto(self, escritorio_basico):
        assert escritorio_basico.tiene_cajones is False

    def test_calcular_precio_basico(self, escritorio_basico):
        assert escritorio_basico.calcular_precio() == 300

    def test_calcular_precio_completo(self, escritorio_completo):
        precio = escritorio_completo.calcular_precio()
        assert precio > 400

    def test_calcular_precio_con_cajones(self):
        e = Escritorio("E", "Madera", "Café", 300, tiene_cajones=True, num_cajones=2)
        assert e.calcular_precio() == 350

    def test_calcular_precio_largo_grande(self):
        e = Escritorio("E", "Madera", "Café", 300, largo=2.0)
        assert e.calcular_precio() == 350

    def test_calcular_precio_con_iluminacion(self):
        e = Escritorio("E", "Madera", "Café", 300, tiene_iluminacion=True)
        assert e.calcular_precio() == 340

    def test_obtener_descripcion(self, escritorio_basico):
        desc = escritorio_basico.obtener_descripcion()
        assert "Escritorio Básico" in desc
        assert "Madera" in desc