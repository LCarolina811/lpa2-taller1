"""
Pruebas unitarias para la clase Mesa.
"""
import pytest
from models.concretos.mesa import Mesa


class TestMesa:
    @pytest.fixture
    def mesa_basica(self):
        return Mesa("Mesa Básica", "Madera", "Café", 200.0)

    @pytest.fixture
    def mesa_redonda(self):
        return Mesa("Mesa Redonda", "Vidrio", "Transparente", 300.0,
                    forma="redonda", capacidad_personas=8)

    def test_instanciacion_correcta(self, mesa_basica):
        assert mesa_basica.nombre == "Mesa Básica"
        assert mesa_basica.material == "Madera"
        assert mesa_basica.color == "Café"
        assert mesa_basica.precio_base == 200.0

    def test_calcular_precio_basico(self, mesa_basica):
        precio = mesa_basica.calcular_precio()
        assert precio > 0

    def test_calcular_precio_con_forma_especial(self, mesa_redonda):
        precio = mesa_redonda.calcular_precio()
        assert precio > 300.0

    def test_calcular_precio_capacidad_alta(self, mesa_redonda):
        precio = mesa_redonda.calcular_precio()
        assert precio > 300.0

    def test_obtener_descripcion(self, mesa_basica):
        desc = mesa_basica.obtener_descripcion()
        assert "Mesa Básica" in desc
        assert "Madera" in desc

    def test_forma_invalida_lanza_error(self, mesa_basica):
        with pytest.raises(ValueError):
            mesa_basica.forma = "triangular"

    def test_capacidad_invalida_lanza_error(self, mesa_basica):
        with pytest.raises(ValueError):
            mesa_basica.capacidad_personas = 0

    def test_precio_negativo_lanza_error(self):
        with pytest.raises(ValueError):
            mesa = Mesa("Mesa", "Madera", "Café", 200.0)
            mesa.precio_base = -10

    def test_nombre_vacio_lanza_error(self):
        with pytest.raises(ValueError):
            mesa = Mesa("Mesa", "Madera", "Café", 200.0)
            mesa.nombre = ""