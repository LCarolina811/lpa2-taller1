"""
Pruebas unitarias para la clase abstracta Mueble.
"""
import pytest
from abc import ABC
from models.mueble import Mueble


class TestMueble:
    def test_es_clase_abstracta(self):
        """Verifica que Mueble no puede ser instanciada directamente."""
        with pytest.raises(TypeError):
            mueble = Mueble("Mesa", "Madera", "Café", 100.0)

    def test_tiene_metodo_abstracto_calcular_precio(self):
        """Verifica que calcular_precio es abstracto."""
        assert hasattr(Mueble, 'calcular_precio')
        assert Mueble.calcular_precio.__isabstractmethod__

    def test_tiene_metodo_abstracto_obtener_descripcion(self):
        """Verifica que obtener_descripcion es abstracto."""
        assert hasattr(Mueble, 'obtener_descripcion')
        assert Mueble.obtener_descripcion.__isabstractmethod__

    def test_hereda_de_abc(self):
        """Verifica que Mueble hereda de ABC."""
        assert issubclass(Mueble, ABC)