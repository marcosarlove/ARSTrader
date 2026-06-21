"""
ARSTrader - Strategy Facade Gateway (__init__.py)
==================================================
Responsável exclusivo por expor a classe principal de execução para o Core Loader.
"""

from modules.eveningstar.state import Candle, MarketState, ResistanceZone
from modules.eveningstar.strategy import EveningStarStrategy


EveningStar = EveningStarStrategy


__all__ = ["Candle", "EveningStar", "EveningStarStrategy", "MarketState", "ResistanceZone"]
