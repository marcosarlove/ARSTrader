"""
ARSTrader - Strategy Facade Gateway (__init__.py)
==================================================
Responsável exclusivo por expor a classe principal de execução para o Core Loader.
"""

from modules.morningstar.state import Candle, MarketState, SupportZone
from modules.morningstar.strategy import MorningStarStrategy


MorningStar = MorningStarStrategy


__all__ = ["Candle", "MarketState", "MorningStar", "MorningStarStrategy", "SupportZone"]
