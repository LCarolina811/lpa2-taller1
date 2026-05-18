"""
Pruebas unitarias para la clase abstracta Almacenamiento.
"""
import pytest
from abc import ABC
from models.categorias.almacenamiento import Almacenamiento


class TestAlmacenamiento:
    def test_es_clase_abstracta(self):
        with pytest.raises(TypeError):
            Almacenamiento("Armario", "Madera", "Café", 100.0, 3, 50.0)

    def test_hereda_de_abc(self):
        assert issubclass(Almacenamiento, ABC)

    def test_tiene_metodo_abstracto_calcular_precio(self):
        assert hasattr(Almacenamiento, 'calcular_precio')
        assert Almacenamiento.calcular_precio.__isabstractmethod__

    def test_tiene_metodo_abstracto_obtener_descripcion(self):
        assert hasattr(Almacenamiento, 'obtener_descripcion')
        assert Almacenamiento.obtener_descripcion.__isabstractmethod__

    def test_compartimentos_invalidos(self):
        class AlmacenamientoConcreto(Almacenamiento):
            def calcular_precio(self): return self.precio_base
            def obtener_descripcion(self): return self.nombre

        a = AlmacenamientoConcreto("Test", "Madera", "Café", 100.0, 3, 50.0)
        with pytest.raises(ValueError):
            a.num_compartimentos = 0

    def test_capacidad_invalida(self):
        class AlmacenamientoConcreto(Almacenamiento):
            def calcular_precio(self): return self.precio_base
            def obtener_descripcion(self): return self.nombre

        a = AlmacenamientoConcreto("Test", "Madera", "Café", 100.0, 3, 50.0)
        with pytest.raises(ValueError):
            a.capacidad_litros = 0

    def test_calcular_factor_almacenamiento(self):
        class AlmacenamientoConcreto(Almacenamiento):
            def calcular_precio(self): return self.precio_base
            def obtener_descripcion(self): return self.nombre

        a = AlmacenamientoConcreto("Test", "Madera", "Café", 100.0, 3, 50.0)
        factor = a.calcular_factor_almacenamiento()
        assert factor > 1.0

    def test_obtener_info_almacenamiento(self):
        class AlmacenamientoConcreto(Almacenamiento):
            def calcular_precio(self): return self.precio_base
            def obtener_descripcion(self): return self.nombre

        a = AlmacenamientoConcreto("Test", "Madera", "Café", 100.0, 3, 50.0)
        info = a.obtener_info_almacenamiento()
        assert "3" in info
        assert "50" in info