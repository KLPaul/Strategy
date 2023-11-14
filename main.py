# La declaracion from __future__ import annotations se utiliza para habilitar
# la evaluacion diferida de las anotaciones de tipo.
# es neceario para futuras refrencias
from __future__ import annotations

# ABC es una clase base abtracta del modulo la cual es un decorador que se
# utiliza para declarar metodos abtractos en clases de la misma propiedad
from abc import ABC, abstractmethod

# List se importa desde el módulo typing y se utiliza como
# una sugerencia de tipo para indicar que se espera que una variable sea una lista.

from typing import List


# la clase context es una clase que mantiene una referencia a una estrategia y delega
# algun trabajo a ella
class Context():
    """
    Context define la interfaz de interés para los clientes.
    """

    def __init__(self, strategy: Strategy) -> None:
        """
        Por lo general, el contexto acepta una estrategia a través del constructor, pero
        También proporciona un configurador para cambiarlo en tiempo de ejecución.
        """

        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        """
        El Contexto mantiene una referencia a uno de los objetos de Estrategia. El
        El contexto no conoce la clase concreta de una estrategia. Deberia de funcionar
        con todas las estrategias a través de la interfaz de Estrategia.
        """

        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """
       Normalmente, el Contexto permite reemplazar un objeto de Estrategia en tiempo de ejecución.
        """

        self._strategy = strategy

    def do_some_business_logic(self) -> None:
        """
        El Contexto delega algo de trabajo al objeto Estrategia en lugar de
        implementar múltiples versiones del algoritmo por sí solo.
        """

        # ...

        print(
            "Contexto: ordenar datos usando la estrategia (no estoy seguro de cómo lo hará)")
        result = self._strategy.do_algorithm(["a", "b", "c", "d", "e"])
        print(",".join(result))

        # ...


# La clase Strategy es una clase base abstracta que define
# la interfaz común para todas las clases concretas de estrategia
class Strategy(ABC):
    """
    La interfaz Strategy declara operaciones comunes a todas las versiones.
    compatibles con algún algoritmo.

    Context utiliza esta interfaz para llamar al algoritmo definido por las
    Estrategias concretas.
    """

    @abstractmethod
    def do_algorithm(self, data: List):
        pass


"""
 
Las estrategias concretas implementan el algoritmo siguiendo la estrategia base.
interfaz. La interfaz los hace intercambiables en el contexto.

"""

# ConcreteStrategyA y ConcreteStrategyB son dos implementaciones concretas de la interfaz Strategy.
# Proporcionan algoritmos diferentes para ordenar una lista de datos.


class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data: List) -> List:
        return sorted(data)


class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data: List) -> List:
        return reversed(sorted(data))


if __name__ == "__main__":
    # En el bloque __main__, se proporciona un ejemplo de código de cliente.
    # Muestra cómo un cliente puede instanciar un objeto Context y configurar
    # su estrategia ya sea a ConcreteStrategyA o ConcreteStrategyB. Luego,
    # se llama al método do_some_business_logic en el contexto, y la salida refleja
    # la estrategia de ordenamiento elegida..

    context = Context(ConcreteStrategyA())
    print("Cliente: La estrategia está configurada para la clasificación normal.")
    context.do_some_business_logic()
    print()

    print("Cliente: La estrategia está configurada para la clasificación inversa.")
    context.strategy = ConcreteStrategyB()
    context.do_some_business_logic()
