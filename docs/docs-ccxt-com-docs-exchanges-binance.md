Ask AI

binance

# binance

binance cryptocurrency exchange — CCXT unified API: methods, parameters and endpoints.

Copy MarkdownOpen

> 🔌 Looking for raw exchange endpoints? See the [binance implicit API](https://docs.ccxt.com/docs/exchanges/binance/implicit-api) — every endpoint in this exchange's API exposed as an implicit method.

## [binance](https://docs.ccxt.com/docs/exchanges/binance\#binance)

**Kind**: global class

**Extends**: `Exchange`

- [enableDemoTrading](https://docs.ccxt.com/docs/exchanges/binance#enabledemotrading)
- [fetchTime](https://docs.ccxt.com/docs/exchanges/binance#fetchtime)
- [fetchCurrencies](https://docs.ccxt.com/docs/exchanges/binance#fetchcurrencies)
- [fetchMarkets](https://docs.ccxt.com/docs/exchanges/binance#fetchmarkets)
- [fetchBalance](https://docs.ccxt.com/docs/exchanges/binance#fetchbalance)
- [fetchOrderBook](https://docs.ccxt.com/docs/exchanges/binance#fetchorderbook)
- [fetchStatus](https://docs.ccxt.com/docs/exchanges/binance#fetchstatus)
- [fetchTicker](https://docs.ccxt.com/docs/exchanges/binance#fetchticker)
- [fetchBidsAsks](https://docs.ccxt.com/docs/exchanges/binance#fetchbidsasks)
- [fetchLastPrices](https://docs.ccxt.com/docs/exchanges/binance#fetchlastprices)
- [fetchTickers](https://docs.ccxt.com/docs/exchanges/binance#fetchtickers)
- [fetchMarkPrice](https://docs.ccxt.com/docs/exchanges/binance#fetchmarkprice)
- [fetchMarkPrices](https://docs.ccxt.com/docs/exchanges/binance#fetchmarkprices)
- [fetchOHLCV](https://docs.ccxt.com/docs/exchanges/binance#fetchohlcv)
- [fetchTrades](https://docs.ccxt.com/docs/exchanges/binance#fetchtrades)
- [editContractOrder](https://docs.ccxt.com/docs/exchanges/binance#editcontractorder)
- [editOrder](https://docs.ccxt.com/docs/exchanges/binance#editorder)
- [editOrders](https://docs.ccxt.com/docs/exchanges/binance#editorders)
- [createOrders](https://docs.ccxt.com/docs/exchanges/binance#createorders)
- [createOrder](https://docs.ccxt.com/docs/exchanges/binance#createorder)
- [createMarketOrderWithCost](https://docs.ccxt.com/docs/exchanges/binance#createmarketorderwithcost)
- [createMarketBuyOrderWithCost](https://docs.ccxt.com/docs/exchanges/binance#createmarketbuyorderwithcost)
- [createMarketSellOrderWithCost](https://docs.ccxt.com/docs/exchanges/binance#createmarketsellorderwithcost)
- [fetchOrder](https://docs.ccxt.com/docs/exchanges/binance#fetchorder)
- [fetchOrders](https://docs.ccxt.com/docs/exchanges/binance#fetchorders)
- [fetchOpenOrders](https://docs.ccxt.com/docs/exchanges/binance#fetchopenorders)
- [fetchOpenOrder](https://docs.ccxt.com/docs/exchanges/binance#fetchopenorder)
- [fetchClosedOrders](https://docs.ccxt.com/docs/exchanges/binance#fetchclosedorders)
- [fetchCanceledOrders](https://docs.ccxt.com/docs/exchanges/binance#fetchcanceledorders)
- [fetchCanceledAndClosedOrders](https://docs.ccxt.com/docs/exchanges/binance#fetchcanceledandclosedorders)
- [cancelOrder](https://docs.ccxt.com/docs/exchanges/binance#cancelorder)
- [cancelAllOrders](https://docs.ccxt.com/docs/exchanges/binance#cancelallorders)
- [cancelOrders](https://docs.ccxt.com/docs/exchanges/binance#cancelorders)
- [fetchOrderTrades](https://docs.ccxt.com/docs/exchanges/binance#fetchordertrades)
- [fetchMyTrades](https://docs.ccxt.com/docs/exchanges/binance#fetchmytrades)
- [fetchMyDustTrades](https://docs.ccxt.com/docs/exchanges/binance#fetchmydusttrades)
- [fetchDeposits](https://docs.ccxt.com/docs/exchanges/binance#fetchdeposits)
- [fetchWithdrawals](https://docs.ccxt.com/docs/exchanges/binance#fetchwithdrawals)
- [transfer](https://docs.ccxt.com/docs/exchanges/binance#transfer)
- [fetchTransfers](https://docs.ccxt.com/docs/exchanges/binance#fetchtransfers)
- [fetchDepositAddress](https://docs.ccxt.com/docs/exchanges/binance#fetchdepositaddress)
- [fetchTransactionFees](https://docs.ccxt.com/docs/exchanges/binance#fetchtransactionfees)
- [fetchDepositWithdrawFees](https://docs.ccxt.com/docs/exchanges/binance#fetchdepositwithdrawfees)
- [withdraw](https://docs.ccxt.com/docs/exchanges/binance#withdraw)
- [fetchTradingFee](https://docs.ccxt.com/docs/exchanges/binance#fetchtradingfee)
- [fetchTradingFees](https://docs.ccxt.com/docs/exchanges/binance#fetchtradingfees)
- [fetchFundingRate](https://docs.ccxt.com/docs/exchanges/binance#fetchfundingrate)
- [fetchFundingRateHistory](https://docs.ccxt.com/docs/exchanges/binance#fetchfundingratehistory)
- [fetchFundingRates](https://docs.ccxt.com/docs/exchanges/binance#fetchfundingrates)
- [fetchLeverageTiers](https://docs.ccxt.com/docs/exchanges/binance#fetchleveragetiers)
- [fetchPosition](https://docs.ccxt.com/docs/exchanges/binance#fetchposition)
- [fetchOptionPositions](https://docs.ccxt.com/docs/exchanges/binance#fetchoptionpositions)
- [fetchPositions](https://docs.ccxt.com/docs/exchanges/binance#fetchpositions)
- [fetchFundingHistory](https://docs.ccxt.com/docs/exchanges/binance#fetchfundinghistory)
- [setLeverage](https://docs.ccxt.com/docs/exchanges/binance#setleverage)
- [setMarginMode](https://docs.ccxt.com/docs/exchanges/binance#setmarginmode)
- [setPositionMode](https://docs.ccxt.com/docs/exchanges/binance#setpositionmode)
- [fetchLeverages](https://docs.ccxt.com/docs/exchanges/binance#fetchleverages)
- [fetchSettlementHistory](https://docs.ccxt.com/docs/exchanges/binance#fetchsettlementhistory)
- [fetchMySettlementHistory](https://docs.ccxt.com/docs/exchanges/binance#fetchmysettlementhistory)
- [fetchLedgerEntry](https://docs.ccxt.com/docs/exchanges/binance#fetchledgerentry)
- [fetchLedger](https://docs.ccxt.com/docs/exchanges/binance#fetchledger)
- [reduceMargin](https://docs.ccxt.com/docs/exchanges/binance#reducemargin)
- [addMargin](https://docs.ccxt.com/docs/exchanges/binance#addmargin)
- [fetchCrossBorrowRate](https://docs.ccxt.com/docs/exchanges/binance#fetchcrossborrowrate)
- [fetchIsolatedBorrowRate](https://docs.ccxt.com/docs/exchanges/binance#fetchisolatedborrowrate)
- [fetchIsolatedBorrowRates](https://docs.ccxt.com/docs/exchanges/binance#fetchisolatedborrowrates)
- [fetchBorrowRateHistory](https://docs.ccxt.com/docs/exchanges/binance#fetchborrowratehistory)
- [createGiftCode](https://docs.ccxt.com/docs/exchanges/binance#creategiftcode)
- [redeemGiftCode](https://docs.ccxt.com/docs/exchanges/binance#redeemgiftcode)
- [verifyGiftCode](https://docs.ccxt.com/docs/exchanges/binance#verifygiftcode)
- [fetchBorrowInterest](https://docs.ccxt.com/docs/exchanges/binance#fetchborrowinterest)
- [repayCrossMargin](https://docs.ccxt.com/docs/exchanges/binance#repaycrossmargin)
- [repayIsolatedMargin](https://docs.ccxt.com/docs/exchanges/binance#repayisolatedmargin)
- [borrowCrossMargin](https://docs.ccxt.com/docs/exchanges/binance#borrowcrossmargin)
- [borrowIsolatedMargin](https://docs.ccxt.com/docs/exchanges/binance#borrowisolatedmargin)
- [fetchOpenInterestHistory](https://docs.ccxt.com/docs/exchanges/binance#fetchopeninteresthistory)
- [fetchOpenInterest](https://docs.ccxt.com/docs/exchanges/binance#fetchopeninterest)
- [fetchMyLiquidations](https://docs.ccxt.com/docs/exchanges/binance#fetchmyliquidations)
- [fetchGreeks](https://docs.ccxt.com/docs/exchanges/binance#fetchgreeks)
- [fetchAllGreeks](https://docs.ccxt.com/docs/exchanges/binance#fetchallgreeks)
- [fetchPositionMode](https://docs.ccxt.com/docs/exchanges/binance#fetchpositionmode)
- [fetchMarginModes](https://docs.ccxt.com/docs/exchanges/binance#fetchmarginmodes)
- [fetchMarginMode](https://docs.ccxt.com/docs/exchanges/binance#fetchmarginmode)
- [fetchOption](https://docs.ccxt.com/docs/exchanges/binance#fetchoption)
- [fetchMarginAdjustmentHistory](https://docs.ccxt.com/docs/exchanges/binance#fetchmarginadjustmenthistory)
- [fetchConvertCurrencies](https://docs.ccxt.com/docs/exchanges/binance#fetchconvertcurrencies)
- [fetchConvertQuote](https://docs.ccxt.com/docs/exchanges/binance#fetchconvertquote)
- [createConvertTrade](https://docs.ccxt.com/docs/exchanges/binance#createconverttrade)
- [fetchConvertTrade](https://docs.ccxt.com/docs/exchanges/binance#fetchconverttrade)
- [fetchConvertTradeHistory](https://docs.ccxt.com/docs/exchanges/binance#fetchconverttradehistory)
- [fetchFundingIntervals](https://docs.ccxt.com/docs/exchanges/binance#fetchfundingintervals)
- [fetchLongShortRatioHistory](https://docs.ccxt.com/docs/exchanges/binance#fetchlongshortratiohistory)
- [fetchADLRank](https://docs.ccxt.com/docs/exchanges/binance#fetchadlrank)
- [fetchPositionsADLRank](https://docs.ccxt.com/docs/exchanges/binance#fetchpositionsadlrank)
- [watchLiquidations](https://docs.ccxt.com/docs/exchanges/binance#watchliquidations)
- [watchLiquidationsForSymbols](https://docs.ccxt.com/docs/exchanges/binance#watchliquidationsforsymbols)
- [watchMyLiquidations](https://docs.ccxt.com/docs/exchanges/binance#watchmyliquidations)
- [watchMyLiquidationsForSymbols](https://docs.ccxt.com/docs/exchanges/binance#watchmyliquidationsforsymbols)
- [watchOrderBook](https://docs.ccxt.com/docs/exchanges/binance#watchorderbook)
- [watchOrderBookForSymbols](https://docs.ccxt.com/docs/exchanges/binance#watchorderbookforsymbols)
- [unWatchOrderBookForSymbols](https://docs.ccxt.com/docs/exchanges/binance#unwatchorderbookforsymbols)
- [unWatchOrderBook](https://docs.ccxt.com/docs/exchanges/binance#unwatchorderbook)
- [fetchOrderBookWs](https://docs.ccxt.com/docs/exchanges/binance#fetchorderbookws)
- [watchTradesForSymbols](https://docs.ccxt.com/docs/exchanges/binance#watchtradesforsymbols)
- [unWatchTradesForSymbols](https://docs.ccxt.com/docs/exchanges/binance#unwatchtradesforsymbols)
- [unWatchTrades](https://docs.ccxt.com/docs/exchanges/binance#unwatchtrades)
- [watchTrades](https://docs.ccxt.com/docs/exchanges/binance#watchtrades)
- [watchOHLCV](https://docs.ccxt.com/docs/exchanges/binance#watchohlcv)
- [watchOHLCVForSymbols](https://docs.ccxt.com/docs/exchanges/binance#watchohlcvforsymbols)
- [unWatchOHLCVForSymbols](https://docs.ccxt.com/docs/exchanges/binance#unwatchohlcvforsymbols)
- [unWatchOHLCV](https://docs.ccxt.com/docs/exchanges/binance#unwatchohlcv)
- [fetchTickerWs](https://docs.ccxt.com/docs/exchanges/binance#fetchtickerws)
- [fetchOHLCVWs](https://docs.ccxt.com/docs/exchanges/binance#fetchohlcvws)
- [watchTicker](https://docs.ccxt.com/docs/exchanges/binance#watchticker)
- [watchMarkPrice](https://docs.ccxt.com/docs/exchanges/binance#watchmarkprice)
- [watchMarkPrices](https://docs.ccxt.com/docs/exchanges/binance#watchmarkprices)
- [watchTickers](https://docs.ccxt.com/docs/exchanges/binance#watchtickers)
- [unWatchTickers](https://docs.ccxt.com/docs/exchanges/binance#unwatchtickers)
- [unWatchMarkPrices](https://docs.ccxt.com/docs/exchanges/binance#unwatchmarkprices)
- [unWatchMarkPrice](https://docs.ccxt.com/docs/exchanges/binance#unwatchmarkprice)
- [unWatchBidsAsks](https://docs.ccxt.com/docs/exchanges/binance#unwatchbidsasks)
- [unWatchTicker](https://docs.ccxt.com/docs/exchanges/binance#unwatchticker)
- [watchBidsAsks](https://docs.ccxt.com/docs/exchanges/binance#watchbidsasks)
- [fetchBalanceWs](https://docs.ccxt.com/docs/exchanges/binance#fetchbalancews)
- [fetchPositionWs](https://docs.ccxt.com/docs/exchanges/binance#fetchpositionws)
- [fetchPositionsWs](https://docs.ccxt.com/docs/exchanges/binance#fetchpositionsws)
- [watchBalance](https://docs.ccxt.com/docs/exchanges/binance#watchbalance)
- [createOrderWs](https://docs.ccxt.com/docs/exchanges/binance#createorderws)
- [editOrderWs](https://docs.ccxt.com/docs/exchanges/binance#editorderws)
- [cancelOrderWs](https://docs.ccxt.com/docs/exchanges/binance#cancelorderws)
- [cancelAllOrdersWs](https://docs.ccxt.com/docs/exchanges/binance#cancelallordersws)
- [fetchOrderWs](https://docs.ccxt.com/docs/exchanges/binance#fetchorderws)
- [fetchOrdersWs](https://docs.ccxt.com/docs/exchanges/binance#fetchordersws)
- [fetchClosedOrdersWs](https://docs.ccxt.com/docs/exchanges/binance#fetchclosedordersws)
- [fetchOpenOrdersWs](https://docs.ccxt.com/docs/exchanges/binance#fetchopenordersws)
- [watchOrders](https://docs.ccxt.com/docs/exchanges/binance#watchorders)
- [watchPositions](https://docs.ccxt.com/docs/exchanges/binance#watchpositions)
- [fetchMyTradesWs](https://docs.ccxt.com/docs/exchanges/binance#fetchmytradesws)
- [fetchTradesWs](https://docs.ccxt.com/docs/exchanges/binance#fetchtradesws)
- [watchMyTrades](https://docs.ccxt.com/docs/exchanges/binance#watchmytrades)

### [enableDemoTrading](https://docs.ccxt.com/docs/exchanges/binance\#enabledemotrading)

enables or disables demo trading mode

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**See**

- [https://www.binance.com/en/support/faq/detail/9be58f73e5e14338809e3b705b9687dd](https://www.binance.com/en/support/faq/detail/9be58f73e5e14338809e3b705b9687dd)
- [https://demo.binance.com/en/my/settings/api-management](https://demo.binance.com/en/my/settings/api-management)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| enable | `boolean` | No | true if demo trading should be enabled, false otherwise |

```
binance.enableDemoTrading (enable?)
```

### [fetchTime](https://docs.ccxt.com/docs/exchanges/binance\#fetchtime)

fetches the current integer timestamp in milliseconds from the exchange server

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `int` \- the current integer timestamp in milliseconds from the exchange server

**See**

- [https://developers.binance.com/docs/binance-spot-api-docs/rest-api/general-endpoints#check-server-time](https://developers.binance.com/docs/binance-spot-api-docs/rest-api/general-endpoints#check-server-time) // spot
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Check-Server-Time](https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Check-Server-Time) // swap
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Check-Server-time](https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Check-Server-time) // future

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.subType | `string` | No | "linear" or "inverse" |

```
binance.fetchTime (params?)
```

### [fetchCurrencies](https://docs.ccxt.com/docs/exchanges/binance\#fetchcurrencies)

fetches all available currencies on an exchange

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- an associative dictionary of currencies

**See**

- [https://developers.binance.com/docs/wallet/capital/all-coins-info](https://developers.binance.com/docs/wallet/capital/all-coins-info)
- [https://developers.binance.com/docs/margin\_trading/market-data/Get-All-Margin-Assets](https://developers.binance.com/docs/margin_trading/market-data/Get-All-Margin-Assets)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

```
binance.fetchCurrencies (params?)
```

### [fetchMarkets](https://docs.ccxt.com/docs/exchanges/binance\#fetchmarkets)

retrieves data on all markets for binance

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `Array<object>` \- an array of objects representing market data

**See**

- [https://developers.binance.com/docs/binance-spot-api-docs/rest-api/general-endpoints#exchange-information](https://developers.binance.com/docs/binance-spot-api-docs/rest-api/general-endpoints#exchange-information) // spot
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Exchange-Information](https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Exchange-Information) // swap
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Exchange-Information](https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Exchange-Information) // future
- [https://developers.binance.com/docs/derivatives/option/market-data/Exchange-Information](https://developers.binance.com/docs/derivatives/option/market-data/Exchange-Information) // option
- [https://developers.binance.com/docs/margin\_trading/market-data/Get-All-Cross-Margin-Pairs](https://developers.binance.com/docs/margin_trading/market-data/Get-All-Cross-Margin-Pairs) // cross margin
- [https://developers.binance.com/docs/margin\_trading/market-data/Get-All-Isolated-Margin-Symbol](https://developers.binance.com/docs/margin_trading/market-data/Get-All-Isolated-Margin-Symbol) // isolated margin
- [https://developers.binance.com/en/docs/catalog/advanced-trading-stocks-trading/api/rest-api/market-data#exchange-info](https://developers.binance.com/en/docs/catalog/advanced-trading-stocks-trading/api/rest-api/market-data#exchange-info) // tokenized stocks

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

```
binance.fetchMarkets (params?)
```

### [fetchBalance](https://docs.ccxt.com/docs/exchanges/binance\#fetchbalance)

query for balance and get the amount of funds available for trading or funds locked in orders

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- a [balance structure](https://docs.ccxt.com/docs/manual#balance-structure)

**See**

- [https://developers.binance.com/docs/binance-spot-api-docs/rest-api/account-endpoints#account-information-user\_data](https://developers.binance.com/docs/binance-spot-api-docs/rest-api/account-endpoints#account-information-user_data) // spot
- [https://developers.binance.com/docs/margin\_trading/account/Query-Cross-Margin-Account-Details](https://developers.binance.com/docs/margin_trading/account/Query-Cross-Margin-Account-Details) // cross margin
- [https://developers.binance.com/docs/margin\_trading/account/Query-Isolated-Margin-Account-Info](https://developers.binance.com/docs/margin_trading/account/Query-Isolated-Margin-Account-Info) // isolated margin
- [https://developers.binance.com/docs/wallet/asset/funding-wallet](https://developers.binance.com/docs/wallet/asset/funding-wallet) // funding
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Futures-Account-Balance-V2](https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Futures-Account-Balance-V2) // swap
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/account/rest-api/Futures-Account-Balance](https://developers.binance.com/docs/derivatives/coin-margined-futures/account/rest-api/Futures-Account-Balance) // future
- [https://developers.binance.com/docs/derivatives/option/account/Option-Account-Information](https://developers.binance.com/docs/derivatives/option/account/Option-Account-Information) // option
- [https://developers.binance.com/docs/derivatives/portfolio-margin/account/Account-Balance](https://developers.binance.com/docs/derivatives/portfolio-margin/account/Account-Balance) // portfolio margin

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.type | `string` | No | 'future', 'delivery', 'savings', 'funding', or 'spot' or 'papi' |
| params.marginMode | `string` | No | 'cross' or 'isolated', for margin trading, uses this.options.defaultMarginMode if not passed, defaults to undefined/None/null |
| params.symbols | `Array<string>`, `undefined` | No | unified market symbols, only used in isolated margin mode |
| params.portfolioMargin | `boolean` | No | set to true if you would like to fetch the balance for a portfolio margin account |
| params.subType | `string` | No | 'linear' or 'inverse' |

```
binance.fetchBalance (params?)
```

### [fetchOrderBook](https://docs.ccxt.com/docs/exchanges/binance\#fetchorderbook)

fetches information on open orders with bid (buy) and ask (sell) prices, volumes and other data

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- an [order book structure](https://docs.ccxt.com/docs/manual#order-book-structure)

**See**

- [https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints#order-book](https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints#order-book) // spot
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Order-Book](https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Order-Book) // swap
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Order-Book-RPI](https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Order-Book-RPI) // swap rpi
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Order-Book](https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Order-Book) // future
- [https://developers.binance.com/docs/derivatives/option/market-data/Order-Book](https://developers.binance.com/docs/derivatives/option/market-data/Order-Book) // option

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to fetch the order book for |
| limit | `int` | No | the maximum amount of order book entries to return |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.rpi | `boolean` | No | _future only_ set to true to use the RPI endpoint |

```
binance.fetchOrderBook (symbol, limit?, params?)
```

### [fetchStatus](https://docs.ccxt.com/docs/exchanges/binance\#fetchstatus)

the latest known information on the availability of the exchange API

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- a [status structure](https://docs.ccxt.com/docs/manual#exchange-status-structure)

**See**: [https://developers.binance.com/docs/wallet/others/system-status](https://developers.binance.com/docs/wallet/others/system-status)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

```
binance.fetchStatus (params?)
```

### [fetchTicker](https://docs.ccxt.com/docs/exchanges/binance\#fetchticker)

fetches a price ticker, a statistical calculation with the information calculated over the past 24 hours for a specific market

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- a [ticker structure](https://docs.ccxt.com/docs/manual#ticker-structure)

**See**

- [https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints#24hr-ticker-price-change-statistics](https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints#24hr-ticker-price-change-statistics) // spot
- [https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints#rolling-window-price-change-statistics](https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints#rolling-window-price-change-statistics) // spot
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/24hr-Ticker-Price-Change-Statistics](https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/24hr-Ticker-Price-Change-Statistics) // swap
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/24hr-Ticker-Price-Change-Statistics](https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/24hr-Ticker-Price-Change-Statistics) // future
- [https://developers.binance.com/docs/derivatives/option/market-data/24hr-Ticker-Price-Change-Statistics](https://developers.binance.com/docs/derivatives/option/market-data/24hr-Ticker-Price-Change-Statistics) // option
- [https://developers.binance.com/en/docs/catalog/advanced-trading-stocks-trading/api/rest-api/market-data#latest-quote](https://developers.binance.com/en/docs/catalog/advanced-trading-stocks-trading/api/rest-api/market-data#latest-quote) // stock

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to fetch the ticker for |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.rolling | `boolean` | No | (spot only) default false, if true, uses the rolling 24 hour ticker endpoint /api/v3/ticker |

```
binance.fetchTicker (symbol, params?)
```

### [fetchBidsAsks](https://docs.ccxt.com/docs/exchanges/binance\#fetchbidsasks)

fetches the bid and ask price and volume for multiple markets

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- a dictionary of [ticker structures](https://docs.ccxt.com/docs/manual#ticker-structure) tokenized stock symbols are not supported here, use fetchTicker() per symbol instead

**See**

- [https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints#symbol-order-book-ticker](https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints#symbol-order-book-ticker) // spot
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Symbol-Order-Book-Ticker](https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Symbol-Order-Book-Ticker) // swap
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Symbol-Order-Book-Ticker](https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Symbol-Order-Book-Ticker) // future
- [https://developers.binance.com/docs/derivatives/options-trading/market-data/24hr-Ticker-Price-Change-Statistics](https://developers.binance.com/docs/derivatives/options-trading/market-data/24hr-Ticker-Price-Change-Statistics) // option

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>`, `undefined` | Yes | unified symbols of the markets to fetch the bids and asks for, all markets are returned if not assigned |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.subType | `string` | No | "linear" or "inverse" |

```
binance.fetchBidsAsks (symbols, params?)
```

### [fetchLastPrices](https://docs.ccxt.com/docs/exchanges/binance\#fetchlastprices)

fetches the last price for multiple markets

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- a dictionary of lastprices structures

**See**

- [https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints#symbol-price-ticker](https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints#symbol-price-ticker) // spot
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Symbol-Price-Ticker](https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Symbol-Price-Ticker) // swap
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Symbol-Price-Ticker](https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Symbol-Price-Ticker) // future

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>`, `undefined` | Yes | unified symbols of the markets to fetch the last prices |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.subType | `string` | No | "linear" or "inverse" |

```
binance.fetchLastPrices (symbols, params?)
```

### [fetchTickers](https://docs.ccxt.com/docs/exchanges/binance\#fetchtickers)

fetches price tickers for multiple markets, statistical information calculated over the past 24 hours for each market

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- a dictionary of [ticker structures](https://docs.ccxt.com/docs/manual#ticker-structure) tokenized stock symbols are not supported here, use fetchTicker() per symbol instead

**See**

- [https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints#24hr-ticker-price-change-statistics](https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints#24hr-ticker-price-change-statistics) // spot
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/24hr-Ticker-Price-Change-Statistics](https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/24hr-Ticker-Price-Change-Statistics) // swap
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/24hr-Ticker-Price-Change-Statistics](https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/24hr-Ticker-Price-Change-Statistics) // future
- [https://developers.binance.com/docs/derivatives/option/market-data/24hr-Ticker-Price-Change-Statistics](https://developers.binance.com/docs/derivatives/option/market-data/24hr-Ticker-Price-Change-Statistics) // option

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>` | No | unified symbols of the markets to fetch the ticker for, all market tickers are returned if not assigned |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.subType | `string` | No | "linear" or "inverse" |
| params.type | `string` | No | 'spot', 'option', use params\["subType"\] for swap and future markets |

```
binance.fetchTickers (symbols?, params?)
```

### [fetchMarkPrice](https://docs.ccxt.com/docs/exchanges/binance\#fetchmarkprice)

fetches mark price for the market

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- a dictionary of [ticker structures](https://docs.ccxt.com/docs/manual#ticker-structure)

**See**

- [https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Index-Price-and-Mark-Price](https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Index-Price-and-Mark-Price)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Mark-Price](https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Mark-Price)
- [https://developers.binance.com/docs/derivatives/options-trading/market-data/Option-Mark-Price](https://developers.binance.com/docs/derivatives/options-trading/market-data/Option-Mark-Price)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to fetch the ticker for |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.subType | `string` | No | "linear" or "inverse" |

```
binance.fetchMarkPrice (symbol, params?)
```

### [fetchMarkPrices](https://docs.ccxt.com/docs/exchanges/binance\#fetchmarkprices)

fetches mark prices for multiple markets

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- a dictionary of [ticker structures](https://docs.ccxt.com/docs/manual#ticker-structure)

**See**

- [https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Index-Price-and-Mark-Price](https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Index-Price-and-Mark-Price)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Mark-Price](https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Mark-Price)
- [https://developers.binance.com/docs/derivatives/options-trading/market-data/Option-Mark-Price](https://developers.binance.com/docs/derivatives/options-trading/market-data/Option-Mark-Price)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>` | No | unified symbols of the markets to fetch the ticker for, all market tickers are returned if not assigned |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.subType | `string` | No | "linear" or "inverse" |

```
binance.fetchMarkPrices (symbols?, params?)
```

### [fetchOHLCV](https://docs.ccxt.com/docs/exchanges/binance\#fetchohlcv)

fetches historical candlestick data containing the open, high, low, and close price, and the volume of a market

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `Array<Array<int>>` \- A list of candles ordered as timestamp, open, high, low, close, volume

**See**

- [https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints#klinecandlestick-data](https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints#klinecandlestick-data)
- [https://developers.binance.com/docs/derivatives/option/market-data/Kline-Candlestick-Data](https://developers.binance.com/docs/derivatives/option/market-data/Kline-Candlestick-Data)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Kline-Candlestick-Data](https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Kline-Candlestick-Data)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Index-Price-Kline-Candlestick-Data](https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Index-Price-Kline-Candlestick-Data)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Mark-Price-Kline-Candlestick-Data](https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Mark-Price-Kline-Candlestick-Data)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Premium-Index-Kline-Data](https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Premium-Index-Kline-Data)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Kline-Candlestick-Data](https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Kline-Candlestick-Data)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Index-Price-Kline-Candlestick-Data](https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Index-Price-Kline-Candlestick-Data)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Mark-Price-Kline-Candlestick-Data](https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Mark-Price-Kline-Candlestick-Data)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Premium-Index-Kline-Data](https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Premium-Index-Kline-Data)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to fetch OHLCV data for |
| timeframe | `string` | Yes | the length of time each candle represents |
| since | `int` | No | timestamp in ms of the earliest candle to fetch |
| limit | `int` | No | the maximum amount of candles to fetch |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.price | `string` | No | "mark" or "index" for mark price and index price candles |
| params.until | `int` | No | timestamp in ms of the latest candle to fetch |
| params.paginate | `boolean` | No | default false, when true will automatically paginate by calling this endpoint multiple times. See in the docs all the [available parameters](https://docs.ccxt.com/docs/manual#pagination-params) |

```
binance.fetchOHLCV (symbol, timeframe, since?, limit?, params?)
```

### [fetchTrades](https://docs.ccxt.com/docs/exchanges/binance\#fetchtrades)

get the list of most recent trades for a particular symbol
Default fetchTradesMethod

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `Array<Trade>` \- a list of [trade structures](https://docs.ccxt.com/docs/manual#public-trades)

**See**

- [https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints#compressedaggregate-trades-list](https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints#compressedaggregate-trades-list) // publicGetAggTrades (spot)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Compressed-Aggregate-Trades-List](https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Compressed-Aggregate-Trades-List) // fapiPublicGetAggTrades (swap)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Compressed-Aggregate-Trades-List](https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Compressed-Aggregate-Trades-List) // dapiPublicGetAggTrades (future)
- [https://developers.binance.com/docs/derivatives/option/market-data/Recent-Trades-List](https://developers.binance.com/docs/derivatives/option/market-data/Recent-Trades-List) // eapiPublicGetTrades (option)
Other fetchTradesMethod
- [https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints#recent-trades-list](https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints#recent-trades-list) // publicGetTrades (spot)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Recent-Trades-List](https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Recent-Trades-List) // fapiPublicGetTrades (swap)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Recent-Trades-List](https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Recent-Trades-List) // dapiPublicGetTrades (future)
- [https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints#old-trade-lookup](https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints#old-trade-lookup) // publicGetHistoricalTrades (spot)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Old-Trades-Lookup](https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Old-Trades-Lookup) // fapiPublicGetHistoricalTrades (swap)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Old-Trades-Lookup](https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Old-Trades-Lookup) // dapiPublicGetHistoricalTrades (future)
- [https://developers.binance.com/docs/derivatives/option/market-data/Old-Trades-Lookup](https://developers.binance.com/docs/derivatives/option/market-data/Old-Trades-Lookup) // eapiPublicGetHistoricalTrades (option)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to fetch trades for |
| since | `int` | No | only used when fetchTradesMethod is 'publicGetAggTrades', 'fapiPublicGetAggTrades', or 'dapiPublicGetAggTrades' |
| limit | `int` | No | default 500, max 1000 |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.until | `int` | No | only used when fetchTradesMethod is 'publicGetAggTrades', 'fapiPublicGetAggTrades', or 'dapiPublicGetAggTrades' |
| params.fetchTradesMethod | `int` | No | 'publicGetAggTrades' (spot default), 'fapiPublicGetAggTrades' (swap default), 'dapiPublicGetAggTrades' (future default), 'eapiPublicGetTrades' (option default), 'publicGetTrades', 'fapiPublicGetTrades', 'dapiPublicGetTrades', 'publicGetHistoricalTrades', 'fapiPublicGetHistoricalTrades', 'dapiPublicGetHistoricalTrades', 'eapiPublicGetHistoricalTrades' |
| params.paginate | `boolean` | No | default false, when true will automatically paginate by calling this endpoint multiple times. See in the docs all the [availble parameters](https://docs.ccxt.com/docs/manual#pagination-params) EXCHANGE SPECIFIC PARAMETERS |
| params.fromId | `int` | No | trade id to fetch from, default gets most recent trades, not used when fetchTradesMethod is 'publicGetTrades', 'fapiPublicGetTrades', 'dapiPublicGetTrades', or 'eapiPublicGetTrades' |

```
binance.fetchTrades (symbol, since?, limit?, params?)
```

### [editContractOrder](https://docs.ccxt.com/docs/exchanges/binance\#editcontractorder)

edit a trade order

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- an [order structure](https://docs.ccxt.com/docs/manual#order-structure)

**See**

- [https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Modify-Order](https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Modify-Order)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/Modify-Order](https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/Modify-Order)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Modify-UM-Order](https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Modify-UM-Order)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Modify-CM-Order](https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Modify-CM-Order)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| id | `string` | Yes | cancel order id |
| symbol | `string` | Yes | unified symbol of the market to create an order in |
| type | `string` | Yes | 'market' or 'limit' |
| side | `string` | Yes | 'buy' or 'sell' |
| amount | `float` | Yes | how much of currency you want to trade in units of base currency |
| price | `float` | No | the price at which the order is to be fulfilled, in units of the quote currency, ignored in market orders |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.portfolioMargin | `boolean` | No | set to true if you would like to edit an order in a portfolio margin account |

```
binance.editContractOrder (id, symbol, type, side, amount, price?, params?)
```

### [editOrder](https://docs.ccxt.com/docs/exchanges/binance\#editorder)

edit a trade order

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- an [order structure](https://docs.ccxt.com/docs/manual#order-structure)

**See**

- [https://developers.binance.com/docs/binance-spot-api-docs/rest-api/trading-endpoints#cancel-an-existing-order-and-send-a-new-order-trade](https://developers.binance.com/docs/binance-spot-api-docs/rest-api/trading-endpoints#cancel-an-existing-order-and-send-a-new-order-trade)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Modify-Order](https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Modify-Order)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/Modify-Order](https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/Modify-Order)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| id | `string` | Yes | cancel order id |
| symbol | `string` | Yes | unified symbol of the market to create an order in |
| type | `string` | Yes | 'market' or 'limit' |
| side | `string` | Yes | 'buy' or 'sell' |
| amount | `float` | Yes | how much of currency you want to trade in units of base currency |
| price | `float` | No | the price at which the order is to be fulfilled, in units of the quote currency, ignored in market orders |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

```
binance.editOrder (id, symbol, type, side, amount, price?, params?)
```

### [editOrders](https://docs.ccxt.com/docs/exchanges/binance\#editorders)

edit a list of trade orders

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- an [order structure](https://docs.ccxt.com/docs/manual#order-structure)

**See**

- [https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Modify-Multiple-Orders](https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Modify-Multiple-Orders)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/Modify-Multiple-Orders](https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/Modify-Multiple-Orders)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| orders | `Array` | Yes | list of orders to create, each object should contain the parameters required by createOrder, namely symbol, type, side, amount, price and params |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

```
binance.editOrders (orders, params?)
```

### [createOrders](https://docs.ccxt.com/docs/exchanges/binance\#createorders)

_contract only_ create a list of trade orders

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- an [order structure](https://docs.ccxt.com/docs/manual#order-structure)

**See**

- [https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/Place-Multiple-Orders](https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/Place-Multiple-Orders)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Place-Multiple-Orders](https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Place-Multiple-Orders)
- [https://developers.binance.com/docs/derivatives/option/trade/Place-Multiple-Orders](https://developers.binance.com/docs/derivatives/option/trade/Place-Multiple-Orders)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| orders | `Array` | Yes | list of orders to create, each object should contain the parameters required by createOrder, namely symbol, type, side, amount, price and params |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

```
binance.createOrders (orders, params?)
```

### [createOrder](https://docs.ccxt.com/docs/exchanges/binance\#createorder)

create a trade order

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- an [order structure](https://docs.ccxt.com/docs/manual#order-structure)

**See**

- [https://developers.binance.com/docs/binance-spot-api-docs/rest-api/trading-endpoints#new-order-trade](https://developers.binance.com/docs/binance-spot-api-docs/rest-api/trading-endpoints#new-order-trade)
- [https://developers.binance.com/docs/binance-spot-api-docs/testnet/rest-api/trading-endpoints#test-new-order-trade](https://developers.binance.com/docs/binance-spot-api-docs/testnet/rest-api/trading-endpoints#test-new-order-trade)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/New-Order](https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/New-Order)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api](https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api)
- [https://developers.binance.com/docs/derivatives/option/trade/New-Order](https://developers.binance.com/docs/derivatives/option/trade/New-Order)
- [https://developers.binance.com/docs/binance-spot-api-docs/rest-api/trading-endpoints#sor](https://developers.binance.com/docs/binance-spot-api-docs/rest-api/trading-endpoints#sor)
- [https://developers.binance.com/docs/binance-spot-api-docs/testnet/rest-api/trading-endpoints#sor](https://developers.binance.com/docs/binance-spot-api-docs/testnet/rest-api/trading-endpoints#sor)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/trade/New-UM-Order](https://developers.binance.com/docs/derivatives/portfolio-margin/trade/New-UM-Order)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/trade/New-CM-Order](https://developers.binance.com/docs/derivatives/portfolio-margin/trade/New-CM-Order)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/trade/New-Margin-Order](https://developers.binance.com/docs/derivatives/portfolio-margin/trade/New-Margin-Order)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/trade/New-UM-Conditional-Order](https://developers.binance.com/docs/derivatives/portfolio-margin/trade/New-UM-Conditional-Order)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/trade/New-CM-Conditional-Order](https://developers.binance.com/docs/derivatives/portfolio-margin/trade/New-CM-Conditional-Order)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/New-Algo-Order](https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/New-Algo-Order)
- [https://developers.binance.com/en/docs/catalog/advanced-trading-stocks-trading/api/rest-api/trade#place-equity-order](https://developers.binance.com/en/docs/catalog/advanced-trading-stocks-trading/api/rest-api/trade#place-equity-order)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to create an order in |
| type | `string` | Yes | 'market' or 'limit' or 'STOP\_LOSS' or 'STOP\_LOSS\_LIMIT' or 'TAKE\_PROFIT' or 'TAKE\_PROFIT\_LIMIT' or 'STOP' |
| side | `string` | Yes | 'buy' or 'sell' |
| amount | `float` | Yes | how much of you want to trade in units of the base currency |
| price | `float` | No | the price that the order is to be fulfilled, in units of the quote currency, ignored in market orders |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.reduceOnly | `string` | No | for swap and future reduceOnly is a string 'true' or 'false' that cant be sent with close position set to true or in hedge mode. For spot margin and option reduceOnly is a boolean. |
| params.marginMode | `string` | No | 'cross' or 'isolated', for spot margin trading |
| params.sor | `boolean` | No | _spot only_ whether to use SOR (Smart Order Routing) or not, default is false |
| params.test | `boolean` | No | _spot only_ whether to use the test endpoint or not, default is false |
| params.trailingPercent | `float` | No | the percent to trail away from the current market price |
| params.trailingTriggerPrice | `float` | No | the price to trigger a trailing order, default uses the price argument |
| params.triggerPrice | `float` | No | the price that a trigger order is triggered at |
| params.stopLossPrice | `float` | No | the price that a stop loss order is triggered at |
| params.takeProfitPrice | `float` | No | the price that a take profit order is triggered at |
| params.portfolioMargin | `boolean` | No | set to true if you would like to create an order in a portfolio margin account |
| params.selfTradePrevention | `string` | No | set unified value for stp, one of NONE, EXPIRE\_MAKER, EXPIRE\_TAKER or EXPIRE\_BOTH |
| params.icebergAmount | `float` | No | set iceberg amount for limit orders |
| params.stopLossOrTakeProfit | `string` | No | 'stopLoss' or 'takeProfit', required for spot trailing orders |
| params.positionSide | `string` | No | _swap and portfolio margin only_ "BOTH" for one-way mode, "LONG" for buy side of hedged mode, "SHORT" for sell side of hedged mode |
| params.hedged | `bool` | No | _swap and portfolio margin only_ true for hedged mode, false for one way mode, default is false |
| params.clientOrderId | `string` | No | the clientOrderId of the order |
| params.tradingSession | `string` | No | _stock only_ required for limit orders, RTH, EXTENDED or 24H, default is 24H |

```
binance.createOrder (symbol, type, side, amount, price?, params?)
```

### [createMarketOrderWithCost](https://docs.ccxt.com/docs/exchanges/binance\#createmarketorderwithcost)

create a market order by providing the symbol, side and cost

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- an [order structure](https://docs.ccxt.com/docs/manual#order-structure)

**See**: [https://developers.binance.com/docs/binance-spot-api-docs/rest-api/trading-endpoints#new-order-trade](https://developers.binance.com/docs/binance-spot-api-docs/rest-api/trading-endpoints#new-order-trade)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to create an order in |
| side | `string` | Yes | 'buy' or 'sell' |
| cost | `float` | Yes | how much you want to trade in units of the quote currency |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

```
binance.createMarketOrderWithCost (symbol, side, cost, params?)
```

### [createMarketBuyOrderWithCost](https://docs.ccxt.com/docs/exchanges/binance\#createmarketbuyorderwithcost)

create a market buy order by providing the symbol and cost

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- an [order structure](https://docs.ccxt.com/docs/manual#order-structure)

**See**: [https://developers.binance.com/docs/binance-spot-api-docs/rest-api/trading-endpoints#new-order-trade](https://developers.binance.com/docs/binance-spot-api-docs/rest-api/trading-endpoints#new-order-trade)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to create an order in |
| cost | `float` | Yes | how much you want to trade in units of the quote currency |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

```
binance.createMarketBuyOrderWithCost (symbol, cost, params?)
```

### [createMarketSellOrderWithCost](https://docs.ccxt.com/docs/exchanges/binance\#createmarketsellorderwithcost)

create a market sell order by providing the symbol and cost

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- an [order structure](https://docs.ccxt.com/docs/manual#order-structure)

**See**: [https://developers.binance.com/docs/binance-spot-api-docs/rest-api/trading-endpoints#new-order-trade](https://developers.binance.com/docs/binance-spot-api-docs/rest-api/trading-endpoints#new-order-trade)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to create an order in |
| cost | `float` | Yes | how much you want to trade in units of the quote currency |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

```
binance.createMarketSellOrderWithCost (symbol, cost, params?)
```

### [fetchOrder](https://docs.ccxt.com/docs/exchanges/binance\#fetchorder)

fetches information on an order made by the user

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- An [order structure](https://docs.ccxt.com/docs/manual#order-structure)

**See**

- [https://developers.binance.com/docs/binance-spot-api-docs/rest-api/trading-endpoints#query-order-user\_data](https://developers.binance.com/docs/binance-spot-api-docs/rest-api/trading-endpoints#query-order-user_data)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Query-Order](https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Query-Order)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/Query-Order](https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/Query-Order)
- [https://developers.binance.com/docs/derivatives/option/trade/Query-Single-Order](https://developers.binance.com/docs/derivatives/option/trade/Query-Single-Order)
- [https://developers.binance.com/docs/margin\_trading/trade/Query-Margin-Account-Order](https://developers.binance.com/docs/margin_trading/trade/Query-Margin-Account-Order)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-UM-Order](https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-UM-Order)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-CM-Order](https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-CM-Order)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Query-Algo-Order](https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Query-Algo-Order)
- [https://developers.binance.com/en/docs/catalog/advanced-trading-stocks-trading/api/rest-api/trade#equity-order-detail](https://developers.binance.com/en/docs/catalog/advanced-trading-stocks-trading/api/rest-api/trade#equity-order-detail)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| id | `string` | Yes | the order id |
| symbol | `string` | Yes | unified symbol of the market the order was made in |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.marginMode | `string` | No | 'cross' or 'isolated', for spot margin trading |
| params.portfolioMargin | `boolean` | No | set to true if you would like to fetch an order in a portfolio margin account |
| params.trigger | `boolean` | No | set to true if you would like to fetch a trigger or conditional order |
| params.stock | `boolean` | No | set to true if you would like to fetch tokenized stock orders |

```
binance.fetchOrder (id, symbol, params?)
```

### [fetchOrders](https://docs.ccxt.com/docs/exchanges/binance\#fetchorders)

fetches information on multiple orders made by the user

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `Array<Order>` \- a list of [order structures](https://docs.ccxt.com/docs/manual#order-structure)

**See**

- [https://developers.binance.com/docs/binance-spot-api-docs/rest-api/trading-endpoints#all-orders-user\_data](https://developers.binance.com/docs/binance-spot-api-docs/rest-api/trading-endpoints#all-orders-user_data)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/All-Orders](https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/All-Orders)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/All-Orders](https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/All-Orders)
- [https://developers.binance.com/docs/derivatives/option/trade/Query-Option-Order-History](https://developers.binance.com/docs/derivatives/option/trade/Query-Option-Order-History)
- [https://developers.binance.com/docs/margin\_trading/trade/Query-Margin-Account-All-Orders](https://developers.binance.com/docs/margin_trading/trade/Query-Margin-Account-All-Orders)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-UM-Orders](https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-UM-Orders)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-CM-Orders](https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-CM-Orders)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-UM-Conditional-Orders](https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-UM-Conditional-Orders)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-CM-Conditional-Orders](https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-CM-Conditional-Orders)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Query-All-Algo-Orders](https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Query-All-Algo-Orders)
- [https://developers.binance.com/en/docs/catalog/advanced-trading-stocks-trading/api/rest-api/trade#equity-order-history](https://developers.binance.com/en/docs/catalog/advanced-trading-stocks-trading/api/rest-api/trade#equity-order-history)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol of the market orders were made in |
| since | `int` | No | the earliest time in ms to fetch orders for |
| limit | `int` | No | the maximum number of order structures to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.marginMode | `string` | No | 'cross' or 'isolated', for spot margin trading |
| params.until | `int` | No | the latest time in ms to fetch orders for |
| params.paginate | `boolean` | No | default false, when true will automatically paginate by calling this endpoint multiple times. See in the docs all the [available parameters](https://docs.ccxt.com/docs/manual#pagination-params) |
| params.portfolioMargin | `boolean` | No | set to true if you would like to fetch orders in a portfolio margin account |
| params.trigger | `boolean` | No | set to true if you would like to fetch portfolio margin account trigger or conditional orders |
| params.stock | `boolean` | No | set to true if you would like to fetch tokenized stock orders |

```
binance.fetchOrders (symbol, since?, limit?, params?)
```

### [fetchOpenOrders](https://docs.ccxt.com/docs/exchanges/binance\#fetchopenorders)

fetch all unfilled currently open orders

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `Array<Order>` \- a list of [order structures](https://docs.ccxt.com/docs/manual#order-structure)

**See**

- [https://developers.binance.com/docs/binance-spot-api-docs/rest-api/trading-endpoints#current-open-orders-user\_data](https://developers.binance.com/docs/binance-spot-api-docs/rest-api/trading-endpoints#current-open-orders-user_data)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Current-All-Open-Orders](https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Current-All-Open-Orders)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/Current-All-Open-Orders](https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/Current-All-Open-Orders)
- [https://developers.binance.com/docs/derivatives/option/trade/Query-Current-Open-Option-Orders](https://developers.binance.com/docs/derivatives/option/trade/Query-Current-Open-Option-Orders)
- [https://developers.binance.com/docs/margin\_trading/trade/Query-Margin-Account-Open-Orders](https://developers.binance.com/docs/margin_trading/trade/Query-Margin-Account-Open-Orders)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-Current-UM-Open-Orders](https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-Current-UM-Open-Orders)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-Current-UM-Open-Conditional-Orders](https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-Current-UM-Open-Conditional-Orders)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-Current-CM-Open-Orders](https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-Current-CM-Open-Orders)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-Current-CM-Open-Conditional-Orders](https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-Current-CM-Open-Conditional-Orders)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Current-All-Algo-Open-Orders](https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Current-All-Algo-Open-Orders)
- [https://developers.binance.com/en/docs/catalog/advanced-trading-stocks-trading/api/rest-api/trade#current-open-orders](https://developers.binance.com/en/docs/catalog/advanced-trading-stocks-trading/api/rest-api/trade#current-open-orders)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | No | unified market symbol |
| since | `int` | No | the earliest time in ms to fetch open orders for |
| limit | `int` | No | the maximum number of open orders structures to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.marginMode | `string` | No | 'cross' or 'isolated', for spot margin trading |
| params.portfolioMargin | `boolean` | No | set to true if you would like to fetch open orders in the portfolio margin account |
| params.trigger | `boolean` | No | set to true if you would like to fetch portfolio margin account conditional orders |
| params.stock | `boolean` | No | set to true if you would like to fetch tokenized stock orders |
| params.subType | `string` | No | "linear" or "inverse" |

```
binance.fetchOpenOrders (symbol?, since?, limit?, params?)
```

### [fetchOpenOrder](https://docs.ccxt.com/docs/exchanges/binance\#fetchopenorder)

fetch an open order by the id

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- an [order structure](https://docs.ccxt.com/docs/manual#order-structure)

**See**

- [https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Query-Current-Open-Order](https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Query-Current-Open-Order)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/Query-Current-Open-Order](https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/Query-Current-Open-Order)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-Current-UM-Open-Order](https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-Current-UM-Open-Order)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-Current-UM-Open-Conditional-Order](https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-Current-UM-Open-Conditional-Order)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-Current-CM-Open-Order](https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-Current-CM-Open-Order)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-Current-CM-Open-Conditional-Order](https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-Current-CM-Open-Conditional-Order)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| id | `string` | Yes | order id |
| symbol | `string` | Yes | unified market symbol |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.trigger | `string` | No | set to true if you would like to fetch portfolio margin account stop or conditional orders |
| params.portfolioMargin | `boolean` | No | set to true if you would like to fetch for a portfolio margin account |

```
binance.fetchOpenOrder (id, symbol, params?)
```

### [fetchClosedOrders](https://docs.ccxt.com/docs/exchanges/binance\#fetchclosedorders)

fetches information on multiple closed orders made by the user

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `Array<Order>` \- a list of [order structures](https://docs.ccxt.com/docs/manual#order-structure)

**See**

- [https://developers.binance.com/docs/binance-spot-api-docs/rest-api/trading-endpoints#all-orders-user\_data](https://developers.binance.com/docs/binance-spot-api-docs/rest-api/trading-endpoints#all-orders-user_data)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/All-Orders](https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/All-Orders)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/All-Orders](https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/All-Orders)
- [https://developers.binance.com/docs/derivatives/option/trade/Query-Option-Order-History](https://developers.binance.com/docs/derivatives/option/trade/Query-Option-Order-History)
- [https://developers.binance.com/docs/margin\_trading/trade/Query-Margin-Account-All-Orders](https://developers.binance.com/docs/margin_trading/trade/Query-Margin-Account-All-Orders)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-UM-Orders](https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-UM-Orders)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-CM-Orders](https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-CM-Orders)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-UM-Conditional-Orders](https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-UM-Conditional-Orders)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-CM-Conditional-Orders](https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-CM-Conditional-Orders)
- [https://developers.binance.com/en/docs/catalog/advanced-trading-stocks-trading/api/rest-api/trade#equity-order-history](https://developers.binance.com/en/docs/catalog/advanced-trading-stocks-trading/api/rest-api/trade#equity-order-history)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | No | unified market symbol of the market orders were made in |
| since | `int` | No | the earliest time in ms to fetch orders for |
| limit | `int` | No | the maximum number of order structures to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.paginate | `boolean` | No | default false, when true will automatically paginate by calling this endpoint multiple times. See in the docs all the [available parameters](https://docs.ccxt.com/docs/manual#pagination-params) |
| params.portfolioMargin | `boolean` | No | set to true if you would like to fetch orders in a portfolio margin account |
| params.trigger | `boolean` | No | set to true if you would like to fetch portfolio margin account trigger or conditional orders |
| params.stock | `boolean` | No | set to true if you would like to fetch tokenized stock orders |

```
binance.fetchClosedOrders (symbol?, since?, limit?, params?)
```

### [fetchCanceledOrders](https://docs.ccxt.com/docs/exchanges/binance\#fetchcanceledorders)

fetches information on multiple canceled orders made by the user

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `Array<object>` \- a list of [order structures](https://docs.ccxt.com/docs/manual#order-structure)

**See**

- [https://developers.binance.com/docs/binance-spot-api-docs/rest-api/trading-endpoints#all-orders-user\_data](https://developers.binance.com/docs/binance-spot-api-docs/rest-api/trading-endpoints#all-orders-user_data)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/All-Orders](https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/All-Orders)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/All-Orders](https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/All-Orders)
- [https://developers.binance.com/docs/derivatives/option/trade/Query-Option-Order-History](https://developers.binance.com/docs/derivatives/option/trade/Query-Option-Order-History)
- [https://developers.binance.com/docs/margin\_trading/trade/Query-Margin-Account-All-Orders](https://developers.binance.com/docs/margin_trading/trade/Query-Margin-Account-All-Orders)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-UM-Orders](https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-UM-Orders)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-CM-Orders](https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-CM-Orders)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-UM-Conditional-Orders](https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-UM-Conditional-Orders)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-CM-Conditional-Orders](https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-CM-Conditional-Orders)
- [https://developers.binance.com/en/docs/catalog/advanced-trading-stocks-trading/api/rest-api/trade#equity-order-history](https://developers.binance.com/en/docs/catalog/advanced-trading-stocks-trading/api/rest-api/trade#equity-order-history)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | No | unified market symbol of the market the orders were made in |
| since | `int` | No | the earliest time in ms to fetch orders for |
| limit | `int` | No | the maximum number of order structures to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.paginate | `boolean` | No | default false, when true will automatically paginate by calling this endpoint multiple times. See in the docs all the [available parameters](https://docs.ccxt.com/docs/manual#pagination-params) |
| params.portfolioMargin | `boolean` | No | set to true if you would like to fetch orders in a portfolio margin account |
| params.trigger | `boolean` | No | set to true if you would like to fetch portfolio margin account trigger or conditional orders |
| params.stock | `boolean` | No | set to true if you would like to fetch tokenized stock orders |

```
binance.fetchCanceledOrders (symbol?, since?, limit?, params?)
```

### [fetchCanceledAndClosedOrders](https://docs.ccxt.com/docs/exchanges/binance\#fetchcanceledandclosedorders)

fetches information on multiple canceled orders made by the user

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `Array<object>` \- a list of [order structures](https://docs.ccxt.com/docs/manual#order-structure)

**See**

- [https://developers.binance.com/docs/binance-spot-api-docs/rest-api/trading-endpoints#all-orders-user\_data](https://developers.binance.com/docs/binance-spot-api-docs/rest-api/trading-endpoints#all-orders-user_data)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/All-Orders](https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/All-Orders)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/All-Orders](https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/All-Orders)
- [https://developers.binance.com/docs/derivatives/option/trade/Query-Option-Order-History](https://developers.binance.com/docs/derivatives/option/trade/Query-Option-Order-History)
- [https://developers.binance.com/docs/margin\_trading/trade/Query-Margin-Account-All-Orders](https://developers.binance.com/docs/margin_trading/trade/Query-Margin-Account-All-Orders)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-UM-Orders](https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-UM-Orders)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-CM-Orders](https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-CM-Orders)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-UM-Conditional-Orders](https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-UM-Conditional-Orders)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-CM-Conditional-Orders](https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-All-CM-Conditional-Orders)
- [https://developers.binance.com/en/docs/catalog/advanced-trading-stocks-trading/api/rest-api/trade#equity-order-history](https://developers.binance.com/en/docs/catalog/advanced-trading-stocks-trading/api/rest-api/trade#equity-order-history)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | No | unified market symbol of the market the orders were made in |
| since | `int` | No | the earliest time in ms to fetch orders for |
| limit | `int` | No | the maximum number of order structures to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.paginate | `boolean` | No | default false, when true will automatically paginate by calling this endpoint multiple times. See in the docs all the [available parameters](https://docs.ccxt.com/docs/manual#pagination-params) |
| params.portfolioMargin | `boolean` | No | set to true if you would like to fetch orders in a portfolio margin account |
| params.trigger | `boolean` | No | set to true if you would like to fetch portfolio margin account trigger or conditional orders |
| params.stock | `boolean` | No | set to true if you would like to fetch tokenized stock orders |

```
binance.fetchCanceledAndClosedOrders (symbol?, since?, limit?, params?)
```

### [cancelOrder](https://docs.ccxt.com/docs/exchanges/binance\#cancelorder)

cancels an open order

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- An [order structure](https://docs.ccxt.com/docs/manual#order-structure)

**See**

- [https://developers.binance.com/docs/binance-spot-api-docs/rest-api/trading-endpoints#cancel-order-trade](https://developers.binance.com/docs/binance-spot-api-docs/rest-api/trading-endpoints#cancel-order-trade)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Cancel-Order](https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Cancel-Order)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/Cancel-Order](https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/Cancel-Order)
- [https://developers.binance.com/docs/derivatives/option/trade/Cancel-Option-Order](https://developers.binance.com/docs/derivatives/option/trade/Cancel-Option-Order)
- [https://developers.binance.com/docs/margin\_trading/trade/Margin-Account-Cancel-Order](https://developers.binance.com/docs/margin_trading/trade/Margin-Account-Cancel-Order)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Cancel-UM-Order](https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Cancel-UM-Order)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Cancel-CM-Order](https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Cancel-CM-Order)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Cancel-UM-Conditional-Order](https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Cancel-UM-Conditional-Order)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Cancel-CM-Conditional-Order](https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Cancel-CM-Conditional-Order)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Cancel-Margin-Account-Order](https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Cancel-Margin-Account-Order)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Cancel-Algo-Order](https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Cancel-Algo-Order)
- [https://developers.binance.com/en/docs/catalog/advanced-trading-stocks-trading/api/rest-api/trade#cancel-equity-order](https://developers.binance.com/en/docs/catalog/advanced-trading-stocks-trading/api/rest-api/trade#cancel-equity-order)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| id | `string` | Yes | order id |
| symbol | `string` | Yes | unified symbol of the market the order was made in |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.portfolioMargin | `boolean` | No | set to true if you would like to cancel an order in a portfolio margin account |
| params.trigger | `boolean` | No | set to true if you would like to cancel a portfolio margin account conditional order |
| params.stock | `boolean` | No | set to true if you would like to cancel a tokenized stock order |

```
binance.cancelOrder (id, symbol, params?)
```

### [cancelAllOrders](https://docs.ccxt.com/docs/exchanges/binance\#cancelallorders)

cancel all open orders in a market

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `Array<object>` \- a list of [order structures](https://docs.ccxt.com/docs/manual#order-structure)

**See**

- [https://developers.binance.com/docs/binance-spot-api-docs/rest-api/trading-endpoints#cancel-all-open-orders-on-a-symbol-trade](https://developers.binance.com/docs/binance-spot-api-docs/rest-api/trading-endpoints#cancel-all-open-orders-on-a-symbol-trade)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Cancel-All-Open-Orders](https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Cancel-All-Open-Orders)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/Cancel-All-Open-Orders](https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/Cancel-All-Open-Orders)
- [https://developers.binance.com/docs/derivatives/option/trade/Cancel-all-Option-orders-on-specific-symbol](https://developers.binance.com/docs/derivatives/option/trade/Cancel-all-Option-orders-on-specific-symbol)
- [https://developers.binance.com/docs/margin\_trading/trade/Margin-Account-Cancel-All-Open-Orders](https://developers.binance.com/docs/margin_trading/trade/Margin-Account-Cancel-All-Open-Orders)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Cancel-All-UM-Open-Orders](https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Cancel-All-UM-Open-Orders)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Cancel-All-UM-Open-Conditional-Orders](https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Cancel-All-UM-Open-Conditional-Orders)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Cancel-All-CM-Open-Orders](https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Cancel-All-CM-Open-Orders)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Cancel-All-CM-Open-Conditional-Orders](https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Cancel-All-CM-Open-Conditional-Orders)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Cancel-Margin-Account-All-Open-Orders-on-a-Symbol](https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Cancel-Margin-Account-All-Open-Orders-on-a-Symbol)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Cancel-All-Algo-Open-Orders](https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Cancel-All-Algo-Open-Orders)
- [https://developers.binance.com/en/docs/catalog/advanced-trading-stocks-trading/api/rest-api/trade#cancel-all-equity-orders](https://developers.binance.com/en/docs/catalog/advanced-trading-stocks-trading/api/rest-api/trade#cancel-all-equity-orders)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol of the market to cancel orders in |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.marginMode | `string` | No | 'cross' or 'isolated', for spot margin trading |
| params.portfolioMargin | `boolean` | No | set to true if you would like to cancel orders in a portfolio margin account |
| params.trigger | `boolean` | No | set to true if you would like to cancel portfolio margin account conditional orders |
| params.stock | `boolean` | No | set to true if you would like to cancel tokenized stock orders |

```
binance.cancelAllOrders (symbol, params?)
```

### [cancelOrders](https://docs.ccxt.com/docs/exchanges/binance\#cancelorders)

cancel multiple orders

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- an list of [order structures](https://docs.ccxt.com/docs/manual#order-structure)

**See**

- [https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Cancel-Multiple-Orders](https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Cancel-Multiple-Orders)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/Cancel-Multiple-Orders](https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/Cancel-Multiple-Orders)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| ids | `Array<string>` | Yes | order ids |
| symbol | `string` | No | unified market symbol |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.clientOrderIds | `Array<string>` | No | alternative to ids, array of client order ids EXCHANGE SPECIFIC PARAMETERS |
| params.origClientOrderIdList | `Array<string>` | No | max length 10 e.g. \["my\_id\_1","my\_id\_2"\], encode the double quotes. No space after comma |
| params.recvWindow | `Array<int>` | No |  |

```
binance.cancelOrders (ids, symbol?, params?)
```

### [fetchOrderTrades](https://docs.ccxt.com/docs/exchanges/binance\#fetchordertrades)

fetch all the trades made from a single order

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `Array<object>` \- a list of [trade structures](https://docs.ccxt.com/docs/manual#trade-structure)

**See**

- [https://developers.binance.com/docs/binance-spot-api-docs/rest-api/account-endpoints#account-trade-list-user\_data](https://developers.binance.com/docs/binance-spot-api-docs/rest-api/account-endpoints#account-trade-list-user_data)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Account-Trade-List](https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Account-Trade-List)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/Account-Trade-List](https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/Account-Trade-List)
- [https://developers.binance.com/docs/margin\_trading/trade/Query-Margin-Account-Trade-List](https://developers.binance.com/docs/margin_trading/trade/Query-Margin-Account-Trade-List)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| id | `string` | Yes | order id |
| symbol | `string` | Yes | unified market symbol |
| since | `int` | No | the earliest time in ms to fetch trades for |
| limit | `int` | No | the maximum number of trades to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

```
binance.fetchOrderTrades (id, symbol, since?, limit?, params?)
```

### [fetchMyTrades](https://docs.ccxt.com/docs/exchanges/binance\#fetchmytrades)

fetch all trades made by the user

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `Array<Trade>` \- a list of [trade structures](https://docs.ccxt.com/docs/manual#trade-structure)

**See**

- [https://developers.binance.com/docs/binance-spot-api-docs/rest-api/account-endpoints#account-trade-list-user\_data](https://developers.binance.com/docs/binance-spot-api-docs/rest-api/account-endpoints#account-trade-list-user_data)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Account-Trade-List](https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Account-Trade-List)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/Account-Trade-List](https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/Account-Trade-List)
- [https://developers.binance.com/docs/margin\_trading/trade/Query-Margin-Account-Trade-List](https://developers.binance.com/docs/margin_trading/trade/Query-Margin-Account-Trade-List)
- [https://developers.binance.com/docs/derivatives/option/trade/Account-Trade-List](https://developers.binance.com/docs/derivatives/option/trade/Account-Trade-List)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/trade/UM-Account-Trade-List](https://developers.binance.com/docs/derivatives/portfolio-margin/trade/UM-Account-Trade-List)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/trade/CM-Account-Trade-List](https://developers.binance.com/docs/derivatives/portfolio-margin/trade/CM-Account-Trade-List)
- [https://developers.binance.com/en/docs/catalog/advanced-trading-stocks-trading/api/rest-api/trade#equity-trade-history](https://developers.binance.com/en/docs/catalog/advanced-trading-stocks-trading/api/rest-api/trade#equity-trade-history)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | No | unified market symbol |
| since | `int` | No | the earliest time in ms to fetch trades for |
| limit | `int` | No | the maximum number of trades structures to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.paginate | `boolean` | No | default false, when true will automatically paginate by calling this endpoint multiple times. See in the docs all the [available parameters](https://docs.ccxt.com/docs/manual#pagination-params) |
| params.until | `int` | No | the latest time in ms to fetch entries for |
| params.portfolioMargin | `boolean` | No | set to true if you would like to fetch trades for a portfolio margin account |
| params.stock | `boolean` | No | set to true if you would like to fetch tokenized stock trades |

```
binance.fetchMyTrades (symbol?, since?, limit?, params?)
```

### [fetchMyDustTrades](https://docs.ccxt.com/docs/exchanges/binance\#fetchmydusttrades)

fetch all dust trades made by the user

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `Array<object>` \- a list of [trade structures](https://docs.ccxt.com/docs/manual#trade-structure)

**See**: [https://developers.binance.com/docs/wallet/asset/dust-log](https://developers.binance.com/docs/wallet/asset/dust-log)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | not used by fetchMyDustTrades () |
| since | `int` | No | the earliest time in ms to fetch my dust trades for |
| limit | `int` | No | the maximum number of dust trades to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.type | `string` | No | 'spot' or 'margin', default spot |

```
binance.fetchMyDustTrades (symbol, since?, limit?, params?)
```

### [fetchDeposits](https://docs.ccxt.com/docs/exchanges/binance\#fetchdeposits)

fetch all deposits made to an account

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `Array<object>` \- a list of [transaction structures](https://docs.ccxt.com/docs/manual#transaction-structure)

**See**

- [https://developers.binance.com/docs/wallet/capital/deposite-history](https://developers.binance.com/docs/wallet/capital/deposite-history)
- [https://developers.binance.com/docs/fiat/rest-api/Get-Fiat-Deposit-Withdraw-History](https://developers.binance.com/docs/fiat/rest-api/Get-Fiat-Deposit-Withdraw-History)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| code | `string` | Yes | unified currency code |
| since | `int` | No | the earliest time in ms to fetch deposits for |
| limit | `int` | No | the maximum number of deposits structures to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.fiat | `bool` | No | if true, only fiat deposits will be returned |
| params.until | `int` | No | the latest time in ms to fetch entries for |
| params.paginate | `boolean` | No | default false, when true will automatically paginate by calling this endpoint multiple times. See in the docs all the [available parameters](https://docs.ccxt.com/docs/manual#pagination-params) |

```
binance.fetchDeposits (code, since?, limit?, params?)
```

### [fetchWithdrawals](https://docs.ccxt.com/docs/exchanges/binance\#fetchwithdrawals)

fetch all withdrawals made from an account

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `Array<object>` \- a list of [transaction structures](https://docs.ccxt.com/docs/manual#transaction-structure)

**See**

- [https://developers.binance.com/docs/wallet/capital/withdraw-history](https://developers.binance.com/docs/wallet/capital/withdraw-history)
- [https://developers.binance.com/docs/fiat/rest-api/Get-Fiat-Deposit-Withdraw-History](https://developers.binance.com/docs/fiat/rest-api/Get-Fiat-Deposit-Withdraw-History)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| code | `string` | Yes | unified currency code |
| since | `int` | No | the earliest time in ms to fetch withdrawals for |
| limit | `int` | No | the maximum number of withdrawals structures to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.fiat | `bool` | No | if true, only fiat withdrawals will be returned |
| params.until | `int` | No | the latest time in ms to fetch withdrawals for |
| params.paginate | `boolean` | No | default false, when true will automatically paginate by calling this endpoint multiple times. See in the docs all the [available parameters](https://docs.ccxt.com/docs/manual#pagination-params) |

```
binance.fetchWithdrawals (code, since?, limit?, params?)
```

### [transfer](https://docs.ccxt.com/docs/exchanges/binance\#transfer)

transfer currency internally between wallets on the same account

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- a [transfer structure](https://docs.ccxt.com/docs/manual#transfer-structure)

**See**: [https://developers.binance.com/docs/wallet/asset/user-universal-transfer](https://developers.binance.com/docs/wallet/asset/user-universal-transfer)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| code | `string` | Yes | unified currency code |
| amount | `float` | Yes | amount to transfer |
| fromAccount | `string` | Yes | account to transfer from |
| toAccount | `string` | Yes | account to transfer to |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.type | `string` | No | exchange specific transfer type |
| params.symbol | `string` | No | the unified symbol, required for isolated margin transfers |

```
binance.transfer (code, amount, fromAccount, toAccount, params?)
```

### [fetchTransfers](https://docs.ccxt.com/docs/exchanges/binance\#fetchtransfers)

fetch a history of internal transfers made on an account

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `Array<object>` \- a list of [transfer structures](https://docs.ccxt.com/docs/manual#transfer-structure)

**See**: [https://developers.binance.com/docs/wallet/asset/query-user-universal-transfer](https://developers.binance.com/docs/wallet/asset/query-user-universal-transfer)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| code | `string` | Yes | unified currency code of the currency transferred |
| since | `int` | No | the earliest time in ms to fetch transfers for |
| limit | `int` | No | the maximum number of transfers structures to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.until | `int` | No | the latest time in ms to fetch transfers for |
| params.paginate | `boolean` | No | default false, when true will automatically paginate by calling this endpoint multiple times. See in the docs all the [available parameters](https://docs.ccxt.com/docs/manual#pagination-params) |
| params.internal | `boolean` | No | default false, when true will fetch pay trade history |

```
binance.fetchTransfers (code, since?, limit?, params?)
```

### [fetchDepositAddress](https://docs.ccxt.com/docs/exchanges/binance\#fetchdepositaddress)

fetch the deposit address for a currency associated with this account

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- an [address structure](https://docs.ccxt.com/docs/manual#address-structure)

**See**: [https://developers.binance.com/docs/wallet/capital/deposite-address](https://developers.binance.com/docs/wallet/capital/deposite-address)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| code | `string` | Yes | unified currency code |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.network | `string` | No | network for fetch deposit address |

```
binance.fetchDepositAddress (code, params?)
```

### [fetchTransactionFees](https://docs.ccxt.com/docs/exchanges/binance\#fetchtransactionfees)

`DEPRECATED`

please use fetchDepositWithdrawFees instead

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `Array<object>` \- a list of [fee structures](https://docs.ccxt.com/docs/manual#fee-structure)

**See**: [https://developers.binance.com/docs/wallet/capital/all-coins-info](https://developers.binance.com/docs/wallet/capital/all-coins-info)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| codes | `Array<string>`, `undefined` | Yes | not used by fetchTransactionFees () |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

```
binance.fetchTransactionFees (codes, params?)
```

### [fetchDepositWithdrawFees](https://docs.ccxt.com/docs/exchanges/binance\#fetchdepositwithdrawfees)

fetch deposit and withdraw fees

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `Array<object>` \- a list of [fee structures](https://docs.ccxt.com/docs/manual#fee-structure)

**See**: [https://developers.binance.com/docs/wallet/capital/all-coins-info](https://developers.binance.com/docs/wallet/capital/all-coins-info)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| codes | `Array<string>`, `undefined` | Yes | not used by fetchDepositWithdrawFees () |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

```
binance.fetchDepositWithdrawFees (codes, params?)
```

### [withdraw](https://docs.ccxt.com/docs/exchanges/binance\#withdraw)

make a withdrawal

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- a [transaction structure](https://docs.ccxt.com/docs/manual#transaction-structure)

**See**: [https://developers.binance.com/docs/wallet/capital/withdraw](https://developers.binance.com/docs/wallet/capital/withdraw)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| code | `string` | Yes | unified currency code |
| amount | `float` | Yes | the amount to withdraw |
| address | `string` | Yes | the address to withdraw to |
| tag | `string` | Yes |  |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

```
binance.withdraw (code, amount, address, tag, params?)
```

### [fetchTradingFee](https://docs.ccxt.com/docs/exchanges/binance\#fetchtradingfee)

fetch the trading fees for a market

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- a [fee structure](https://docs.ccxt.com/docs/manual#fee-structure)

**See**

- [https://developers.binance.com/docs/wallet/asset/trade-fee](https://developers.binance.com/docs/wallet/asset/trade-fee)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/User-Commission-Rate](https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/User-Commission-Rate)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/account/rest-api/User-Commission-Rate](https://developers.binance.com/docs/derivatives/coin-margined-futures/account/rest-api/User-Commission-Rate)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/account/Get-User-Commission-Rate-for-UM](https://developers.binance.com/docs/derivatives/portfolio-margin/account/Get-User-Commission-Rate-for-UM)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/account/Get-User-Commission-Rate-for-CM](https://developers.binance.com/docs/derivatives/portfolio-margin/account/Get-User-Commission-Rate-for-CM)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.portfolioMargin | `boolean` | No | set to true if you would like to fetch trading fees in a portfolio margin account |
| params.subType | `string` | No | "linear" or "inverse" |

```
binance.fetchTradingFee (symbol, params?)
```

### [fetchTradingFees](https://docs.ccxt.com/docs/exchanges/binance\#fetchtradingfees)

fetch the trading fees for multiple markets

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- a dictionary of [fee structures](https://docs.ccxt.com/docs/manual#fee-structure) indexed by market symbols

**See**

- [https://developers.binance.com/docs/wallet/asset/trade-fee](https://developers.binance.com/docs/wallet/asset/trade-fee)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Account-Information-V2](https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Account-Information-V2)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/account/rest-api/Account-Information](https://developers.binance.com/docs/derivatives/coin-margined-futures/account/rest-api/Account-Information)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Account-Config](https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Account-Config)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.subType | `string` | No | "linear" or "inverse" |

```
binance.fetchTradingFees (params?)
```

### [fetchFundingRate](https://docs.ccxt.com/docs/exchanges/binance\#fetchfundingrate)

fetch the current funding rate

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- a [funding rate structure](https://docs.ccxt.com/docs/manual#funding-rate-structure)

**See**

- [https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Mark-Price](https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Mark-Price)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Index-Price-and-Mark-Price](https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Index-Price-and-Mark-Price)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

```
binance.fetchFundingRate (symbol, params?)
```

### [fetchFundingRateHistory](https://docs.ccxt.com/docs/exchanges/binance\#fetchfundingratehistory)

fetches historical funding rate prices

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `Array<object>` \- a list of [funding rate structures](https://docs.ccxt.com/docs/manual#funding-rate-history-structure)

**See**

- [https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Get-Funding-Rate-History](https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Get-Funding-Rate-History)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Get-Funding-Rate-History-of-Perpetual-Futures](https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Get-Funding-Rate-History-of-Perpetual-Futures)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to fetch the funding rate history for |
| since | `int` | No | timestamp in ms of the earliest funding rate to fetch |
| limit | `int` | No | the maximum amount of [funding rate structures](https://docs.ccxt.com/docs/manual#funding-rate-history-structure) to fetch |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.until | `int` | No | timestamp in ms of the latest funding rate |
| params.paginate | `boolean` | No | default false, when true will automatically paginate by calling this endpoint multiple times. See in the docs all the [available parameters](https://docs.ccxt.com/docs/manual#pagination-params) |
| params.subType | `string` | No | "linear" or "inverse" |

```
binance.fetchFundingRateHistory (symbol, since?, limit?, params?)
```

### [fetchFundingRates](https://docs.ccxt.com/docs/exchanges/binance\#fetchfundingrates)

fetch the funding rate for multiple markets

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `Array<object>` \- a list of [funding rate structures](https://docs.ccxt.com/docs/manual#funding-rates-structure), indexed by market symbols

**See**

- [https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Mark-Price](https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Mark-Price)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Index-Price-and-Mark-Price](https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Index-Price-and-Mark-Price)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>`, `undefined` | Yes | list of unified market symbols |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.subType | `string` | No | "linear" or "inverse" |

```
binance.fetchFundingRates (symbols, params?)
```

### [fetchLeverageTiers](https://docs.ccxt.com/docs/exchanges/binance\#fetchleveragetiers)

retrieve information on the maximum leverage, and maintenance margin for trades of varying trade sizes

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- a dictionary of [leverage tiers structures](https://docs.ccxt.com/docs/manual#leverage-tiers-structure), indexed by market symbols

**See**

- [https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Notional-and-Leverage-Brackets](https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Notional-and-Leverage-Brackets)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/account/rest-api/Notional-Bracket-for-Pair](https://developers.binance.com/docs/derivatives/coin-margined-futures/account/rest-api/Notional-Bracket-for-Pair)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/account/UM-Notional-and-Leverage-Brackets](https://developers.binance.com/docs/derivatives/portfolio-margin/account/UM-Notional-and-Leverage-Brackets)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/account/CM-Notional-and-Leverage-Brackets](https://developers.binance.com/docs/derivatives/portfolio-margin/account/CM-Notional-and-Leverage-Brackets)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>`, `undefined` | Yes | list of unified market symbols |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.portfolioMargin | `boolean` | No | set to true if you would like to fetch the leverage tiers for a portfolio margin account |
| params.subType | `string` | No | "linear" or "inverse" |

```
binance.fetchLeverageTiers (symbols, params?)
```

### [fetchPosition](https://docs.ccxt.com/docs/exchanges/binance\#fetchposition)

fetch data on an open position

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- a [position structure](https://docs.ccxt.com/docs/manual#position-structure)

**See**: [https://developers.binance.com/docs/derivatives/option/trade/Option-Position-Information](https://developers.binance.com/docs/derivatives/option/trade/Option-Position-Information)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol of the market the position is held in |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

```
binance.fetchPosition (symbol, params?)
```

### [fetchOptionPositions](https://docs.ccxt.com/docs/exchanges/binance\#fetchoptionpositions)

fetch data on open options positions

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `Array<object>` \- a list of [position structures](https://docs.ccxt.com/docs/manual#position-structure)

**See**: [https://developers.binance.com/docs/derivatives/option/trade/Option-Position-Information](https://developers.binance.com/docs/derivatives/option/trade/Option-Position-Information)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>`, `undefined` | Yes | list of unified market symbols |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

```
binance.fetchOptionPositions (symbols, params?)
```

### [fetchPositions](https://docs.ccxt.com/docs/exchanges/binance\#fetchpositions)

fetch all open positions

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `Array<object>` \- a list of [position structure](https://docs.ccxt.com/docs/manual#position-structure)

**See**

- [https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Account-Information-V2](https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Account-Information-V2)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/account/rest-api/Account-Information](https://developers.binance.com/docs/derivatives/coin-margined-futures/account/rest-api/Account-Information)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Position-Information-V2](https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Position-Information-V2)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/Position-Information](https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/Position-Information)
- [https://developers.binance.com/docs/derivatives/option/trade/Option-Position-Information](https://developers.binance.com/docs/derivatives/option/trade/Option-Position-Information)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>` | No | list of unified market symbols |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.method | `string` | No | method name to call, "positionRisk", "account" or "option", default is "positionRisk" |
| params.useV2 | `bool` | No | set to true if you want to use the obsolete endpoint, where some more additional fields were provided |

```
binance.fetchPositions (symbols?, params?)
```

### [fetchFundingHistory](https://docs.ccxt.com/docs/exchanges/binance\#fetchfundinghistory)

fetch the history of funding payments paid and received on this account

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- a [funding history structure](https://docs.ccxt.com/docs/manual#funding-history-structure)

**See**

- [https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Get-Income-History](https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Get-Income-History)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/account/rest-api/Get-Income-History](https://developers.binance.com/docs/derivatives/coin-margined-futures/account/rest-api/Get-Income-History)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/account/Get-UM-Income-History](https://developers.binance.com/docs/derivatives/portfolio-margin/account/Get-UM-Income-History)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/account/Get-CM-Income-History](https://developers.binance.com/docs/derivatives/portfolio-margin/account/Get-CM-Income-History)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol |
| since | `int` | No | the earliest time in ms to fetch funding history for |
| limit | `int` | No | the maximum number of funding history structures to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.until | `int` | No | timestamp in ms of the latest funding history entry |
| params.portfolioMargin | `boolean` | No | set to true if you would like to fetch the funding history for a portfolio margin account |
| params.subType | `string` | No | "linear" or "inverse" |

```
binance.fetchFundingHistory (symbol, since?, limit?, params?)
```

### [setLeverage](https://docs.ccxt.com/docs/exchanges/binance\#setleverage)

set the level of leverage for a market

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- response from the exchange

**See**

- [https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Change-Initial-Leverage](https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Change-Initial-Leverage)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/Change-Initial-Leverage](https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/Change-Initial-Leverage)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/account/Change-UM-Initial-Leverage](https://developers.binance.com/docs/derivatives/portfolio-margin/account/Change-UM-Initial-Leverage)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/account/Change-CM-Initial-Leverage](https://developers.binance.com/docs/derivatives/portfolio-margin/account/Change-CM-Initial-Leverage)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| leverage | `float` | Yes | the rate of leverage |
| symbol | `string` | Yes | unified market symbol |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.portfolioMargin | `boolean` | No | set to true if you would like to set the leverage for a trading pair in a portfolio margin account |

```
binance.setLeverage (leverage, symbol, params?)
```

### [setMarginMode](https://docs.ccxt.com/docs/exchanges/binance\#setmarginmode)

set margin mode to 'cross' or 'isolated'

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- response from the exchange

**See**

- [https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Change-Margin-Type](https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Change-Margin-Type)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/Change-Margin-Type](https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/Change-Margin-Type)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| marginMode | `string` | Yes | 'cross' or 'isolated' |
| symbol | `string` | Yes | unified market symbol |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

```
binance.setMarginMode (marginMode, symbol, params?)
```

### [setPositionMode](https://docs.ccxt.com/docs/exchanges/binance\#setpositionmode)

set hedged to true or false for a market

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- response from the exchange

**See**

- [https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Change-Position-Mode](https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Change-Position-Mode)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/Change-Position-Mode](https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/Change-Position-Mode)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/account/Get-UM-Current-Position-Mode](https://developers.binance.com/docs/derivatives/portfolio-margin/account/Get-UM-Current-Position-Mode)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/account/Get-CM-Current-Position-Mode](https://developers.binance.com/docs/derivatives/portfolio-margin/account/Get-CM-Current-Position-Mode)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| hedged | `bool` | Yes | set to true to use dualSidePosition |
| symbol | `string` | Yes | not used by setPositionMode () |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.portfolioMargin | `boolean` | No | set to true if you would like to set the position mode for a portfolio margin account |
| params.subType | `string` | No | "linear" or "inverse" |

```
binance.setPositionMode (hedged, symbol, params?)
```

### [fetchLeverages](https://docs.ccxt.com/docs/exchanges/binance\#fetchleverages)

fetch the set leverage for all markets

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- a list of [leverage structures](https://docs.ccxt.com/docs/manual#leverage-structure)

**See**

- [https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Account-Information-V2](https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Account-Information-V2)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/account/rest-api/Account-Information](https://developers.binance.com/docs/derivatives/coin-margined-futures/account/rest-api/Account-Information)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/account/Get-UM-Account-Detail](https://developers.binance.com/docs/derivatives/portfolio-margin/account/Get-UM-Account-Detail)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/account/Get-CM-Account-Detail](https://developers.binance.com/docs/derivatives/portfolio-margin/account/Get-CM-Account-Detail)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Symbol-Config](https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Symbol-Config)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>` | No | a list of unified market symbols |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.subType | `string` | No | "linear" or "inverse" |

```
binance.fetchLeverages (symbols?, params?)
```

### [fetchSettlementHistory](https://docs.ccxt.com/docs/exchanges/binance\#fetchsettlementhistory)

fetches historical settlement records

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `Array<object>` \- a list of [settlement history objects](https://docs.ccxt.com/docs/manual#settlement-history-structure)

**See**: [https://developers.binance.com/docs/derivatives/option/market-data/Historical-Exercise-Records](https://developers.binance.com/docs/derivatives/option/market-data/Historical-Exercise-Records)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol of the settlement history |
| since | `int` | No | timestamp in ms |
| limit | `int` | No | number of records, default 100, max 100 |
| params | `object` | No | exchange specific params |

```
binance.fetchSettlementHistory (symbol, since?, limit?, params?)
```

### [fetchMySettlementHistory](https://docs.ccxt.com/docs/exchanges/binance\#fetchmysettlementhistory)

fetches historical settlement records of the user

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `Array<object>` \- a list of \[settlement history objects\]

**See**: [https://developers.binance.com/docs/derivatives/option/trade/User-Exercise-Record](https://developers.binance.com/docs/derivatives/option/trade/User-Exercise-Record)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol of the settlement history |
| since | `int` | No | timestamp in ms |
| limit | `int` | No | number of records |
| params | `object` | No | exchange specific params |

```
binance.fetchMySettlementHistory (symbol, since?, limit?, params?)
```

### [fetchLedgerEntry](https://docs.ccxt.com/docs/exchanges/binance\#fetchledgerentry)

fetch the history of changes, actions done by the user or operations that altered the balance of the user

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- a [ledger structure](https://docs.ccxt.com/docs/manual#ledger-entry-structure)

**See**: [https://developers.binance.com/docs/derivatives/option/account/Account-Funding-Flow](https://developers.binance.com/docs/derivatives/option/account/Account-Funding-Flow)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| id | `string` | Yes | the identification number of the ledger entry |
| code | `string` | Yes | unified currency code |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

```
binance.fetchLedgerEntry (id, code, params?)
```

### [fetchLedger](https://docs.ccxt.com/docs/exchanges/binance\#fetchledger)

fetch the history of changes, actions done by the user or operations that altered the balance of the user

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- a [ledger structure](https://docs.ccxt.com/docs/manual#ledger-entry-structure)

**See**

- [https://developers.binance.com/docs/derivatives/option/account/Account-Funding-Flow](https://developers.binance.com/docs/derivatives/option/account/Account-Funding-Flow)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Get-Income-History](https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Get-Income-History)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/account/rest-api/Get-Income-History](https://developers.binance.com/docs/derivatives/coin-margined-futures/account/rest-api/Get-Income-History)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/account/Get-UM-Income-History](https://developers.binance.com/docs/derivatives/portfolio-margin/account/Get-UM-Income-History)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/account/Get-CM-Income-History](https://developers.binance.com/docs/derivatives/portfolio-margin/account/Get-CM-Income-History)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| code | `string` | No | unified currency code |
| since | `int` | No | timestamp in ms of the earliest ledger entry |
| limit | `int` | No | max number of ledger entries to return |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.until | `int` | No | timestamp in ms of the latest ledger entry |
| params.paginate | `boolean` | No | default false, when true will automatically paginate by calling this endpoint multiple times. See in the docs all the [available parameters](https://docs.ccxt.com/docs/manual#pagination-params) |
| params.portfolioMargin | `boolean` | No | set to true if you would like to fetch the ledger for a portfolio margin account |
| params.subType | `string` | No | "linear" or "inverse" |

```
binance.fetchLedger (code?, since?, limit?, params?)
```

### [reduceMargin](https://docs.ccxt.com/docs/exchanges/binance\#reducemargin)

remove margin from a position

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- a [margin structure](https://docs.ccxt.com/docs/manual#margin-structure)

**See**

- [https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Modify-Isolated-Position-Margin](https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Modify-Isolated-Position-Margin)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/Modify-Isolated-Position-Margin](https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/Modify-Isolated-Position-Margin)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol |
| amount | `float` | Yes | the amount of margin to remove |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

```
binance.reduceMargin (symbol, amount, params?)
```

### [addMargin](https://docs.ccxt.com/docs/exchanges/binance\#addmargin)

add margin

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- a [margin structure](https://docs.ccxt.com/docs/manual#margin-structure)

**See**

- [https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Modify-Isolated-Position-Margin](https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Modify-Isolated-Position-Margin)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/Modify-Isolated-Position-Margin](https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/Modify-Isolated-Position-Margin)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol |
| amount | `float` | Yes | amount of margin to add |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

```
binance.addMargin (symbol, amount, params?)
```

### [fetchCrossBorrowRate](https://docs.ccxt.com/docs/exchanges/binance\#fetchcrossborrowrate)

fetch the rate of interest to borrow a currency for margin trading

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- a [borrow rate structure](https://docs.ccxt.com/docs/manual#borrow-rate-structure)

**See**: [https://developers.binance.com/docs/margin\_trading/borrow-and-repay/Query-Margin-Interest-Rate-History](https://developers.binance.com/docs/margin_trading/borrow-and-repay/Query-Margin-Interest-Rate-History)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| code | `string` | Yes | unified currency code |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

```
binance.fetchCrossBorrowRate (code, params?)
```

### [fetchIsolatedBorrowRate](https://docs.ccxt.com/docs/exchanges/binance\#fetchisolatedborrowrate)

fetch the rate of interest to borrow a currency for margin trading

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- an [isolated borrow rate structure](https://docs.ccxt.com/docs/manual#isolated-borrow-rate-structure)

**See**: [https://developers.binance.com/docs/margin\_trading/account/Query-Isolated-Margin-Fee-Data](https://developers.binance.com/docs/margin_trading/account/Query-Isolated-Margin-Fee-Data)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol |
| params | `object` | No | extra parameters specific to the exchange API endpoint EXCHANGE SPECIFIC PARAMETERS |
| params.vipLevel | `object` | No | user's current specific margin data will be returned if viplevel is omitted |

```
binance.fetchIsolatedBorrowRate (symbol, params?)
```

### [fetchIsolatedBorrowRates](https://docs.ccxt.com/docs/exchanges/binance\#fetchisolatedborrowrates)

fetch the borrow interest rates of all currencies

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- a [borrow rate structure](https://docs.ccxt.com/docs/manual#borrow-rate-structure)

**See**: [https://developers.binance.com/docs/margin\_trading/account/Query-Isolated-Margin-Fee-Data](https://developers.binance.com/docs/margin_trading/account/Query-Isolated-Margin-Fee-Data)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.symbol | `object` | No | unified market symbol EXCHANGE SPECIFIC PARAMETERS |
| params.vipLevel | `object` | No | user's current specific margin data will be returned if viplevel is omitted |

```
binance.fetchIsolatedBorrowRates (params?)
```

### [fetchBorrowRateHistory](https://docs.ccxt.com/docs/exchanges/binance\#fetchborrowratehistory)

retrieves a history of a currencies borrow interest rate at specific time slots

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `Array<object>` \- an array of [borrow rate structures](https://docs.ccxt.com/docs/manual#borrow-rate-structure)

**See**: [https://developers.binance.com/docs/margin\_trading/borrow-and-repay/Query-Margin-Interest-Rate-History](https://developers.binance.com/docs/margin_trading/borrow-and-repay/Query-Margin-Interest-Rate-History)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| code | `string` | Yes | unified currency code |
| since | `int` | No | timestamp for the earliest borrow rate |
| limit | `int` | No | the maximum number of [borrow rate structures](https://docs.ccxt.com/docs/manual#borrow-rate-structure) to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

```
binance.fetchBorrowRateHistory (code, since?, limit?, params?)
```

### [createGiftCode](https://docs.ccxt.com/docs/exchanges/binance\#creategiftcode)

create gift code

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- The gift code id, code, currency and amount

**See**: [https://developers.binance.com/docs/gift\_card/market-data/Create-a-single-token-gift-card](https://developers.binance.com/docs/gift_card/market-data/Create-a-single-token-gift-card)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| code | `string` | Yes | gift code |
| amount | `float` | Yes | amount of currency for the gift |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

```
binance.createGiftCode (code, amount, params?)
```

### [redeemGiftCode](https://docs.ccxt.com/docs/exchanges/binance\#redeemgiftcode)

redeem gift code

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- response from the exchange

**See**: [https://developers.binance.com/docs/gift\_card/market-data/Redeem-a-Binance-Gift-Card](https://developers.binance.com/docs/gift_card/market-data/Redeem-a-Binance-Gift-Card)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| giftcardCode | `string` | Yes |  |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

```
binance.redeemGiftCode (giftcardCode, params?)
```

### [verifyGiftCode](https://docs.ccxt.com/docs/exchanges/binance\#verifygiftcode)

verify gift code

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- response from the exchange

**See**: [https://developers.binance.com/docs/gift\_card/market-data/Verify-Binance-Gift-Card-by-Gift-Card-Number](https://developers.binance.com/docs/gift_card/market-data/Verify-Binance-Gift-Card-by-Gift-Card-Number)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| id | `string` | Yes | reference number id |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

```
binance.verifyGiftCode (id, params?)
```

### [fetchBorrowInterest](https://docs.ccxt.com/docs/exchanges/binance\#fetchborrowinterest)

fetch the interest owed by the user for borrowing currency for margin trading

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `Array<object>` \- a list of [borrow interest structures](https://docs.ccxt.com/docs/manual#borrow-interest-structure)

**See**

- [https://developers.binance.com/docs/margin\_trading/borrow-and-repay/Get-Interest-History](https://developers.binance.com/docs/margin_trading/borrow-and-repay/Get-Interest-History)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/account/Get-Margin-BorrowLoan-Interest-History](https://developers.binance.com/docs/derivatives/portfolio-margin/account/Get-Margin-BorrowLoan-Interest-History)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| code | `string` | No | unified currency code |
| symbol | `string` | No | unified market symbol when fetch interest in isolated markets |
| since | `int` | No | the earliest time in ms to fetch borrrow interest for |
| limit | `int` | No | the maximum number of structures to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.portfolioMargin | `boolean` | No | set to true if you would like to fetch the borrow interest in a portfolio margin account |

```
binance.fetchBorrowInterest (code?, symbol?, since?, limit?, params?)
```

### [repayCrossMargin](https://docs.ccxt.com/docs/exchanges/binance\#repaycrossmargin)

repay borrowed margin and interest

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- a [margin loan structure](https://docs.ccxt.com/docs/manual#margin-loan-structure)

**See**

- [https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Margin-Account-Repay](https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Margin-Account-Repay)
- [https://developers.binance.com/docs/margin\_trading/borrow-and-repay/Margin-Account-Borrow-Repay](https://developers.binance.com/docs/margin_trading/borrow-and-repay/Margin-Account-Borrow-Repay)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Margin-Account-Repay-Debt](https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Margin-Account-Repay-Debt)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| code | `string` | Yes | unified currency code of the currency to repay |
| amount | `float` | Yes | the amount to repay |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.portfolioMargin | `boolean` | No | set to true if you would like to repay margin in a portfolio margin account |
| params.repayCrossMarginMethod | `string` | No | _portfolio margin only_ 'papiPostRepayLoan' (default), 'papiPostMarginRepayDebt' (alternative) |
| params.specifyRepayAssets | `string` | No | _portfolio margin papiPostMarginRepayDebt only_ specific asset list to repay debt |

```
binance.repayCrossMargin (code, amount, params?)
```

### [repayIsolatedMargin](https://docs.ccxt.com/docs/exchanges/binance\#repayisolatedmargin)

repay borrowed margin and interest

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- a [margin loan structure](https://docs.ccxt.com/docs/manual#margin-loan-structure)

**See**: [https://developers.binance.com/docs/margin\_trading/borrow-and-repay/Margin-Account-Borrow-Repay](https://developers.binance.com/docs/margin_trading/borrow-and-repay/Margin-Account-Borrow-Repay)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol, required for isolated margin |
| code | `string` | Yes | unified currency code of the currency to repay |
| amount | `float` | Yes | the amount to repay |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

```
binance.repayIsolatedMargin (symbol, code, amount, params?)
```

### [borrowCrossMargin](https://docs.ccxt.com/docs/exchanges/binance\#borrowcrossmargin)

create a loan to borrow margin

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- a [margin loan structure](https://docs.ccxt.com/docs/manual#margin-loan-structure)

**See**

- [https://developers.binance.com/docs/margin\_trading/borrow-and-repay/Margin-Account-Borrow-Repay](https://developers.binance.com/docs/margin_trading/borrow-and-repay/Margin-Account-Borrow-Repay)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Margin-Account-Borrow](https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Margin-Account-Borrow)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| code | `string` | Yes | unified currency code of the currency to borrow |
| amount | `float` | Yes | the amount to borrow |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.portfolioMargin | `boolean` | No | set to true if you would like to borrow margin in a portfolio margin account |

```
binance.borrowCrossMargin (code, amount, params?)
```

### [borrowIsolatedMargin](https://docs.ccxt.com/docs/exchanges/binance\#borrowisolatedmargin)

create a loan to borrow margin

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- a [margin loan structure](https://docs.ccxt.com/docs/manual#margin-loan-structure)

**See**: [https://developers.binance.com/docs/margin\_trading/borrow-and-repay/Margin-Account-Borrow-Repay](https://developers.binance.com/docs/margin_trading/borrow-and-repay/Margin-Account-Borrow-Repay)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol, required for isolated margin |
| code | `string` | Yes | unified currency code of the currency to borrow |
| amount | `float` | Yes | the amount to borrow |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

```
binance.borrowIsolatedMargin (symbol, code, amount, params?)
```

### [fetchOpenInterestHistory](https://docs.ccxt.com/docs/exchanges/binance\#fetchopeninteresthistory)

Retrieves the open interest history of a currency

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- an array of [open interest structure](https://docs.ccxt.com/docs/manual#open-interest-structure)

**See**

- [https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Open-Interest-Statistics](https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Open-Interest-Statistics)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Open-Interest-Statistics](https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Open-Interest-Statistics)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | Unified CCXT market symbol |
| timeframe | `string` | Yes | "5m","15m","30m","1h","2h","4h","6h","12h", or "1d" |
| since | `int` | No | the time(ms) of the earliest record to retrieve as a unix timestamp |
| limit | `int` | No | default 30, max 500 |
| params | `object` | No | exchange specific parameters |
| params.until | `int` | No | the time(ms) of the latest record to retrieve as a unix timestamp |
| params.paginate | `boolean` | No | default false, when true will automatically paginate by calling this endpoint multiple times. See in the docs all the [availble parameters](https://docs.ccxt.com/docs/manual#pagination-params) |

```
binance.fetchOpenInterestHistory (symbol, timeframe, since?, limit?, params?)
```

### [fetchOpenInterest](https://docs.ccxt.com/docs/exchanges/binance\#fetchopeninterest)

retrieves the open interest of a contract trading pair

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- an open interest structure [/docs/manual#open-interest-structure](https://docs.ccxt.com/docs/manual#open-interest-structure)

**See**

- [https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Open-Interest](https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Open-Interest)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Open-Interest](https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Open-Interest)
- [https://developers.binance.com/docs/derivatives/option/market-data/Open-Interest](https://developers.binance.com/docs/derivatives/option/market-data/Open-Interest)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified CCXT market symbol |
| params | `object` | No | exchange specific parameters |

```
binance.fetchOpenInterest (symbol, params?)
```

### [fetchMyLiquidations](https://docs.ccxt.com/docs/exchanges/binance\#fetchmyliquidations)

retrieves the users liquidated positions

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- an array of [liquidation structures](https://docs.ccxt.com/docs/manual#liquidation-structure)

**See**

- [https://developers.binance.com/docs/margin\_trading/trade/Get-Force-Liquidation-Record](https://developers.binance.com/docs/margin_trading/trade/Get-Force-Liquidation-Record)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Users-Force-Orders](https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Users-Force-Orders)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/Users-Force-Orders](https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/Users-Force-Orders)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-Users-UM-Force-Orders](https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-Users-UM-Force-Orders)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-Users-CM-Force-Orders](https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-Users-CM-Force-Orders)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | No | unified CCXT market symbol |
| since | `int` | No | the earliest time in ms to fetch liquidations for |
| limit | `int` | No | the maximum number of liquidation structures to retrieve |
| params | `object` | No | exchange specific parameters for the binance api endpoint |
| params.until | `int` | No | timestamp in ms of the latest liquidation |
| params.paginate | `boolean` | No | _spot only_ default false, when true will automatically paginate by calling this endpoint multiple times. See in the docs all the [available parameters](https://docs.ccxt.com/docs/manual#pagination-params) |
| params.portfolioMargin | `boolean` | No | set to true if you would like to fetch liquidations in a portfolio margin account |
| params.type | `string` | No | "spot" |
| params.subType | `string` | No | "linear" or "inverse" |

```
binance.fetchMyLiquidations (symbol?, since?, limit?, params?)
```

### [fetchGreeks](https://docs.ccxt.com/docs/exchanges/binance\#fetchgreeks)

fetches an option contracts greeks, financial metrics used to measure the factors that affect the price of an options contract

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- a [greeks structure](https://docs.ccxt.com/docs/manual#greeks-structure)

**See**: [https://developers.binance.com/docs/derivatives/option/market-data/Option-Mark-Price](https://developers.binance.com/docs/derivatives/option/market-data/Option-Mark-Price)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to fetch greeks for |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

```
binance.fetchGreeks (symbol, params?)
```

### [fetchAllGreeks](https://docs.ccxt.com/docs/exchanges/binance\#fetchallgreeks)

fetches all option contracts greeks, financial metrics used to measure the factors that affect the price of an options contract

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- a dictionary of [greeks structures](https://docs.ccxt.com/docs/manual#greeks-structure) indexed by market symbol

**See**: [https://developers.binance.com/docs/derivatives/option/market-data/Option-Mark-Price](https://developers.binance.com/docs/derivatives/option/market-data/Option-Mark-Price)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>` | No | unified symbols of the markets to fetch greeks for, all markets are returned if not assigned |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

```
binance.fetchAllGreeks (symbols?, params?)
```

### [fetchPositionMode](https://docs.ccxt.com/docs/exchanges/binance\#fetchpositionmode)

fetchs the position mode, hedged or one way, hedged for binance is set identically for all linear markets or all inverse markets

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- an object detailing whether the market is in hedged or one-way mode

**See**

- [https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Get-Current-Position-Mode](https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Get-Current-Position-Mode)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/account/rest-api/Get-Current-Position-Mode](https://developers.binance.com/docs/derivatives/coin-margined-futures/account/rest-api/Get-Current-Position-Mode)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to fetch the order book for |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.subType | `string` | No | "linear" or "inverse" |

```
binance.fetchPositionMode (symbol, params?)
```

### [fetchMarginModes](https://docs.ccxt.com/docs/exchanges/binance\#fetchmarginmodes)

fetches margin modes ("isolated" or "cross") that the market for the symbol in in, with symbol=undefined all markets for a subType (linear/inverse) are returned

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- a list of [margin mode structures](https://docs.ccxt.com/docs/manual#margin-mode-structure)

**See**

- [https://developers.binance.com/docs/derivatives/coin-margined-futures/account/rest-api/Account-Information](https://developers.binance.com/docs/derivatives/coin-margined-futures/account/rest-api/Account-Information)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Account-Information-V2](https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Account-Information-V2)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Symbol-Config](https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Symbol-Config)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>` | Yes | unified market symbols |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.subType | `string` | No | "linear" or "inverse" |

```
binance.fetchMarginModes (symbols, params?)
```

### [fetchMarginMode](https://docs.ccxt.com/docs/exchanges/binance\#fetchmarginmode)

fetches the margin mode of a specific symbol

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- a [margin mode structure](https://docs.ccxt.com/docs/manual#margin-mode-structure)

**See**

- [https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Symbol-Config](https://developers.binance.com/docs/derivatives/usds-margined-futures/account/rest-api/Symbol-Config)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/account/rest-api/Account-Information](https://developers.binance.com/docs/derivatives/coin-margined-futures/account/rest-api/Account-Information)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market the order was made in |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.subType | `string` | No | "linear" or "inverse" |

```
binance.fetchMarginMode (symbol, params?)
```

### [fetchOption](https://docs.ccxt.com/docs/exchanges/binance\#fetchoption)

fetches option data that is commonly found in an option chain

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- an [option chain structure](https://docs.ccxt.com/docs/manual#option-chain-structure)

**See**: [https://developers.binance.com/docs/derivatives/option/market-data/24hr-Ticker-Price-Change-Statistics](https://developers.binance.com/docs/derivatives/option/market-data/24hr-Ticker-Price-Change-Statistics)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

```
binance.fetchOption (symbol, params?)
```

### [fetchMarginAdjustmentHistory](https://docs.ccxt.com/docs/exchanges/binance\#fetchmarginadjustmenthistory)

fetches the history of margin added or reduced from contract isolated positions

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `Array<object>` \- a list of [margin structures](https://docs.ccxt.com/docs/manual#margin-loan-structure)

**See**

- [https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Get-Position-Margin-Change-History](https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Get-Position-Margin-Change-History)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/Get-Position-Margin-Change-History](https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/Get-Position-Margin-Change-History)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol |
| type | `string` | No | "add" or "reduce" |
| since | `int` | No | timestamp in ms of the earliest change to fetch |
| limit | `int` | No | the maximum amount of changes to fetch |
| params | `object` | Yes | extra parameters specific to the exchange API endpoint |
| params.until | `int` | No | timestamp in ms of the latest change to fetch |

```
binance.fetchMarginAdjustmentHistory (symbol, type?, since?, limit?, params)
```

### [fetchConvertCurrencies](https://docs.ccxt.com/docs/exchanges/binance\#fetchconvertcurrencies)

fetches all available currencies that can be converted

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- an associative dictionary of currencies

**See**: [https://developers.binance.com/docs/convert/market-data/Query-order-quantity-precision-per-asset](https://developers.binance.com/docs/convert/market-data/Query-order-quantity-precision-per-asset)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

```
binance.fetchConvertCurrencies (params?)
```

### [fetchConvertQuote](https://docs.ccxt.com/docs/exchanges/binance\#fetchconvertquote)

fetch a quote for converting from one currency to another

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- a [conversion structure](https://docs.ccxt.com/docs/manual#conversion-structure)

**See**: [https://developers.binance.com/docs/convert/trade/Send-quote-request](https://developers.binance.com/docs/convert/trade/Send-quote-request)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| fromCode | `string` | Yes | the currency that you want to sell and convert from |
| toCode | `string` | Yes | the currency that you want to buy and convert into |
| amount | `float` | Yes | how much you want to trade in units of the from currency |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.walletType | `string` | No | either 'SPOT' or 'FUNDING', the default is 'SPOT' |

```
binance.fetchConvertQuote (fromCode, toCode, amount, params?)
```

### [createConvertTrade](https://docs.ccxt.com/docs/exchanges/binance\#createconverttrade)

convert from one currency to another

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- a [conversion structure](https://docs.ccxt.com/docs/manual#conversion-structure)

**See**: [https://developers.binance.com/docs/convert/trade/Accept-Quote](https://developers.binance.com/docs/convert/trade/Accept-Quote)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| id | `string` | Yes | the id of the trade that you want to make |
| fromCode | `string` | Yes | the currency that you want to sell and convert from |
| toCode | `string` | Yes | the currency that you want to buy and convert into |
| amount | `float` | No | how much you want to trade in units of the from currency |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

```
binance.createConvertTrade (id, fromCode, toCode, amount?, params?)
```

### [fetchConvertTrade](https://docs.ccxt.com/docs/exchanges/binance\#fetchconverttrade)

fetch the data for a conversion trade

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- a [conversion structure](https://docs.ccxt.com/docs/manual#conversion-structure)

**See**: [https://developers.binance.com/docs/convert/trade/Order-Status](https://developers.binance.com/docs/convert/trade/Order-Status)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| id | `string` | Yes | the id of the trade that you want to fetch |
| code | `string` | No | the unified currency code of the conversion trade |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

```
binance.fetchConvertTrade (id, code?, params?)
```

### [fetchConvertTradeHistory](https://docs.ccxt.com/docs/exchanges/binance\#fetchconverttradehistory)

fetch the users history of conversion trades

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `Array<object>` \- a list of [conversion structures](https://docs.ccxt.com/docs/manual#conversion-structure)

**See**: [https://developers.binance.com/docs/convert/trade/Get-Convert-Trade-History](https://developers.binance.com/docs/convert/trade/Get-Convert-Trade-History)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| code | `string` | No | the unified currency code |
| since | `int` | No | the earliest time in ms to fetch conversions for |
| limit | `int` | No | the maximum number of conversion structures to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.until | `int` | No | timestamp in ms of the latest conversion to fetch |

```
binance.fetchConvertTradeHistory (code?, since?, limit?, params?)
```

### [fetchFundingIntervals](https://docs.ccxt.com/docs/exchanges/binance\#fetchfundingintervals)

fetch the funding rate interval for multiple markets

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `Array<object>` \- a list of [funding rate structures](https://docs.ccxt.com/docs/manual#funding-rate-structure)

**See**

- [https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Get-Funding-Rate-Info](https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Get-Funding-Rate-Info)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Get-Funding-Info](https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Get-Funding-Info)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>` | No | list of unified market symbols |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.subType | `string` | No | "linear" or "inverse" |

```
binance.fetchFundingIntervals (symbols?, params?)
```

### [fetchLongShortRatioHistory](https://docs.ccxt.com/docs/exchanges/binance\#fetchlongshortratiohistory)

fetches the long short ratio history for a unified market symbol

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `Array<object>` \- an array of [long short ratio structures](https://docs.ccxt.com/docs/manual#long-short-ratio-structure)

**See**

- [https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Long-Short-Ratio](https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Long-Short-Ratio)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Long-Short-Ratio](https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Long-Short-Ratio)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to fetch the long short ratio for |
| timeframe | `string` | No | the period for the ratio, default is 24 hours |
| since | `int` | No | the earliest time in ms to fetch ratios for |
| limit | `int` | No | the maximum number of long short ratio structures to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.until | `int` | No | timestamp in ms of the latest ratio to fetch |

```
binance.fetchLongShortRatioHistory (symbol, timeframe?, since?, limit?, params?)
```

### [fetchADLRank](https://docs.ccxt.com/docs/exchanges/binance\#fetchadlrank)

fetches the auto deleveraging rank and risk percentage for a symbol

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- an [auto de leverage structure](https://docs.ccxt.com/docs/manual#auto-de-leverage-structure)

**See**: [https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/ADL-Risk](https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/ADL-Risk)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to fetch the auto deleveraging rank for |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

```
binance.fetchADLRank (symbol, params?)
```

### [fetchPositionsADLRank](https://docs.ccxt.com/docs/exchanges/binance\#fetchpositionsadlrank)

fetches the auto deleveraging rank and risk percentage for a list of symbols that have open positions

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `Array<object>` \- an array of [auto de leverage structure](https://docs.ccxt.com/docs/manual#auto-de-leverage-structure)

**See**

- [https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Position-ADL-Quantile-Estimation](https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Position-ADL-Quantile-Estimation)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/Position-ADL-Quantile-Estimation](https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/rest-api/Position-ADL-Quantile-Estimation)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/trade/UM-Position-ADL-Quantile-Estimation](https://developers.binance.com/docs/derivatives/portfolio-margin/trade/UM-Position-ADL-Quantile-Estimation)
- [https://developers.binance.com/docs/derivatives/portfolio-margin/trade/CM-Position-ADL-Quantile-Estimation](https://developers.binance.com/docs/derivatives/portfolio-margin/trade/CM-Position-ADL-Quantile-Estimation)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>` | No | list of unified market symbols |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.portfolioMargin | `boolean` | No | set to true for the portfolio margin account |

```
binance.fetchPositionsADLRank (symbols?, params?)
```

### [ensureUserDataStreamWsSubscribeSignature](https://docs.ccxt.com/docs/exchanges/binance\#ensureuserdatastreamwssubscribesignature)

watches best bid & ask for symbols

**Kind**: instance property of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: Promise The subscription ID for the user data stream

**See**: [Binance User Data Stream Documentation](https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/user-data-stream-requests#subscribe-to-user-data-stream-through-signature-subscription-user_data)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| marketType | `string` | No | only supports 'spot' |

```
binance.ensureUserDataStreamWsSubscribeSignature (marketType?)
```

### [ensureUserDataStreamWsSubscribeListenToken](https://docs.ccxt.com/docs/exchanges/binance\#ensureuserdatastreamwssubscribelistentoken)

subscribes to user data stream using listenToken (for margin)

**Kind**: instance property of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: Promise

**See**: [Binance User Data Stream Documentation](https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-api/user-data-stream)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| marketType | `string` | Yes | the market type (e.g., 'margin') |
| params | `object` | Yes | extra parameters specific to the request |
| params.symbol | `string` | No | required for isolated margin |
| params.isIsolated | `boolean` | No | whether it is isolated margin |
| params.validity | `number` | No | validity in milliseconds, default 24 hours, max 24 hours |

```
binance.ensureUserDataStreamWsSubscribeListenToken (marketType, params)
```

### [watchLiquidations](https://docs.ccxt.com/docs/exchanges/binance\#watchliquidations)

watch the public liquidations of a trading pair

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- an array of [liquidation structures](https://docs.ccxt.com/docs/manual#liquidation-structure)

**See**

- [https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Liquidation-Order-Streams](https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Liquidation-Order-Streams)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Liquidation-Order-Streams](https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Liquidation-Order-Streams)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified CCXT market symbol |
| since | `int` | No | the earliest time in ms to fetch liquidations for |
| limit | `int` | No | the maximum number of liquidation structures to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

```
binance.watchLiquidations (symbol, since?, limit?, params?)
```

### [watchLiquidationsForSymbols](https://docs.ccxt.com/docs/exchanges/binance\#watchliquidationsforsymbols)

watch the public liquidations of a trading pair

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- an array of [liquidation structures](https://docs.ccxt.com/docs/manual#liquidation-structure)

**See**

- [https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/All-Market-Liquidation-Order-Streams](https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/All-Market-Liquidation-Order-Streams)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/All-Market-Liquidation-Order-Streams](https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/All-Market-Liquidation-Order-Streams)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>` | Yes | list of unified market symbols |
| since | `int` | No | the earliest time in ms to fetch liquidations for |
| limit | `int` | No | the maximum number of liquidation structures to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

```
binance.watchLiquidationsForSymbols (symbols, since?, limit?, params?)
```

### [watchMyLiquidations](https://docs.ccxt.com/docs/exchanges/binance\#watchmyliquidations)

watch the private liquidations of a trading pair

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- an array of [liquidation structures](https://docs.ccxt.com/docs/manual#liquidation-structure)

**See**

- [https://developers.binance.com/docs/derivatives/usds-margined-futures/user-data-streams/Event-Order-Update](https://developers.binance.com/docs/derivatives/usds-margined-futures/user-data-streams/Event-Order-Update)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/user-data-streams/Event-Order-Update](https://developers.binance.com/docs/derivatives/coin-margined-futures/user-data-streams/Event-Order-Update)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified CCXT market symbol |
| since | `int` | No | the earliest time in ms to fetch liquidations for |
| limit | `int` | No | the maximum number of liquidation structures to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

```
binance.watchMyLiquidations (symbol, since?, limit?, params?)
```

### [watchMyLiquidationsForSymbols](https://docs.ccxt.com/docs/exchanges/binance\#watchmyliquidationsforsymbols)

watch the private liquidations of a trading pair

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- an array of [liquidation structures](https://docs.ccxt.com/docs/manual#liquidation-structure)

**See**

- [https://developers.binance.com/docs/derivatives/usds-margined-futures/user-data-streams/Event-Order-Update](https://developers.binance.com/docs/derivatives/usds-margined-futures/user-data-streams/Event-Order-Update)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/user-data-streams/Event-Order-Update](https://developers.binance.com/docs/derivatives/coin-margined-futures/user-data-streams/Event-Order-Update)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>` | Yes | list of unified market symbols |
| since | `int` | No | the earliest time in ms to fetch liquidations for |
| limit | `int` | No | the maximum number of liquidation structures to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

```
binance.watchMyLiquidationsForSymbols (symbols, since?, limit?, params?)
```

### [watchOrderBook](https://docs.ccxt.com/docs/exchanges/binance\#watchorderbook)

watches information on open orders with bid (buy) and ask (sell) prices, volumes and other data

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- A dictionary of [order book structures](https://docs.ccxt.com/docs/manual#order-book-structure)

**See**

- [https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#partial-book-depth-streams](https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#partial-book-depth-streams)
- [https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#diff-depth-stream](https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#diff-depth-stream)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Partial-Book-Depth-Streams](https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Partial-Book-Depth-Streams)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams](https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams-RPI](https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams-RPI)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Partial-Book-Depth-Streams](https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Partial-Book-Depth-Streams)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams](https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to fetch the order book for |
| limit | `int` | No | the maximum amount of order book entries to return |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

```
binance.watchOrderBook (symbol, limit?, params?)
```

### [watchOrderBookForSymbols](https://docs.ccxt.com/docs/exchanges/binance\#watchorderbookforsymbols)

watches information on open orders with bid (buy) and ask (sell) prices, volumes and other data

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- an [order book structure](https://docs.ccxt.com/docs/manual#order-book-structure)

**See**

- [https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#partial-book-depth-streams](https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#partial-book-depth-streams)
- [https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#diff-depth-stream](https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#diff-depth-stream)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Partial-Book-Depth-Streams](https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Partial-Book-Depth-Streams)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams](https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams-RPI](https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams-RPI)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Partial-Book-Depth-Streams](https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Partial-Book-Depth-Streams)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams](https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>` | Yes | unified array of symbols |
| limit | `int` | No | the maximum amount of order book entries to return |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.rpi | `boolean` | No | _future only_ set to true to use the RPI endpoint |

```
binance.watchOrderBookForSymbols (symbols, limit?, params?)
```

### [unWatchOrderBookForSymbols](https://docs.ccxt.com/docs/exchanges/binance\#unwatchorderbookforsymbols)

unWatches information on open orders with bid (buy) and ask (sell) prices, volumes and other data

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- A dictionary of [order book structures](https://docs.ccxt.com/docs/manual#order-book-structure)

**See**

- [https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#partial-book-depth-streams](https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#partial-book-depth-streams)
- [https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#diff-depth-stream](https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#diff-depth-stream)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Partial-Book-Depth-Streams](https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Partial-Book-Depth-Streams)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams](https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Partial-Book-Depth-Streams](https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Partial-Book-Depth-Streams)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams](https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>` | Yes | unified array of symbols |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

```
binance.unWatchOrderBookForSymbols (symbols, params?)
```

### [unWatchOrderBook](https://docs.ccxt.com/docs/exchanges/binance\#unwatchorderbook)

unWatches information on open orders with bid (buy) and ask (sell) prices, volumes and other data

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- A dictionary of [order book structures](https://docs.ccxt.com/docs/manual#order-book-structure)

**See**

- [https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#partial-book-depth-streams](https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#partial-book-depth-streams)
- [https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#diff-depth-stream](https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#diff-depth-stream)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Partial-Book-Depth-Streams](https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Partial-Book-Depth-Streams)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams](https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Partial-Book-Depth-Streams](https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Partial-Book-Depth-Streams)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams](https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Diff-Book-Depth-Streams)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified array of symbols |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

```
binance.unWatchOrderBook (symbol, params?)
```

### [fetchOrderBookWs](https://docs.ccxt.com/docs/exchanges/binance\#fetchorderbookws)

fetches information on open orders with bid (buy) and ask (sell) prices, volumes and other data

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- A dictionary of [order book structures](https://docs.ccxt.com/docs/manual#order-book-structure)

**See**

- [https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/market-data-requests#order-book](https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/market-data-requests#order-book)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/websocket-api/Order-Book](https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/websocket-api/Order-Book)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to fetch the order book for |
| limit | `int` | No | the maximum amount of order book entries to return |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

```
binance.fetchOrderBookWs (symbol, limit?, params?)
```

### [watchTradesForSymbols](https://docs.ccxt.com/docs/exchanges/binance\#watchtradesforsymbols)

get the list of most recent trades for a list of symbols

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `Array<object>` \- a list of [trade structures](https://docs.ccxt.com/docs/manual#public-trades)

**See**

- [https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/market-data-requests#aggregate-trades](https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/market-data-requests#aggregate-trades)
- [https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/market-data-requests#recent-trades](https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/market-data-requests#recent-trades)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Aggregate-Trade-Streams](https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Aggregate-Trade-Streams)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Aggregate-Trade-Streams](https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Aggregate-Trade-Streams)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>` | Yes | unified symbol of the market to fetch trades for |
| since | `int` | No | timestamp in ms of the earliest trade to fetch |
| limit | `int` | No | the maximum amount of trades to fetch |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.name | `string` | No | the name of the method to call, 'trade' or 'aggTrade', default is 'trade' |

```
binance.watchTradesForSymbols (symbols, since?, limit?, params?)
```

### [unWatchTradesForSymbols](https://docs.ccxt.com/docs/exchanges/binance\#unwatchtradesforsymbols)

unsubscribes from the trades channel

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `Array<object>` \- a list of [trade structures](https://docs.ccxt.com/docs/manual#public-trades)

**See**

- [https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/market-data-requests#aggregate-trades](https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/market-data-requests#aggregate-trades)
- [https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/market-data-requests#recent-trades](https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/market-data-requests#recent-trades)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Aggregate-Trade-Streams](https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Aggregate-Trade-Streams)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Aggregate-Trade-Streams](https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Aggregate-Trade-Streams)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>` | Yes | unified symbol of the market to fetch trades for |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.name | `string` | No | the name of the method to call, 'trade' or 'aggTrade', default is 'trade' |

```
binance.unWatchTradesForSymbols (symbols, params?)
```

### [unWatchTrades](https://docs.ccxt.com/docs/exchanges/binance\#unwatchtrades)

unsubscribes from the trades channel

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `Array<object>` \- a list of [trade structures](https://docs.ccxt.com/docs/manual#public-trades)

**See**

- [https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/market-data-requests#aggregate-trades](https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/market-data-requests#aggregate-trades)
- [https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/market-data-requests#recent-trades](https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/market-data-requests#recent-trades)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Aggregate-Trade-Streams](https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Aggregate-Trade-Streams)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Aggregate-Trade-Streams](https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Aggregate-Trade-Streams)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to fetch trades for |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.name | `string` | No | the name of the method to call, 'trade' or 'aggTrade', default is 'trade' |

```
binance.unWatchTrades (symbol, params?)
```

### [watchTrades](https://docs.ccxt.com/docs/exchanges/binance\#watchtrades)

get the list of most recent trades for a particular symbol

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `Array<object>` \- a list of [trade structures](https://docs.ccxt.com/docs/manual#public-trades)

**See**

- [https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/market-data-requests#aggregate-trades](https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/market-data-requests#aggregate-trades)
- [https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/market-data-requests#recent-trades](https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/market-data-requests#recent-trades)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Aggregate-Trade-Streams](https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Aggregate-Trade-Streams)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Aggregate-Trade-Streams](https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Aggregate-Trade-Streams)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to fetch trades for |
| since | `int` | No | timestamp in ms of the earliest trade to fetch |
| limit | `int` | No | the maximum amount of trades to fetch |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.name | `string` | No | the name of the method to call, 'trade' or 'aggTrade', default is 'trade' |

```
binance.watchTrades (symbol, since?, limit?, params?)
```

### [watchOHLCV](https://docs.ccxt.com/docs/exchanges/binance\#watchohlcv)

watches historical candlestick data containing the open, high, low, and close price, and the volume of a market

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `Array<Array<int>>` \- A list of candles ordered as timestamp, open, high, low, close, volume

**See**

- [https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/market-data-requests#klines](https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/market-data-requests#klines)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Kline-Candlestick-Streams](https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Kline-Candlestick-Streams)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Kline-Candlestick-Streams](https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Kline-Candlestick-Streams)
- [https://developers.binance.com/en/docs/catalog/advanced-trading-stocks-trading/api/ws-streams/market-streams#kline-stream](https://developers.binance.com/en/docs/catalog/advanced-trading-stocks-trading/api/ws-streams/market-streams#kline-stream)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to fetch OHLCV data for |
| timeframe | `string` | Yes | the length of time each candle represents |
| since | `int` | No | timestamp in ms of the earliest candle to fetch |
| limit | `int` | No | the maximum amount of candles to fetch |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.stock | `boolean` | No | set to true to use stocks market streams |
| params.timezone | `object` | No | if provided, kline intervals are interpreted in that timezone instead of UTC, example '+08:00' |

```
binance.watchOHLCV (symbol, timeframe, since?, limit?, params?)
```

### [watchOHLCVForSymbols](https://docs.ccxt.com/docs/exchanges/binance\#watchohlcvforsymbols)

watches historical candlestick data containing the open, high, low, and close price, and the volume of a market

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `Array<Array<int>>` \- A list of candles ordered as timestamp, open, high, low, close, volume

**See**

- [https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/market-data-requests#klines](https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/market-data-requests#klines)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Kline-Candlestick-Streams](https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Kline-Candlestick-Streams)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Kline-Candlestick-Streams](https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Kline-Candlestick-Streams)
- [https://developers.binance.com/en/docs/catalog/advanced-trading-stocks-trading/api/ws-streams/market-streams#kline-stream](https://developers.binance.com/en/docs/catalog/advanced-trading-stocks-trading/api/ws-streams/market-streams#kline-stream)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbolsAndTimeframes | `Array<Array<string>>` | Yes | array of arrays containing unified symbols and timeframes to fetch OHLCV data for, example \[\['BTC/USDT', '1m'\], \['LTC/USDT', '5m'\]\] |
| since | `int` | No | timestamp in ms of the earliest candle to fetch |
| limit | `int` | No | the maximum amount of candles to fetch |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.stock | `boolean` | No | set to true to use stocks market streams |
| params.timezone | `object` | No | if provided, kline intervals are interpreted in that timezone instead of UTC, example '+08:00' |

```
binance.watchOHLCVForSymbols (symbolsAndTimeframes, since?, limit?, params?)
```

### [unWatchOHLCVForSymbols](https://docs.ccxt.com/docs/exchanges/binance\#unwatchohlcvforsymbols)

unWatches historical candlestick data containing the open, high, low, and close price, and the volume of a market

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `Array<Array<int>>` \- A list of candles ordered as timestamp, open, high, low, close, volume

**See**

- [https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/market-data-requests#klines](https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/market-data-requests#klines)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Kline-Candlestick-Streams](https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Kline-Candlestick-Streams)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Kline-Candlestick-Streams](https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Kline-Candlestick-Streams)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbolsAndTimeframes | `Array<Array<string>>` | Yes | array of arrays containing unified symbols and timeframes to fetch OHLCV data for, example \[\['BTC/USDT', '1m'\], \['LTC/USDT', '5m'\]\] |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.timezone | `object` | No | if provided, kline intervals are interpreted in that timezone instead of UTC, example '+08:00' |

```
binance.unWatchOHLCVForSymbols (symbolsAndTimeframes, params?)
```

### [unWatchOHLCV](https://docs.ccxt.com/docs/exchanges/binance\#unwatchohlcv)

unWatches historical candlestick data containing the open, high, low, and close price, and the volume of a market

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `Array<Array<int>>` \- A list of candles ordered as timestamp, open, high, low, close, volume

**See**

- [https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/market-data-requests#klines](https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/market-data-requests#klines)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Kline-Candlestick-Streams](https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Kline-Candlestick-Streams)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Kline-Candlestick-Streams](https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Kline-Candlestick-Streams)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to fetch OHLCV data for |
| timeframe | `string` | Yes | the length of time each candle represents |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.timezone | `object` | No | if provided, kline intervals are interpreted in that timezone instead of UTC, example '+08:00' |

```
binance.unWatchOHLCV (symbol, timeframe, params?)
```

### [fetchTickerWs](https://docs.ccxt.com/docs/exchanges/binance\#fetchtickerws)

fetches a price ticker, a statistical calculation with the information calculated over the past 24 hours for a specific market

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- a [ticker structure](https://docs.ccxt.com/docs/manual#ticker-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to fetch the ticker for |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.method | `string` | No | method to use can be ticker.price or ticker.book |
| params.returnRateLimits | `boolean` | No | return the rate limits for the exchange |

```
binance.fetchTickerWs (symbol, params?)
```

### [fetchOHLCVWs](https://docs.ccxt.com/docs/exchanges/binance\#fetchohlcvws)

query historical candlestick data containing the open, high, low, and close price, and the volume of a market

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `Array<Array<int>>` \- A list of candles ordered as timestamp, open, high, low, close, volume

**See**: [https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/market-data-requests#klines](https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/market-data-requests#klines)

| Param | Type | Description |
| --- | --- | --- |
| symbol | `string` | unified symbol of the market to query OHLCV data for |
| timeframe | `string` | the length of time each candle represents |
| since | `int` | timestamp in ms of the earliest candle to fetch |
| limit | `int` | the maximum amount of candles to fetch |
| params | `object` | extra parameters specific to the exchange API endpoint |
| params.until | `int` | timestamp in ms of the earliest candle to fetch EXCHANGE SPECIFIC PARAMETERS |
| params.timeZone | `string` | default=0 (UTC) |

```
binance.fetchOHLCVWs (symbol, timeframe, since, limit, params)
```

### [watchTicker](https://docs.ccxt.com/docs/exchanges/binance\#watchticker)

watches a price ticker, a statistical calculation with the information calculated over the past 24 hours for a specific market

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- a [ticker structure](https://docs.ccxt.com/docs/manual#ticker-structure)

**See**

- [https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#individual-symbol-mini-ticker-stream](https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#individual-symbol-mini-ticker-stream)
- [https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#all-market-mini-tickers-stream](https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#all-market-mini-tickers-stream)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Ticker-Streams](https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Ticker-Streams)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/All-Market-Mini-Tickers-Stream](https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/All-Market-Mini-Tickers-Stream)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/All-Market-Mini-Tickers-Stream](https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/All-Market-Mini-Tickers-Stream)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Individual-Symbol-Ticker-Streams](https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Individual-Symbol-Ticker-Streams)
- [https://developers.binance.com/en/docs/catalog/advanced-trading-stocks-trading/api/ws-streams/market-streams#price-stream](https://developers.binance.com/en/docs/catalog/advanced-trading-stocks-trading/api/ws-streams/market-streams#price-stream)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to fetch the ticker for |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.stock | `boolean` | No | set to true to use the stocks aggregated price stream |
| params.name | `string` | No | stream to use can be ticker or miniTicker |

```
binance.watchTicker (symbol, params?)
```

### [watchMarkPrice](https://docs.ccxt.com/docs/exchanges/binance\#watchmarkprice)

watches a mark price for a specific market

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- a [ticker structure](https://docs.ccxt.com/docs/manual#ticker-structure)

**See**: [https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Mark-Price-Stream](https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Mark-Price-Stream)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to fetch the ticker for |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.use1sFreq | `boolean` | No | _default is true_ if set to true, the mark price will be updated every second, otherwise every 3 seconds |

```
binance.watchMarkPrice (symbol, params?)
```

### [watchMarkPrices](https://docs.ccxt.com/docs/exchanges/binance\#watchmarkprices)

watches the mark price for all markets

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- a [ticker structure](https://docs.ccxt.com/docs/manual#ticker-structure)

**See**: [https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Mark-Price-Stream-for-All-market](https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Mark-Price-Stream-for-All-market)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>` | Yes | unified symbol of the market to fetch the ticker for |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.use1sFreq | `boolean` | No | _default is true_ if set to true, the mark price will be updated every second, otherwise every 3 seconds |

```
binance.watchMarkPrices (symbols, params?)
```

### [watchTickers](https://docs.ccxt.com/docs/exchanges/binance\#watchtickers)

watches a price ticker, a statistical calculation with the information calculated over the past 24 hours for all markets of a specific list

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- a [ticker structure](https://docs.ccxt.com/docs/manual#ticker-structure)

**See**

- [https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#individual-symbol-mini-ticker-stream](https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#individual-symbol-mini-ticker-stream)
- [https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#all-market-mini-tickers-stream](https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#all-market-mini-tickers-stream)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Ticker-Streams](https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Ticker-Streams)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/All-Market-Mini-Tickers-Stream](https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/All-Market-Mini-Tickers-Stream)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/All-Market-Mini-Tickers-Stream](https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/All-Market-Mini-Tickers-Stream)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Individual-Symbol-Ticker-Streams](https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Individual-Symbol-Ticker-Streams)
- [https://developers.binance.com/en/docs/catalog/advanced-trading-stocks-trading/api/ws-streams/market-streams#price-stream](https://developers.binance.com/en/docs/catalog/advanced-trading-stocks-trading/api/ws-streams/market-streams#price-stream)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>` | Yes | unified symbol of the market to fetch the ticker for |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.stock | `boolean` | No | set to true to use the stocks price stream |

```
binance.watchTickers (symbols, params?)
```

### [unWatchTickers](https://docs.ccxt.com/docs/exchanges/binance\#unwatchtickers)

unWatches a price ticker, a statistical calculation with the information calculated over the past 24 hours for all markets of a specific list

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- a [ticker structure](https://docs.ccxt.com/docs/manual#ticker-structure)

**See**

- [https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#individual-symbol-mini-ticker-stream](https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#individual-symbol-mini-ticker-stream)
- [https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#all-market-mini-tickers-stream](https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#all-market-mini-tickers-stream)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Ticker-Streams](https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Ticker-Streams)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/All-Market-Mini-Tickers-Stream](https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/All-Market-Mini-Tickers-Stream)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/All-Market-Mini-Tickers-Stream](https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/All-Market-Mini-Tickers-Stream)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Individual-Symbol-Ticker-Streams](https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Individual-Symbol-Ticker-Streams)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>` | Yes | unified symbol of the market to fetch the ticker for |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

```
binance.unWatchTickers (symbols, params?)
```

### [unWatchMarkPrices](https://docs.ccxt.com/docs/exchanges/binance\#unwatchmarkprices)

unWatches a price ticker, a statistical calculation with the information calculated over the past 24 hours for all markets of a specific list

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- a [ticker structure](https://docs.ccxt.com/docs/manual#ticker-structure)

**See**: [https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Mark-Price-Stream](https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Mark-Price-Stream)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>` | Yes | unified symbol of the market to fetch the ticker for |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

```
binance.unWatchMarkPrices (symbols, params?)
```

### [unWatchMarkPrice](https://docs.ccxt.com/docs/exchanges/binance\#unwatchmarkprice)

unWatches a price ticker, a statistical calculation with the information calculated over the past 24 hours for all markets of a specific list

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- a [ticker structure](https://docs.ccxt.com/docs/manual#ticker-structure)

**See**: [https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Mark-Price-Stream](https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Mark-Price-Stream)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to fetch the ticker for |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

```
binance.unWatchMarkPrice (symbol, params?)
```

### [unWatchBidsAsks](https://docs.ccxt.com/docs/exchanges/binance\#unwatchbidsasks)

unWatches best bid & ask for symbols

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- a dictionary of [ticker structures](https://docs.ccxt.com/docs/manual#ticker-structure)

**See**

- [https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#individual-book-ticker-streams](https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#individual-book-ticker-streams)
- [https://developers.binance.com/docs/derivatives/options-trading/websocket-market-streams/Bookticker](https://developers.binance.com/docs/derivatives/options-trading/websocket-market-streams/Bookticker)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>` | No | unified symbols |
| params | `object` | No | extra parameters |

```
binance.unWatchBidsAsks (symbols?, params?)
```

### [unWatchTicker](https://docs.ccxt.com/docs/exchanges/binance\#unwatchticker)

unWatches a price ticker, a statistical calculation with the information calculated over the past 24 hours for all markets of a specific list

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- a [ticker structure](https://docs.ccxt.com/docs/manual#ticker-structure)

**See**

- [https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#individual-symbol-mini-ticker-stream](https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#individual-symbol-mini-ticker-stream)
- [https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#all-market-mini-tickers-stream](https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#all-market-mini-tickers-stream)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Ticker-Streams](https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Ticker-Streams)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/All-Market-Mini-Tickers-Stream](https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/All-Market-Mini-Tickers-Stream)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/All-Market-Mini-Tickers-Stream](https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/All-Market-Mini-Tickers-Stream)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Individual-Symbol-Ticker-Streams](https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Individual-Symbol-Ticker-Streams)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to fetch the ticker for |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

```
binance.unWatchTicker (symbol, params?)
```

### [watchBidsAsks](https://docs.ccxt.com/docs/exchanges/binance\#watchbidsasks)

watches best bid & ask for symbols

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- a [ticker structure](https://docs.ccxt.com/docs/manual#ticker-structure)

**See**

- [https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/market-data-requests#symbol-order-book-ticker](https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/market-data-requests#symbol-order-book-ticker)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/All-Book-Tickers-Stream](https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/All-Book-Tickers-Stream)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/All-Book-Tickers-Stream](https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/All-Book-Tickers-Stream)
- [https://developers.binance.com/en/docs/catalog/advanced-trading-stocks-trading/api/ws-streams/market-streams#quote-stream](https://developers.binance.com/en/docs/catalog/advanced-trading-stocks-trading/api/ws-streams/market-streams#quote-stream)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>` | Yes | unified symbol of the market to fetch the ticker for |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.stock | `boolean` | No | set to true to use stocks quote streams |

```
binance.watchBidsAsks (symbols, params?)
```

### [fetchBalanceWs](https://docs.ccxt.com/docs/exchanges/binance\#fetchbalancews)

fetch balance and get the amount of funds available for trading or funds locked in orders

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- a [balance structure](https://docs.ccxt.com/docs/manual#balance-structure)

**See**

- [https://developers.binance.com/docs/derivatives/usds-margined-futures/account/websocket-api/Futures-Account-Balance](https://developers.binance.com/docs/derivatives/usds-margined-futures/account/websocket-api/Futures-Account-Balance)
- [https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/account-requests#account-information-user\_data](https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/account-requests#account-information-user_data)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/account/websocket-api](https://developers.binance.com/docs/derivatives/coin-margined-futures/account/websocket-api)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.type | `string`, `undefined` | No | 'future', 'delivery', 'savings', 'funding', or 'spot' |
| params.marginMode | `string`, `undefined` | No | 'cross' or 'isolated', for margin trading, uses this.options.defaultMarginMode if not passed, defaults to undefined/None/null |
| params.symbols | `Array<string>`, `undefined` | No | unified market symbols, only used in isolated margin mode |
| params.method | `string`, `undefined` | No | method to use. Can be account.balance, account.status, v2/account.balance or v2/account.status |

```
binance.fetchBalanceWs (params?)
```

### [fetchPositionWs](https://docs.ccxt.com/docs/exchanges/binance\#fetchpositionws)

fetch data on an open position

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- a [position structure](https://docs.ccxt.com/docs/manual#position-structure)

**See**: [https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/websocket-api/Position-Information](https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/websocket-api/Position-Information)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol of the market the position is held in |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

```
binance.fetchPositionWs (symbol, params?)
```

### [fetchPositionsWs](https://docs.ccxt.com/docs/exchanges/binance\#fetchpositionsws)

fetch all open positions

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `Array<object>` \- a list of [position structure](https://docs.ccxt.com/docs/manual#position-structure)

**See**

- [https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/websocket-api/Position-Information](https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/websocket-api/Position-Information)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/websocket-api/Position-Information](https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/websocket-api/Position-Information)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>` | No | list of unified market symbols |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.returnRateLimits | `boolean` | No | set to true to return rate limit informations, defaults to false. |
| params.method | `string`, `undefined` | No | method to use. Can be account.position or v2/account.position |

```
binance.fetchPositionsWs (symbols?, params?)
```

### [watchBalance](https://docs.ccxt.com/docs/exchanges/binance\#watchbalance)

watch balance and get the amount of funds available for trading or funds locked in orders

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- a [balance structure](https://docs.ccxt.com/docs/manual#balance-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.portfolioMargin | `boolean` | No | set to true if you would like to watch the balance of a portfolio margin account |

```
binance.watchBalance (params?)
```

### [createOrderWs](https://docs.ccxt.com/docs/exchanges/binance\#createorderws)

create a trade order

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- an [order structure](https://docs.ccxt.com/docs/manual#order-structure)

**See**

- [https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/trading-requests#place-new-order-trade](https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/trading-requests#place-new-order-trade)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/websocket-api/New-Order](https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/websocket-api/New-Order)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/websocket-api](https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/websocket-api)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/websocket-api/New-Algo-Order](https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/websocket-api/New-Algo-Order)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to create an order in |
| type | `string` | Yes | 'market' or 'limit' |
| side | `string` | Yes | 'buy' or 'sell' |
| amount | `float` | Yes | how much of currency you want to trade in units of base currency |
| price | `float`, `undefined` | No | the price at which the order is to be fulfilled, in units of the quote currency, ignored in market orders |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.test | `boolean` | Yes | test order, default false |
| params.returnRateLimits | `boolean` | Yes | set to true to return rate limit information, default false |

```
binance.createOrderWs (symbol, type, side, amount, price?, params?)
```

### [editOrderWs](https://docs.ccxt.com/docs/exchanges/binance\#editorderws)

edit a trade order

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- an [order structure](https://docs.ccxt.com/docs/manual#order-structure)

**See**

- [https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/trading-requests#cancel-and-replace-order-trade](https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/trading-requests#cancel-and-replace-order-trade)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/websocket-api/Modify-Order](https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/websocket-api/Modify-Order)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/websocket-api/Modify-Order](https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/websocket-api/Modify-Order)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| id | `string` | Yes | order id |
| symbol | `string` | Yes | unified symbol of the market to create an order in |
| type | `string` | Yes | 'market' or 'limit' |
| side | `string` | Yes | 'buy' or 'sell' |
| amount | `float` | Yes | how much of the currency you want to trade in units of the base currency |
| price | `float`, `undefined` | No | the price at which the order is to be fulfilled, in units of the quote currency, ignored in market orders |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

```
binance.editOrderWs (id, symbol, type, side, amount, price?, params?)
```

### [cancelOrderWs](https://docs.ccxt.com/docs/exchanges/binance\#cancelorderws)

cancel multiple orders

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- an list of [order structures](https://docs.ccxt.com/docs/manual#order-structure)

**See**

- [https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/trading-requests#cancel-order-trade](https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/trading-requests#cancel-order-trade)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/websocket-api/Cancel-Order](https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/websocket-api/Cancel-Order)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/websocket-api/Cancel-Order](https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/websocket-api/Cancel-Order)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/websocket-api/Cancel-Algo-Order](https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/websocket-api/Cancel-Algo-Order)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| id | `string` | Yes | order id |
| symbol | `string` | No | unified market symbol, default is undefined |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.cancelRestrictions | `string`, `undefined` | No | Supported values: ONLY\_NEW - Cancel will succeed if the order status is NEW. ONLY\_PARTIALLY\_FILLED - Cancel will succeed if order status is PARTIALLY\_FILLED. |
| params.trigger | `boolean` | No | set to true if you would like to cancel a conditional order |

```
binance.cancelOrderWs (id, symbol?, params?)
```

### [cancelAllOrdersWs](https://docs.ccxt.com/docs/exchanges/binance\#cancelallordersws)

cancel all open orders in a market

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `Array<object>` \- a list of [order structures](https://docs.ccxt.com/docs/manual#order-structure)

**See**: [https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/trading-requests#cancel-open-orders-trade](https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/trading-requests#cancel-open-orders-trade)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | No | unified market symbol of the market to cancel orders in |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

```
binance.cancelAllOrdersWs (symbol?, params?)
```

### [fetchOrderWs](https://docs.ccxt.com/docs/exchanges/binance\#fetchorderws)

fetches information on an order made by the user

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `object` \- An [order structure](https://docs.ccxt.com/docs/manual#order-structure)

**See**

- [https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/trading-requests#query-order-user\_data](https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/trading-requests#query-order-user_data)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/websocket-api/Query-Order](https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/websocket-api/Query-Order)
- [https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/websocket-api/Query-Order](https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/websocket-api/Query-Order)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| id | `string` | Yes | order id |
| symbol | `string` | No | unified symbol of the market the order was made in |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

```
binance.fetchOrderWs (id, symbol?, params?)
```

### [fetchOrdersWs](https://docs.ccxt.com/docs/exchanges/binance\#fetchordersws)

fetches information on multiple orders made by the user

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `Array<object>` \- a list of [order structures](https://docs.ccxt.com/docs/manual#order-structure)

**See**: [https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/trading-requests#order-lists](https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/trading-requests#order-lists)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol of the market orders were made in |
| since | `int`, `undefined` | No | the earliest time in ms to fetch orders for |
| limit | `int`, `undefined` | No | the maximum number of order structures to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.orderId | `int` | No | order id to begin at |
| params.startTime | `int` | No | earliest time in ms to retrieve orders for |
| params.endTime | `int` | No | latest time in ms to retrieve orders for |
| params.limit | `int` | No | the maximum number of order structures to retrieve |

```
binance.fetchOrdersWs (symbol, since?, limit?, params?)
```

### [fetchClosedOrdersWs](https://docs.ccxt.com/docs/exchanges/binance\#fetchclosedordersws)

fetch closed orders

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `Array<object>` \- a list of [order structures](https://docs.ccxt.com/docs/manual#order-structure)

**See**: [https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/trading-requests#order-lists](https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/trading-requests#order-lists)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol |
| since | `int` | No | the earliest time in ms to fetch open orders for |
| limit | `int` | No | the maximum number of open orders structures to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

```
binance.fetchClosedOrdersWs (symbol, since?, limit?, params?)
```

### [fetchOpenOrdersWs](https://docs.ccxt.com/docs/exchanges/binance\#fetchopenordersws)

fetch all unfilled currently open orders

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `Array<object>` \- a list of [order structures](https://docs.ccxt.com/docs/manual#order-structure)

**See**: [https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/trading-requests#current-open-orders-user\_data](https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/trading-requests#current-open-orders-user_data)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol |
| since | `int`, `undefined` | No | the earliest time in ms to fetch open orders for |
| limit | `int`, `undefined` | No | the maximum number of open orders structures to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

```
binance.fetchOpenOrdersWs (symbol, since?, limit?, params?)
```

### [watchOrders](https://docs.ccxt.com/docs/exchanges/binance\#watchorders)

watches information on multiple orders made by the user

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `Array<object>` \- a list of [order structures](https://docs.ccxt.com/docs/manual#order-structure)

**See**

- [https://developers.binance.com/docs/binance-spot-api-docs/user-data-stream#order-update](https://developers.binance.com/docs/binance-spot-api-docs/user-data-stream#order-update)
- [https://developers.binance.com/docs/margin\_trading/trade-data-stream/Event-Order-Update](https://developers.binance.com/docs/margin_trading/trade-data-stream/Event-Order-Update)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/user-data-streams/Event-Order-Update](https://developers.binance.com/docs/derivatives/usds-margined-futures/user-data-streams/Event-Order-Update)
- [https://developers.binance.com/docs/derivatives/usds-margined-futures/user-data-streams/Event-Algo-Order-Update](https://developers.binance.com/docs/derivatives/usds-margined-futures/user-data-streams/Event-Algo-Order-Update)
- [https://developers.binance.com/en/docs/catalog/advanced-trading-stocks-trading/api/ws-streams/user-streams#order-report-stream](https://developers.binance.com/en/docs/catalog/advanced-trading-stocks-trading/api/ws-streams/user-streams#order-report-stream)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol of the market the orders were made in |
| since | `int` | No | the earliest time in ms to fetch orders for |
| limit | `int` | No | the maximum number of order structures to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.stock | `boolean` | No | set to true to use stocks user data streams |
| params.marginMode | `string`, `undefined` | No | 'cross' or 'isolated', for spot margin |
| params.portfolioMargin | `boolean` | No | set to true if you would like to watch portfolio margin account orders |

```
binance.watchOrders (symbol, since?, limit?, params?)
```

### [watchPositions](https://docs.ccxt.com/docs/exchanges/binance\#watchpositions)

watch all open positions

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `Array<object>` \- a list of [position structure](https://docs.ccxt.com/docs/manual#position-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>`, `undefined` | Yes | list of unified market symbols |
| since | `number` | No | since timestamp |
| limit | `number` | No | limit |
| params | `object` | Yes | extra parameters specific to the exchange API endpoint |
| params.portfolioMargin | `boolean` | No | set to true if you would like to watch positions in a portfolio margin account |

```
binance.watchPositions (symbols, since?, limit?, params)
```

### [fetchMyTradesWs](https://docs.ccxt.com/docs/exchanges/binance\#fetchmytradesws)

fetch all trades made by the user

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `Array<object>` \- a list of [trade structures](https://docs.ccxt.com/docs/manual#trade-structure)

**See**: [https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/account-requests#account-trade-history-user\_data](https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/account-requests#account-trade-history-user_data)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol |
| since | `int`, `undefined` | No | the earliest time in ms to fetch trades for |
| limit | `int`, `undefined` | No | the maximum number of trades structures to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.endTime | `int` | No | the latest time in ms to fetch trades for |
| params.fromId | `int` | No | first trade Id to fetch |

```
binance.fetchMyTradesWs (symbol, since?, limit?, params?)
```

### [fetchTradesWs](https://docs.ccxt.com/docs/exchanges/binance\#fetchtradesws)

fetch all trades made by the user

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `Array<object>` \- a list of [trade structures](https://docs.ccxt.com/docs/manual#trade-structure)

**See**: [https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/market-data-requests#recent-trades](https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/market-data-requests#recent-trades)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol |
| since | `int` | No | the earliest time in ms to fetch trades for |
| limit | `int` | No | the maximum number of trades structures to retrieve, default=500, max=1000 |
| params | `object` | No | extra parameters specific to the exchange API endpoint EXCHANGE SPECIFIC PARAMETERS |
| params.fromId | `int` | No | trade ID to begin at |

```
binance.fetchTradesWs (symbol, since?, limit?, params?)
```

### [watchMyTrades](https://docs.ccxt.com/docs/exchanges/binance\#watchmytrades)

watches information on multiple trades made by the user

**Kind**: instance method of [`binance`](https://docs.ccxt.com/docs/exchanges/binance#binance)

**Returns**: `Array<object>` \- a list of [trade structures](https://docs.ccxt.com/docs/manual#trade-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol of the market orders were made in |
| since | `int` | No | the earliest time in ms to fetch orders for |
| limit | `int` | No | the maximum number of order structures to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.portfolioMargin | `boolean` | No | set to true if you would like to watch trades in a portfolio margin account |

```
binance.watchMyTrades (symbol, since?, limit?, params?)
```

[Implicit API\\
\\
Every raw bigone endpoint exposed as a CCXT implicit method — names, HTTP verbs, paths and rate-limit costs.](https://docs.ccxt.com/docs/exchanges/bigone/implicit-api) [Implicit API\\
\\
Every raw binance endpoint exposed as a CCXT implicit method — names, HTTP verbs, paths and rate-limit costs.](https://docs.ccxt.com/docs/exchanges/binance/implicit-api)

### On this page

[binance](https://docs.ccxt.com/docs/exchanges/binance#binance) [enableDemoTrading](https://docs.ccxt.com/docs/exchanges/binance#enabledemotrading) [fetchTime](https://docs.ccxt.com/docs/exchanges/binance#fetchtime) [fetchCurrencies](https://docs.ccxt.com/docs/exchanges/binance#fetchcurrencies) [fetchMarkets](https://docs.ccxt.com/docs/exchanges/binance#fetchmarkets) [fetchBalance](https://docs.ccxt.com/docs/exchanges/binance#fetchbalance) [fetchOrderBook](https://docs.ccxt.com/docs/exchanges/binance#fetchorderbook) [fetchStatus](https://docs.ccxt.com/docs/exchanges/binance#fetchstatus) [fetchTicker](https://docs.ccxt.com/docs/exchanges/binance#fetchticker) [fetchBidsAsks](https://docs.ccxt.com/docs/exchanges/binance#fetchbidsasks) [fetchLastPrices](https://docs.ccxt.com/docs/exchanges/binance#fetchlastprices) [fetchTickers](https://docs.ccxt.com/docs/exchanges/binance#fetchtickers) [fetchMarkPrice](https://docs.ccxt.com/docs/exchanges/binance#fetchmarkprice) [fetchMarkPrices](https://docs.ccxt.com/docs/exchanges/binance#fetchmarkprices) [fetchOHLCV](https://docs.ccxt.com/docs/exchanges/binance#fetchohlcv) [fetchTrades](https://docs.ccxt.com/docs/exchanges/binance#fetchtrades) [editContractOrder](https://docs.ccxt.com/docs/exchanges/binance#editcontractorder) [editOrder](https://docs.ccxt.com/docs/exchanges/binance#editorder) [editOrders](https://docs.ccxt.com/docs/exchanges/binance#editorders) [createOrders](https://docs.ccxt.com/docs/exchanges/binance#createorders) [createOrder](https://docs.ccxt.com/docs/exchanges/binance#createorder) [createMarketOrderWithCost](https://docs.ccxt.com/docs/exchanges/binance#createmarketorderwithcost) [createMarketBuyOrderWithCost](https://docs.ccxt.com/docs/exchanges/binance#createmarketbuyorderwithcost) [createMarketSellOrderWithCost](https://docs.ccxt.com/docs/exchanges/binance#createmarketsellorderwithcost) [fetchOrder](https://docs.ccxt.com/docs/exchanges/binance#fetchorder) [fetchOrders](https://docs.ccxt.com/docs/exchanges/binance#fetchorders) [fetchOpenOrders](https://docs.ccxt.com/docs/exchanges/binance#fetchopenorders) [fetchOpenOrder](https://docs.ccxt.com/docs/exchanges/binance#fetchopenorder) [fetchClosedOrders](https://docs.ccxt.com/docs/exchanges/binance#fetchclosedorders) [fetchCanceledOrders](https://docs.ccxt.com/docs/exchanges/binance#fetchcanceledorders) [fetchCanceledAndClosedOrders](https://docs.ccxt.com/docs/exchanges/binance#fetchcanceledandclosedorders) [cancelOrder](https://docs.ccxt.com/docs/exchanges/binance#cancelorder) [cancelAllOrders](https://docs.ccxt.com/docs/exchanges/binance#cancelallorders) [cancelOrders](https://docs.ccxt.com/docs/exchanges/binance#cancelorders) [fetchOrderTrades](https://docs.ccxt.com/docs/exchanges/binance#fetchordertrades) [fetchMyTrades](https://docs.ccxt.com/docs/exchanges/binance#fetchmytrades) [fetchMyDustTrades](https://docs.ccxt.com/docs/exchanges/binance#fetchmydusttrades) [fetchDeposits](https://docs.ccxt.com/docs/exchanges/binance#fetchdeposits) [fetchWithdrawals](https://docs.ccxt.com/docs/exchanges/binance#fetchwithdrawals) [transfer](https://docs.ccxt.com/docs/exchanges/binance#transfer) [fetchTransfers](https://docs.ccxt.com/docs/exchanges/binance#fetchtransfers) [fetchDepositAddress](https://docs.ccxt.com/docs/exchanges/binance#fetchdepositaddress) [fetchTransactionFees](https://docs.ccxt.com/docs/exchanges/binance#fetchtransactionfees) [fetchDepositWithdrawFees](https://docs.ccxt.com/docs/exchanges/binance#fetchdepositwithdrawfees) [withdraw](https://docs.ccxt.com/docs/exchanges/binance#withdraw) [fetchTradingFee](https://docs.ccxt.com/docs/exchanges/binance#fetchtradingfee) [fetchTradingFees](https://docs.ccxt.com/docs/exchanges/binance#fetchtradingfees) [fetchFundingRate](https://docs.ccxt.com/docs/exchanges/binance#fetchfundingrate) [fetchFundingRateHistory](https://docs.ccxt.com/docs/exchanges/binance#fetchfundingratehistory) [fetchFundingRates](https://docs.ccxt.com/docs/exchanges/binance#fetchfundingrates) [fetchLeverageTiers](https://docs.ccxt.com/docs/exchanges/binance#fetchleveragetiers) [fetchPosition](https://docs.ccxt.com/docs/exchanges/binance#fetchposition) [fetchOptionPositions](https://docs.ccxt.com/docs/exchanges/binance#fetchoptionpositions) [fetchPositions](https://docs.ccxt.com/docs/exchanges/binance#fetchpositions) [fetchFundingHistory](https://docs.ccxt.com/docs/exchanges/binance#fetchfundinghistory) [setLeverage](https://docs.ccxt.com/docs/exchanges/binance#setleverage) [setMarginMode](https://docs.ccxt.com/docs/exchanges/binance#setmarginmode) [setPositionMode](https://docs.ccxt.com/docs/exchanges/binance#setpositionmode) [fetchLeverages](https://docs.ccxt.com/docs/exchanges/binance#fetchleverages) [fetchSettlementHistory](https://docs.ccxt.com/docs/exchanges/binance#fetchsettlementhistory) [fetchMySettlementHistory](https://docs.ccxt.com/docs/exchanges/binance#fetchmysettlementhistory) [fetchLedgerEntry](https://docs.ccxt.com/docs/exchanges/binance#fetchledgerentry) [fetchLedger](https://docs.ccxt.com/docs/exchanges/binance#fetchledger) [reduceMargin](https://docs.ccxt.com/docs/exchanges/binance#reducemargin) [addMargin](https://docs.ccxt.com/docs/exchanges/binance#addmargin) [fetchCrossBorrowRate](https://docs.ccxt.com/docs/exchanges/binance#fetchcrossborrowrate) [fetchIsolatedBorrowRate](https://docs.ccxt.com/docs/exchanges/binance#fetchisolatedborrowrate) [fetchIsolatedBorrowRates](https://docs.ccxt.com/docs/exchanges/binance#fetchisolatedborrowrates) [fetchBorrowRateHistory](https://docs.ccxt.com/docs/exchanges/binance#fetchborrowratehistory) [createGiftCode](https://docs.ccxt.com/docs/exchanges/binance#creategiftcode) [redeemGiftCode](https://docs.ccxt.com/docs/exchanges/binance#redeemgiftcode) [verifyGiftCode](https://docs.ccxt.com/docs/exchanges/binance#verifygiftcode) [fetchBorrowInterest](https://docs.ccxt.com/docs/exchanges/binance#fetchborrowinterest) [repayCrossMargin](https://docs.ccxt.com/docs/exchanges/binance#repaycrossmargin) [repayIsolatedMargin](https://docs.ccxt.com/docs/exchanges/binance#repayisolatedmargin) [borrowCrossMargin](https://docs.ccxt.com/docs/exchanges/binance#borrowcrossmargin) [borrowIsolatedMargin](https://docs.ccxt.com/docs/exchanges/binance#borrowisolatedmargin) [fetchOpenInterestHistory](https://docs.ccxt.com/docs/exchanges/binance#fetchopeninteresthistory) [fetchOpenInterest](https://docs.ccxt.com/docs/exchanges/binance#fetchopeninterest) [fetchMyLiquidations](https://docs.ccxt.com/docs/exchanges/binance#fetchmyliquidations) [fetchGreeks](https://docs.ccxt.com/docs/exchanges/binance#fetchgreeks) [fetchAllGreeks](https://docs.ccxt.com/docs/exchanges/binance#fetchallgreeks) [fetchPositionMode](https://docs.ccxt.com/docs/exchanges/binance#fetchpositionmode) [fetchMarginModes](https://docs.ccxt.com/docs/exchanges/binance#fetchmarginmodes) [fetchMarginMode](https://docs.ccxt.com/docs/exchanges/binance#fetchmarginmode) [fetchOption](https://docs.ccxt.com/docs/exchanges/binance#fetchoption) [fetchMarginAdjustmentHistory](https://docs.ccxt.com/docs/exchanges/binance#fetchmarginadjustmenthistory) [fetchConvertCurrencies](https://docs.ccxt.com/docs/exchanges/binance#fetchconvertcurrencies) [fetchConvertQuote](https://docs.ccxt.com/docs/exchanges/binance#fetchconvertquote) [createConvertTrade](https://docs.ccxt.com/docs/exchanges/binance#createconverttrade) [fetchConvertTrade](https://docs.ccxt.com/docs/exchanges/binance#fetchconverttrade) [fetchConvertTradeHistory](https://docs.ccxt.com/docs/exchanges/binance#fetchconverttradehistory) [fetchFundingIntervals](https://docs.ccxt.com/docs/exchanges/binance#fetchfundingintervals) [fetchLongShortRatioHistory](https://docs.ccxt.com/docs/exchanges/binance#fetchlongshortratiohistory) [fetchADLRank](https://docs.ccxt.com/docs/exchanges/binance#fetchadlrank) [fetchPositionsADLRank](https://docs.ccxt.com/docs/exchanges/binance#fetchpositionsadlrank) [ensureUserDataStreamWsSubscribeSignature](https://docs.ccxt.com/docs/exchanges/binance#ensureuserdatastreamwssubscribesignature) [ensureUserDataStreamWsSubscribeListenToken](https://docs.ccxt.com/docs/exchanges/binance#ensureuserdatastreamwssubscribelistentoken) [watchLiquidations](https://docs.ccxt.com/docs/exchanges/binance#watchliquidations) [watchLiquidationsForSymbols](https://docs.ccxt.com/docs/exchanges/binance#watchliquidationsforsymbols) [watchMyLiquidations](https://docs.ccxt.com/docs/exchanges/binance#watchmyliquidations) [watchMyLiquidationsForSymbols](https://docs.ccxt.com/docs/exchanges/binance#watchmyliquidationsforsymbols) [watchOrderBook](https://docs.ccxt.com/docs/exchanges/binance#watchorderbook) [watchOrderBookForSymbols](https://docs.ccxt.com/docs/exchanges/binance#watchorderbookforsymbols) [unWatchOrderBookForSymbols](https://docs.ccxt.com/docs/exchanges/binance#unwatchorderbookforsymbols) [unWatchOrderBook](https://docs.ccxt.com/docs/exchanges/binance#unwatchorderbook) [fetchOrderBookWs](https://docs.ccxt.com/docs/exchanges/binance#fetchorderbookws) [watchTradesForSymbols](https://docs.ccxt.com/docs/exchanges/binance#watchtradesforsymbols) [unWatchTradesForSymbols](https://docs.ccxt.com/docs/exchanges/binance#unwatchtradesforsymbols) [unWatchTrades](https://docs.ccxt.com/docs/exchanges/binance#unwatchtrades) [watchTrades](https://docs.ccxt.com/docs/exchanges/binance#watchtrades) [watchOHLCV](https://docs.ccxt.com/docs/exchanges/binance#watchohlcv) [watchOHLCVForSymbols](https://docs.ccxt.com/docs/exchanges/binance#watchohlcvforsymbols) [unWatchOHLCVForSymbols](https://docs.ccxt.com/docs/exchanges/binance#unwatchohlcvforsymbols) [unWatchOHLCV](https://docs.ccxt.com/docs/exchanges/binance#unwatchohlcv) [fetchTickerWs](https://docs.ccxt.com/docs/exchanges/binance#fetchtickerws) [fetchOHLCVWs](https://docs.ccxt.com/docs/exchanges/binance#fetchohlcvws) [watchTicker](https://docs.ccxt.com/docs/exchanges/binance#watchticker) [watchMarkPrice](https://docs.ccxt.com/docs/exchanges/binance#watchmarkprice) [watchMarkPrices](https://docs.ccxt.com/docs/exchanges/binance#watchmarkprices) [watchTickers](https://docs.ccxt.com/docs/exchanges/binance#watchtickers) [unWatchTickers](https://docs.ccxt.com/docs/exchanges/binance#unwatchtickers) [unWatchMarkPrices](https://docs.ccxt.com/docs/exchanges/binance#unwatchmarkprices) [unWatchMarkPrice](https://docs.ccxt.com/docs/exchanges/binance#unwatchmarkprice) [unWatchBidsAsks](https://docs.ccxt.com/docs/exchanges/binance#unwatchbidsasks) [unWatchTicker](https://docs.ccxt.com/docs/exchanges/binance#unwatchticker) [watchBidsAsks](https://docs.ccxt.com/docs/exchanges/binance#watchbidsasks) [fetchBalanceWs](https://docs.ccxt.com/docs/exchanges/binance#fetchbalancews) [fetchPositionWs](https://docs.ccxt.com/docs/exchanges/binance#fetchpositionws) [fetchPositionsWs](https://docs.ccxt.com/docs/exchanges/binance#fetchpositionsws) [watchBalance](https://docs.ccxt.com/docs/exchanges/binance#watchbalance) [createOrderWs](https://docs.ccxt.com/docs/exchanges/binance#createorderws) [editOrderWs](https://docs.ccxt.com/docs/exchanges/binance#editorderws) [cancelOrderWs](https://docs.ccxt.com/docs/exchanges/binance#cancelorderws) [cancelAllOrdersWs](https://docs.ccxt.com/docs/exchanges/binance#cancelallordersws) [fetchOrderWs](https://docs.ccxt.com/docs/exchanges/binance#fetchorderws) [fetchOrdersWs](https://docs.ccxt.com/docs/exchanges/binance#fetchordersws) [fetchClosedOrdersWs](https://docs.ccxt.com/docs/exchanges/binance#fetchclosedordersws) [fetchOpenOrdersWs](https://docs.ccxt.com/docs/exchanges/binance#fetchopenordersws) [watchOrders](https://docs.ccxt.com/docs/exchanges/binance#watchorders) [watchPositions](https://docs.ccxt.com/docs/exchanges/binance#watchpositions) [fetchMyTradesWs](https://docs.ccxt.com/docs/exchanges/binance#fetchmytradesws) [fetchTradesWs](https://docs.ccxt.com/docs/exchanges/binance#fetchtradesws) [watchMyTrades](https://docs.ccxt.com/docs/exchanges/binance#watchmytrades)