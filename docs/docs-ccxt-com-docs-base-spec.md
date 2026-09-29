Ask AI

# API Spec by Method

CCXT unified API specification — every method and the exchanges that implement it.

Copy MarkdownOpen

## [addMargin](https://docs.ccxt.com/docs/base-spec\#addmargin)

add margin

**Kind**: instance

**Returns**: `object` \- a [margin structure](https://docs.ccxt.com/docs/manual#add-margin-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol |
| amount | `float` | Yes | amount of margin to add |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges)

- [aster](https://docs.ccxt.com/docs/exchanges/aster#addmargin)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#addmargin)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#addmargin)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#addmargin)
- [delta](https://docs.ccxt.com/docs/exchanges/delta#addmargin)
- [digifinex](https://docs.ccxt.com/docs/exchanges/digifinex#addmargin)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#addmargin)
- [hashkey](https://docs.ccxt.com/docs/exchanges/hashkey#addmargin)
- [hitbtc](https://docs.ccxt.com/docs/exchanges/hitbtc#addmargin)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#addmargin)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#addmargin)
- [lighter](https://docs.ccxt.com/docs/exchanges/lighter#addmargin)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#addmargin)
- [mudrex](https://docs.ccxt.com/docs/exchanges/mudrex#addmargin)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#addmargin)
- [poloniex](https://docs.ccxt.com/docs/exchanges/poloniex#addmargin)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#addmargin)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#addmargin)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#addmargin)
- [xt](https://docs.ccxt.com/docs/exchanges/xt#addmargin)
- [zebpay](https://docs.ccxt.com/docs/exchanges/zebpay#addmargin)

* * *

## [borrowCrossMargin](https://docs.ccxt.com/docs/base-spec\#borrowcrossmargin)

create a loan to borrow margin

**Kind**: instance

**Returns**: `object` \- a [margin loan structure](https://docs.ccxt.com/docs/manual#margin-loan-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| code | `string` | Yes | unified currency code of the currency to borrow |
| amount | `float` | Yes | the amount to borrow |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.portfolioMargin | `boolean` | No | set to true if you would like to borrow margin in a portfolio margin account |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-1)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#borrowcrossmargin)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#borrowcrossmargin)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#borrowcrossmargin)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#borrowcrossmargin)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#borrowcrossmargin)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#borrowcrossmargin)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#borrowcrossmargin)

* * *

## [borrowIsolatedMargin](https://docs.ccxt.com/docs/base-spec\#borrowisolatedmargin)

create a loan to borrow margin

**Kind**: instance

**Returns**: `object` \- a [margin loan structure](https://docs.ccxt.com/docs/manual#margin-loan-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol, required for isolated margin |
| code | `string` | Yes | unified currency code of the currency to borrow |
| amount | `float` | Yes | the amount to borrow |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-2)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#borrowisolatedmargin)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#borrowisolatedmargin)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#borrowisolatedmargin)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#borrowisolatedmargin)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#borrowisolatedmargin)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#borrowisolatedmargin)

* * *

## [calculatePricePrecision](https://docs.ccxt.com/docs/base-spec\#calculatepriceprecision)

Helper function to calculate the Hyperliquid DECIMAL\_PLACES price precision

**Kind**: instance

**Returns**: `int` \- The calculated price precision

| Param | Type | Description |
| --- | --- | --- |
| price | `float` | the price to use in the calculation |
| amountPrecision | `int` | the amountPrecision to use in the calculation |
| maxDecimals | `int` | the maxDecimals to use in the calculation |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-3)

- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#calculatepriceprecision)

* * *

## [cancelAllContractOrders](https://docs.ccxt.com/docs/base-spec\#cancelallcontractorders)

helper method for cancelling all contract orders

**Kind**: instance

**Returns**: Response from the exchange

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol, only orders in the market of this symbol are cancelled when symbol is not undefined |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.trigger | `object` | No | When true, all the trigger orders will be cancelled |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-4)

- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#cancelallcontractorders)

* * *

## [cancelAllOrders](https://docs.ccxt.com/docs/base-spec\#cancelallorders)

cancel all open orders in a market

**Kind**: instance

**Returns**: `Array<object>` \- a list of [order structures](https://docs.ccxt.com/docs/manual#order-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | No | alpaca cancelAllOrders cannot setting symbol, it will cancel all open orders |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-5)

- [alpaca](https://docs.ccxt.com/docs/exchanges/alpaca#cancelallorders)
- [apex](https://docs.ccxt.com/docs/exchanges/apex#cancelallorders)
- [aster](https://docs.ccxt.com/docs/exchanges/aster#cancelallorders)
- [backpack](https://docs.ccxt.com/docs/exchanges/backpack#cancelallorders)
- [bigone](https://docs.ccxt.com/docs/exchanges/bigone#cancelallorders)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#cancelallorders)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#cancelallorders)
- [bitfinex](https://docs.ccxt.com/docs/exchanges/bitfinex#cancelallorders)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#cancelallorders)
- [bitopro](https://docs.ccxt.com/docs/exchanges/bitopro#cancelallorders)
- [bitrue](https://docs.ccxt.com/docs/exchanges/bitrue#cancelallorders)
- [bitso](https://docs.ccxt.com/docs/exchanges/bitso#cancelallorders)
- [bitstamp](https://docs.ccxt.com/docs/exchanges/bitstamp#cancelallorders)
- [bitteam](https://docs.ccxt.com/docs/exchanges/bitteam#cancelallorders)
- [bittrade](https://docs.ccxt.com/docs/exchanges/bittrade#cancelallorders)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#cancelallorders)
- [blockchaincom](https://docs.ccxt.com/docs/exchanges/blockchaincom#cancelallorders)
- [btse](https://docs.ccxt.com/docs/exchanges/btse#cancelallorders)
- [bullish](https://docs.ccxt.com/docs/exchanges/bullish#cancelallorders)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#cancelallorders)
- [bydfi](https://docs.ccxt.com/docs/exchanges/bydfi#cancelallorders)
- [cex](https://docs.ccxt.com/docs/exchanges/cex#cancelallorders)
- [coinbaseexchange](https://docs.ccxt.com/docs/exchanges/coinbaseexchange#cancelallorders)
- [coinbaseinternational](https://docs.ccxt.com/docs/exchanges/coinbaseinternational#cancelallorders)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#cancelallorders)
- [coinsph](https://docs.ccxt.com/docs/exchanges/coinsph#cancelallorders)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#cancelallorders)
- [deepcoin](https://docs.ccxt.com/docs/exchanges/deepcoin#cancelallorders)
- [delta](https://docs.ccxt.com/docs/exchanges/delta#cancelallorders)
- [deribit](https://docs.ccxt.com/docs/exchanges/deribit#cancelallorders)
- [derive](https://docs.ccxt.com/docs/exchanges/derive#cancelallorders)
- [extended](https://docs.ccxt.com/docs/exchanges/extended#cancelallorders)
- [foxbit](https://docs.ccxt.com/docs/exchanges/foxbit#cancelallorders)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#cancelallorders)
- [grvt](https://docs.ccxt.com/docs/exchanges/grvt#cancelallorders)
- [hashkey](https://docs.ccxt.com/docs/exchanges/hashkey#cancelallorders)
- [hibachi](https://docs.ccxt.com/docs/exchanges/hibachi#cancelallorders)
- [hitbtc](https://docs.ccxt.com/docs/exchanges/hitbtc#cancelallorders)
- [hollaex](https://docs.ccxt.com/docs/exchanges/hollaex#cancelallorders)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#cancelallorders)
- [kraken](https://docs.ccxt.com/docs/exchanges/kraken#cancelallorders)
- [krakenfutures](https://docs.ccxt.com/docs/exchanges/krakenfutures#cancelallorders)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#cancelallorders)
- [latoken](https://docs.ccxt.com/docs/exchanges/latoken#cancelallorders)
- [lbank](https://docs.ccxt.com/docs/exchanges/lbank#cancelallorders)
- [lighter](https://docs.ccxt.com/docs/exchanges/lighter#cancelallorders)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#cancelallorders)
- [modetrade](https://docs.ccxt.com/docs/exchanges/modetrade#cancelallorders)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#cancelallorders)
- [ndax](https://docs.ccxt.com/docs/exchanges/ndax#cancelallorders)
- [onetrading](https://docs.ccxt.com/docs/exchanges/onetrading#cancelallorders)
- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#cancelallorders)
- [paradex](https://docs.ccxt.com/docs/exchanges/paradex#cancelallorders)
- [phemex](https://docs.ccxt.com/docs/exchanges/phemex#cancelallorders)
- [poloniex](https://docs.ccxt.com/docs/exchanges/poloniex#cancelallorders)
- [revolutx](https://docs.ccxt.com/docs/exchanges/revolutx#cancelallorders)
- [toobit](https://docs.ccxt.com/docs/exchanges/toobit#cancelallorders)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#cancelallorders)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#cancelallorders)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#cancelallorders)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#cancelallorders)
- [xt](https://docs.ccxt.com/docs/exchanges/xt#cancelallorders)
- [zebpay](https://docs.ccxt.com/docs/exchanges/zebpay#cancelallorders)

* * *

## [cancelAllOrdersAfter](https://docs.ccxt.com/docs/base-spec\#cancelallordersafter)

dead man's switch, cancel all orders after the given timeout

**Kind**: instance

**Returns**: `object` \- the api result

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| timeout | `number` | Yes | time in milliseconds, 0 represents cancel the timer |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.type | `string` | No | spot or swap market |
| params.subType | `string` | No | 'linear' or 'inverse' (default is 'linear'), 'inverse' is not supported |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-6)

- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#cancelallordersafter)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#cancelallordersafter)
- [btse](https://docs.ccxt.com/docs/exchanges/btse#cancelallordersafter)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#cancelallordersafter)
- [extended](https://docs.ccxt.com/docs/exchanges/extended#cancelallordersafter)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#cancelallordersafter)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#cancelallordersafter)
- [kraken](https://docs.ccxt.com/docs/exchanges/kraken#cancelallordersafter)
- [krakenfutures](https://docs.ccxt.com/docs/exchanges/krakenfutures#cancelallordersafter)
- [lighter](https://docs.ccxt.com/docs/exchanges/lighter#cancelallordersafter)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#cancelallordersafter)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#cancelallordersafter)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#cancelallordersafter)

* * *

## [cancelAllOrdersWs](https://docs.ccxt.com/docs/base-spec\#cancelallordersws)

cancel all open orders in a market

**Kind**: instance

**Returns**: `Array<object>` \- a list of [order structures](https://docs.ccxt.com/docs/manual#order-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | No | unified market symbol of the market to cancel orders in |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-7)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#cancelallordersws)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#cancelallordersws)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#cancelallordersws)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#cancelallordersws)
- [lighter](https://docs.ccxt.com/docs/exchanges/lighter#cancelallordersws)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#cancelallordersws)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#cancelallordersws)
- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#cancelallordersws)

* * *

## [cancelAllSpotOrders](https://docs.ccxt.com/docs/base-spec\#cancelallspotorders)

helper method for cancelling all spot orders

**Kind**: instance

**Returns**: Response from the exchange

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol, only orders in the market of this symbol are cancelled when symbol is not undefined |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.trigger | `bool` | No | _invalid for isolated margin_ true if cancelling all stop orders |
| params.marginMode | `string` | No | 'cross' or 'isolated' |
| params.orderIds | `string` | No | _stop orders only_ Comma separated order IDs |
| params.hf | `bool` | No | false, // true for hf order |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-8)

- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#cancelallspotorders)

* * *

## [cancelAllUtaOrders](https://docs.ccxt.com/docs/base-spec\#cancelallutaorders)

helper method for cancelling all uta orders

**Kind**: instance

**Returns**: Response from the exchange

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol, only orders in the market of this symbol are cancelled when symbol is not undefined |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.trigger | `bool` | No | true if cancelling all stop orders |
| params.marginMode | `string` | No | 'CROSS' or 'ISOLATED' |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-9)

- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#cancelallutaorders)

* * *

## [cancelContractOrder](https://docs.ccxt.com/docs/base-spec\#cancelcontractorder)

helper method for cancelling contract orders

**Kind**: instance

**Returns**: `object` \- An [order structure](https://docs.ccxt.com/docs/manual#order-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| id | `string` | Yes | order id |
| symbol | `string` | Yes | unified symbol of the market the order was made in |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.clientOrderId | `string` | No | cancel order by client order id |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-10)

- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#cancelcontractorder)

* * *

## [cancelOrder](https://docs.ccxt.com/docs/base-spec\#cancelorder)

cancels an open order

**Kind**: instance

**Returns**: `object` \- An [order structure](https://docs.ccxt.com/docs/manual#order-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| id | `string` | Yes | order id |
| symbol | `string` | Yes | unified symbol of the market the order was made in |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-11)

- [alpaca](https://docs.ccxt.com/docs/exchanges/alpaca#cancelorder)
- [apex](https://docs.ccxt.com/docs/exchanges/apex#cancelorder)
- [aster](https://docs.ccxt.com/docs/exchanges/aster#cancelorder)
- [backpack](https://docs.ccxt.com/docs/exchanges/backpack#cancelorder)
- [bigone](https://docs.ccxt.com/docs/exchanges/bigone#cancelorder)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#cancelorder)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#cancelorder)
- [bit2c](https://docs.ccxt.com/docs/exchanges/bit2c#cancelorder)
- [bitbank](https://docs.ccxt.com/docs/exchanges/bitbank#cancelorder)
- [bitbns](https://docs.ccxt.com/docs/exchanges/bitbns#cancelorder)
- [bitfinex](https://docs.ccxt.com/docs/exchanges/bitfinex#cancelorder)
- [bitflyer](https://docs.ccxt.com/docs/exchanges/bitflyer#cancelorder)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#cancelorder)
- [bithumb](https://docs.ccxt.com/docs/exchanges/bithumb#cancelorder)
- [bitopro](https://docs.ccxt.com/docs/exchanges/bitopro#cancelorder)
- [bitrue](https://docs.ccxt.com/docs/exchanges/bitrue#cancelorder)
- [bitso](https://docs.ccxt.com/docs/exchanges/bitso#cancelorder)
- [bitstamp](https://docs.ccxt.com/docs/exchanges/bitstamp#cancelorder)
- [bitteam](https://docs.ccxt.com/docs/exchanges/bitteam#cancelorder)
- [bittrade](https://docs.ccxt.com/docs/exchanges/bittrade#cancelorder)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#cancelorder)
- [blockchaincom](https://docs.ccxt.com/docs/exchanges/blockchaincom#cancelorder)
- [blofin](https://docs.ccxt.com/docs/exchanges/blofin#cancelorder)
- [btcbox](https://docs.ccxt.com/docs/exchanges/btcbox#cancelorder)
- [btcmarkets](https://docs.ccxt.com/docs/exchanges/btcmarkets#cancelorder)
- [btcturk](https://docs.ccxt.com/docs/exchanges/btcturk#cancelorder)
- [btse](https://docs.ccxt.com/docs/exchanges/btse#cancelorder)
- [bullish](https://docs.ccxt.com/docs/exchanges/bullish#cancelorder)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#cancelorder)
- [cex](https://docs.ccxt.com/docs/exchanges/cex#cancelorder)
- [coinbase](https://docs.ccxt.com/docs/exchanges/coinbase#cancelorder)
- [coinbaseexchange](https://docs.ccxt.com/docs/exchanges/coinbaseexchange#cancelorder)
- [coinbaseinternational](https://docs.ccxt.com/docs/exchanges/coinbaseinternational#cancelorder)
- [coincheck](https://docs.ccxt.com/docs/exchanges/coincheck#cancelorder)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#cancelorder)
- [coinmate](https://docs.ccxt.com/docs/exchanges/coinmate#cancelorder)
- [coinone](https://docs.ccxt.com/docs/exchanges/coinone#cancelorder)
- [coinsph](https://docs.ccxt.com/docs/exchanges/coinsph#cancelorder)
- [coinspot](https://docs.ccxt.com/docs/exchanges/coinspot#cancelorder)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#cancelorder)
- [cryptomus](https://docs.ccxt.com/docs/exchanges/cryptomus#cancelorder)
- [deepcoin](https://docs.ccxt.com/docs/exchanges/deepcoin#cancelorder)
- [delta](https://docs.ccxt.com/docs/exchanges/delta#cancelorder)
- [deribit](https://docs.ccxt.com/docs/exchanges/deribit#cancelorder)
- [derive](https://docs.ccxt.com/docs/exchanges/derive#cancelorder)
- [digifinex](https://docs.ccxt.com/docs/exchanges/digifinex#cancelorder)
- [dydx](https://docs.ccxt.com/docs/exchanges/dydx#cancelorder)
- [extended](https://docs.ccxt.com/docs/exchanges/extended#cancelorder)
- [foxbit](https://docs.ccxt.com/docs/exchanges/foxbit#cancelorder)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#cancelorder)
- [gemini](https://docs.ccxt.com/docs/exchanges/gemini#cancelorder)
- [grvt](https://docs.ccxt.com/docs/exchanges/grvt#cancelorder)
- [hashkey](https://docs.ccxt.com/docs/exchanges/hashkey#cancelorder)
- [hibachi](https://docs.ccxt.com/docs/exchanges/hibachi#cancelorder)
- [hitbtc](https://docs.ccxt.com/docs/exchanges/hitbtc#cancelorder)
- [hollaex](https://docs.ccxt.com/docs/exchanges/hollaex#cancelorder)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#cancelorder)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#cancelorder)
- [independentreserve](https://docs.ccxt.com/docs/exchanges/independentreserve#cancelorder)
- [indodax](https://docs.ccxt.com/docs/exchanges/indodax#cancelorder)
- [kraken](https://docs.ccxt.com/docs/exchanges/kraken#cancelorder)
- [krakenfutures](https://docs.ccxt.com/docs/exchanges/krakenfutures#cancelorder)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#cancelorder)
- [latoken](https://docs.ccxt.com/docs/exchanges/latoken#cancelorder)
- [lbank](https://docs.ccxt.com/docs/exchanges/lbank#cancelorder)
- [lighter](https://docs.ccxt.com/docs/exchanges/lighter#cancelorder)
- [luno](https://docs.ccxt.com/docs/exchanges/luno#cancelorder)
- [mercado](https://docs.ccxt.com/docs/exchanges/mercado#cancelorder)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#cancelorder)
- [modetrade](https://docs.ccxt.com/docs/exchanges/modetrade#cancelorder)
- [mudrex](https://docs.ccxt.com/docs/exchanges/mudrex#cancelorder)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#cancelorder)
- [ndax](https://docs.ccxt.com/docs/exchanges/ndax#cancelorder)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#cancelorder)
- [onetrading](https://docs.ccxt.com/docs/exchanges/onetrading#cancelorder)
- [p2b](https://docs.ccxt.com/docs/exchanges/p2b#cancelorder)
- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#cancelorder)
- [paradex](https://docs.ccxt.com/docs/exchanges/paradex#cancelorder)
- [paymium](https://docs.ccxt.com/docs/exchanges/paymium#cancelorder)
- [phemex](https://docs.ccxt.com/docs/exchanges/phemex#cancelorder)
- [revolutx](https://docs.ccxt.com/docs/exchanges/revolutx#cancelorder)
- [tokocrypto](https://docs.ccxt.com/docs/exchanges/tokocrypto#cancelorder)
- [toobit](https://docs.ccxt.com/docs/exchanges/toobit#cancelorder)
- [upbit](https://docs.ccxt.com/docs/exchanges/upbit#cancelorder)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#cancelorder)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#cancelorder)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#cancelorder)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#cancelorder)
- [xt](https://docs.ccxt.com/docs/exchanges/xt#cancelorder)
- [zaif](https://docs.ccxt.com/docs/exchanges/zaif#cancelorder)
- [zebpay](https://docs.ccxt.com/docs/exchanges/zebpay#cancelorder)

* * *

## [cancelOrderWs](https://docs.ccxt.com/docs/base-spec\#cancelorderws)

cancel multiple orders

**Kind**: instance

**Returns**: `object` \- an list of [order structures](https://docs.ccxt.com/docs/manual#order-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| id | `string` | Yes | order id |
| symbol | `string` | No | unified market symbol, default is undefined |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.cancelRestrictions | `string`, `undefined` | No | Supported values: ONLY\_NEW - Cancel will succeed if the order status is NEW. ONLY\_PARTIALLY\_FILLED - Cancel will succeed if order status is PARTIALLY\_FILLED. |
| params.trigger | `boolean` | No | set to true if you would like to cancel a conditional order |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-12)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#cancelorderws)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#cancelorderws)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#cancelorderws)
- [cex](https://docs.ccxt.com/docs/exchanges/cex#cancelorderws)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#cancelorderws)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#cancelorderws)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#cancelorderws)
- [lighter](https://docs.ccxt.com/docs/exchanges/lighter#cancelorderws)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#cancelorderws)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#cancelorderws)
- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#cancelorderws)

* * *

## [cancelOrders](https://docs.ccxt.com/docs/base-spec\#cancelorders)

cancel multiple orders

**Kind**: instance

**Returns**: `object` \- an list of [order structures](https://docs.ccxt.com/docs/manual#order-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| ids | `Array<string>` | Yes | order ids |
| symbol | `string` | No | unified market symbol |
| params | `object` | No | extra parameters specific to the exchange API endpoint EXCHANGE SPECIFIC PARAMETERS |
| params.origClientOrderIdList | `Array<string>` | No | max length 10 e.g. \["my\_id\_1","my\_id\_2"\], encode the double quotes. No space after comma |
| params.recvWindow | `Array<int>` | No |  |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-13)

- [aster](https://docs.ccxt.com/docs/exchanges/aster#cancelorders)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#cancelorders)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#cancelorders)
- [bitfinex](https://docs.ccxt.com/docs/exchanges/bitfinex#cancelorders)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#cancelorders)
- [bithumb](https://docs.ccxt.com/docs/exchanges/bithumb#cancelorders)
- [bitopro](https://docs.ccxt.com/docs/exchanges/bitopro#cancelorders)
- [bitso](https://docs.ccxt.com/docs/exchanges/bitso#cancelorders)
- [bittrade](https://docs.ccxt.com/docs/exchanges/bittrade#cancelorders)
- [blofin](https://docs.ccxt.com/docs/exchanges/blofin#cancelorders)
- [btcmarkets](https://docs.ccxt.com/docs/exchanges/btcmarkets#cancelorders)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#cancelorders)
- [coinbase](https://docs.ccxt.com/docs/exchanges/coinbase#cancelorders)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#cancelorders)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#cancelorders)
- [deepcoin](https://docs.ccxt.com/docs/exchanges/deepcoin#cancelorders)
- [digifinex](https://docs.ccxt.com/docs/exchanges/digifinex#cancelorders)
- [dydx](https://docs.ccxt.com/docs/exchanges/dydx#cancelorders)
- [extended](https://docs.ccxt.com/docs/exchanges/extended#cancelorders)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#cancelorders)
- [hashkey](https://docs.ccxt.com/docs/exchanges/hashkey#cancelorders)
- [hibachi](https://docs.ccxt.com/docs/exchanges/hibachi#cancelorders)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#cancelorders)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#cancelorders)
- [kraken](https://docs.ccxt.com/docs/exchanges/kraken#cancelorders)
- [krakenfutures](https://docs.ccxt.com/docs/exchanges/krakenfutures#cancelorders)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#cancelorders)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#cancelorders)
- [modetrade](https://docs.ccxt.com/docs/exchanges/modetrade#cancelorders)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#cancelorders)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#cancelorders)
- [onetrading](https://docs.ccxt.com/docs/exchanges/onetrading#cancelorders)
- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#cancelorders)
- [paradex](https://docs.ccxt.com/docs/exchanges/paradex#cancelorders)
- [toobit](https://docs.ccxt.com/docs/exchanges/toobit#cancelorders)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#cancelorders)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#cancelorders)
- [xt](https://docs.ccxt.com/docs/exchanges/xt#cancelorders)

* * *

## [cancelOrdersForSymbols](https://docs.ccxt.com/docs/base-spec\#cancelordersforsymbols)

cancel multiple orders for multiple symbols

**Kind**: instance

**Returns**: `object` \- an list of [order structures](https://docs.ccxt.com/docs/manual#order-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| orders | `Array<CancellationRequest>` | Yes | list of order ids with symbol, example \[{"id": "a", "symbol": "BTC/USDT"}, {"id": "b", "symbol": "ETH/USDT"}\] |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-14)

- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#cancelordersforsymbols)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#cancelordersforsymbols)
- [digifinex](https://docs.ccxt.com/docs/exchanges/digifinex#cancelordersforsymbols)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#cancelordersforsymbols)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#cancelordersforsymbols)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#cancelordersforsymbols)

* * *

## [cancelOrdersRequest](https://docs.ccxt.com/docs/base-spec\#cancelordersrequest)

build the request payload for cancelling multiple orders

**Kind**: instance

**Returns**: `object` \- the raw request object to be sent to the exchange

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| ids | `Array<string>` | Yes | order ids |
| symbol | `string` | Yes | unified market symbol |
| params | `object` | No |  |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-15)

- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#cancelordersrequest)

* * *

## [cancelOrdersWs](https://docs.ccxt.com/docs/base-spec\#cancelordersws)

cancel multiple orders

**Kind**: instance

**Returns**: `object` \- a list of [order structures](https://docs.ccxt.com/docs/manual#order-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| ids | `Array<string>` | Yes | order ids |
| symbol | `string` | Yes | not used by cancelOrders() |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-16)

- [cex](https://docs.ccxt.com/docs/exchanges/cex#cancelordersws)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#cancelordersws)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#cancelordersws)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#cancelordersws)
- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#cancelordersws)

* * *

## [cancelSpotOrder](https://docs.ccxt.com/docs/base-spec\#cancelspotorder)

helper method for cancelling spot orders

**Kind**: instance

**Returns**: Response from the exchange

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| id | `string` | Yes | order id |
| symbol | `string` | Yes | unified symbol of the market the order was made in |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.trigger | `bool` | No | True if cancelling a stop order |
| params.hf | `bool` | No | false, // true for hf order |
| params.sync | `bool` | No | false, // true to use the hf sync call |
| params.marginMode | `string` | No | 'cross' or 'isolated' |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-17)

- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#cancelspotorder)

* * *

## [cancelTwapOrder](https://docs.ccxt.com/docs/base-spec\#canceltwaporder)

cancels a running twap order

**Kind**: instance

**Returns**: `object` \- An [order structure](https://docs.ccxt.com/docs/manual#order-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| id | `string` | Yes | order id |
| symbol | `string` | Yes | unified symbol of the market the order was made in |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.expiresAfter | `int` | No | time in ms after which the twap order expires |
| params.vaultAddress | `string` | No | the vault address for order |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-18)

- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#canceltwaporder)

* * *

## [cancelUtaOrder](https://docs.ccxt.com/docs/base-spec\#cancelutaorder)

helper method for cancelling uta orders

**Kind**: instance

**Returns**: Response from the exchange

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| id | `string` | Yes | order id |
| symbol | `string` | Yes | unified symbol of the market the order was made in |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.accountMode | `string` | No | 'unified' or 'classic' (default is 'unified') |
| params.clientOrderId | `string` | No | client order id, required if id is not provided |
| params.marginMode | `string` | No | 'cross' or 'isolated', required if fetching a margin order (unified accountMode supports only cross margin) |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-19)

- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#cancelutaorder)

* * *

## [closeAllPositions](https://docs.ccxt.com/docs/base-spec\#closeallpositions)

closes all open positions for a market type

**Kind**: instance

**Returns**: `Array<object>` \- A list of [position structures](https://docs.ccxt.com/docs/manual#position-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.productType | `string` | No | 'USDT-FUTURES', 'USDC-FUTURES', 'COIN-FUTURES', 'SUSDT-FUTURES', 'SUSDC-FUTURES' or 'SCOIN-FUTURES' |
| params.uta | `boolean` | No | set to true for the unified trading account (uta), defaults to false |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-20)

- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#closeallpositions)
- [delta](https://docs.ccxt.com/docs/exchanges/delta#closeallpositions)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#closeallpositions)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#closeallpositions)

* * *

## [closePosition](https://docs.ccxt.com/docs/base-spec\#closeposition)

closes open positions for a market

**Kind**: instance

**Returns**: `object` \- an [order structure](https://docs.ccxt.com/docs/manual#order-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | Unified CCXT market symbol |
| side | `string` | No | not used by bingx |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.positionId | `string`, `undefined` | No | the id of the position you would like to close, only supported for linear swap |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-21)

- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#closeposition)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#closeposition)
- [blofin](https://docs.ccxt.com/docs/exchanges/blofin#closeposition)
- [btse](https://docs.ccxt.com/docs/exchanges/btse#closeposition)
- [coinbase](https://docs.ccxt.com/docs/exchanges/coinbase#closeposition)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#closeposition)
- [deepcoin](https://docs.ccxt.com/docs/exchanges/deepcoin#closeposition)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#closeposition)
- [hitbtc](https://docs.ccxt.com/docs/exchanges/hitbtc#closeposition)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#closeposition)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#closeposition)
- [mudrex](https://docs.ccxt.com/docs/exchanges/mudrex#closeposition)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#closeposition)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#closeposition)
- [zebpay](https://docs.ccxt.com/docs/exchanges/zebpay#closeposition)

* * *

## [closePositions](https://docs.ccxt.com/docs/base-spec\#closepositions)

closes open positions for a market

**Kind**: instance

**Returns**: `Array<object>` \- [a list of position structures](https://docs.ccxt.com/docs/manual#position-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.recvWindow | `string` | No | request valid time window value |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-22)

- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#closepositions)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#closepositions)

* * *

## [createAccount](https://docs.ccxt.com/docs/base-spec\#createaccount)

creates a sub-account under the main account

**Kind**: instance

**Returns**: `object` \- a response object

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| name | `string` | Yes | the name of the sub-account |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.expiresAfter | `int` | No | time in ms after which the sub-account will expire |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-23)

- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#createaccount)

* * *

## [createContractOrder](https://docs.ccxt.com/docs/base-spec\#createcontractorder)

create a trade order on contract market

**Kind**: instance

**Returns**: `object` \- an [order structure](https://docs.ccxt.com/docs/manual#order-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to create an order in |
| type | `string` | Yes | 'market', 'limit', 'OCO', 'PEG', 'TWAP' or 'TRAILING' |
| side | `string` | Yes | 'buy' or 'sell' |
| amount | `float` | Yes | how much of you want to trade in units of the base currency |
| price | `float` | No | the price that the order is to be fulfilled, in units of the quote currency, ignored in market orders |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.clientOrderId | `string` | No | a unique id for the order |
| params.postOnly | `bool` | No | if true, the order will only be posted to the order book and not executed immediately, default is false |
| params.reduceOnly | `bool` | No | if true, the order will only reduce a current position, not increase it, default is false |
| params.timeInForce | `string` | No | 'GTC', 'IOC', 'FOK', 'PO', 'HALFSEC', 'HALFMIN', 'FIVEMIN', 'HOUR', 'TWELVEHOUR', 'DAY', 'WEEK' or 'MONTH' |
| params.hedged | `bool` | No | true for hedged mode, false for one way mode, default is false |
| params.marginMode | `string` | No | 'cross' or 'isolated', default is 'cross' - the exchange does not have cross/isolated margin modes but instead has 'ONE\_WAY', 'HEDGE' and 'ISOLATED' position modes, so this param will be converted to the appropriate position mode |
| params.positionMode | `string` | No | 'ONE\_WAY', 'HEDGE' or 'ISOLATED' - if not provided, it will be derived from the marginMode and hedged params |
| params.triggerPrice | `float` | No | the price that a trigger order is triggered at, same as takeProfitPrice |
| params.stopLossPrice | `float` | No | the price that a stop loss order is triggered at |
| params.takeProfitPrice | `float` | No | the price that a take profit order is triggered at |
| params.triggerPriceType | `string` | No | 'last', 'mark' or 'index', default is 'mark' |
| params.trailingAmount | `float` | No | the quote amount to trail away from the current market price |
| params.trailingPercent | `float` | No | the percent to trail away from the current market price |
| params.takeProfit | `object` | No | _takeProfit object in params_ containing the triggerPrice at which the attached take profit order will be triggered |
| params.takeProfit.triggerPrice | `float` | No | take profit trigger price |
| params.takeProfit.priceType | `string` | No | 'last', 'mark' or 'index', default is 'mark' |
| params.stopLoss | `object` | No | _stopLoss object in params_ containing the triggerPrice at which the attached stop loss order will be triggered |
| params.stopLoss.triggerPrice | `float` | No | stop loss trigger price |
| params.stopLoss.priceType | `string` | No | 'last', 'mark' or 'index', default is 'mark' |
| params.deviation | `float` | No | _PEG orders only_ the offset applied to the pegged reference price |
| params.stealth | `float` | No | _PEG orders only_ the portion of the order size displayed on the book |
| params.stopPrice | `float` | No | _NB - It is NOT the stopLossPrice!!! OCO orders only_ the limit price of the stop loss leg |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-24)

- [btse](https://docs.ccxt.com/docs/exchanges/btse#createcontractorder)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#createcontractorder)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#createcontractorder)

* * *

## [createContractOrders](https://docs.ccxt.com/docs/base-spec\#createcontractorders)

helper method for creating contract orders in batch

**Kind**: instance

**Returns**: `object` \- an [order structure](https://docs.ccxt.com/docs/manual#order-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| orders | `Array` | Yes | list of orders to create, each object should contain the parameters required by createOrder, namely symbol, type, side, amount, price and params |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-25)

- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#createcontractorders)

* * *

## [createConvertTrade](https://docs.ccxt.com/docs/base-spec\#createconverttrade)

convert from one currency to another

**Kind**: instance

**Returns**: `object` \- a [conversion structure](https://docs.ccxt.com/docs/manual#conversion-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| id | `string` | Yes | the id of the trade that you want to make |
| fromCode | `string` | Yes | the currency that you want to sell and convert from |
| toCode | `string` | Yes | the currency that you want to buy and convert into |
| amount | `float` | No | how much you want to trade in units of the from currency |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-26)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#createconverttrade)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#createconverttrade)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#createconverttrade)
- [coinbase](https://docs.ccxt.com/docs/exchanges/coinbase#createconverttrade)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#createconverttrade)
- [phemex](https://docs.ccxt.com/docs/exchanges/phemex#createconverttrade)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#createconverttrade)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#createconverttrade)

* * *

## [createDepositAddress](https://docs.ccxt.com/docs/base-spec\#createdepositaddress)

create a currency deposit address

**Kind**: instance

**Returns**: `object` \- an [address structure](https://docs.ccxt.com/docs/manual#address-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| code | `string` | Yes | unified currency code of the currency for the deposit address |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-27)

- [bitfinex](https://docs.ccxt.com/docs/exchanges/bitfinex#createdepositaddress)
- [bithumb](https://docs.ccxt.com/docs/exchanges/bithumb#createdepositaddress)
- [coinbase](https://docs.ccxt.com/docs/exchanges/coinbase#createdepositaddress)
- [coinbaseexchange](https://docs.ccxt.com/docs/exchanges/coinbaseexchange#createdepositaddress)
- [coinbaseinternational](https://docs.ccxt.com/docs/exchanges/coinbaseinternational#createdepositaddress)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#createdepositaddress)
- [deribit](https://docs.ccxt.com/docs/exchanges/deribit#createdepositaddress)
- [gemini](https://docs.ccxt.com/docs/exchanges/gemini#createdepositaddress)
- [hitbtc](https://docs.ccxt.com/docs/exchanges/hitbtc#createdepositaddress)
- [kraken](https://docs.ccxt.com/docs/exchanges/kraken#createdepositaddress)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#createdepositaddress)
- [luno](https://docs.ccxt.com/docs/exchanges/luno#createdepositaddress)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#createdepositaddress)
- [ndax](https://docs.ccxt.com/docs/exchanges/ndax#createdepositaddress)
- [paymium](https://docs.ccxt.com/docs/exchanges/paymium#createdepositaddress)
- [poloniex](https://docs.ccxt.com/docs/exchanges/poloniex#createdepositaddress)
- [upbit](https://docs.ccxt.com/docs/exchanges/upbit#createdepositaddress)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#createdepositaddress)

* * *

## [createGiftCode](https://docs.ccxt.com/docs/base-spec\#creategiftcode)

create gift code

**Kind**: instance

**Returns**: `object` \- The gift code id, code, currency and amount

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| code | `string` | Yes | gift code |
| amount | `float` | Yes | amount of currency for the gift |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-28)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#creategiftcode)

* * *

## [createMarkeSellOrderWithCost](https://docs.ccxt.com/docs/base-spec\#createmarkesellorderwithcost)

create a market sell order by providing the symbol and cost

**Kind**: instance

**Returns**: `object` \- an [order structure](https://docs.ccxt.com/docs/manual#order-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to create an order in |
| cost | `float` | Yes | how much you want to trade in units of the quote currency |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-29)

- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#createmarkesellorderwithcost)

* * *

## [createMarketBuyOrderWithCost](https://docs.ccxt.com/docs/base-spec\#createmarketbuyorderwithcost)

create a market buy order by providing the symbol and cost

**Kind**: instance

**Returns**: `object` \- an [order structure](https://docs.ccxt.com/docs/manual#order-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to create an order in |
| cost | `float` | Yes | how much you want to trade in units of the quote currency |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-30)

- [alpaca](https://docs.ccxt.com/docs/exchanges/alpaca#createmarketbuyorderwithcost)
- [bigone](https://docs.ccxt.com/docs/exchanges/bigone#createmarketbuyorderwithcost)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#createmarketbuyorderwithcost)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#createmarketbuyorderwithcost)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#createmarketbuyorderwithcost)
- [bithumb](https://docs.ccxt.com/docs/exchanges/bithumb#createmarketbuyorderwithcost)
- [bitrue](https://docs.ccxt.com/docs/exchanges/bitrue#createmarketbuyorderwithcost)
- [bittrade](https://docs.ccxt.com/docs/exchanges/bittrade#createmarketbuyorderwithcost)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#createmarketbuyorderwithcost)
- [coinbase](https://docs.ccxt.com/docs/exchanges/coinbase#createmarketbuyorderwithcost)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#createmarketbuyorderwithcost)
- [deepcoin](https://docs.ccxt.com/docs/exchanges/deepcoin#createmarketbuyorderwithcost)
- [digifinex](https://docs.ccxt.com/docs/exchanges/digifinex#createmarketbuyorderwithcost)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#createmarketbuyorderwithcost)
- [hashkey](https://docs.ccxt.com/docs/exchanges/hashkey#createmarketbuyorderwithcost)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#createmarketbuyorderwithcost)
- [kraken](https://docs.ccxt.com/docs/exchanges/kraken#createmarketbuyorderwithcost)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#createmarketbuyorderwithcost)
- [lbank](https://docs.ccxt.com/docs/exchanges/lbank#createmarketbuyorderwithcost)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#createmarketbuyorderwithcost)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#createmarketbuyorderwithcost)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#createmarketbuyorderwithcost)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#createmarketbuyorderwithcost)
- [xt](https://docs.ccxt.com/docs/exchanges/xt#createmarketbuyorderwithcost)

* * *

## [createMarketOrderWithCost](https://docs.ccxt.com/docs/base-spec\#createmarketorderwithcost)

create a market order by providing the symbol, side and cost

**Kind**: instance

**Returns**: `object` \- an [order structure](https://docs.ccxt.com/docs/manual#order-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to create an order in |
| side | `string` | Yes | 'buy' or 'sell' |
| cost | `float` | Yes | how much you want to trade in units of the quote currency |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-31)

- [alpaca](https://docs.ccxt.com/docs/exchanges/alpaca#createmarketorderwithcost)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#createmarketorderwithcost)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#createmarketorderwithcost)
- [deepcoin](https://docs.ccxt.com/docs/exchanges/deepcoin#createmarketorderwithcost)
- [kraken](https://docs.ccxt.com/docs/exchanges/kraken#createmarketorderwithcost)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#createmarketorderwithcost)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#createmarketorderwithcost)

* * *

## [createMarketSellOrderWithCost](https://docs.ccxt.com/docs/base-spec\#createmarketsellorderwithcost)

create a market sell order by providing the symbol and cost

**Kind**: instance

**Returns**: `object` \- an [order structure](https://docs.ccxt.com/docs/manual#order-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to create an order in |
| cost | `float` | Yes | how much you want to trade in units of the quote currency |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-32)

- [alpaca](https://docs.ccxt.com/docs/exchanges/alpaca#createmarketsellorderwithcost)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#createmarketsellorderwithcost)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#createmarketsellorderwithcost)
- [deepcoin](https://docs.ccxt.com/docs/exchanges/deepcoin#createmarketsellorderwithcost)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#createmarketsellorderwithcost)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#createmarketsellorderwithcost)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#createmarketsellorderwithcost)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#createmarketsellorderwithcost)

* * *

## [createOrder](https://docs.ccxt.com/docs/base-spec\#createorder)

create a trade order

**Kind**: instance

**Returns**: `object` \- an [order structure](https://docs.ccxt.com/docs/manual#order-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to create an order in |
| type | `string` | Yes | 'market', 'limit' or 'stop\_limit' |
| side | `string` | Yes | 'buy' or 'sell' |
| amount | `float` | Yes | how much of currency you want to trade in units of base currency |
| price | `float` | No | the price at which the order is to be fulfilled, in units of the quote currency, ignored in market orders |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.triggerPrice | `float` | No | The price at which a trigger order is triggered at |
| params.timeInForce | `string` | No | 'GTC' or 'IOC', the venue supports only these two for crypto orders, defaults to 'GTC' |
| params.cost | `float` | No | _market orders only_ the cost of the order in units of the quote currency |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-33)

- [alpaca](https://docs.ccxt.com/docs/exchanges/alpaca#createorder)
- [apex](https://docs.ccxt.com/docs/exchanges/apex#createorder)
- [aster](https://docs.ccxt.com/docs/exchanges/aster#createorder)
- [backpack](https://docs.ccxt.com/docs/exchanges/backpack#createorder)
- [bigone](https://docs.ccxt.com/docs/exchanges/bigone#createorder)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#createorder)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#createorder)
- [bit2c](https://docs.ccxt.com/docs/exchanges/bit2c#createorder)
- [bitbank](https://docs.ccxt.com/docs/exchanges/bitbank#createorder)
- [bitbns](https://docs.ccxt.com/docs/exchanges/bitbns#createorder)
- [bitfinex](https://docs.ccxt.com/docs/exchanges/bitfinex#createorder)
- [bitflyer](https://docs.ccxt.com/docs/exchanges/bitflyer#createorder)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#createorder)
- [bithumb](https://docs.ccxt.com/docs/exchanges/bithumb#createorder)
- [bitopro](https://docs.ccxt.com/docs/exchanges/bitopro#createorder)
- [bitrue](https://docs.ccxt.com/docs/exchanges/bitrue#createorder)
- [bitso](https://docs.ccxt.com/docs/exchanges/bitso#createorder)
- [bitstamp](https://docs.ccxt.com/docs/exchanges/bitstamp#createorder)
- [bitteam](https://docs.ccxt.com/docs/exchanges/bitteam#createorder)
- [bittrade](https://docs.ccxt.com/docs/exchanges/bittrade#createorder)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#createorder)
- [blockchaincom](https://docs.ccxt.com/docs/exchanges/blockchaincom#createorder)
- [blofin](https://docs.ccxt.com/docs/exchanges/blofin#createorder)
- [btcbox](https://docs.ccxt.com/docs/exchanges/btcbox#createorder)
- [btcmarkets](https://docs.ccxt.com/docs/exchanges/btcmarkets#createorder)
- [btcturk](https://docs.ccxt.com/docs/exchanges/btcturk#createorder)
- [btse](https://docs.ccxt.com/docs/exchanges/btse#createorder)
- [bullish](https://docs.ccxt.com/docs/exchanges/bullish#createorder)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#createorder)
- [bydfi](https://docs.ccxt.com/docs/exchanges/bydfi#createorder)
- [cex](https://docs.ccxt.com/docs/exchanges/cex#createorder)
- [coinbase](https://docs.ccxt.com/docs/exchanges/coinbase#createorder)
- [coinbaseexchange](https://docs.ccxt.com/docs/exchanges/coinbaseexchange#createorder)
- [coinbaseinternational](https://docs.ccxt.com/docs/exchanges/coinbaseinternational#createorder)
- [coincheck](https://docs.ccxt.com/docs/exchanges/coincheck#createorder)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#createorder)
- [coinmate](https://docs.ccxt.com/docs/exchanges/coinmate#createorder)
- [coinone](https://docs.ccxt.com/docs/exchanges/coinone#createorder)
- [coinsph](https://docs.ccxt.com/docs/exchanges/coinsph#createorder)
- [coinspot](https://docs.ccxt.com/docs/exchanges/coinspot#createorder)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#createorder)
- [cryptomus](https://docs.ccxt.com/docs/exchanges/cryptomus#createorder)
- [deepcoin](https://docs.ccxt.com/docs/exchanges/deepcoin#createorder)
- [delta](https://docs.ccxt.com/docs/exchanges/delta#createorder)
- [deribit](https://docs.ccxt.com/docs/exchanges/deribit#createorder)
- [derive](https://docs.ccxt.com/docs/exchanges/derive#createorder)
- [digifinex](https://docs.ccxt.com/docs/exchanges/digifinex#createorder)
- [dydx](https://docs.ccxt.com/docs/exchanges/dydx#createorder)
- [extended](https://docs.ccxt.com/docs/exchanges/extended#createorder)
- [foxbit](https://docs.ccxt.com/docs/exchanges/foxbit#createorder)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#createorder)
- [gemini](https://docs.ccxt.com/docs/exchanges/gemini#createorder)
- [grvt](https://docs.ccxt.com/docs/exchanges/grvt#createorder)
- [hashkey](https://docs.ccxt.com/docs/exchanges/hashkey#createorder)
- [hibachi](https://docs.ccxt.com/docs/exchanges/hibachi#createorder)
- [hitbtc](https://docs.ccxt.com/docs/exchanges/hitbtc#createorder)
- [hollaex](https://docs.ccxt.com/docs/exchanges/hollaex#createorder)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#createorder)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#createorder)
- [independentreserve](https://docs.ccxt.com/docs/exchanges/independentreserve#createorder)
- [indodax](https://docs.ccxt.com/docs/exchanges/indodax#createorder)
- [kraken](https://docs.ccxt.com/docs/exchanges/kraken#createorder)
- [krakenfutures](https://docs.ccxt.com/docs/exchanges/krakenfutures#createorder)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#createorder)
- [latoken](https://docs.ccxt.com/docs/exchanges/latoken#createorder)
- [lbank](https://docs.ccxt.com/docs/exchanges/lbank#createorder)
- [lighter](https://docs.ccxt.com/docs/exchanges/lighter#createorder)
- [luno](https://docs.ccxt.com/docs/exchanges/luno#createorder)
- [mercado](https://docs.ccxt.com/docs/exchanges/mercado#createorder)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#createorder)
- [modetrade](https://docs.ccxt.com/docs/exchanges/modetrade#createorder)
- [mudrex](https://docs.ccxt.com/docs/exchanges/mudrex#createorder)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#createorder)
- [ndax](https://docs.ccxt.com/docs/exchanges/ndax#createorder)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#createorder)
- [onetrading](https://docs.ccxt.com/docs/exchanges/onetrading#createorder)
- [p2b](https://docs.ccxt.com/docs/exchanges/p2b#createorder)
- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#createorder)
- [paradex](https://docs.ccxt.com/docs/exchanges/paradex#createorder)
- [paymium](https://docs.ccxt.com/docs/exchanges/paymium#createorder)
- [phemex](https://docs.ccxt.com/docs/exchanges/phemex#createorder)
- [poloniex](https://docs.ccxt.com/docs/exchanges/poloniex#createorder)
- [revolutx](https://docs.ccxt.com/docs/exchanges/revolutx#createorder)
- [tokocrypto](https://docs.ccxt.com/docs/exchanges/tokocrypto#createorder)
- [toobit](https://docs.ccxt.com/docs/exchanges/toobit#createorder)
- [upbit](https://docs.ccxt.com/docs/exchanges/upbit#createorder)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#createorder)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#createorder)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#createorder)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#createorder)
- [xt](https://docs.ccxt.com/docs/exchanges/xt#createorder)
- [zaif](https://docs.ccxt.com/docs/exchanges/zaif#createorder)
- [zebpay](https://docs.ccxt.com/docs/exchanges/zebpay#createorder)

* * *

## [createOrderWs](https://docs.ccxt.com/docs/base-spec\#createorderws)

create a trade order

**Kind**: instance

**Returns**: `object` \- an [order structure](https://docs.ccxt.com/docs/manual#order-structure)

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

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-34)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#createorderws)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#createorderws)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#createorderws)
- [cex](https://docs.ccxt.com/docs/exchanges/cex#createorderws)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#createorderws)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#createorderws)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#createorderws)
- [lighter](https://docs.ccxt.com/docs/exchanges/lighter#createorderws)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#createorderws)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#createorderws)
- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#createorderws)

* * *

## [createOrders](https://docs.ccxt.com/docs/base-spec\#createorders)

create a list of trade orders

**Kind**: instance

**Returns**: `object` \- an [order structure](https://docs.ccxt.com/docs/manual#order-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| orders | `Array` | Yes | list of orders to create, each object should contain the parameters required by createOrder, namely symbol, type, side, amount, price and params |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-35)

- [aster](https://docs.ccxt.com/docs/exchanges/aster#createorders)
- [backpack](https://docs.ccxt.com/docs/exchanges/backpack#createorders)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#createorders)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#createorders)
- [bitfinex](https://docs.ccxt.com/docs/exchanges/bitfinex#createorders)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#createorders)
- [bithumb](https://docs.ccxt.com/docs/exchanges/bithumb#createorders)
- [blofin](https://docs.ccxt.com/docs/exchanges/blofin#createorders)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#createorders)
- [bydfi](https://docs.ccxt.com/docs/exchanges/bydfi#createorders)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#createorders)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#createorders)
- [digifinex](https://docs.ccxt.com/docs/exchanges/digifinex#createorders)
- [foxbit](https://docs.ccxt.com/docs/exchanges/foxbit#createorders)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#createorders)
- [hashkey](https://docs.ccxt.com/docs/exchanges/hashkey#createorders)
- [hibachi](https://docs.ccxt.com/docs/exchanges/hibachi#createorders)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#createorders)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#createorders)
- [kraken](https://docs.ccxt.com/docs/exchanges/kraken#createorders)
- [krakenfutures](https://docs.ccxt.com/docs/exchanges/krakenfutures#createorders)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#createorders)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#createorders)
- [modetrade](https://docs.ccxt.com/docs/exchanges/modetrade#createorders)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#createorders)
- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#createorders)
- [paradex](https://docs.ccxt.com/docs/exchanges/paradex#createorders)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#createorders)

* * *

## [createOrdersRequest](https://docs.ccxt.com/docs/base-spec\#createordersrequest)

create a list of trade orders

**Kind**: instance

**Returns**: `object` \- an [order structure](https://docs.ccxt.com/docs/manual#order-structure)

| Param | Type | Description |
| --- | --- | --- |
| orders | `Array` | list of orders to create, each object should contain the parameters required by createOrder, namely symbol, type, side, amount, price and params |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-36)

- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#createordersrequest)

* * *

## [createOrdersWs](https://docs.ccxt.com/docs/base-spec\#createordersws)

create a list of trade orders

**Kind**: instance

**Returns**: `object` \- an [order structure](https://docs.ccxt.com/docs/manual#order-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| orders | `Array` | Yes | list of orders to create, each object should contain the parameters required by createOrder, namely symbol, type, side, amount, price and params |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-37)

- [gate](https://docs.ccxt.com/docs/exchanges/gate#createordersws)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#createordersws)

* * *

## [createSpotOrder](https://docs.ccxt.com/docs/base-spec\#createspotorder)

create a trade order on spot market

**Kind**: instance

**Returns**: `object` \- an [order structure](https://docs.ccxt.com/docs/manual#order-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to create an order in |
| type | `string` | Yes | 'market', 'limit', 'OCO', 'PEG', 'TWAP' or 'TRAILING' |
| side | `string` | Yes | 'buy' or 'sell' |
| amount | `float` | Yes | how much of you want to trade in units of the base currency |
| price | `float` | No | the price that the order is to be fulfilled, in units of the quote currency, ignored in market orders |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.clientOrderId | `string` | No | a unique id for the order |
| params.postOnly | `bool` | No | if true, the order will only be posted to the order book and not executed immediately, default is false |
| params.timeInForce | `string` | No | 'GTC', 'IOC' or 'FOK' |
| params.cost | `float` | No | _market buy and trailing buy orders only_ the quote quantity that can be used as an alternative for the amount |
| params.triggerPrice | `float` | No | the price that a trigger order is triggered at, same as takeProfitPrice |
| params.stopLossPrice | `float` | No | the price that a stop loss order is triggered at |
| params.takeProfitPrice | `float` | No | the price that a take profit order is triggered at |
| params.triggerPriceType | `string` | No | 'last', 'mark' or 'index', default is 'last' |
| params.trailingAmount | `float` | No | the quote amount to trail away from the current market price |
| params.trailingPercent | `float` | No | the percent to trail away from the current market price |
| params.deviation | `float` | No | _PEG orders only_ how much should the order price deviate from the pegged price, in percent from -10 to 10 |
| params.stealth | `float` | No | _PEG orders only_ how many percent of the order is to be displayed on the orderbook, from 1 to 100 |
| params.stopPrice | `float` | No | _NB - It is NOT stopLossPrice or triggerPrice!!! OCO orders only_ the limit price of the stop loss leg |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-38)

- [btse](https://docs.ccxt.com/docs/exchanges/btse#createspotorder)
- [hashkey](https://docs.ccxt.com/docs/exchanges/hashkey#createspotorder)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#createspotorder)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#createspotorder)

* * *

## [createSpotOrders](https://docs.ccxt.com/docs/base-spec\#createspotorders)

helper method for creating spot orders in batch

**Kind**: instance

**Returns**: `object` \- an [order structure](https://docs.ccxt.com/docs/manual#order-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| orders | `Array` | Yes | list of orders to create, each object should contain the parameters required by createOrder, namely symbol, type, side, amount, price and params |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.hf | `bool` | No | false, // true for hf orders |
| params.sync | `bool` | No | false, // true to use the hf sync call |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-39)

- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#createspotorders)

* * *

## [createSubAccount](https://docs.ccxt.com/docs/base-spec\#createsubaccount)

creates a sub-account under the main account

**Kind**: instance

**Returns**: `object` \- a response object

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| name | `string` | Yes | unused argument |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.expiryWindow | `int` | No | time to live in milliseconds |
| params.subAccountAddress | `string` | No | The public key (address) of the sub-account to use for creation |
| params.subAccountPrivateKey | `string` | No | The private key of the sub-account to use for creation |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-40)

- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#createsubaccount)

* * *

## [createSwapOrder](https://docs.ccxt.com/docs/base-spec\#createswaporder)

create a trade order on swap market

**Kind**: instance

**Returns**: `object` \- an [order structure](https://docs.ccxt.com/docs/manual#order-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to create an order in |
| type | `string` | Yes | 'market' or 'limit' or 'STOP' |
| side | `string` | Yes | 'buy' or 'sell' |
| amount | `float` | Yes | how much of you want to trade in units of the base currency |
| price | `float` | No | the price that the order is to be fulfilled, in units of the quote currency, ignored in market orders |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.postOnly | `bool` | No | if true, the order will only be posted to the order book and not executed immediately |
| params.reduceOnly | `bool` | No | true or false whether the order is reduce only |
| params.triggerPrice | `float` | No | The price at which a trigger order is triggered at |
| params.timeInForce | `string` | No | 'GTC', 'FOK', 'IOC', 'LIMIT\_MAKER' or 'PO' |
| params.clientOrderId | `string` | No | a unique id for the order |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-41)

- [hashkey](https://docs.ccxt.com/docs/exchanges/hashkey#createswaporder)

* * *

## [createTrailingAmountOrder](https://docs.ccxt.com/docs/base-spec\#createtrailingamountorder)

create a trailing order by providing the symbol, type, side, amount, price and trailingAmount

**Kind**: instance

**Returns**: `object` \- an [order structure](https://docs.ccxt.com/docs/manual#order-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to create an order in |
| type | `string` | Yes | 'market' or 'limit' |
| side | `string` | Yes | 'buy' or 'sell' |
| amount | `float` | Yes | how much you want to trade in units of the base currency, or number of contracts |
| price | `float` | No | the price for the order to be filled at, in units of the quote currency, ignored in market orders |
| trailingAmount | `float` | Yes | the quote amount to trail away from the current market price |
| trailingTriggerPrice | `float` | Yes | the price to activate a trailing order, default uses the price argument |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-42)

- [woo](https://docs.ccxt.com/docs/exchanges/woo#createtrailingamountorder)

* * *

## [createTrailingPercentOrder](https://docs.ccxt.com/docs/base-spec\#createtrailingpercentorder)

create a trailing order by providing the symbol, type, side, amount, price and trailingPercent

**Kind**: instance

**Returns**: `object` \- an [order structure](https://docs.ccxt.com/docs/manual#order-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to create an order in |
| type | `string` | Yes | 'market' or 'limit' |
| side | `string` | Yes | 'buy' or 'sell' |
| amount | `float` | Yes | how much you want to trade in units of the base currency, or number of contracts |
| price | `float` | No | the price for the order to be filled at, in units of the quote currency, ignored in market orders |
| trailingPercent | `float` | Yes | the percent to trail away from the current market price |
| trailingTriggerPrice | `float` | Yes | the price to activate a trailing order, default uses the price argument |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-43)

- [htx](https://docs.ccxt.com/docs/exchanges/htx#createtrailingpercentorder)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#createtrailingpercentorder)

* * *

## [createTwapOrder](https://docs.ccxt.com/docs/base-spec\#createtwaporder)

create a trade order that is executed as a TWAP order over a specified duration.

**Kind**: instance

**Returns**: `object` \- an [order structure](https://docs.ccxt.com/docs/manual#order-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to create an order in |
| side | `string` | Yes | 'buy' or 'sell' |
| amount | `float` | Yes | how much of currency you want to trade in units of base currency, only required for sale |
| duration | `int` | Yes | the duration of the TWAP order in milliseconds |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.frequency | `string` | Yes | required order interval in seconds, 15, 20, 30, 60 or 120 |
| params.price | `string` | No | order price, required for purchase |
| params.generation | `int` | No | _only generation 2 is supported_ if you want to use the API generation 1 or 2, default is 2 |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-44)

- [bithumb](https://docs.ccxt.com/docs/exchanges/bithumb#createtwaporder)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#createtwaporder)

* * *

## [createUtaOrder](https://docs.ccxt.com/docs/base-spec\#createutaorder)

helper method for creating uta orders

**Kind**: instance

**Returns**: `object` \- an [order structure](https://docs.ccxt.com/docs/manual#order-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | Unified CCXT market symbol |
| type | `string` | Yes | 'limit' or 'market' |
| side | `string` | Yes | 'buy' or 'sell' |
| amount | `float` | Yes | the amount of currency to trade |
| price | `float` | No | the price at which the order is to be fulfilled, in units of the quote currency, ignored in market orders |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.clientOrderId | `string` | No | client order id, defaults to uuid if not passed |
| params.cost | `float` | No | the cost of the order in units of quote currency |
| params.timeInForce | `string` | No | GTC, GTD, IOC, FOK or PO |
| params.postOnly | `bool` | No | Post only flag, invalid when timeInForce is IOC or FOK (default is false) |
| params.reduceOnly | `bool` | No | _contract markets only_ A mark to reduce the position size only. Set to false by default |
| params.triggerPrice | `float` | No | The price a trigger order is triggered at |
| params.triggerDirection | `string` | No | 'ascending' or 'descending', the direction the triggerPrice is triggered from, requires triggerPrice |
| params.triggerPriceType | `string` | No | _contract markets only_ "last", "mark", "index" - defaults to "mark" |
| params.stopLossPrice | `float` | No | price to trigger stop-loss orders |
| params.takeProfitPrice | `float` | No | price to trigger take-profit orders |
| params.marginMode | `string` | No | 'cross' or 'isolated', (default is 'cross' for margin orders, default is 'isolated' for contract orders) Exchange-specific parameters ------------------------------------------------- |
| params.accountMode | `string` | No | 'unified' or 'classic', default is 'unified' |
| params.stp | `string` | No | '', // self trade prevention, CN, CO, CB or DC |
| params.cancelAfter | `int` | No | Cancel After N Seconds (Calculated from the time of entering the matching engine), only effective when timeInForce is GTD |
| params.sizeUnit | `string` | No | _contracts only_ 'BASECCY' (amount of base currency) or 'UNIT' (number of contracts), default is 'UNIT' Classic account parameters |
| params.autoBorrow | `bool` | No | _classic margin orders only_ |
| params.autoRepay | `bool` | No | _classic margin orders only_ |
| params.hedged | `string` | No | _classic contract orders only_ true for hedged mode, false for one way mode, default is false |
| params.leverage | `int` | No | _classic contract orders with isolated marginMode only_ Leverage size of the order |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-45)

- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#createutaorder)

* * *

## [createVault](https://docs.ccxt.com/docs/base-spec\#createvault)

creates a value

**Kind**: instance

**Returns**: `object` \- the api result

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| name | `string` | Yes | The name of the vault |
| description | `string` | Yes | The description of the vault |
| initialUsd | `number` | Yes | The initialUsd of the vault |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-46)

- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#createvault)

* * *

## [deposit](https://docs.ccxt.com/docs/base-spec\#deposit)

make a deposit

**Kind**: instance

**Returns**: `object` \- a [transaction structure](https://docs.ccxt.com/docs/manual#transaction-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| code | `string` | Yes | unified currency code |
| amount | `float` | Yes | the amount to deposit |
| id | `string` | Yes | the payment method id to be used for the deposit, can be retrieved from v2PrivateGetPaymentMethods |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.accountId | `string` | No | the id of the account to deposit into |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-47)

- [coinbase](https://docs.ccxt.com/docs/exchanges/coinbase#deposit)

* * *

## [editContractOrder](https://docs.ccxt.com/docs/base-spec\#editcontractorder)

edit a trade order

**Kind**: instance

**Returns**: `object` \- an [order structure](https://docs.ccxt.com/docs/manual#order-structure)

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

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-48)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#editcontractorder)

* * *

## [editOrder](https://docs.ccxt.com/docs/base-spec\#editorder)

edit a trade order

**Kind**: instance

**Returns**: `object` \- an [order structure](https://docs.ccxt.com/docs/manual#order-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| id | `string` | Yes | order id |
| symbol | `string` | No | unified symbol of the market to create an order in |
| type | `string` | No | 'market', 'limit' or 'stop\_limit' |
| side | `string` | No | 'buy' or 'sell' |
| amount | `float` | No | how much of the currency you want to trade in units of the base currency |
| price | `float` | No | the price for the order, in units of the quote currency, ignored in market orders |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.triggerPrice | `string` | No | the price to trigger a stop order |
| params.timeInForce | `string` | No | 'GTC' or 'IOC', the venue supports only these two for crypto orders, defaults to 'GTC' |
| params.clientOrderId | `string` | No | a unique identifier for the order, automatically generated if not sent |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-49)

- [alpaca](https://docs.ccxt.com/docs/exchanges/alpaca#editorder)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#editorder)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#editorder)
- [bitfinex](https://docs.ccxt.com/docs/exchanges/bitfinex#editorder)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#editorder)
- [bitstamp](https://docs.ccxt.com/docs/exchanges/bitstamp#editorder)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#editorder)
- [btse](https://docs.ccxt.com/docs/exchanges/btse#editorder)
- [bullish](https://docs.ccxt.com/docs/exchanges/bullish#editorder)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#editorder)
- [bydfi](https://docs.ccxt.com/docs/exchanges/bydfi#editorder)
- [coinbase](https://docs.ccxt.com/docs/exchanges/coinbase#editorder)
- [coinbaseinternational](https://docs.ccxt.com/docs/exchanges/coinbaseinternational#editorder)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#editorder)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#editorder)
- [deepcoin](https://docs.ccxt.com/docs/exchanges/deepcoin#editorder)
- [delta](https://docs.ccxt.com/docs/exchanges/delta#editorder)
- [deribit](https://docs.ccxt.com/docs/exchanges/deribit#editorder)
- [derive](https://docs.ccxt.com/docs/exchanges/derive#editorder)
- [extended](https://docs.ccxt.com/docs/exchanges/extended#editorder)
- [foxbit](https://docs.ccxt.com/docs/exchanges/foxbit#editorder)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#editorder)
- [hibachi](https://docs.ccxt.com/docs/exchanges/hibachi#editorder)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#editorder)
- [kraken](https://docs.ccxt.com/docs/exchanges/kraken#editorder)
- [krakenfutures](https://docs.ccxt.com/docs/exchanges/krakenfutures#editorder)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#editorder)
- [lighter](https://docs.ccxt.com/docs/exchanges/lighter#editorder)
- [modetrade](https://docs.ccxt.com/docs/exchanges/modetrade#editorder)
- [mudrex](https://docs.ccxt.com/docs/exchanges/mudrex#editorder)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#editorder)
- [ndax](https://docs.ccxt.com/docs/exchanges/ndax#editorder)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#editorder)
- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#editorder)
- [paradex](https://docs.ccxt.com/docs/exchanges/paradex#editorder)
- [phemex](https://docs.ccxt.com/docs/exchanges/phemex#editorder)
- [poloniex](https://docs.ccxt.com/docs/exchanges/poloniex#editorder)
- [revolutx](https://docs.ccxt.com/docs/exchanges/revolutx#editorder)
- [upbit](https://docs.ccxt.com/docs/exchanges/upbit#editorder)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#editorder)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#editorder)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#editorder)
- [xt](https://docs.ccxt.com/docs/exchanges/xt#editorder)

* * *

## [editOrderWs](https://docs.ccxt.com/docs/base-spec\#editorderws)

edit a trade order

**Kind**: instance

**Returns**: `object` \- an [order structure](https://docs.ccxt.com/docs/manual#order-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| id | `string` | Yes | order id |
| symbol | `string` | Yes | unified symbol of the market to create an order in |
| type | `string` | Yes | 'market' or 'limit' |
| side | `string` | Yes | 'buy' or 'sell' |
| amount | `float` | Yes | how much of the currency you want to trade in units of the base currency |
| price | `float`, `undefined` | No | the price at which the order is to be fulfilled, in units of the quote currency, ignored in market orders |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-50)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#editorderws)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#editorderws)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#editorderws)
- [cex](https://docs.ccxt.com/docs/exchanges/cex#editorderws)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#editorderws)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#editorderws)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#editorderws)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#editorderws)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#editorderws)
- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#editorderws)

* * *

## [editOrders](https://docs.ccxt.com/docs/base-spec\#editorders)

edit a list of trade orders

**Kind**: instance

**Returns**: `object` \- an [order structure](https://docs.ccxt.com/docs/manual#order-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| orders | `Array` | Yes | list of orders to create, each object should contain the parameters required by createOrder, namely symbol, type, side, amount, price and params |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-51)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#editorders)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#editorders)
- [bydfi](https://docs.ccxt.com/docs/exchanges/bydfi#editorders)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#editorders)
- [hibachi](https://docs.ccxt.com/docs/exchanges/hibachi#editorders)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#editorders)

* * *

## [enableDemoTrading](https://docs.ccxt.com/docs/base-spec\#enabledemotrading)

enables or disables demo trading mode

**Kind**: instance

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| enable | `boolean` | No | true if demo trading should be enabled, false otherwise |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-52)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#enabledemotrading)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#enabledemotrading)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#enabledemotrading)

* * *

## [enableUserDexAbstraction](https://docs.ccxt.com/docs/base-spec\#enableuserdexabstraction)

If set, actions on HIP-3 perps will automatically transfer collateral from validator-operated USDC perps balance for HIP-3 DEXs where USDC is the collateral token, and spot otherwise

**Kind**: instance

**Returns**: dictionary response from the exchange

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| enabled | `boolean` | Yes | whether to enable user dex abstraction |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.type | `string` | No | 'userDexAbstraction' or 'agentEnableDexAbstraction' default is 'userDexAbstraction' |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-53)

- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#enableuserdexabstraction)

* * *

## [fetchADLRank](https://docs.ccxt.com/docs/base-spec\#fetchadlrank)

fetches the auto deleveraging rank and risk percentage for a symbol

**Kind**: instance

**Returns**: `object` \- an [auto de leverage structure](https://docs.ccxt.com/docs/manual#auto-de-leverage-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to fetch the auto deleveraging rank for |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-54)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchadlrank)

* * *

## [fetchAccount](https://docs.ccxt.com/docs/base-spec\#fetchaccount)

query for balance and get the amount of funds available for trading or funds locked in orders

**Kind**: instance

**Returns**: `object` \- a [balance structure](https://docs.ccxt.com/docs/manual#balance-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-55)

- [apex](https://docs.ccxt.com/docs/exchanges/apex#fetchaccount)
- [extended](https://docs.ccxt.com/docs/exchanges/extended#fetchaccount)

* * *

## [fetchAccountIdByType](https://docs.ccxt.com/docs/base-spec\#fetchaccountidbytype)

fetch all the accounts by a type and marginModeassociated with a profile

**Kind**: instance

**Returns**: `object` \- a dictionary of [account structures](https://docs.ccxt.com/docs/manual#account-structure) indexed by the account type

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| type | `string` | Yes | 'spot', 'swap' or 'future |
| marginMode | `string` | No | 'cross' or 'isolated' |
| symbol | `string` | No | unified ccxt market symbol |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-56)

- [htx](https://docs.ccxt.com/docs/exchanges/htx#fetchaccountidbytype)

* * *

## [fetchAccountSettings](https://docs.ccxt.com/docs/base-spec\#fetchaccountsettings)

fetch account's market settings. Settings are cached for walletAddress. To refresh the cache, call loadAccountSettings with refresh=true

**Kind**: instance

**Returns**: `object` \- Dict repacked from list by symbol key

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.account | `string` | No | will default to walletAddress if not provided |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-57)

- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#fetchaccountsettings)

* * *

## [fetchAccounts](https://docs.ccxt.com/docs/base-spec\#fetchaccounts)

fetch all the accounts associated with a profile

**Kind**: instance

**Returns**: `object` \- a dictionary of [account structures](https://docs.ccxt.com/docs/manual#account-structure) indexed by the account type

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-58)

- [bittrade](https://docs.ccxt.com/docs/exchanges/bittrade#fetchaccounts)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#fetchaccounts)
- [bullish](https://docs.ccxt.com/docs/exchanges/bullish#fetchaccounts)
- [coinbase](https://docs.ccxt.com/docs/exchanges/coinbase#fetchaccounts)
- [coinbaseexchange](https://docs.ccxt.com/docs/exchanges/coinbaseexchange#fetchaccounts)
- [coinbaseinternational](https://docs.ccxt.com/docs/exchanges/coinbaseinternational#fetchaccounts)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#fetchaccounts)
- [deribit](https://docs.ccxt.com/docs/exchanges/deribit#fetchaccounts)
- [dydx](https://docs.ccxt.com/docs/exchanges/dydx#fetchaccounts)
- [extended](https://docs.ccxt.com/docs/exchanges/extended#fetchaccounts)
- [hashkey](https://docs.ccxt.com/docs/exchanges/hashkey#fetchaccounts)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#fetchaccounts)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchaccounts)
- [lighter](https://docs.ccxt.com/docs/exchanges/lighter#fetchaccounts)
- [luno](https://docs.ccxt.com/docs/exchanges/luno#fetchaccounts)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#fetchaccounts)
- [ndax](https://docs.ccxt.com/docs/exchanges/ndax#fetchaccounts)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchaccounts)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#fetchaccounts)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#fetchaccounts)

* * *

## [fetchAllGreeks](https://docs.ccxt.com/docs/base-spec\#fetchallgreeks)

fetches all option contracts greeks, financial metrics used to measure the factors that affect the price of an options contract

**Kind**: instance

**Returns**: `object` \- a dictionary of [greeks structures](https://docs.ccxt.com/docs/manual#greeks-structure) indexed by market symbol

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>` | No | unified symbols of the markets to fetch greeks for, all markets are returned if not assigned |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-59)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchallgreeks)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchallgreeks)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchallgreeks)
- [paradex](https://docs.ccxt.com/docs/exchanges/paradex#fetchallgreeks)

* * *

## [fetchBalance](https://docs.ccxt.com/docs/base-spec\#fetchbalance)

query for balance and get the amount of funds available for trading or funds locked in orders

**Kind**: instance

**Returns**: `object` \- a [balance structure](https://docs.ccxt.com/docs/manual#balance-structure). note that `info` is
the composite `{ account, positions }` wrapper of both raw venue payloads, not the bare account payload it was
before crypto positions were included — read `info['account']['cash']` where `info['cash']` used to be read

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-60)

- [alpaca](https://docs.ccxt.com/docs/exchanges/alpaca#fetchbalance)
- [apex](https://docs.ccxt.com/docs/exchanges/apex#fetchbalance)
- [aster](https://docs.ccxt.com/docs/exchanges/aster#fetchbalance)
- [backpack](https://docs.ccxt.com/docs/exchanges/backpack#fetchbalance)
- [bigone](https://docs.ccxt.com/docs/exchanges/bigone#fetchbalance)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchbalance)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#fetchbalance)
- [bit2c](https://docs.ccxt.com/docs/exchanges/bit2c#fetchbalance)
- [bitbank](https://docs.ccxt.com/docs/exchanges/bitbank#fetchbalance)
- [bitbns](https://docs.ccxt.com/docs/exchanges/bitbns#fetchbalance)
- [bitfinex](https://docs.ccxt.com/docs/exchanges/bitfinex#fetchbalance)
- [bitflyer](https://docs.ccxt.com/docs/exchanges/bitflyer#fetchbalance)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#fetchbalance)
- [bithumb](https://docs.ccxt.com/docs/exchanges/bithumb#fetchbalance)
- [bitopro](https://docs.ccxt.com/docs/exchanges/bitopro#fetchbalance)
- [bitrue](https://docs.ccxt.com/docs/exchanges/bitrue#fetchbalance)
- [bitso](https://docs.ccxt.com/docs/exchanges/bitso#fetchbalance)
- [bitstamp](https://docs.ccxt.com/docs/exchanges/bitstamp#fetchbalance)
- [betteam](https://docs.ccxt.com/docs/exchanges/betteam#fetchbalance)
- [bittrade](https://docs.ccxt.com/docs/exchanges/bittrade#fetchbalance)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#fetchbalance)
- [blockchaincom](https://docs.ccxt.com/docs/exchanges/blockchaincom#fetchbalance)
- [blofin](https://docs.ccxt.com/docs/exchanges/blofin#fetchbalance)
- [btcbox](https://docs.ccxt.com/docs/exchanges/btcbox#fetchbalance)
- [btcmarkets](https://docs.ccxt.com/docs/exchanges/btcmarkets#fetchbalance)
- [btcturk](https://docs.ccxt.com/docs/exchanges/btcturk#fetchbalance)
- [btse](https://docs.ccxt.com/docs/exchanges/btse#fetchbalance)
- [bullish](https://docs.ccxt.com/docs/exchanges/bullish#fetchbalance)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchbalance)
- [bydfi](https://docs.ccxt.com/docs/exchanges/bydfi#fetchbalance)
- [cex](https://docs.ccxt.com/docs/exchanges/cex#fetchbalance)
- [coinbase](https://docs.ccxt.com/docs/exchanges/coinbase#fetchbalance)
- [coinbaseexchange](https://docs.ccxt.com/docs/exchanges/coinbaseexchange#fetchbalance)
- [coinbaseinternational](https://docs.ccxt.com/docs/exchanges/coinbaseinternational#fetchbalance)
- [coincheck](https://docs.ccxt.com/docs/exchanges/coincheck#fetchbalance)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#fetchbalance)
- [coinmate](https://docs.ccxt.com/docs/exchanges/coinmate#fetchbalance)
- [coinone](https://docs.ccxt.com/docs/exchanges/coinone#fetchbalance)
- [coinsph](https://docs.ccxt.com/docs/exchanges/coinsph#fetchbalance)
- [coinspot](https://docs.ccxt.com/docs/exchanges/coinspot#fetchbalance)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#fetchbalance)
- [cryptomus](https://docs.ccxt.com/docs/exchanges/cryptomus#fetchbalance)
- [deepcoin](https://docs.ccxt.com/docs/exchanges/deepcoin#fetchbalance)
- [delta](https://docs.ccxt.com/docs/exchanges/delta#fetchbalance)
- [deribit](https://docs.ccxt.com/docs/exchanges/deribit#fetchbalance)
- [derive](https://docs.ccxt.com/docs/exchanges/derive#fetchbalance)
- [digifinex](https://docs.ccxt.com/docs/exchanges/digifinex#fetchbalance)
- [dydx](https://docs.ccxt.com/docs/exchanges/dydx#fetchbalance)
- [extended](https://docs.ccxt.com/docs/exchanges/extended#fetchbalance)
- [foxbit](https://docs.ccxt.com/docs/exchanges/foxbit#fetchbalance)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#fetchbalance)
- [gemini](https://docs.ccxt.com/docs/exchanges/gemini#fetchbalance)
- [grvt](https://docs.ccxt.com/docs/exchanges/grvt#fetchbalance)
- [hashkey](https://docs.ccxt.com/docs/exchanges/hashkey#fetchbalance)
- [hibachi](https://docs.ccxt.com/docs/exchanges/hibachi#fetchbalance)
- [hitbtc](https://docs.ccxt.com/docs/exchanges/hitbtc#fetchbalance)
- [hollaex](https://docs.ccxt.com/docs/exchanges/hollaex#fetchbalance)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#fetchbalance)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#fetchbalance)
- [independentreserve](https://docs.ccxt.com/docs/exchanges/independentreserve#fetchbalance)
- [indodax](https://docs.ccxt.com/docs/exchanges/indodax#fetchbalance)
- [kraken](https://docs.ccxt.com/docs/exchanges/kraken#fetchbalance)
- [krakenfutures](https://docs.ccxt.com/docs/exchanges/krakenfutures#fetchbalance)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchbalance)
- [latoken](https://docs.ccxt.com/docs/exchanges/latoken#fetchbalance)
- [lbank](https://docs.ccxt.com/docs/exchanges/lbank#fetchbalance)
- [ligher](https://docs.ccxt.com/docs/exchanges/ligher#fetchbalance)
- [luno](https://docs.ccxt.com/docs/exchanges/luno#fetchbalance)
- [mercado](https://docs.ccxt.com/docs/exchanges/mercado#fetchbalance)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#fetchbalance)
- [modetrade](https://docs.ccxt.com/docs/exchanges/modetrade#fetchbalance)
- [mudrex](https://docs.ccxt.com/docs/exchanges/mudrex#fetchbalance)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#fetchbalance)
- [ndax](https://docs.ccxt.com/docs/exchanges/ndax#fetchbalance)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchbalance)
- [onetrading](https://docs.ccxt.com/docs/exchanges/onetrading#fetchbalance)
- [p2b](https://docs.ccxt.com/docs/exchanges/p2b#fetchbalance)
- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#fetchbalance)
- [paradex](https://docs.ccxt.com/docs/exchanges/paradex#fetchbalance)
- [paymium](https://docs.ccxt.com/docs/exchanges/paymium#fetchbalance)
- [phemex](https://docs.ccxt.com/docs/exchanges/phemex#fetchbalance)
- [poloniex](https://docs.ccxt.com/docs/exchanges/poloniex#fetchbalance)
- [revolutx](https://docs.ccxt.com/docs/exchanges/revolutx#fetchbalance)
- [tokocrypto](https://docs.ccxt.com/docs/exchanges/tokocrypto#fetchbalance)
- [toobit](https://docs.ccxt.com/docs/exchanges/toobit#fetchbalance)
- [upbit](https://docs.ccxt.com/docs/exchanges/upbit#fetchbalance)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#fetchbalance)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#fetchbalance)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#fetchbalance)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#fetchbalance)
- [xt](https://docs.ccxt.com/docs/exchanges/xt#fetchbalance)
- [zaif](https://docs.ccxt.com/docs/exchanges/zaif#fetchbalance)
- [zebpay](https://docs.ccxt.com/docs/exchanges/zebpay#fetchbalance)

* * *

## [fetchBalanceWs](https://docs.ccxt.com/docs/base-spec\#fetchbalancews)

fetch balance and get the amount of funds available for trading or funds locked in orders

**Kind**: instance

**Returns**: `object` \- a [balance structure](https://docs.ccxt.com/docs/manual#balance-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.type | `string`, `undefined` | No | 'future', 'delivery', 'savings', 'funding', or 'spot' |
| params.marginMode | `string`, `undefined` | No | 'cross' or 'isolated', for margin trading, uses this.options.defaultMarginMode if not passed, defaults to undefined/None/null |
| params.symbols | `Array<string>`, `undefined` | No | unified market symbols, only used in isolated margin mode |
| params.method | `string`, `undefined` | No | method to use. Can be account.balance, account.status, v2/account.balance or v2/account.status |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-61)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchbalancews)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#fetchbalancews)
- [cex](https://docs.ccxt.com/docs/exchanges/cex#fetchbalancews)

* * *

## [fetchBidsAsks](https://docs.ccxt.com/docs/base-spec\#fetchbidsasks)

fetches the bid and ask price and volume for multiple markets

**Kind**: instance

**Returns**: `object` \- a dictionary of [ticker structures](https://docs.ccxt.com/docs/manual#ticker-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>`, `undefined` | Yes | unified symbols of the markets to fetch the bids and asks for, all markets are returned if not assigned |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.subType | `string` | No | "linear" or "inverse" |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-62)

- [aster](https://docs.ccxt.com/docs/exchanges/aster#fetchbidsasks)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchbidsasks)
- [bitrue](https://docs.ccxt.com/docs/exchanges/bitrue#fetchbidsasks)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchbidsasks)
- [coinbase](https://docs.ccxt.com/docs/exchanges/coinbase#fetchbidsasks)
- [kucoinfutures](https://docs.ccxt.com/docs/exchanges/kucoinfutures#fetchbidsasks)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#fetchbidsasks)
- [tokocrypto](https://docs.ccxt.com/docs/exchanges/tokocrypto#fetchbidsasks)
- [toobit](https://docs.ccxt.com/docs/exchanges/toobit#fetchbidsasks)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#fetchbidsasks)
- [xt](https://docs.ccxt.com/docs/exchanges/xt#fetchbidsasks)

* * *

## [fetchBorrowInterest](https://docs.ccxt.com/docs/base-spec\#fetchborrowinterest)

fetch the interest owed by the user for borrowing currency for margin trading

**Kind**: instance

**Returns**: `Array<object>` \- a list of [borrow interest structures](https://docs.ccxt.com/docs/manual#borrow-interest-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| code | `string` | No | unified currency code |
| symbol | `string` | No | unified market symbol when fetch interest in isolated markets |
| since | `int` | No | the earliest time in ms to fetch borrrow interest for |
| limit | `int` | No | the maximum number of structures to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.portfolioMargin | `boolean` | No | set to true if you would like to fetch the borrow interest in a portfolio margin account |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-63)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchborrowinterest)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#fetchborrowinterest)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchborrowinterest)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#fetchborrowinterest)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#fetchborrowinterest)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#fetchborrowinterest)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchborrowinterest)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchborrowinterest)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#fetchborrowinterest)

* * *

## [fetchBorrowRateHistories](https://docs.ccxt.com/docs/base-spec\#fetchborrowratehistories)

retrieves a history of a multiple currencies borrow interest rate at specific time slots, returns all currencies if no symbols passed, default is undefined

**Kind**: instance

**Returns**: `object` \- a dictionary of [borrow rate structures](https://docs.ccxt.com/docs/manual#borrow-rate-structure) indexed by the market symbol

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| codes | `Array<string>`, `undefined` | Yes | list of unified currency codes, default is undefined |
| since | `int` | No | timestamp in ms of the earliest borrowRate, default is undefined |
| limit | `int` | No | max number of borrow rate prices to return, default is undefined |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.marginMode | `string` | No | 'cross' or 'isolated' default is 'cross' |
| params.until | `int` | No | the latest time in ms to fetch entries for |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-64)

- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchborrowratehistories)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchborrowratehistories)

* * *

## [fetchBorrowRateHistory](https://docs.ccxt.com/docs/base-spec\#fetchborrowratehistory)

retrieves a history of a currencies borrow interest rate at specific time slots

**Kind**: instance

**Returns**: `Array<object>` \- an array of [borrow rate structures](https://docs.ccxt.com/docs/manual#borrow-rate-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| code | `string` | Yes | unified currency code |
| since | `int` | No | timestamp for the earliest borrow rate |
| limit | `int` | No | the maximum number of [borrow rate structures](https://docs.ccxt.com/docs/manual#borrow-rate-structure) to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-65)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchborrowratehistory)
- [bullish](https://docs.ccxt.com/docs/exchanges/bullish#fetchborrowratehistory)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchborrowratehistory)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchborrowratehistory)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchborrowratehistory)

* * *

## [fetchCanceledAndClosedOrders](https://docs.ccxt.com/docs/base-spec\#fetchcanceledandclosedorders)

fetches information on multiple canceled orders made by the user

**Kind**: instance

**Returns**: `Array<object>` \- a list of [order structures](https://docs.ccxt.com/docs/manual#order-structure)

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

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-66)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchcanceledandclosedorders)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#fetchcanceledandclosedorders)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#fetchcanceledandclosedorders)
- [bullish](https://docs.ccxt.com/docs/exchanges/bullish#fetchcanceledandclosedorders)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchcanceledandclosedorders)
- [bydfi](https://docs.ccxt.com/docs/exchanges/bydfi#fetchcanceledandclosedorders)
- [deepcoin](https://docs.ccxt.com/docs/exchanges/deepcoin#fetchcanceledandclosedorders)
- [hashkey](https://docs.ccxt.com/docs/exchanges/hashkey#fetchcanceledandclosedorders)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#fetchcanceledandclosedorders)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#fetchcanceledandclosedorders)
- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#fetchcanceledandclosedorders)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#fetchcanceledandclosedorders)

* * *

## [fetchCanceledOrders](https://docs.ccxt.com/docs/base-spec\#fetchcanceledorders)

fetches information on multiple canceled orders made by the user

**Kind**: instance

**Returns**: `Array<object>` \- a list of [order structures](https://docs.ccxt.com/docs/manual#order-structure)

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

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-67)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchcanceledorders)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#fetchcanceledorders)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#fetchcanceledorders)
- [bithumb](https://docs.ccxt.com/docs/exchanges/bithumb#fetchcanceledorders)
- [bitteam](https://docs.ccxt.com/docs/exchanges/bitteam#fetchcanceledorders)
- [blockchaincom](https://docs.ccxt.com/docs/exchanges/blockchaincom#fetchcanceledorders)
- [bullish](https://docs.ccxt.com/docs/exchanges/bullish#fetchcanceledorders)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchcanceledorders)
- [coinbase](https://docs.ccxt.com/docs/exchanges/coinbase#fetchcanceledorders)
- [deepcoin](https://docs.ccxt.com/docs/exchanges/deepcoin#fetchcanceledorders)
- [derive](https://docs.ccxt.com/docs/exchanges/derive#fetchcanceledorders)
- [extended](https://docs.ccxt.com/docs/exchanges/extended#fetchcanceledorders)
- [hibachi](https://docs.ccxt.com/docs/exchanges/hibachi#fetchcanceledorders)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#fetchcanceledorders)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#fetchcanceledorders)
- [krakenfutures](https://docs.ccxt.com/docs/exchanges/krakenfutures#fetchcanceledorders)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#fetchcanceledorders)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#fetchcanceledorders)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchcanceledorders)
- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#fetchcanceledorders)
- [upbit](https://docs.ccxt.com/docs/exchanges/upbit#fetchcanceledorders)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#fetchcanceledorders)
- [xt](https://docs.ccxt.com/docs/exchanges/xt#fetchcanceledorders)

* * *

## [fetchClosedOrder](https://docs.ccxt.com/docs/base-spec\#fetchclosedorder)

fetch an open order by it's id

**Kind**: instance

**Returns**: `object` \- an [order structure](https://docs.ccxt.com/docs/manual#order-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| id | `string` | Yes | order id |
| symbol | `string` | Yes | unified market symbol, default is undefined |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-68)

- [bitfinex](https://docs.ccxt.com/docs/exchanges/bitfinex#fetchclosedorder)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchclosedorder)
- [cex](https://docs.ccxt.com/docs/exchanges/cex#fetchclosedorder)
- [deepcoin](https://docs.ccxt.com/docs/exchanges/deepcoin#fetchclosedorder)

* * *

## [fetchClosedOrders](https://docs.ccxt.com/docs/base-spec\#fetchclosedorders)

fetches information on multiple closed orders made by the user

**Kind**: instance

**Returns**: `Array<Order>` \- a list of [order structures](https://docs.ccxt.com/docs/manual#order-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol of the market orders were made in |
| since | `int` | No | the earliest time in ms to fetch orders for |
| limit | `int` | No | the maximum number of order structures to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.until | `int` | No | the latest time in ms to fetch orders for |
| params.direction | `string` | No | the ordering of the results, 'asc' or 'desc', defaults to 'asc' when since is set |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-69)

- [alpaca](https://docs.ccxt.com/docs/exchanges/alpaca#fetchclosedorders)
- [bigone](https://docs.ccxt.com/docs/exchanges/bigone#fetchclosedorders)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchclosedorders)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#fetchclosedorders)
- [bitfinex](https://docs.ccxt.com/docs/exchanges/bitfinex#fetchclosedorders)
- [bitflyer](https://docs.ccxt.com/docs/exchanges/bitflyer#fetchclosedorders)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#fetchclosedorders)
- [bithumb](https://docs.ccxt.com/docs/exchanges/bithumb#fetchclosedorders)
- [bitopro](https://docs.ccxt.com/docs/exchanges/bitopro#fetchclosedorders)
- [bitrue](https://docs.ccxt.com/docs/exchanges/bitrue#fetchclosedorders)
- [bitteam](https://docs.ccxt.com/docs/exchanges/bitteam#fetchclosedorders)
- [bittrade](https://docs.ccxt.com/docs/exchanges/bittrade#fetchclosedorders)
- [blockchaincom](https://docs.ccxt.com/docs/exchanges/blockchaincom#fetchclosedorders)
- [blofin](https://docs.ccxt.com/docs/exchanges/blofin#fetchclosedorders)
- [btcmarkets](https://docs.ccxt.com/docs/exchanges/btcmarkets#fetchclosedorders)
- [bullish](https://docs.ccxt.com/docs/exchanges/bullish#fetchclosedorders)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchclosedorders)
- [cex](https://docs.ccxt.com/docs/exchanges/cex#fetchclosedorders)
- [coinbase](https://docs.ccxt.com/docs/exchanges/coinbase#fetchclosedorders)
- [coinbaseexchange](https://docs.ccxt.com/docs/exchanges/coinbaseexchange#fetchclosedorders)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#fetchclosedorders)
- [coinsph](https://docs.ccxt.com/docs/exchanges/coinsph#fetchclosedorders)
- [deepcoin](https://docs.ccxt.com/docs/exchanges/deepcoin#fetchclosedorders)
- [delta](https://docs.ccxt.com/docs/exchanges/delta#fetchclosedorders)
- [deribit](https://docs.ccxt.com/docs/exchanges/deribit#fetchclosedorders)
- [derive](https://docs.ccxt.com/docs/exchanges/derive#fetchclosedorders)
- [dydx](https://docs.ccxt.com/docs/exchanges/dydx#fetchclosedorders)
- [extended](https://docs.ccxt.com/docs/exchanges/extended#fetchclosedorders)
- [foxbit](https://docs.ccxt.com/docs/exchanges/foxbit#fetchclosedorders)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#fetchclosedorders)
- [hibachi](https://docs.ccxt.com/docs/exchanges/hibachi#fetchclosedorders)
- [hitbtc](https://docs.ccxt.com/docs/exchanges/hitbtc#fetchclosedorders)
- [hollaex](https://docs.ccxt.com/docs/exchanges/hollaex#fetchclosedorders)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#fetchclosedorders)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#fetchclosedorders)
- [independentreserve](https://docs.ccxt.com/docs/exchanges/independentreserve#fetchclosedorders)
- [indodax](https://docs.ccxt.com/docs/exchanges/indodax#fetchclosedorders)
- [kraken](https://docs.ccxt.com/docs/exchanges/kraken#fetchclosedorders)
- [krakenfutures](https://docs.ccxt.com/docs/exchanges/krakenfutures#fetchclosedorders)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchclosedorders)
- [lighter](https://docs.ccxt.com/docs/exchanges/lighter#fetchclosedorders)
- [luno](https://docs.ccxt.com/docs/exchanges/luno#fetchclosedorders)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#fetchclosedorders)
- [modetrade](https://docs.ccxt.com/docs/exchanges/modetrade#fetchclosedorders)
- [mudrex](https://docs.ccxt.com/docs/exchanges/mudrex#fetchclosedorders)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#fetchclosedorders)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchclosedorders)
- [onetrading](https://docs.ccxt.com/docs/exchanges/onetrading#fetchclosedorders)
- [p2b](https://docs.ccxt.com/docs/exchanges/p2b#fetchclosedorders)
- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#fetchclosedorders)
- [phemex](https://docs.ccxt.com/docs/exchanges/phemex#fetchclosedorders)
- [poloniex](https://docs.ccxt.com/docs/exchanges/poloniex#fetchclosedorders)
- [revolutx](https://docs.ccxt.com/docs/exchanges/revolutx#fetchclosedorders)
- [tokocrypto](https://docs.ccxt.com/docs/exchanges/tokocrypto#fetchclosedorders)
- [toobit](https://docs.ccxt.com/docs/exchanges/toobit#fetchclosedorders)
- [upbit](https://docs.ccxt.com/docs/exchanges/upbit#fetchclosedorders)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#fetchclosedorders)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#fetchclosedorders)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#fetchclosedorders)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#fetchclosedorders)
- [xt](https://docs.ccxt.com/docs/exchanges/xt#fetchclosedorders)
- [zaif](https://docs.ccxt.com/docs/exchanges/zaif#fetchclosedorders)

* * *

## [fetchClosedOrdersWs](https://docs.ccxt.com/docs/base-spec\#fetchclosedordersws)

fetch closed orders

**Kind**: instance

**Returns**: `Array<object>` \- a list of [order structures](https://docs.ccxt.com/docs/manual#order-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol |
| since | `int` | No | the earliest time in ms to fetch open orders for |
| limit | `int` | No | the maximum number of open orders structures to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-70)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchclosedordersws)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#fetchclosedordersws)

* * *

## [fetchContractBalance](https://docs.ccxt.com/docs/base-spec\#fetchcontractbalance)

query for balance and get the amount of funds available for trading or funds locked in orders

**Kind**: instance

**Returns**: `object` \- a [balance structure](https://docs.ccxt.com/docs/manual#balance-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.code | `object` | No | the unified currency code to fetch the balance for, if not provided, the default .options\['fetchBalance'\]\['code'\] will be used |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-71)

- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchcontractbalance)

* * *

## [fetchContractDepositAddress](https://docs.ccxt.com/docs/base-spec\#fetchcontractdepositaddress)

fetch the deposit address for a currency associated with this account

**Kind**: instance

**Returns**: `object` \- an [address structure](https://docs.ccxt.com/docs/manual#address-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| code | `string` | Yes | unified currency code |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-72)

- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchcontractdepositaddress)

* * *

## [fetchContractDeposits](https://docs.ccxt.com/docs/base-spec\#fetchcontractdeposits)

helper method for fetching deposits for futures accounts

**Kind**: instance

**Returns**: `Array<object>` \- a list of [transaction structures](https://docs.ccxt.com/docs/manual#transaction-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| code | `string` | Yes | unified currency code |
| since | `int` | No | the earliest time in ms to fetch deposits for |
| limit | `int` | No | the maximum number of deposits structures to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-73)

- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchcontractdeposits)

* * *

## [fetchContractOrder](https://docs.ccxt.com/docs/base-spec\#fetchcontractorder)

fetc contract order

**Kind**: instance

**Returns**: `object` \- An [order structure](https://docs.ccxt.com/docs/manual#order-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| id | `string` | Yes | order id |
| symbol | `string` | Yes | unified symbol of the market the order was made in |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-74)

- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchcontractorder)

* * *

## [fetchContractOrdersByStatus](https://docs.ccxt.com/docs/base-spec\#fetchcontractordersbystatus)

fetches a list of contract orders placed on the exchange

**Kind**: instance

**Returns**: An [array of order structures](https://docs.ccxt.com/docs/manual#order-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| status | `string` | Yes | 'active' or 'closed', only 'active' is valid for stop orders |
| symbol | `string` | Yes | unified symbol for the market to retrieve orders from |
| since | `int` | No | timestamp in ms of the earliest order to retrieve |
| limit | `int` | No | The maximum number of orders to retrieve |
| params | `object` | No | exchange specific parameters |
| params.trigger | `bool` | No | set to true to retrieve untriggered stop orders |
| params.until | `int` | No | End time in ms |
| params.side | `string` | No | buy or sell |
| params.type | `string` | No | limit or market |
| params.paginate | `boolean` | No | default false, when true will automatically paginate by calling this endpoint multiple times. See in the docs all the [availble parameters](https://docs.ccxt.com/docs/manual#pagination-params) |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-75)

- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchcontractordersbystatus)

* * *

## [fetchContractWithdrawals](https://docs.ccxt.com/docs/base-spec\#fetchcontractwithdrawals)

helper method for fetching withdrawals for futures accounts

**Kind**: instance

**Returns**: `Array<object>` \- a list of [transaction structures](https://docs.ccxt.com/docs/manual#transaction-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| code | `string` | Yes | unified currency code |
| since | `int` | No | the earliest time in ms to fetch withdrawals for |
| limit | `int` | No | the maximum number of withdrawals structures to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-76)

- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchcontractwithdrawals)

* * *

## [fetchConvertCurrencies](https://docs.ccxt.com/docs/base-spec\#fetchconvertcurrencies)

fetches all available currencies that can be converted

**Kind**: instance

**Returns**: `object` \- an associative dictionary of currencies

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-77)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchconvertcurrencies)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#fetchconvertcurrencies)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchconvertcurrencies)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchconvertcurrencies)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#fetchconvertcurrencies)

* * *

## [fetchConvertQuote](https://docs.ccxt.com/docs/base-spec\#fetchconvertquote)

fetch a quote for converting from one currency to another

**Kind**: instance

**Returns**: `object` \- a [conversion structure](https://docs.ccxt.com/docs/manual#conversion-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| fromCode | `string` | Yes | the currency that you want to sell and convert from |
| toCode | `string` | Yes | the currency that you want to buy and convert into |
| amount | `float` | Yes | how much you want to trade in units of the from currency |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.walletType | `string` | No | either 'SPOT' or 'FUNDING', the default is 'SPOT' |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-78)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchconvertquote)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#fetchconvertquote)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchconvertquote)
- [coinbase](https://docs.ccxt.com/docs/exchanges/coinbase#fetchconvertquote)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchconvertquote)
- [phemex](https://docs.ccxt.com/docs/exchanges/phemex#fetchconvertquote)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#fetchconvertquote)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#fetchconvertquote)

* * *

## [fetchConvertTrade](https://docs.ccxt.com/docs/base-spec\#fetchconverttrade)

fetch the data for a conversion trade

**Kind**: instance

**Returns**: `object` \- a [conversion structure](https://docs.ccxt.com/docs/manual#conversion-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| id | `string` | Yes | the id of the trade that you want to fetch |
| code | `string` | No | the unified currency code of the conversion trade |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-79)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchconverttrade)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchconverttrade)
- [coinbase](https://docs.ccxt.com/docs/exchanges/coinbase#fetchconverttrade)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchconverttrade)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#fetchconverttrade)

* * *

## [fetchConvertTradeHistory](https://docs.ccxt.com/docs/base-spec\#fetchconverttradehistory)

fetch the users history of conversion trades

**Kind**: instance

**Returns**: `Array<object>` \- a list of [conversion structures](https://docs.ccxt.com/docs/manual#conversion-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| code | `string` | No | the unified currency code |
| since | `int` | No | the earliest time in ms to fetch conversions for |
| limit | `int` | No | the maximum number of conversion structures to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.until | `int` | No | timestamp in ms of the latest conversion to fetch |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-80)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchconverttradehistory)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#fetchconverttradehistory)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchconverttradehistory)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchconverttradehistory)
- [phemex](https://docs.ccxt.com/docs/exchanges/phemex#fetchconverttradehistory)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#fetchconverttradehistory)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#fetchconverttradehistory)

* * *

## [fetchCrossBorrowRate](https://docs.ccxt.com/docs/base-spec\#fetchcrossborrowrate)

fetch the rate of interest to borrow a currency for margin trading

**Kind**: instance

**Returns**: `object` \- a [borrow rate structure](https://docs.ccxt.com/docs/manual#borrow-rate-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| code | `string` | Yes | unified currency code |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-81)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchcrossborrowrate)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#fetchcrossborrowrate)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchcrossborrowrate)
- [digifinex](https://docs.ccxt.com/docs/exchanges/digifinex#fetchcrossborrowrate)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchcrossborrowrate)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchcrossborrowrate)

* * *

## [fetchCrossBorrowRates](https://docs.ccxt.com/docs/base-spec\#fetchcrossborrowrates)

fetch the borrow interest rates of all currencies

**Kind**: instance

**Returns**: `object` \- a list of [borrow rate structures](https://docs.ccxt.com/docs/manual#borrow-rate-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-82)

- [digifinex](https://docs.ccxt.com/docs/exchanges/digifinex#fetchcrossborrowrates)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchcrossborrowrates)

* * *

## [fetchCurrencies](https://docs.ccxt.com/docs/base-spec\#fetchcurrencies)

fetches all available currencies on an exchange

**Kind**: instance

**Returns**: `object` \- an associative dictionary of currencies

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-83)

- [apex](https://docs.ccxt.com/docs/exchanges/apex#fetchcurrencies)
- [aster](https://docs.ccxt.com/docs/exchanges/aster#fetchcurrencies)
- [backpack](https://docs.ccxt.com/docs/exchanges/backpack#fetchcurrencies)
- [bigone](https://docs.ccxt.com/docs/exchanges/bigone#fetchcurrencies)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchcurrencies)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#fetchcurrencies)
- [bitfinex](https://docs.ccxt.com/docs/exchanges/bitfinex#fetchcurrencies)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#fetchcurrencies)
- [bitopro](https://docs.ccxt.com/docs/exchanges/bitopro#fetchcurrencies)
- [bitrue](https://docs.ccxt.com/docs/exchanges/bitrue#fetchcurrencies)
- [bitso](https://docs.ccxt.com/docs/exchanges/bitso#fetchcurrencies)
- [bitstamp](https://docs.ccxt.com/docs/exchanges/bitstamp#fetchcurrencies)
- [bitteam](https://docs.ccxt.com/docs/exchanges/bitteam#fetchcurrencies)
- [bittrade](https://docs.ccxt.com/docs/exchanges/bittrade#fetchcurrencies)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#fetchcurrencies)
- [bullish](https://docs.ccxt.com/docs/exchanges/bullish#fetchcurrencies)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchcurrencies)
- [cex](https://docs.ccxt.com/docs/exchanges/cex#fetchcurrencies)
- [coinbase](https://docs.ccxt.com/docs/exchanges/coinbase#fetchcurrencies)
- [coinbaseexchange](https://docs.ccxt.com/docs/exchanges/coinbaseexchange#fetchcurrencies)
- [coinbaseinternational](https://docs.ccxt.com/docs/exchanges/coinbaseinternational#fetchcurrencies)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#fetchcurrencies)
- [coinone](https://docs.ccxt.com/docs/exchanges/coinone#fetchcurrencies)
- [coinsph](https://docs.ccxt.com/docs/exchanges/coinsph#fetchcurrencies)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#fetchcurrencies)
- [cryptomus](https://docs.ccxt.com/docs/exchanges/cryptomus#fetchcurrencies)
- [delta](https://docs.ccxt.com/docs/exchanges/delta#fetchcurrencies)
- [deribit](https://docs.ccxt.com/docs/exchanges/deribit#fetchcurrencies)
- [derive](https://docs.ccxt.com/docs/exchanges/derive#fetchcurrencies)
- [digifinex](https://docs.ccxt.com/docs/exchanges/digifinex#fetchcurrencies)
- [extended](https://docs.ccxt.com/docs/exchanges/extended#fetchcurrencies)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#fetchcurrencies)
- [gemini](https://docs.ccxt.com/docs/exchanges/gemini#fetchcurrencies)
- [grvt](https://docs.ccxt.com/docs/exchanges/grvt#fetchcurrencies)
- [hashkey](https://docs.ccxt.com/docs/exchanges/hashkey#fetchcurrencies)
- [hitbtc](https://docs.ccxt.com/docs/exchanges/hitbtc#fetchcurrencies)
- [hollaex](https://docs.ccxt.com/docs/exchanges/hollaex#fetchcurrencies)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#fetchcurrencies)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#fetchcurrencies)
- [kraken](https://docs.ccxt.com/docs/exchanges/kraken#fetchcurrencies)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchcurrencies)
- [latoken](https://docs.ccxt.com/docs/exchanges/latoken#fetchcurrencies)
- [lbank](https://docs.ccxt.com/docs/exchanges/lbank#fetchcurrencies)
- [lighter](https://docs.ccxt.com/docs/exchanges/lighter#fetchcurrencies)
- [luno](https://docs.ccxt.com/docs/exchanges/luno#fetchcurrencies)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#fetchcurrencies)
- [modetrade](https://docs.ccxt.com/docs/exchanges/modetrade#fetchcurrencies)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#fetchcurrencies)
- [ndax](https://docs.ccxt.com/docs/exchanges/ndax#fetchcurrencies)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchcurrencies)
- [onetrading](https://docs.ccxt.com/docs/exchanges/onetrading#fetchcurrencies)
- [phemex](https://docs.ccxt.com/docs/exchanges/phemex#fetchcurrencies)
- [poloniex](https://docs.ccxt.com/docs/exchanges/poloniex#fetchcurrencies)
- [revolutx](https://docs.ccxt.com/docs/exchanges/revolutx#fetchcurrencies)
- [toobit](https://docs.ccxt.com/docs/exchanges/toobit#fetchcurrencies)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#fetchcurrencies)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#fetchcurrencies)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#fetchcurrencies)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#fetchcurrencies)
- [xt](https://docs.ccxt.com/docs/exchanges/xt#fetchcurrencies)
- [zebpay](https://docs.ccxt.com/docs/exchanges/zebpay#fetchcurrencies)

* * *

## [fetchCurrenciesWs](https://docs.ccxt.com/docs/base-spec\#fetchcurrenciesws)

fetches all available currencies on an exchange

**Kind**: instance

**Returns**: `object` \- an associative dictionary of currencies

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-84)

- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#fetchcurrenciesws)

* * *

## [fetchDeposit](https://docs.ccxt.com/docs/base-spec\#fetchdeposit)

fetch data on a currency deposit via the deposit id, looks back 30 days for uta accounts and 90 days otherwise

**Kind**: instance

**Returns**: `object` \- a [transaction structure](https://docs.ccxt.com/docs/manual#transaction-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| id | `string` | Yes | deposit id |
| code | `string` | No | unified currency code |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.uta | `boolean` | No | set to true for the unified trading account (uta), defaults to false |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-85)

- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#fetchdeposit)
- [bithumb](https://docs.ccxt.com/docs/exchanges/bithumb#fetchdeposit)
- [bitso](https://docs.ccxt.com/docs/exchanges/bitso#fetchdeposit)
- [blockchaincom](https://docs.ccxt.com/docs/exchanges/blockchaincom#fetchdeposit)
- [coinbase](https://docs.ccxt.com/docs/exchanges/coinbase#fetchdeposit)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchdeposit)
- [upbit](https://docs.ccxt.com/docs/exchanges/upbit#fetchdeposit)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#fetchdeposit)

* * *

## [fetchDepositAddress](https://docs.ccxt.com/docs/base-spec\#fetchdepositaddress)

fetch the deposit address for a currency associated with this account

**Kind**: instance

**Returns**: `object` \- an [address structure](https://docs.ccxt.com/docs/manual#address-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| code | `string` | Yes | unified currency code |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-86)

- [alpaca](https://docs.ccxt.com/docs/exchanges/alpaca#fetchdepositaddress)
- [backpack](https://docs.ccxt.com/docs/exchanges/backpack#fetchdepositaddress)
- [bigone](https://docs.ccxt.com/docs/exchanges/bigone#fetchdepositaddress)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchdepositaddress)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#fetchdepositaddress)
- [bit2c](https://docs.ccxt.com/docs/exchanges/bit2c#fetchdepositaddress)
- [bitbank](https://docs.ccxt.com/docs/exchanges/bitbank#fetchdepositaddress)
- [bitbns](https://docs.ccxt.com/docs/exchanges/bitbns#fetchdepositaddress)
- [bitfinex](https://docs.ccxt.com/docs/exchanges/bitfinex#fetchdepositaddress)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#fetchdepositaddress)
- [bithumb](https://docs.ccxt.com/docs/exchanges/bithumb#fetchdepositaddress)
- [bitso](https://docs.ccxt.com/docs/exchanges/bitso#fetchdepositaddress)
- [bitstamp](https://docs.ccxt.com/docs/exchanges/bitstamp#fetchdepositaddress)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#fetchdepositaddress)
- [blockchaincom](https://docs.ccxt.com/docs/exchanges/blockchaincom#fetchdepositaddress)
- [bullish](https://docs.ccxt.com/docs/exchanges/bullish#fetchdepositaddress)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchdepositaddress)
- [cex](https://docs.ccxt.com/docs/exchanges/cex#fetchdepositaddress)
- [coinbase](https://docs.ccxt.com/docs/exchanges/coinbase#fetchdepositaddress)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#fetchdepositaddress)
- [coinsph](https://docs.ccxt.com/docs/exchanges/coinsph#fetchdepositaddress)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#fetchdepositaddress)
- [deepcoin](https://docs.ccxt.com/docs/exchanges/deepcoin#fetchdepositaddress)
- [delta](https://docs.ccxt.com/docs/exchanges/delta#fetchdepositaddress)
- [deribit](https://docs.ccxt.com/docs/exchanges/deribit#fetchdepositaddress)
- [digifinex](https://docs.ccxt.com/docs/exchanges/digifinex#fetchdepositaddress)
- [foxbit](https://docs.ccxt.com/docs/exchanges/foxbit#fetchdepositaddress)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#fetchdepositaddress)
- [gemini](https://docs.ccxt.com/docs/exchanges/gemini#fetchdepositaddress)
- [hashkey](https://docs.ccxt.com/docs/exchanges/hashkey#fetchdepositaddress)
- [hibachi](https://docs.ccxt.com/docs/exchanges/hibachi#fetchdepositaddress)
- [hitbtc](https://docs.ccxt.com/docs/exchanges/hitbtc#fetchdepositaddress)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#fetchdepositaddress)
- [independentreserve](https://docs.ccxt.com/docs/exchanges/independentreserve#fetchdepositaddress)
- [kraken](https://docs.ccxt.com/docs/exchanges/kraken#fetchdepositaddress)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchdepositaddress)
- [lbank](https://docs.ccxt.com/docs/exchanges/lbank#fetchdepositaddress)
- [luno](https://docs.ccxt.com/docs/exchanges/luno#fetchdepositaddress)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#fetchdepositaddress)
- [ndax](https://docs.ccxt.com/docs/exchanges/ndax#fetchdepositaddress)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchdepositaddress)
- [paymium](https://docs.ccxt.com/docs/exchanges/paymium#fetchdepositaddress)
- [phemex](https://docs.ccxt.com/docs/exchanges/phemex#fetchdepositaddress)
- [poloniex](https://docs.ccxt.com/docs/exchanges/poloniex#fetchdepositaddress)
- [tokocrypto](https://docs.ccxt.com/docs/exchanges/tokocrypto#fetchdepositaddress)
- [toobit](https://docs.ccxt.com/docs/exchanges/toobit#fetchdepositaddress)
- [upbit](https://docs.ccxt.com/docs/exchanges/upbit#fetchdepositaddress)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#fetchdepositaddress)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#fetchdepositaddress)
- [xt](https://docs.ccxt.com/docs/exchanges/xt#fetchdepositaddress)

* * *

## [fetchDepositAddresses](https://docs.ccxt.com/docs/base-spec\#fetchdepositaddresses)

fetch deposit addresses for multiple currencies (when available)

**Kind**: instance

**Returns**: `object` \- a dictionary of [address structures](https://docs.ccxt.com/docs/manual#address-structure) indexed by currency code

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| codes | `Array<string>` | No | list of unified currency codes, default is undefined (all currencies) |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.generation | `int` | No | _only generation 2 is supported_ if you want to use the API generation 1 or 2, default is 2 |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-87)

- [bithumb](https://docs.ccxt.com/docs/exchanges/bithumb#fetchdepositaddresses)
- [coinbase](https://docs.ccxt.com/docs/exchanges/coinbase#fetchdepositaddresses)
- [coinone](https://docs.ccxt.com/docs/exchanges/coinone#fetchdepositaddresses)
- [deepcoin](https://docs.ccxt.com/docs/exchanges/deepcoin#fetchdepositaddresses)
- [hollaex](https://docs.ccxt.com/docs/exchanges/hollaex#fetchdepositaddresses)
- [indodax](https://docs.ccxt.com/docs/exchanges/indodax#fetchdepositaddresses)
- [paymium](https://docs.ccxt.com/docs/exchanges/paymium#fetchdepositaddresses)
- [upbit](https://docs.ccxt.com/docs/exchanges/upbit#fetchdepositaddresses)

* * *

## [fetchDepositAddressesByNetwork](https://docs.ccxt.com/docs/base-spec\#fetchdepositaddressesbynetwork)

fetch the deposit addresses for a currency associated with this account

**Kind**: instance

**Returns**: `object` \- a dictionary [address structures](https://docs.ccxt.com/docs/manual#address-structure), indexed by the network

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| code | `string` | Yes | unified currency code |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-88)

- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#fetchdepositaddressesbynetwork)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchdepositaddressesbynetwork)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#fetchdepositaddressesbynetwork)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#fetchdepositaddressesbynetwork)
- [gemini](https://docs.ccxt.com/docs/exchanges/gemini#fetchdepositaddressesbynetwork)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#fetchdepositaddressesbynetwork)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchdepositaddressesbynetwork)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#fetchdepositaddressesbynetwork)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchdepositaddressesbynetwork)

* * *

## [fetchDepositMethodId](https://docs.ccxt.com/docs/base-spec\#fetchdepositmethodid)

fetch the deposit id for a fiat currency associated with this account

**Kind**: instance

**Returns**: `object` \- a [deposit id structure](https://docs.ccxt.com/docs/manual#deposit-id-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| id | `string` | Yes | the deposit payment method id |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-89)

- [coinbase](https://docs.ccxt.com/docs/exchanges/coinbase#fetchdepositmethodid)

* * *

## [fetchDepositMethodIds](https://docs.ccxt.com/docs/base-spec\#fetchdepositmethodids)

fetch the deposit id for a fiat currency associated with this account

**Kind**: instance

**Returns**: `object` \- an array of [deposit id structures](https://docs.ccxt.com/docs/manual#deposit-id-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-90)

- [coinbase](https://docs.ccxt.com/docs/exchanges/coinbase#fetchdepositmethodids)

* * *

## [fetchDepositMethods](https://docs.ccxt.com/docs/base-spec\#fetchdepositmethods)

fetch deposit methods for a currency associated with this account

**Kind**: instance

**Returns**: `object` \- of deposit methods

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| code | `string` | Yes | unified currency code |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-91)

- [kraken](https://docs.ccxt.com/docs/exchanges/kraken#fetchdepositmethods)

* * *

## [fetchDepositWithdrawFee](https://docs.ccxt.com/docs/base-spec\#fetchdepositwithdrawfee)

fetch the fee for deposits and withdrawals

**Kind**: instance

**Returns**: `object` \- a [fee structure](https://docs.ccxt.com/docs/manual#fee-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| code | `string` | Yes | unified currency code |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-92)

- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#fetchdepositwithdrawfee)
- [indodax](https://docs.ccxt.com/docs/exchanges/indodax#fetchdepositwithdrawfee)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchdepositwithdrawfee)
- [luno](https://docs.ccxt.com/docs/exchanges/luno#fetchdepositwithdrawfee)

* * *

## [fetchDepositWithdrawFees](https://docs.ccxt.com/docs/base-spec\#fetchdepositwithdrawfees)

fetch deposit and withdraw fees

**Kind**: instance

**Returns**: `Array<object>` \- a list of [fee structures](https://docs.ccxt.com/docs/manual#fee-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| codes | `Array<string>`, `undefined` | Yes | not used by fetchDepositWithdrawFees () |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-93)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchdepositwithdrawfees)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#fetchdepositwithdrawfees)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#fetchdepositwithdrawfees)
- [bitopro](https://docs.ccxt.com/docs/exchanges/bitopro#fetchdepositwithdrawfees)
- [bitrue](https://docs.ccxt.com/docs/exchanges/bitrue#fetchdepositwithdrawfees)
- [bitso](https://docs.ccxt.com/docs/exchanges/bitso#fetchdepositwithdrawfees)
- [bitstamp](https://docs.ccxt.com/docs/exchanges/bitstamp#fetchdepositwithdrawfees)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#fetchdepositwithdrawfees)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchdepositwithdrawfees)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#fetchdepositwithdrawfees)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#fetchdepositwithdrawfees)
- [deribit](https://docs.ccxt.com/docs/exchanges/deribit#fetchdepositwithdrawfees)
- [digifinex](https://docs.ccxt.com/docs/exchanges/digifinex#fetchdepositwithdrawfees)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#fetchdepositwithdrawfees)
- [hitbtc](https://docs.ccxt.com/docs/exchanges/hitbtc#fetchdepositwithdrawfees)
- [hollaex](https://docs.ccxt.com/docs/exchanges/hollaex#fetchdepositwithdrawfees)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#fetchdepositwithdrawfees)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchdepositwithdrawfees)
- [lbank](https://docs.ccxt.com/docs/exchanges/lbank#fetchdepositwithdrawfees)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#fetchdepositwithdrawfees)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchdepositwithdrawfees)
- [poloniex](https://docs.ccxt.com/docs/exchanges/poloniex#fetchdepositwithdrawfees)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#fetchdepositwithdrawfees)

* * *

## [fetchDeposits](https://docs.ccxt.com/docs/base-spec\#fetchdeposits)

fetch all deposits made to an account

**Kind**: instance

**Returns**: `Array<object>` \- a list of [transaction structures](https://docs.ccxt.com/docs/manual#transaction-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| code | `string` | No | unified currency code |
| since | `int` | No | the earliest time in ms to fetch deposits for |
| limit | `int` | No | the maximum number of deposit structures to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-94)

- [alpaca](https://docs.ccxt.com/docs/exchanges/alpaca#fetchdeposits)
- [backpack](https://docs.ccxt.com/docs/exchanges/backpack#fetchdeposits)
- [bigone](https://docs.ccxt.com/docs/exchanges/bigone#fetchdeposits)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchdeposits)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#fetchdeposits)
- [bitbns](https://docs.ccxt.com/docs/exchanges/bitbns#fetchdeposits)
- [bitflyer](https://docs.ccxt.com/docs/exchanges/bitflyer#fetchdeposits)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#fetchdeposits)
- [bithumb](https://docs.ccxt.com/docs/exchanges/bithumb#fetchdeposits)
- [bitopro](https://docs.ccxt.com/docs/exchanges/bitopro#fetchdeposits)
- [bitrue](https://docs.ccxt.com/docs/exchanges/bitrue#fetchdeposits)
- [bitso](https://docs.ccxt.com/docs/exchanges/bitso#fetchdeposits)
- [bittrade](https://docs.ccxt.com/docs/exchanges/bittrade#fetchdeposits)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#fetchdeposits)
- [blockchaincom](https://docs.ccxt.com/docs/exchanges/blockchaincom#fetchdeposits)
- [blofin](https://docs.ccxt.com/docs/exchanges/blofin#fetchdeposits)
- [btcmarkets](https://docs.ccxt.com/docs/exchanges/btcmarkets#fetchdeposits)
- [btse](https://docs.ccxt.com/docs/exchanges/btse#fetchdeposits)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchdeposits)
- [bydfi](https://docs.ccxt.com/docs/exchanges/bydfi#fetchdeposits)
- [coinbase](https://docs.ccxt.com/docs/exchanges/coinbase#fetchdeposits)
- [coinbaseexchange](https://docs.ccxt.com/docs/exchanges/coinbaseexchange#fetchdeposits)
- [coinbaseinternational](https://docs.ccxt.com/docs/exchanges/coinbaseinternational#fetchdeposits)
- [coincheck](https://docs.ccxt.com/docs/exchanges/coincheck#fetchdeposits)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#fetchdeposits)
- [coinsph](https://docs.ccxt.com/docs/exchanges/coinsph#fetchdeposits)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#fetchdeposits)
- [deepcoin](https://docs.ccxt.com/docs/exchanges/deepcoin#fetchdeposits)
- [deribit](https://docs.ccxt.com/docs/exchanges/deribit#fetchdeposits)
- [derive](https://docs.ccxt.com/docs/exchanges/derive#fetchdeposits)
- [digifinex](https://docs.ccxt.com/docs/exchanges/digifinex#fetchdeposits)
- [dydx](https://docs.ccxt.com/docs/exchanges/dydx#fetchdeposits)
- [extended](https://docs.ccxt.com/docs/exchanges/extended#fetchdeposits)
- [foxbit](https://docs.ccxt.com/docs/exchanges/foxbit#fetchdeposits)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#fetchdeposits)
- [grvt](https://docs.ccxt.com/docs/exchanges/grvt#fetchdeposits)
- [hashkey](https://docs.ccxt.com/docs/exchanges/hashkey#fetchdeposits)
- [hibachi](https://docs.ccxt.com/docs/exchanges/hibachi#fetchdeposits)
- [hitbtc](https://docs.ccxt.com/docs/exchanges/hitbtc#fetchdeposits)
- [hollaex](https://docs.ccxt.com/docs/exchanges/hollaex#fetchdeposits)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#fetchdeposits)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#fetchdeposits)
- [kraken](https://docs.ccxt.com/docs/exchanges/kraken#fetchdeposits)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchdeposits)
- [lbank](https://docs.ccxt.com/docs/exchanges/lbank#fetchdeposits)
- [lighter](https://docs.ccxt.com/docs/exchanges/lighter#fetchdeposits)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#fetchdeposits)
- [modetrade](https://docs.ccxt.com/docs/exchanges/modetrade#fetchdeposits)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#fetchdeposits)
- [ndax](https://docs.ccxt.com/docs/exchanges/ndax#fetchdeposits)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchdeposits)
- [paradex](https://docs.ccxt.com/docs/exchanges/paradex#fetchdeposits)
- [phemex](https://docs.ccxt.com/docs/exchanges/phemex#fetchdeposits)
- [poloniex](https://docs.ccxt.com/docs/exchanges/poloniex#fetchdeposits)
- [tokocrypto](https://docs.ccxt.com/docs/exchanges/tokocrypto#fetchdeposits)
- [toobit](https://docs.ccxt.com/docs/exchanges/toobit#fetchdeposits)
- [upbit](https://docs.ccxt.com/docs/exchanges/upbit#fetchdeposits)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#fetchdeposits)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#fetchdeposits)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#fetchdeposits)
- [xt](https://docs.ccxt.com/docs/exchanges/xt#fetchdeposits)

* * *

## [fetchDepositsWithdrawals](https://docs.ccxt.com/docs/base-spec\#fetchdepositswithdrawals)

fetch history of deposits and withdrawals

**Kind**: instance

**Returns**: `object` \- a list of [transaction structure](https://docs.ccxt.com/docs/manual#transaction-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| code | `string` | No | unified currency code for the currency of the deposit/withdrawals, default is undefined |
| since | `int` | No | timestamp in ms of the earliest deposit/withdrawal, default is undefined |
| limit | `int` | No | max number of deposit/withdrawals to return, default is undefined |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-95)

- [alpaca](https://docs.ccxt.com/docs/exchanges/alpaca#fetchdepositswithdrawals)
- [bitfinex](https://docs.ccxt.com/docs/exchanges/bitfinex#fetchdepositswithdrawals)
- [bitstamp](https://docs.ccxt.com/docs/exchanges/bitstamp#fetchdepositswithdrawals)
- [bitteam](https://docs.ccxt.com/docs/exchanges/bitteam#fetchdepositswithdrawals)
- [btcmarkets](https://docs.ccxt.com/docs/exchanges/btcmarkets#fetchdepositswithdrawals)
- [btse](https://docs.ccxt.com/docs/exchanges/btse#fetchdepositswithdrawals)
- [bullish](https://docs.ccxt.com/docs/exchanges/bullish#fetchdepositswithdrawals)
- [cex](https://docs.ccxt.com/docs/exchanges/cex#fetchdepositswithdrawals)
- [coinbase](https://docs.ccxt.com/docs/exchanges/coinbase#fetchdepositswithdrawals)
- [coinbaseexchange](https://docs.ccxt.com/docs/exchanges/coinbaseexchange#fetchdepositswithdrawals)
- [coinbaseinternational](https://docs.ccxt.com/docs/exchanges/coinbaseinternational#fetchdepositswithdrawals)
- [coinmate](https://docs.ccxt.com/docs/exchanges/coinmate#fetchdepositswithdrawals)
- [dydx](https://docs.ccxt.com/docs/exchanges/dydx#fetchdepositswithdrawals)
- [gemini](https://docs.ccxt.com/docs/exchanges/gemini#fetchdepositswithdrawals)
- [hibachi](https://docs.ccxt.com/docs/exchanges/hibachi#fetchdepositswithdrawals)
- [hitbtc](https://docs.ccxt.com/docs/exchanges/hitbtc#fetchdepositswithdrawals)
- [indodax](https://docs.ccxt.com/docs/exchanges/indodax#fetchdepositswithdrawals)
- [modetrade](https://docs.ccxt.com/docs/exchanges/modetrade#fetchdepositswithdrawals)
- [poloniex](https://docs.ccxt.com/docs/exchanges/poloniex#fetchdepositswithdrawals)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#fetchdepositswithdrawals)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#fetchdepositswithdrawals)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#fetchdepositswithdrawals)

* * *

## [fetchDepositsWs](https://docs.ccxt.com/docs/base-spec\#fetchdepositsws)

fetch all deposits made to an account

**Kind**: instance

**Returns**: `Array<object>` \- a list of [transaction structures](https://docs.ccxt.com/docs/manual#transaction-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| code | `string` | Yes | unified currency code |
| since | `int` | No | the earliest time in ms to fetch deposits for |
| limit | `int` | No | the maximum number of deposits structures to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-96)

- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#fetchdepositsws)

* * *

## [fetchFundingHistory](https://docs.ccxt.com/docs/base-spec\#fetchfundinghistory)

fetches information on multiple orders made by the user _classic accounts only_

**Kind**: instance

**Returns**: `Array<Trade>` \- a list of [trade structures](https://docs.ccxt.com/docs/manual#funding-history-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol of the market orders were made in |
| since | `int` | No | the earliest time in ms to fetch orders for |
| limit | `int` | No | the maximum number of order structures to retrieve, default 100 |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.until | `object` | No | end time, ms |
| params.side | `boolean` | No | BUY or SELL |
| params.page | `boolean` | No | Page numbers start from 0 |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-97)

- [apex](https://docs.ccxt.com/docs/exchanges/apex#fetchfundinghistory)
- [aster](https://docs.ccxt.com/docs/exchanges/aster#fetchfundinghistory)
- [backpack](https://docs.ccxt.com/docs/exchanges/backpack#fetchfundinghistory)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchfundinghistory)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#fetchfundinghistory)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#fetchfundinghistory)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchfundinghistory)
- [coinbaseinternational](https://docs.ccxt.com/docs/exchanges/coinbaseinternational#fetchfundinghistory)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#fetchfundinghistory)
- [derive](https://docs.ccxt.com/docs/exchanges/derive#fetchfundinghistory)
- [digifinex](https://docs.ccxt.com/docs/exchanges/digifinex#fetchfundinghistory)
- [extended](https://docs.ccxt.com/docs/exchanges/extended#fetchfundinghistory)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#fetchfundinghistory)
- [grvt](https://docs.ccxt.com/docs/exchanges/grvt#fetchfundinghistory)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#fetchfundinghistory)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#fetchfundinghistory)
- [krakenfutures](https://docs.ccxt.com/docs/exchanges/krakenfutures#fetchfundinghistory)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchfundinghistory)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#fetchfundinghistory)
- [modetrade](https://docs.ccxt.com/docs/exchanges/modetrade#fetchfundinghistory)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#fetchfundinghistory)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchfundinghistory)
- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#fetchfundinghistory)
- [paradex](https://docs.ccxt.com/docs/exchanges/paradex#fetchfundinghistory)
- [phemex](https://docs.ccxt.com/docs/exchanges/phemex#fetchfundinghistory)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#fetchfundinghistory)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#fetchfundinghistory)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#fetchfundinghistory)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#fetchfundinghistory)
- [xt](https://docs.ccxt.com/docs/exchanges/xt#fetchfundinghistory)

* * *

## [fetchFundingInterval](https://docs.ccxt.com/docs/base-spec\#fetchfundinginterval)

fetch the current funding rate interval

**Kind**: instance

**Returns**: `object` \- a [funding rate structure](https://docs.ccxt.com/docs/manual#funding-rate-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.uta | `boolean` | No | set to true for the unified trading account (uta), defaults to false |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-98)

- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#fetchfundinginterval)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#fetchfundinginterval)
- [digifinex](https://docs.ccxt.com/docs/exchanges/digifinex#fetchfundinginterval)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchfundinginterval)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#fetchfundinginterval)
- [modetrade](https://docs.ccxt.com/docs/exchanges/modetrade#fetchfundinginterval)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchfundinginterval)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#fetchfundinginterval)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#fetchfundinginterval)
- [xt](https://docs.ccxt.com/docs/exchanges/xt#fetchfundinginterval)

* * *

## [fetchFundingIntervals](https://docs.ccxt.com/docs/base-spec\#fetchfundingintervals)

fetch the funding rate interval for multiple markets

**Kind**: instance

**Returns**: `Array<object>` \- a list of [funding rate structures](https://docs.ccxt.com/docs/manual#funding-rate-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>` | No | list of unified market symbols |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-99)

- [aster](https://docs.ccxt.com/docs/exchanges/aster#fetchfundingintervals)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchfundingintervals)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#fetchfundingintervals)

* * *

## [fetchFundingLimits](https://docs.ccxt.com/docs/base-spec\#fetchfundinglimits)

fetch the deposit and withdrawal limits for a currency

**Kind**: instance

**Returns**: `object` \- a [funding limits structure](https://docs.ccxt.com/docs/manual#funding-limits-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| codes | `Array<string>`, `undefined` | Yes | unified currency codes |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-100)

- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#fetchfundinglimits)

* * *

## [fetchFundingRate](https://docs.ccxt.com/docs/base-spec\#fetchfundingrate)

fetch the current funding rate

**Kind**: instance

**Returns**: `object` \- a [funding rate structure](https://docs.ccxt.com/docs/manual#funding-rate-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-101)

- [aster](https://docs.ccxt.com/docs/exchanges/aster#fetchfundingrate)
- [backpack](https://docs.ccxt.com/docs/exchanges/backpack#fetchfundingrate)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchfundingrate)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#fetchfundingrate)
- [bitflyer](https://docs.ccxt.com/docs/exchanges/bitflyer#fetchfundingrate)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#fetchfundingrate)
- [bitstamp](https://docs.ccxt.com/docs/exchanges/bitstamp#fetchfundingrate)
- [blofin](https://docs.ccxt.com/docs/exchanges/blofin#fetchfundingrate)
- [btse](https://docs.ccxt.com/docs/exchanges/btse#fetchfundingrate)
- [bydfi](https://docs.ccxt.com/docs/exchanges/bydfi#fetchfundingrate)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#fetchfundingrate)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#fetchfundingrate)
- [deepcoin](https://docs.ccxt.com/docs/exchanges/deepcoin#fetchfundingrate)
- [delta](https://docs.ccxt.com/docs/exchanges/delta#fetchfundingrate)
- [deribit](https://docs.ccxt.com/docs/exchanges/deribit#fetchfundingrate)
- [derive](https://docs.ccxt.com/docs/exchanges/derive#fetchfundingrate)
- [digifinex](https://docs.ccxt.com/docs/exchanges/digifinex#fetchfundingrate)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#fetchfundingrate)
- [hashkey](https://docs.ccxt.com/docs/exchanges/hashkey#fetchfundingrate)
- [hibachi](https://docs.ccxt.com/docs/exchanges/hibachi#fetchfundingrate)
- [hitbtc](https://docs.ccxt.com/docs/exchanges/hitbtc#fetchfundingrate)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#fetchfundingrate)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#fetchfundingrate)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchfundingrate)
- [lbank](https://docs.ccxt.com/docs/exchanges/lbank#fetchfundingrate)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#fetchfundingrate)
- [modetrade](https://docs.ccxt.com/docs/exchanges/modetrade#fetchfundingrate)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#fetchfundingrate)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchfundingrate)
- [paradex](https://docs.ccxt.com/docs/exchanges/paradex#fetchfundingrate)
- [phemex](https://docs.ccxt.com/docs/exchanges/phemex#fetchfundingrate)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#fetchfundingrate)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#fetchfundingrate)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#fetchfundingrate)
- [xt](https://docs.ccxt.com/docs/exchanges/xt#fetchfundingrate)

* * *

## [fetchFundingRateHistory](https://docs.ccxt.com/docs/base-spec\#fetchfundingratehistory)

fetches historical funding rate prices

**Kind**: instance

**Returns**: `Array<object>` \- a list of [funding rate structures](https://docs.ccxt.com/docs/manual#funding-rate-history-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to fetch the funding rate history for |
| since | `int` | No | timestamp in ms of the earliest funding rate to fetch |
| limit | `int` | No | the maximum amount of [funding rate structures](https://docs.ccxt.com/docs/manual#funding-rate-history-structure) to fetch |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.until | `int` | No | timestamp in ms of the latest funding rate |
| params.paginate | `boolean` | No | default false, when true will automatically paginate by calling this endpoint multiple times. See in the docs all the [availble parameters](https://docs.ccxt.com/docs/manual#pagination-params) |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-102)

- [apex](https://docs.ccxt.com/docs/exchanges/apex#fetchfundingratehistory)
- [aster](https://docs.ccxt.com/docs/exchanges/aster#fetchfundingratehistory)
- [backpack](https://docs.ccxt.com/docs/exchanges/backpack#fetchfundingratehistory)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchfundingratehistory)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#fetchfundingratehistory)
- [bitfinex](https://docs.ccxt.com/docs/exchanges/bitfinex#fetchfundingratehistory)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#fetchfundingratehistory)
- [bitstamp](https://docs.ccxt.com/docs/exchanges/bitstamp#fetchfundingratehistory)
- [blofin](https://docs.ccxt.com/docs/exchanges/blofin#fetchfundingratehistory)
- [btse](https://docs.ccxt.com/docs/exchanges/btse#fetchfundingratehistory)
- [bullish](https://docs.ccxt.com/docs/exchanges/bullish#fetchfundingratehistory)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchfundingratehistory)
- [bydfi](https://docs.ccxt.com/docs/exchanges/bydfi#fetchfundingratehistory)
- [coinbaseinternational](https://docs.ccxt.com/docs/exchanges/coinbaseinternational#fetchfundingratehistory)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#fetchfundingratehistory)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#fetchfundingratehistory)
- [deepcoin](https://docs.ccxt.com/docs/exchanges/deepcoin#fetchfundingratehistory)
- [deribit](https://docs.ccxt.com/docs/exchanges/deribit#fetchfundingratehistory)
- [derive](https://docs.ccxt.com/docs/exchanges/derive#fetchfundingratehistory)
- [digifinex](https://docs.ccxt.com/docs/exchanges/digifinex#fetchfundingratehistory)
- [dydx](https://docs.ccxt.com/docs/exchanges/dydx#fetchfundingratehistory)
- [extended](https://docs.ccxt.com/docs/exchanges/extended#fetchfundingratehistory)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#fetchfundingratehistory)
- [grvt](https://docs.ccxt.com/docs/exchanges/grvt#fetchfundingratehistory)
- [hashkey](https://docs.ccxt.com/docs/exchanges/hashkey#fetchfundingratehistory)
- [hibachi](https://docs.ccxt.com/docs/exchanges/hibachi#fetchfundingratehistory)
- [hitbtc](https://docs.ccxt.com/docs/exchanges/hitbtc#fetchfundingratehistory)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#fetchfundingratehistory)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#fetchfundingratehistory)
- [krakenfutures](https://docs.ccxt.com/docs/exchanges/krakenfutures#fetchfundingratehistory)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchfundingratehistory)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#fetchfundingratehistory)
- [modetrade](https://docs.ccxt.com/docs/exchanges/modetrade#fetchfundingratehistory)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchfundingratehistory)
- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#fetchfundingratehistory)
- [paradex](https://docs.ccxt.com/docs/exchanges/paradex#fetchfundingratehistory)
- [phemex](https://docs.ccxt.com/docs/exchanges/phemex#fetchfundingratehistory)
- [toobit](https://docs.ccxt.com/docs/exchanges/toobit#fetchfundingratehistory)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#fetchfundingratehistory)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#fetchfundingratehistory)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#fetchfundingratehistory)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#fetchfundingratehistory)
- [xt](https://docs.ccxt.com/docs/exchanges/xt#fetchfundingratehistory)

* * *

## [fetchFundingRates](https://docs.ccxt.com/docs/base-spec\#fetchfundingrates)

fetch the current funding rate for multiple symbols

**Kind**: instance

**Returns**: `Array<object>` \- a list of [funding rate structures](https://docs.ccxt.com/docs/manual#funding-rate-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>` | No | list of unified market symbols |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-103)

- [aster](https://docs.ccxt.com/docs/exchanges/aster#fetchfundingrates)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchfundingrates)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#fetchfundingrates)
- [bitfinex](https://docs.ccxt.com/docs/exchanges/bitfinex#fetchfundingrates)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#fetchfundingrates)
- [btse](https://docs.ccxt.com/docs/exchanges/btse#fetchfundingrates)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchfundingrates)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#fetchfundingrates)
- [deepcoin](https://docs.ccxt.com/docs/exchanges/deepcoin#fetchfundingrates)
- [delta](https://docs.ccxt.com/docs/exchanges/delta#fetchfundingrates)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#fetchfundingrates)
- [hashkey](https://docs.ccxt.com/docs/exchanges/hashkey#fetchfundingrates)
- [hitbtc](https://docs.ccxt.com/docs/exchanges/hitbtc#fetchfundingrates)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#fetchfundingrates)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#fetchfundingrates)
- [krakenfutures](https://docs.ccxt.com/docs/exchanges/krakenfutures#fetchfundingrates)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchfundingrates)
- [lbank](https://docs.ccxt.com/docs/exchanges/lbank#fetchfundingrates)
- [lighter](https://docs.ccxt.com/docs/exchanges/lighter#fetchfundingrates)
- [modetrade](https://docs.ccxt.com/docs/exchanges/modetrade#fetchfundingrates)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#fetchfundingrates)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchfundingrates)
- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#fetchfundingrates)
- [paradex](https://docs.ccxt.com/docs/exchanges/paradex#fetchfundingrates)
- [toobit](https://docs.ccxt.com/docs/exchanges/toobit#fetchfundingrates)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#fetchfundingrates)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#fetchfundingrates)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#fetchfundingrates)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#fetchfundingrates)

* * *

## [fetchGreeks](https://docs.ccxt.com/docs/base-spec\#fetchgreeks)

fetches an option contracts greeks, financial metrics used to measure the factors that affect the price of an options contract

**Kind**: instance

**Returns**: `object` \- a [greeks structure](https://docs.ccxt.com/docs/manual#greeks-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to fetch greeks for |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-104)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchgreeks)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchgreeks)
- [delta](https://docs.ccxt.com/docs/exchanges/delta#fetchgreeks)
- [deribit](https://docs.ccxt.com/docs/exchanges/deribit#fetchgreeks)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#fetchgreeks)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchgreeks)
- [paradex](https://docs.ccxt.com/docs/exchanges/paradex#fetchgreeks)

* * *

## [fetchHip3Markets](https://docs.ccxt.com/docs/base-spec\#fetchhip3markets)

retrieves data on all hip3 markets for hyperliquid

**Kind**: instance

**Returns**: `Array<object>` \- an array of objects representing market data

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-105)

- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#fetchhip3markets)

* * *

## [fetchIsolatedBorrowRate](https://docs.ccxt.com/docs/base-spec\#fetchisolatedborrowrate)

fetch the rate of interest to borrow a currency for margin trading

**Kind**: instance

**Returns**: `object` \- an [isolated borrow rate structure](https://docs.ccxt.com/docs/manual#isolated-borrow-rate-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol |
| params | `object` | No | extra parameters specific to the exchange API endpoint EXCHANGE SPECIFIC PARAMETERS |
| params.vipLevel | `object` | No | user's current specific margin data will be returned if viplevel is omitted |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-106)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchisolatedborrowrate)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#fetchisolatedborrowrate)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#fetchisolatedborrowrate)

* * *

## [fetchIsolatedBorrowRates](https://docs.ccxt.com/docs/base-spec\#fetchisolatedborrowrates)

fetch the borrow interest rates of all currencies

**Kind**: instance

**Returns**: `object` \- a [borrow rate structure](https://docs.ccxt.com/docs/manual#borrow-rate-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.symbol | `object` | No | unified market symbol EXCHANGE SPECIFIC PARAMETERS |
| params.vipLevel | `object` | No | user's current specific margin data will be returned if viplevel is omitted |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-107)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchisolatedborrowrates)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#fetchisolatedborrowrates)

* * *

## [fetchL3OrderBook](https://docs.ccxt.com/docs/base-spec\#fetchl3orderbook)

fetches level 3 information on open orders with bid (buy) and ask (sell) prices, volumes and other data

**Kind**: instance

**Returns**: `object` \- an [order book structure](https://docs.ccxt.com/docs/manual#order-book-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol |
| limit | `int` | No | max number of orders to return, default is undefined |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-108)

- [blockchaincom](https://docs.ccxt.com/docs/exchanges/blockchaincom#fetchl3orderbook)

* * *

## [fetchLastPrices](https://docs.ccxt.com/docs/base-spec\#fetchlastprices)

fetches the last price for multiple markets

**Kind**: instance

**Returns**: `object` \- a dictionary of lastprices structures

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>`, `undefined` | Yes | unified symbols of the markets to fetch the last prices |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.subType | `string` | No | "linear" or "inverse" |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-109)

- [aster](https://docs.ccxt.com/docs/exchanges/aster#fetchlastprices)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchlastprices)
- [hashkey](https://docs.ccxt.com/docs/exchanges/hashkey#fetchlastprices)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#fetchlastprices)
- [toobit](https://docs.ccxt.com/docs/exchanges/toobit#fetchlastprices)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#fetchlastprices)

* * *

## [fetchLedger](https://docs.ccxt.com/docs/base-spec\#fetchledger)

fetch the history of changes, actions done by the user or operations that altered the balance of the user

**Kind**: instance

**Returns**: `object` \- a [ledger structure](https://docs.ccxt.com/docs/manual#ledger)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| code | `string` | No | unified currency code |
| since | `int` | No | timestamp in ms of the earliest ledger entry |
| limit | `int` | No | max number of ledger entries to return |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.until | `int` | No | timestamp in ms of the latest ledger entry |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-110)

- [aster](https://docs.ccxt.com/docs/exchanges/aster#fetchledger)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchledger)
- [bitfinex](https://docs.ccxt.com/docs/exchanges/bitfinex#fetchledger)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#fetchledger)
- [bitso](https://docs.ccxt.com/docs/exchanges/bitso#fetchledger)
- [bitstamp](https://docs.ccxt.com/docs/exchanges/bitstamp#fetchledger)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#fetchledger)
- [blofin](https://docs.ccxt.com/docs/exchanges/blofin#fetchledger)
- [btse](https://docs.ccxt.com/docs/exchanges/btse#fetchledger)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchledger)
- [cex](https://docs.ccxt.com/docs/exchanges/cex#fetchledger)
- [coinbase](https://docs.ccxt.com/docs/exchanges/coinbase#fetchledger)
- [coinbaseexchange](https://docs.ccxt.com/docs/exchanges/coinbaseexchange#fetchledger)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#fetchledger)
- [deepcoin](https://docs.ccxt.com/docs/exchanges/deepcoin#fetchledger)
- [delta](https://docs.ccxt.com/docs/exchanges/delta#fetchledger)
- [digifinex](https://docs.ccxt.com/docs/exchanges/digifinex#fetchledger)
- [dydx](https://docs.ccxt.com/docs/exchanges/dydx#fetchledger)
- [extended](https://docs.ccxt.com/docs/exchanges/extended#fetchledger)
- [foxbit](https://docs.ccxt.com/docs/exchanges/foxbit#fetchledger)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#fetchledger)
- [hashkey](https://docs.ccxt.com/docs/exchanges/hashkey#fetchledger)
- [hibachi](https://docs.ccxt.com/docs/exchanges/hibachi#fetchledger)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#fetchledger)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#fetchledger)
- [kraken](https://docs.ccxt.com/docs/exchanges/kraken#fetchledger)
- [krakenfutures](https://docs.ccxt.com/docs/exchanges/krakenfutures#fetchledger)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchledger)
- [luno](https://docs.ccxt.com/docs/exchanges/luno#fetchledger)
- [modetrade](https://docs.ccxt.com/docs/exchanges/modetrade#fetchledger)
- [ndax](https://docs.ccxt.com/docs/exchanges/ndax#fetchledger)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchledger)
- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#fetchledger)
- [toobit](https://docs.ccxt.com/docs/exchanges/toobit#fetchledger)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#fetchledger)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#fetchledger)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#fetchledger)
- [xt](https://docs.ccxt.com/docs/exchanges/xt#fetchledger)

* * *

## [fetchLedgerEntry](https://docs.ccxt.com/docs/base-spec\#fetchledgerentry)

fetch the history of changes, actions done by the user or operations that altered the balance of the user

**Kind**: instance

**Returns**: `object` \- a [ledger structure](https://docs.ccxt.com/docs/manual#ledger-entry-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| id | `string` | Yes | the identification number of the ledger entry |
| code | `string` | Yes | unified currency code |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-111)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchledgerentry)

* * *

## [fetchLeverage](https://docs.ccxt.com/docs/base-spec\#fetchleverage)

fetch the set leverage for a market

**Kind**: instance

**Returns**: `object` \- a [leverage structure](https://docs.ccxt.com/docs/manual#leverage-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-112)

- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#fetchleverage)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#fetchleverage)
- [blofin](https://docs.ccxt.com/docs/exchanges/blofin#fetchleverage)
- [btse](https://docs.ccxt.com/docs/exchanges/btse#fetchleverage)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchleverage)
- [bydfi](https://docs.ccxt.com/docs/exchanges/bydfi#fetchleverage)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#fetchleverage)
- [delta](https://docs.ccxt.com/docs/exchanges/delta#fetchleverage)
- [extended](https://docs.ccxt.com/docs/exchanges/extended#fetchleverage)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#fetchleverage)
- [hashkey](https://docs.ccxt.com/docs/exchanges/hashkey#fetchleverage)
- [hitbtc](https://docs.ccxt.com/docs/exchanges/hitbtc#fetchleverage)
- [krakenfutures](https://docs.ccxt.com/docs/exchanges/krakenfutures#fetchleverage)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchleverage)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#fetchleverage)
- [modetrade](https://docs.ccxt.com/docs/exchanges/modetrade#fetchleverage)
- [mudrex](https://docs.ccxt.com/docs/exchanges/mudrex#fetchleverage)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchleverage)
- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#fetchleverage)
- [paradex](https://docs.ccxt.com/docs/exchanges/paradex#fetchleverage)
- [poloniex](https://docs.ccxt.com/docs/exchanges/poloniex#fetchleverage)
- [toobit](https://docs.ccxt.com/docs/exchanges/toobit#fetchleverage)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#fetchleverage)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#fetchleverage)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#fetchleverage)
- [zebpay](https://docs.ccxt.com/docs/exchanges/zebpay#fetchleverage)

* * *

## [fetchLeverageTiers](https://docs.ccxt.com/docs/base-spec\#fetchleveragetiers)

retrieve information on the maximum leverage, and maintenance margin for trades of varying trade sizes

**Kind**: instance

**Returns**: `object` \- a dictionary of [leverage tiers structures](https://docs.ccxt.com/docs/manual#leverage-tiers-structure), indexed by market symbols

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>`, `undefined` | Yes | list of unified market symbols |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.portfolioMargin | `boolean` | No | set to true if you would like to fetch the leverage tiers for a portfolio margin account |
| params.subType | `string` | No | "linear" or "inverse" |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-113)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchleveragetiers)
- [btse](https://docs.ccxt.com/docs/exchanges/btse#fetchleveragetiers)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchleveragetiers)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#fetchleveragetiers)
- [digifinex](https://docs.ccxt.com/docs/exchanges/digifinex#fetchleveragetiers)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#fetchleveragetiers)
- [hashkey](https://docs.ccxt.com/docs/exchanges/hashkey#fetchleveragetiers)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#fetchleveragetiers)
- [krakenfutures](https://docs.ccxt.com/docs/exchanges/krakenfutures#fetchleveragetiers)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchleveragetiers)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#fetchleveragetiers)
- [phemex](https://docs.ccxt.com/docs/exchanges/phemex#fetchleveragetiers)
- [xt](https://docs.ccxt.com/docs/exchanges/xt#fetchleveragetiers)

* * *

## [fetchLeverages](https://docs.ccxt.com/docs/base-spec\#fetchleverages)

fetch the set leverage for all markets

**Kind**: instance

**Returns**: `object` \- a list of [leverage structures](https://docs.ccxt.com/docs/manual#leverage-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>` | No | a list of unified market symbols |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-114)

- [aster](https://docs.ccxt.com/docs/exchanges/aster#fetchleverages)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchleverages)
- [blofin](https://docs.ccxt.com/docs/exchanges/blofin#fetchleverages)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#fetchleverages)
- [grvt](https://docs.ccxt.com/docs/exchanges/grvt#fetchleverages)
- [krakenfutures](https://docs.ccxt.com/docs/exchanges/krakenfutures#fetchleverages)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#fetchleverages)
- [zebpay](https://docs.ccxt.com/docs/exchanges/zebpay#fetchleverages)

* * *

## [fetchLiquidations](https://docs.ccxt.com/docs/base-spec\#fetchliquidations)

retrieves the public liquidations of a trading pair

**Kind**: instance

**Returns**: `object` \- an array of [liquidation structures](https://docs.ccxt.com/docs/manual#liquidation-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified CCXT market symbol |
| since | `int` | No | the earliest time in ms to fetch liquidations for |
| limit | `int` | No | the maximum number of liquidation structures to retrieve |
| params | `object` | No | exchange specific parameters |
| params.until | `int` | No | timestamp in ms of the latest liquidation |
| params.paginate | `boolean` | No | default false, when true will automatically paginate by calling this endpoint multiple times. See in the docs all the [available parameters](https://docs.ccxt.com/docs/manual#pagination-params) |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-115)

- [bitfinex](https://docs.ccxt.com/docs/exchanges/bitfinex#fetchliquidations)
- [deribit](https://docs.ccxt.com/docs/exchanges/deribit#fetchliquidations)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#fetchliquidations)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#fetchliquidations)

* * *

## [fetchLongShortRatioHistory](https://docs.ccxt.com/docs/base-spec\#fetchlongshortratiohistory)

fetches the long short ratio history for a unified market symbol

**Kind**: instance

**Returns**: `Array<object>` \- an array of [long short ratio structures](https://docs.ccxt.com/docs/manual#long-short-ratio-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to fetch the long short ratio for |
| timeframe | `string` | No | the period for the ratio, default is 24 hours |
| since | `int` | No | the earliest time in ms to fetch ratios for |
| limit | `int` | No | the maximum number of long short ratio structures to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.until | `int` | No | timestamp in ms of the latest ratio to fetch |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-116)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchlongshortratiohistory)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#fetchlongshortratiohistory)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchlongshortratiohistory)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchlongshortratiohistory)

* * *

## [fetchMarginAdjustmentHistory](https://docs.ccxt.com/docs/base-spec\#fetchmarginadjustmenthistory)

fetches the history of margin added or reduced from contract isolated positions

**Kind**: instance

**Returns**: `Array<object>` \- a list of [margin structures](https://docs.ccxt.com/docs/manual#margin-loan-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol |
| type | `string` | No | "add" or "reduce" |
| since | `int` | No | timestamp in ms of the earliest change to fetch |
| limit | `int` | No | the maximum amount of changes to fetch |
| params | `object` | Yes | extra parameters specific to the exchange API endpoint |
| params.until | `int` | No | timestamp in ms of the latest change to fetch |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-117)

- [aster](https://docs.ccxt.com/docs/exchanges/aster#fetchmarginadjustmenthistory)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchmarginadjustmenthistory)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#fetchmarginadjustmenthistory)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchmarginadjustmenthistory)

* * *

## [fetchMarginMode](https://docs.ccxt.com/docs/base-spec\#fetchmarginmode)

fetches the margin mode of a specific symbol

**Kind**: instance

**Returns**: `object` \- a [margin mode structure](https://docs.ccxt.com/docs/manual#margin-mode-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market the order was made in |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.subType | `string` | No | "linear" or "inverse" |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-118)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchmarginmode)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#fetchmarginmode)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#fetchmarginmode)
- [blofin](https://docs.ccxt.com/docs/exchanges/blofin#fetchmarginmode)
- [btse](https://docs.ccxt.com/docs/exchanges/btse#fetchmarginmode)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchmarginmode)
- [bydfi](https://docs.ccxt.com/docs/exchanges/bydfi#fetchmarginmode)
- [delta](https://docs.ccxt.com/docs/exchanges/delta#fetchmarginmode)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchmarginmode)
- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#fetchmarginmode)
- [paradex](https://docs.ccxt.com/docs/exchanges/paradex#fetchmarginmode)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#fetchmarginmode)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#fetchmarginmode)

* * *

## [fetchMarginModes](https://docs.ccxt.com/docs/base-spec\#fetchmarginmodes)

fetches margin mode of the user

**Kind**: instance

**Returns**: `object` \- a list of [margin mode structures](https://docs.ccxt.com/docs/manual#margin-mode-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>` | Yes | unified market symbols |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-119)

- [aster](https://docs.ccxt.com/docs/exchanges/aster#fetchmarginmodes)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchmarginmodes)
- [grvt](https://docs.ccxt.com/docs/exchanges/grvt#fetchmarginmodes)
- [hitbtc](https://docs.ccxt.com/docs/exchanges/hitbtc#fetchmarginmodes)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#fetchmarginmodes)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#fetchmarginmodes)

* * *

## [fetchMarkOHLCV](https://docs.ccxt.com/docs/base-spec\#fetchmarkohlcv)

fetches historical mark price candlestick data containing the open, high, low, and close price of a market

**Kind**: instance

**Returns**: `Array<Array<int>>` \- A list of candles ordered as timestamp, open, high, low, close, volume

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to fetch OHLCV data for |
| timeframe | `string` | Yes | the length of time each candle represents |
| since | `int` | No | timestamp in ms of the earliest candle to fetch |
| limit | `int` | No | the maximum amount of candles to fetch |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-120)

- [mudrex](https://docs.ccxt.com/docs/exchanges/mudrex#fetchmarkohlcv)

* * *

## [fetchMarkPrice](https://docs.ccxt.com/docs/base-spec\#fetchmarkprice)

fetches mark price for the market

**Kind**: instance

**Returns**: `object` \- a dictionary of [ticker structures](https://docs.ccxt.com/docs/manual#ticker-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to fetch the ticker for |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.subType | `string` | No | "linear" or "inverse" |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-121)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchmarkprice)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#fetchmarkprice)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#fetchmarkprice)
- [blofin](https://docs.ccxt.com/docs/exchanges/blofin#fetchmarkprice)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchmarkprice)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchmarkprice)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#fetchmarkprice)

* * *

## [fetchMarkPrices](https://docs.ccxt.com/docs/base-spec\#fetchmarkprices)

fetches mark prices for multiple markets

**Kind**: instance

**Returns**: `object` \- a dictionary of [ticker structures](https://docs.ccxt.com/docs/manual#ticker-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>` | No | unified symbols of the markets to fetch the ticker for, all market tickers are returned if not assigned |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.subType | `string` | No | "linear" or "inverse" |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-122)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchmarkprices)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#fetchmarkprices)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchmarkprices)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchmarkprices)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#fetchmarkprices)

* * *

## [fetchMarketLeverageTiers](https://docs.ccxt.com/docs/base-spec\#fetchmarketleveragetiers)

retrieve information on the maximum leverage, for different trade sizes for a single market

**Kind**: instance

**Returns**: `object` \- a [leverage tiers structure](https://docs.ccxt.com/docs/manual#leverage-tiers-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol, inverse (Coin-M) markets are not supported |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-123)

- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#fetchmarketleveragetiers)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#fetchmarketleveragetiers)
- [btse](https://docs.ccxt.com/docs/exchanges/btse#fetchmarketleveragetiers)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchmarketleveragetiers)
- [digifinex](https://docs.ccxt.com/docs/exchanges/digifinex#fetchmarketleveragetiers)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#fetchmarketleveragetiers)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchmarketleveragetiers)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchmarketleveragetiers)
- [xt](https://docs.ccxt.com/docs/exchanges/xt#fetchmarketleveragetiers)

* * *

## [fetchMarkets](https://docs.ccxt.com/docs/base-spec\#fetchmarkets)

retrieves data on all markets for alpaca

**Kind**: instance

**Returns**: `Array<object>` \- an array of objects representing market data

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-124)

- [alpaca](https://docs.ccxt.com/docs/exchanges/alpaca#fetchmarkets)
- [apex](https://docs.ccxt.com/docs/exchanges/apex#fetchmarkets)
- [aster](https://docs.ccxt.com/docs/exchanges/aster#fetchmarkets)
- [backpack](https://docs.ccxt.com/docs/exchanges/backpack#fetchmarkets)
- [bigone](https://docs.ccxt.com/docs/exchanges/bigone#fetchmarkets)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchmarkets)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#fetchmarkets)
- [bitbank](https://docs.ccxt.com/docs/exchanges/bitbank#fetchmarkets)
- [bitbns](https://docs.ccxt.com/docs/exchanges/bitbns#fetchmarkets)
- [bitfinex](https://docs.ccxt.com/docs/exchanges/bitfinex#fetchmarkets)
- [bitflyer](https://docs.ccxt.com/docs/exchanges/bitflyer#fetchmarkets)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#fetchmarkets)
- [bithumb](https://docs.ccxt.com/docs/exchanges/bithumb#fetchmarkets)
- [bitopro](https://docs.ccxt.com/docs/exchanges/bitopro#fetchmarkets)
- [bitrue](https://docs.ccxt.com/docs/exchanges/bitrue#fetchmarkets)
- [bitso](https://docs.ccxt.com/docs/exchanges/bitso#fetchmarkets)
- [bitstamp](https://docs.ccxt.com/docs/exchanges/bitstamp#fetchmarkets)
- [bitteam](https://docs.ccxt.com/docs/exchanges/bitteam#fetchmarkets)
- [bittrade](https://docs.ccxt.com/docs/exchanges/bittrade#fetchmarkets)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#fetchmarkets)
- [blockchaincom](https://docs.ccxt.com/docs/exchanges/blockchaincom#fetchmarkets)
- [blofin](https://docs.ccxt.com/docs/exchanges/blofin#fetchmarkets)
- [btcbox](https://docs.ccxt.com/docs/exchanges/btcbox#fetchmarkets)
- [btcmarkets](https://docs.ccxt.com/docs/exchanges/btcmarkets#fetchmarkets)
- [btcturk](https://docs.ccxt.com/docs/exchanges/btcturk#fetchmarkets)
- [btse](https://docs.ccxt.com/docs/exchanges/btse#fetchmarkets)
- [bullish](https://docs.ccxt.com/docs/exchanges/bullish#fetchmarkets)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchmarkets)
- [bydfi](https://docs.ccxt.com/docs/exchanges/bydfi#fetchmarkets)
- [cex](https://docs.ccxt.com/docs/exchanges/cex#fetchmarkets)
- [coinbase](https://docs.ccxt.com/docs/exchanges/coinbase#fetchmarkets)
- [coinbaseexchange](https://docs.ccxt.com/docs/exchanges/coinbaseexchange#fetchmarkets)
- [coinbaseinternational](https://docs.ccxt.com/docs/exchanges/coinbaseinternational#fetchmarkets)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#fetchmarkets)
- [coinmate](https://docs.ccxt.com/docs/exchanges/coinmate#fetchmarkets)
- [coinone](https://docs.ccxt.com/docs/exchanges/coinone#fetchmarkets)
- [coinsph](https://docs.ccxt.com/docs/exchanges/coinsph#fetchmarkets)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#fetchmarkets)
- [cryptomus](https://docs.ccxt.com/docs/exchanges/cryptomus#fetchmarkets)
- [deepcoin](https://docs.ccxt.com/docs/exchanges/deepcoin#fetchmarkets)
- [delta](https://docs.ccxt.com/docs/exchanges/delta#fetchmarkets)
- [deribit](https://docs.ccxt.com/docs/exchanges/deribit#fetchmarkets)
- [derive](https://docs.ccxt.com/docs/exchanges/derive#fetchmarkets)
- [digifinex](https://docs.ccxt.com/docs/exchanges/digifinex#fetchmarkets)
- [dydx](https://docs.ccxt.com/docs/exchanges/dydx#fetchmarkets)
- [extended](https://docs.ccxt.com/docs/exchanges/extended#fetchmarkets)
- [foxbit](https://docs.ccxt.com/docs/exchanges/foxbit#fetchmarkets)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#fetchmarkets)
- [gemini](https://docs.ccxt.com/docs/exchanges/gemini#fetchmarkets)
- [grvt](https://docs.ccxt.com/docs/exchanges/grvt#fetchmarkets)
- [hashkey](https://docs.ccxt.com/docs/exchanges/hashkey#fetchmarkets)
- [hibachi](https://docs.ccxt.com/docs/exchanges/hibachi#fetchmarkets)
- [hitbtc](https://docs.ccxt.com/docs/exchanges/hitbtc#fetchmarkets)
- [hollaex](https://docs.ccxt.com/docs/exchanges/hollaex#fetchmarkets)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#fetchmarkets)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#fetchmarkets)
- [independentreserve](https://docs.ccxt.com/docs/exchanges/independentreserve#fetchmarkets)
- [indodax](https://docs.ccxt.com/docs/exchanges/indodax#fetchmarkets)
- [kraken](https://docs.ccxt.com/docs/exchanges/kraken#fetchmarkets)
- [krakenfutures](https://docs.ccxt.com/docs/exchanges/krakenfutures#fetchmarkets)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchmarkets)
- [latoken](https://docs.ccxt.com/docs/exchanges/latoken#fetchmarkets)
- [lbank](https://docs.ccxt.com/docs/exchanges/lbank#fetchmarkets)
- [lighter](https://docs.ccxt.com/docs/exchanges/lighter#fetchmarkets)
- [luno](https://docs.ccxt.com/docs/exchanges/luno#fetchmarkets)
- [mercado](https://docs.ccxt.com/docs/exchanges/mercado#fetchmarkets)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#fetchmarkets)
- [modetrade](https://docs.ccxt.com/docs/exchanges/modetrade#fetchmarkets)
- [mudrex](https://docs.ccxt.com/docs/exchanges/mudrex#fetchmarkets)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#fetchmarkets)
- [ndax](https://docs.ccxt.com/docs/exchanges/ndax#fetchmarkets)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchmarkets)
- [onetrading](https://docs.ccxt.com/docs/exchanges/onetrading#fetchmarkets)
- [p2b](https://docs.ccxt.com/docs/exchanges/p2b#fetchmarkets)
- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#fetchmarkets)
- [paradex](https://docs.ccxt.com/docs/exchanges/paradex#fetchmarkets)
- [phemex](https://docs.ccxt.com/docs/exchanges/phemex#fetchmarkets)
- [poloniex](https://docs.ccxt.com/docs/exchanges/poloniex#fetchmarkets)
- [revolutx](https://docs.ccxt.com/docs/exchanges/revolutx#fetchmarkets)
- [tokocrypto](https://docs.ccxt.com/docs/exchanges/tokocrypto#fetchmarkets)
- [toobit](https://docs.ccxt.com/docs/exchanges/toobit#fetchmarkets)
- [upbit](https://docs.ccxt.com/docs/exchanges/upbit#fetchmarkets)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#fetchmarkets)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#fetchmarkets)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#fetchmarkets)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#fetchmarkets)
- [xt](https://docs.ccxt.com/docs/exchanges/xt#fetchmarkets)
- [zaif](https://docs.ccxt.com/docs/exchanges/zaif#fetchmarkets)
- [zebpay](https://docs.ccxt.com/docs/exchanges/zebpay#fetchmarkets)

* * *

## [fetchMarketsWs](https://docs.ccxt.com/docs/base-spec\#fetchmarketsws)

retrieves data on all markets for bitvavo

**Kind**: instance

**Returns**: `Array<object>` \- an array of objects representing market data

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-125)

- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#fetchmarketsws)

* * *

## [fetchMyContractTrades](https://docs.ccxt.com/docs/base-spec\#fetchmycontracttrades)

fetch all contract trades made by the user

**Kind**: instance

**Returns**: `Array<Trade>` \- a list of [trade structures](https://docs.ccxt.com/docs/manual#trade-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol |
| since | `int` | No | the earliest time in ms to fetch trades for |
| limit | `int` | No | the maximum number of trades structures to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.until | `int` | No | End time in ms |
| params.paginate | `boolean` | No | default false, when true will automatically paginate by calling this endpoint multiple times. See in the docs all the [availble parameters](https://docs.ccxt.com/docs/manual#pagination-params) |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-126)

- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchmycontracttrades)

* * *

## [fetchMyDustTrades](https://docs.ccxt.com/docs/base-spec\#fetchmydusttrades)

fetch all dust trades made by the user

**Kind**: instance

**Returns**: `Array<object>` \- a list of [trade structures](https://docs.ccxt.com/docs/manual#trade-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | not used by fetchMyDustTrades () |
| since | `int` | No | the earliest time in ms to fetch my dust trades for |
| limit | `int` | No | the maximum number of dust trades to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.type | `string` | No | 'spot' or 'margin', default spot |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-127)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchmydusttrades)

* * *

## [fetchMyLiquidations](https://docs.ccxt.com/docs/base-spec\#fetchmyliquidations)

retrieves the users liquidated positions

**Kind**: instance

**Returns**: `object` \- an array of [liquidation structures](https://docs.ccxt.com/docs/manual#liquidation-structure)

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

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-128)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchmyliquidations)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#fetchmyliquidations)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#fetchmyliquidations)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchmyliquidations)
- [deribit](https://docs.ccxt.com/docs/exchanges/deribit#fetchmyliquidations)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#fetchmyliquidations)
- [paradex](https://docs.ccxt.com/docs/exchanges/paradex#fetchmyliquidations)

* * *

## [fetchMySettlementHistory](https://docs.ccxt.com/docs/base-spec\#fetchmysettlementhistory)

fetches historical settlement records of the user

**Kind**: instance

**Returns**: `Array<object>` \- a list of \[settlement history objects\]

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol of the settlement history |
| since | `int` | No | timestamp in ms |
| limit | `int` | No | number of records |
| params | `object` | No | exchange specific params |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-129)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchmysettlementhistory)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchmysettlementhistory)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#fetchmysettlementhistory)
- [hibachi](https://docs.ccxt.com/docs/exchanges/hibachi#fetchmysettlementhistory)

* * *

## [fetchMySpotTrades](https://docs.ccxt.com/docs/base-spec\#fetchmyspottrades)

fetch all spot trades made by the user

**Kind**: instance

**Returns**: `Array<Trade>` \- a list of [trade structures](https://docs.ccxt.com/docs/manual#trade-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol |
| since | `int` | No | the earliest time in ms to fetch trades for |
| limit | `int` | No | the maximum number of trades structures to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.until | `int` | No | the latest time in ms to fetch entries for |
| params.hf | `bool` | No | false, // true for hf order |
| params.marginMode | `string` | No | 'cross' or 'isolated', only for margin trades |
| params.paginate | `boolean` | No | default false, when true will automatically paginate by calling this endpoint multiple times. See in the docs all the [availble parameters](https://docs.ccxt.com/docs/manual#pagination-params) |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-130)

- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchmyspottrades)

* * *

## [fetchMyTrades](https://docs.ccxt.com/docs/base-spec\#fetchmytrades)

fetch all trades made by the user

**Kind**: instance

**Returns**: `Array<Trade>` \- a list of [trade structures](https://docs.ccxt.com/docs/manual#trade-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | No | unified market symbol |
| since | `int` | No | the earliest time in ms to fetch trades for |
| limit | `int` | No | the maximum number of trade structures to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.until | `int` | No | the latest time in ms to fetch trades for |
| params.page\_token | `string` | No | page\_token - used for paging |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-131)

- [alpaca](https://docs.ccxt.com/docs/exchanges/alpaca#fetchmytrades)
- [apex](https://docs.ccxt.com/docs/exchanges/apex#fetchmytrades)
- [aster](https://docs.ccxt.com/docs/exchanges/aster#fetchmytrades)
- [backpack](https://docs.ccxt.com/docs/exchanges/backpack#fetchmytrades)
- [bigone](https://docs.ccxt.com/docs/exchanges/bigone#fetchmytrades)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchmytrades)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#fetchmytrades)
- [bit2c](https://docs.ccxt.com/docs/exchanges/bit2c#fetchmytrades)
- [bitbank](https://docs.ccxt.com/docs/exchanges/bitbank#fetchmytrades)
- [bitbns](https://docs.ccxt.com/docs/exchanges/bitbns#fetchmytrades)
- [bitfinex](https://docs.ccxt.com/docs/exchanges/bitfinex#fetchmytrades)
- [bitflyer](https://docs.ccxt.com/docs/exchanges/bitflyer#fetchmytrades)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#fetchmytrades)
- [bitopro](https://docs.ccxt.com/docs/exchanges/bitopro#fetchmytrades)
- [bitrue](https://docs.ccxt.com/docs/exchanges/bitrue#fetchmytrades)
- [bitso](https://docs.ccxt.com/docs/exchanges/bitso#fetchmytrades)
- [bitstamp](https://docs.ccxt.com/docs/exchanges/bitstamp#fetchmytrades)
- [bitteam](https://docs.ccxt.com/docs/exchanges/bitteam#fetchmytrades)
- [bittrade](https://docs.ccxt.com/docs/exchanges/bittrade#fetchmytrades)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#fetchmytrades)
- [blockchaincom](https://docs.ccxt.com/docs/exchanges/blockchaincom#fetchmytrades)
- [blofin](https://docs.ccxt.com/docs/exchanges/blofin#fetchmytrades)
- [btcmarkets](https://docs.ccxt.com/docs/exchanges/btcmarkets#fetchmytrades)
- [btcturk](https://docs.ccxt.com/docs/exchanges/btcturk#fetchmytrades)
- [btse](https://docs.ccxt.com/docs/exchanges/btse#fetchmytrades)
- [bullish](https://docs.ccxt.com/docs/exchanges/bullish#fetchmytrades)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchmytrades)
- [bydfi](https://docs.ccxt.com/docs/exchanges/bydfi#fetchmytrades)
- [coinbase](https://docs.ccxt.com/docs/exchanges/coinbase#fetchmytrades)
- [coinbaseexchange](https://docs.ccxt.com/docs/exchanges/coinbaseexchange#fetchmytrades)
- [coinbaseinternational](https://docs.ccxt.com/docs/exchanges/coinbaseinternational#fetchmytrades)
- [coincheck](https://docs.ccxt.com/docs/exchanges/coincheck#fetchmytrades)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#fetchmytrades)
- [coinmate](https://docs.ccxt.com/docs/exchanges/coinmate#fetchmytrades)
- [coinone](https://docs.ccxt.com/docs/exchanges/coinone#fetchmytrades)
- [coinsph](https://docs.ccxt.com/docs/exchanges/coinsph#fetchmytrades)
- [coinspot](https://docs.ccxt.com/docs/exchanges/coinspot#fetchmytrades)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#fetchmytrades)
- [deepcoin](https://docs.ccxt.com/docs/exchanges/deepcoin#fetchmytrades)
- [delta](https://docs.ccxt.com/docs/exchanges/delta#fetchmytrades)
- [deribit](https://docs.ccxt.com/docs/exchanges/deribit#fetchmytrades)
- [derive](https://docs.ccxt.com/docs/exchanges/derive#fetchmytrades)
- [digifinex](https://docs.ccxt.com/docs/exchanges/digifinex#fetchmytrades)
- [extended](https://docs.ccxt.com/docs/exchanges/extended#fetchmytrades)
- [foxbit](https://docs.ccxt.com/docs/exchanges/foxbit#fetchmytrades)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#fetchmytrades)
- [gemini](https://docs.ccxt.com/docs/exchanges/gemini#fetchmytrades)
- [grvt](https://docs.ccxt.com/docs/exchanges/grvt#fetchmytrades)
- [hashkey](https://docs.ccxt.com/docs/exchanges/hashkey#fetchmytrades)
- [hibachi](https://docs.ccxt.com/docs/exchanges/hibachi#fetchmytrades)
- [hitbtc](https://docs.ccxt.com/docs/exchanges/hitbtc#fetchmytrades)
- [hollaex](https://docs.ccxt.com/docs/exchanges/hollaex#fetchmytrades)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#fetchmytrades)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#fetchmytrades)
- [independentreserve](https://docs.ccxt.com/docs/exchanges/independentreserve#fetchmytrades)
- [kraken](https://docs.ccxt.com/docs/exchanges/kraken#fetchmytrades)
- [krakenfutures](https://docs.ccxt.com/docs/exchanges/krakenfutures#fetchmytrades)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchmytrades)
- [latoken](https://docs.ccxt.com/docs/exchanges/latoken#fetchmytrades)
- [lbank](https://docs.ccxt.com/docs/exchanges/lbank#fetchmytrades)
- [lighter](https://docs.ccxt.com/docs/exchanges/lighter#fetchmytrades)
- [luno](https://docs.ccxt.com/docs/exchanges/luno#fetchmytrades)
- [mercado](https://docs.ccxt.com/docs/exchanges/mercado#fetchmytrades)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#fetchmytrades)
- [modetrade](https://docs.ccxt.com/docs/exchanges/modetrade#fetchmytrades)
- [mudrex](https://docs.ccxt.com/docs/exchanges/mudrex#fetchmytrades)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#fetchmytrades)
- [ndax](https://docs.ccxt.com/docs/exchanges/ndax#fetchmytrades)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchmytrades)
- [onetrading](https://docs.ccxt.com/docs/exchanges/onetrading#fetchmytrades)
- [p2b](https://docs.ccxt.com/docs/exchanges/p2b#fetchmytrades)
- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#fetchmytrades)
- [paradex](https://docs.ccxt.com/docs/exchanges/paradex#fetchmytrades)
- [phemex](https://docs.ccxt.com/docs/exchanges/phemex#fetchmytrades)
- [poloniex](https://docs.ccxt.com/docs/exchanges/poloniex#fetchmytrades)
- [revolutx](https://docs.ccxt.com/docs/exchanges/revolutx#fetchmytrades)
- [tokocrypto](https://docs.ccxt.com/docs/exchanges/tokocrypto#fetchmytrades)
- [toobit](https://docs.ccxt.com/docs/exchanges/toobit#fetchmytrades)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#fetchmytrades)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#fetchmytrades)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#fetchmytrades)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#fetchmytrades)
- [xt](https://docs.ccxt.com/docs/exchanges/xt#fetchmytrades)
- [zebpay](https://docs.ccxt.com/docs/exchanges/zebpay#fetchmytrades)

* * *

## [fetchMyTradesWs](https://docs.ccxt.com/docs/base-spec\#fetchmytradesws)

fetch all trades made by the user

**Kind**: instance

**Returns**: `Array<object>` \- a list of [trade structures](https://docs.ccxt.com/docs/manual#trade-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol |
| since | `int`, `undefined` | No | the earliest time in ms to fetch trades for |
| limit | `int`, `undefined` | No | the maximum number of trades structures to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.endTime | `int` | No | the latest time in ms to fetch trades for |
| params.fromId | `int` | No | first trade Id to fetch |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-132)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchmytradesws)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#fetchmytradesws)

* * *

## [fetchMyUtaTrades](https://docs.ccxt.com/docs/base-spec\#fetchmyutatrades)

fetch all trades made by the user

**Kind**: instance

**Returns**: `Array<Trade>` \- a list of [trade structures](https://docs.ccxt.com/docs/manual#trade-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol |
| since | `int` | No | the earliest time in ms to fetch trades for |
| limit | `int` | No | the maximum number of trades structures to retrieve (default is 50, max is 200) |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.until | `int` | No | the latest time in ms to fetch entries for |
| params.accountMode | `string` | No | 'unified' or 'classic', defaults to 'unified' |
| params.marginMode | `string` | No | 'cross' or 'isolated', only for margin trades (unified accountMode support only cross margin) |
| params.side | `string` | No | 'BUY' or 'SELL' (both if not provided) |
| params.paginate | `boolean` | No | default false, when true will automatically paginate by calling this endpoint multiple times. See in the docs all the [availble parameters](https://docs.ccxt.com/docs/manual#pagination-params) |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-133)

- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchmyutatrades)

* * *

## [fetchOHLCV](https://docs.ccxt.com/docs/base-spec\#fetchohlcv)

fetches historical candlestick data containing the open, high, low, and close price, and the volume of a market

**Kind**: instance

**Returns**: `Array<Array<int>>` \- A list of candles ordered as timestamp, open, high, low, close, volume

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to fetch OHLCV data for |
| timeframe | `string` | Yes | the length of time each candle represents |
| since | `int` | No | timestamp in ms of the earliest candle to fetch |
| limit | `int` | No | the maximum amount of candles to fetch |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.until | `int` | No | timestamp in ms of the latest candle to fetch |
| params.paginate | `boolean` | No | default false, when true will automatically paginate by calling this endpoint multiple times. See in the docs all the [available parameters](https://docs.ccxt.com/docs/manual#pagination-params) |
| params.paginationCalls | `int` | No | the maximum number of requests while following next\_page\_token, default 10 — when the cap is reached the result is silently truncated to the pages already fetched, so raise it for long ranges, 10 requests cover roughly 30 days of 1h candles |
| params.loc | `string` | No | crypto location, default: us |
| params.method | `string` | No | method, default: marketPublicGetV1beta3CryptoLocBars |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-134)

- [alpaca](https://docs.ccxt.com/docs/exchanges/alpaca#fetchohlcv)
- [apex](https://docs.ccxt.com/docs/exchanges/apex#fetchohlcv)
- [aster](https://docs.ccxt.com/docs/exchanges/aster#fetchohlcv)
- [backpack](https://docs.ccxt.com/docs/exchanges/backpack#fetchohlcv)
- [bigone](https://docs.ccxt.com/docs/exchanges/bigone#fetchohlcv)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchohlcv)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#fetchohlcv)
- [bitbank](https://docs.ccxt.com/docs/exchanges/bitbank#fetchohlcv)
- [bitfinex](https://docs.ccxt.com/docs/exchanges/bitfinex#fetchohlcv)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#fetchohlcv)
- [bithumb](https://docs.ccxt.com/docs/exchanges/bithumb#fetchohlcv)
- [bitopro](https://docs.ccxt.com/docs/exchanges/bitopro#fetchohlcv)
- [bitrue](https://docs.ccxt.com/docs/exchanges/bitrue#fetchohlcv)
- [bitso](https://docs.ccxt.com/docs/exchanges/bitso#fetchohlcv)
- [bitstamp](https://docs.ccxt.com/docs/exchanges/bitstamp#fetchohlcv)
- [bitteam](https://docs.ccxt.com/docs/exchanges/bitteam#fetchohlcv)
- [bittrade](https://docs.ccxt.com/docs/exchanges/bittrade#fetchohlcv)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#fetchohlcv)
- [blofin](https://docs.ccxt.com/docs/exchanges/blofin#fetchohlcv)
- [btcmarkets](https://docs.ccxt.com/docs/exchanges/btcmarkets#fetchohlcv)
- [btcturk](https://docs.ccxt.com/docs/exchanges/btcturk#fetchohlcv)
- [btse](https://docs.ccxt.com/docs/exchanges/btse#fetchohlcv)
- [bullish](https://docs.ccxt.com/docs/exchanges/bullish#fetchohlcv)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchohlcv)
- [bydfi](https://docs.ccxt.com/docs/exchanges/bydfi#fetchohlcv)
- [cex](https://docs.ccxt.com/docs/exchanges/cex#fetchohlcv)
- [coinbase](https://docs.ccxt.com/docs/exchanges/coinbase#fetchohlcv)
- [coinbaseexchange](https://docs.ccxt.com/docs/exchanges/coinbaseexchange#fetchohlcv)
- [coinbaseinternational](https://docs.ccxt.com/docs/exchanges/coinbaseinternational#fetchohlcv)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#fetchohlcv)
- [coinsph](https://docs.ccxt.com/docs/exchanges/coinsph#fetchohlcv)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#fetchohlcv)
- [deepcoin](https://docs.ccxt.com/docs/exchanges/deepcoin#fetchohlcv)
- [delta](https://docs.ccxt.com/docs/exchanges/delta#fetchohlcv)
- [deribit](https://docs.ccxt.com/docs/exchanges/deribit#fetchohlcv)
- [digifinex](https://docs.ccxt.com/docs/exchanges/digifinex#fetchohlcv)
- [dydx](https://docs.ccxt.com/docs/exchanges/dydx#fetchohlcv)
- [extended](https://docs.ccxt.com/docs/exchanges/extended#fetchohlcv)
- [foxbit](https://docs.ccxt.com/docs/exchanges/foxbit#fetchohlcv)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#fetchohlcv)
- [gemini](https://docs.ccxt.com/docs/exchanges/gemini#fetchohlcv)
- [grvt](https://docs.ccxt.com/docs/exchanges/grvt#fetchohlcv)
- [hashkey](https://docs.ccxt.com/docs/exchanges/hashkey#fetchohlcv)
- [hibachi](https://docs.ccxt.com/docs/exchanges/hibachi#fetchohlcv)
- [hitbtc](https://docs.ccxt.com/docs/exchanges/hitbtc#fetchohlcv)
- [hollaex](https://docs.ccxt.com/docs/exchanges/hollaex#fetchohlcv)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#fetchohlcv)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#fetchohlcv)
- [indodax](https://docs.ccxt.com/docs/exchanges/indodax#fetchohlcv)
- [kraken](https://docs.ccxt.com/docs/exchanges/kraken#fetchohlcv)
- [krakenfutures](https://docs.ccxt.com/docs/exchanges/krakenfutures#fetchohlcv)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchohlcv)
- [lbank](https://docs.ccxt.com/docs/exchanges/lbank#fetchohlcv)
- [lighter](https://docs.ccxt.com/docs/exchanges/lighter#fetchohlcv)
- [luno](https://docs.ccxt.com/docs/exchanges/luno#fetchohlcv)
- [mercado](https://docs.ccxt.com/docs/exchanges/mercado#fetchohlcv)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#fetchohlcv)
- [modetrade](https://docs.ccxt.com/docs/exchanges/modetrade#fetchohlcv)
- [mudrex](https://docs.ccxt.com/docs/exchanges/mudrex#fetchohlcv)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#fetchohlcv)
- [ndax](https://docs.ccxt.com/docs/exchanges/ndax#fetchohlcv)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchohlcv)
- [onetrading](https://docs.ccxt.com/docs/exchanges/onetrading#fetchohlcv)
- [p2b](https://docs.ccxt.com/docs/exchanges/p2b#fetchohlcv)
- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#fetchohlcv)
- [paradex](https://docs.ccxt.com/docs/exchanges/paradex#fetchohlcv)
- [phemex](https://docs.ccxt.com/docs/exchanges/phemex#fetchohlcv)
- [poloniex](https://docs.ccxt.com/docs/exchanges/poloniex#fetchohlcv)
- [revolutx](https://docs.ccxt.com/docs/exchanges/revolutx#fetchohlcv)
- [tokocrypto](https://docs.ccxt.com/docs/exchanges/tokocrypto#fetchohlcv)
- [toobit](https://docs.ccxt.com/docs/exchanges/toobit#fetchohlcv)
- [upbit](https://docs.ccxt.com/docs/exchanges/upbit#fetchohlcv)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#fetchohlcv)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#fetchohlcv)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#fetchohlcv)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#fetchohlcv)
- [xt](https://docs.ccxt.com/docs/exchanges/xt#fetchohlcv)
- [zebpay](https://docs.ccxt.com/docs/exchanges/zebpay#fetchohlcv)

* * *

## [fetchOHLCVWs](https://docs.ccxt.com/docs/base-spec\#fetchohlcvws)

query historical candlestick data containing the open, high, low, and close price, and the volume of a market

**Kind**: instance

**Returns**: `Array<Array<int>>` \- A list of candles ordered as timestamp, open, high, low, close, volume

| Param | Type | Description |
| --- | --- | --- |
| symbol | `string` | unified symbol of the market to query OHLCV data for |
| timeframe | `string` | the length of time each candle represents |
| since | `int` | timestamp in ms of the earliest candle to fetch |
| limit | `int` | the maximum amount of candles to fetch |
| params | `object` | extra parameters specific to the exchange API endpoint |
| params.until | `int` | timestamp in ms of the earliest candle to fetch EXCHANGE SPECIFIC PARAMETERS |
| params.timeZone | `string` | default=0 (UTC) |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-135)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchohlcvws)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#fetchohlcvws)
- [lbank](https://docs.ccxt.com/docs/exchanges/lbank#fetchohlcvws)

* * *

## [fetchOpenInterest](https://docs.ccxt.com/docs/base-spec\#fetchopeninterest)

retrieves the open interest of a contract trading pair

**Kind**: instance

**Returns**: `object` \- an open interest structure [/docs/manual#open-interest-structure](https://docs.ccxt.com/docs/manual#open-interest-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified CCXT market symbol |
| params | `object` | No | exchange specific parameters |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-136)

- [apex](https://docs.ccxt.com/docs/exchanges/apex#fetchopeninterest)
- [backpack](https://docs.ccxt.com/docs/exchanges/backpack#fetchopeninterest)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchopeninterest)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#fetchopeninterest)
- [bitfinex](https://docs.ccxt.com/docs/exchanges/bitfinex#fetchopeninterest)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#fetchopeninterest)
- [btse](https://docs.ccxt.com/docs/exchanges/btse#fetchopeninterest)
- [bullish](https://docs.ccxt.com/docs/exchanges/bullish#fetchopeninterest)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchopeninterest)
- [delta](https://docs.ccxt.com/docs/exchanges/delta#fetchopeninterest)
- [deribit](https://docs.ccxt.com/docs/exchanges/deribit#fetchopeninterest)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#fetchopeninterest)
- [gemini](https://docs.ccxt.com/docs/exchanges/gemini#fetchopeninterest)
- [hibachi](https://docs.ccxt.com/docs/exchanges/hibachi#fetchopeninterest)
- [hitbtc](https://docs.ccxt.com/docs/exchanges/hitbtc#fetchopeninterest)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#fetchopeninterest)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#fetchopeninterest)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#fetchopeninterest)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchopeninterest)
- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#fetchopeninterest)
- [paradex](https://docs.ccxt.com/docs/exchanges/paradex#fetchopeninterest)
- [phemex](https://docs.ccxt.com/docs/exchanges/phemex#fetchopeninterest)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#fetchopeninterest)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#fetchopeninterest)
- [xt](https://docs.ccxt.com/docs/exchanges/xt#fetchopeninterest)

* * *

## [fetchOpenInterestHistory](https://docs.ccxt.com/docs/base-spec\#fetchopeninteresthistory)

Retrieves the open interest history of a currency

**Kind**: instance

**Returns**: `object` \- an array of [open interest structure](https://docs.ccxt.com/docs/manual#open-interest-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | Unified CCXT market symbol |
| timeframe | `string` | Yes | "5m","15m","30m","1h","2h","4h","6h","12h", or "1d" |
| since | `int` | No | the time(ms) of the earliest record to retrieve as a unix timestamp |
| limit | `int` | No | default 30, max 500 |
| params | `object` | No | exchange specific parameters |
| params.until | `int` | No | the time(ms) of the latest record to retrieve as a unix timestamp |
| params.paginate | `boolean` | No | default false, when true will automatically paginate by calling this endpoint multiple times. See in the docs all the [availble parameters](https://docs.ccxt.com/docs/manual#pagination-params) |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-137)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchopeninteresthistory)
- [bitfinex](https://docs.ccxt.com/docs/exchanges/bitfinex#fetchopeninteresthistory)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchopeninteresthistory)
- [extended](https://docs.ccxt.com/docs/exchanges/extended#fetchopeninteresthistory)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#fetchopeninteresthistory)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchopeninteresthistory)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchopeninteresthistory)

* * *

## [fetchOpenInterests](https://docs.ccxt.com/docs/base-spec\#fetchopeninterests)

Retrieves the open interest for a list of symbols

**Kind**: instance

**Returns**: `Array<object>` \- a list of [open interest structures](https://docs.ccxt.com/docs/manual#open-interest-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>` | No | a list of unified CCXT market symbols |
| params | `object` | No | exchange specific parameters |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-138)

- [bitfinex](https://docs.ccxt.com/docs/exchanges/bitfinex#fetchopeninterests)
- [btse](https://docs.ccxt.com/docs/exchanges/btse#fetchopeninterests)
- [hitbtc](https://docs.ccxt.com/docs/exchanges/hitbtc#fetchopeninterests)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#fetchopeninterests)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#fetchopeninterests)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchopeninterests)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#fetchopeninterests)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchopeninterests)
- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#fetchopeninterests)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#fetchopeninterests)

* * *

## [fetchOpenOrder](https://docs.ccxt.com/docs/base-spec\#fetchopenorder)

fetch an open order by the id

**Kind**: instance

**Returns**: `object` \- an [order structure](https://docs.ccxt.com/docs/manual#order-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| id | `string` | Yes | order id |
| symbol | `string` | Yes | unified market symbol |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-139)

- [aster](https://docs.ccxt.com/docs/exchanges/aster#fetchopenorder)
- [backpack](https://docs.ccxt.com/docs/exchanges/backpack#fetchopenorder)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchopenorder)
- [bitfinex](https://docs.ccxt.com/docs/exchanges/bitfinex#fetchopenorder)
- [btse](https://docs.ccxt.com/docs/exchanges/btse#fetchopenorder)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchopenorder)
- [bydfi](https://docs.ccxt.com/docs/exchanges/bydfi#fetchopenorder)
- [cex](https://docs.ccxt.com/docs/exchanges/cex#fetchopenorder)
- [deepcoin](https://docs.ccxt.com/docs/exchanges/deepcoin#fetchopenorder)
- [hitbtc](https://docs.ccxt.com/docs/exchanges/hitbtc#fetchopenorder)
- [hollaex](https://docs.ccxt.com/docs/exchanges/hollaex#fetchopenorder)

* * *

## [fetchOpenOrders](https://docs.ccxt.com/docs/base-spec\#fetchopenorders)

fetch all unfilled currently open orders

**Kind**: instance

**Returns**: `Array<Order>` \- a list of [order structures](https://docs.ccxt.com/docs/manual#order-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol of the market orders were made in |
| since | `int` | No | the earliest time in ms to fetch orders for |
| limit | `int` | No | the maximum number of order structures to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.until | `int` | No | the latest time in ms to fetch orders for |
| params.direction | `string` | No | the ordering of the results, 'asc' or 'desc', defaults to 'asc' when since is set |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-140)

- [alpaca](https://docs.ccxt.com/docs/exchanges/alpaca#fetchopenorders)
- [apex](https://docs.ccxt.com/docs/exchanges/apex#fetchopenorders)
- [aster](https://docs.ccxt.com/docs/exchanges/aster#fetchopenorders)
- [backpack](https://docs.ccxt.com/docs/exchanges/backpack#fetchopenorders)
- [bigone](https://docs.ccxt.com/docs/exchanges/bigone#fetchopenorders)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchopenorders)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#fetchopenorders)
- [bit2c](https://docs.ccxt.com/docs/exchanges/bit2c#fetchopenorders)
- [bitbank](https://docs.ccxt.com/docs/exchanges/bitbank#fetchopenorders)
- [bitbns](https://docs.ccxt.com/docs/exchanges/bitbns#fetchopenorders)
- [bitfinex](https://docs.ccxt.com/docs/exchanges/bitfinex#fetchopenorders)
- [bitflyer](https://docs.ccxt.com/docs/exchanges/bitflyer#fetchopenorders)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#fetchopenorders)
- [bithumb](https://docs.ccxt.com/docs/exchanges/bithumb#fetchopenorders)
- [bitopro](https://docs.ccxt.com/docs/exchanges/bitopro#fetchopenorders)
- [bitrue](https://docs.ccxt.com/docs/exchanges/bitrue#fetchopenorders)
- [bitso](https://docs.ccxt.com/docs/exchanges/bitso#fetchopenorders)
- [bitstamp](https://docs.ccxt.com/docs/exchanges/bitstamp#fetchopenorders)
- [bitteam](https://docs.ccxt.com/docs/exchanges/bitteam#fetchopenorders)
- [bittrade](https://docs.ccxt.com/docs/exchanges/bittrade#fetchopenorders)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#fetchopenorders)
- [blockchaincom](https://docs.ccxt.com/docs/exchanges/blockchaincom#fetchopenorders)
- [blofin](https://docs.ccxt.com/docs/exchanges/blofin#fetchopenorders)
- [btcbox](https://docs.ccxt.com/docs/exchanges/btcbox#fetchopenorders)
- [btcmarkets](https://docs.ccxt.com/docs/exchanges/btcmarkets#fetchopenorders)
- [btcturk](https://docs.ccxt.com/docs/exchanges/btcturk#fetchopenorders)
- [btse](https://docs.ccxt.com/docs/exchanges/btse#fetchopenorders)
- [bullish](https://docs.ccxt.com/docs/exchanges/bullish#fetchopenorders)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchopenorders)
- [bydfi](https://docs.ccxt.com/docs/exchanges/bydfi#fetchopenorders)
- [cex](https://docs.ccxt.com/docs/exchanges/cex#fetchopenorders)
- [coinbase](https://docs.ccxt.com/docs/exchanges/coinbase#fetchopenorders)
- [coinbaseexchange](https://docs.ccxt.com/docs/exchanges/coinbaseexchange#fetchopenorders)
- [coinbaseinternational](https://docs.ccxt.com/docs/exchanges/coinbaseinternational#fetchopenorders)
- [coincheck](https://docs.ccxt.com/docs/exchanges/coincheck#fetchopenorders)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#fetchopenorders)
- [coinmate](https://docs.ccxt.com/docs/exchanges/coinmate#fetchopenorders)
- [coinone](https://docs.ccxt.com/docs/exchanges/coinone#fetchopenorders)
- [coinsph](https://docs.ccxt.com/docs/exchanges/coinsph#fetchopenorders)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#fetchopenorders)
- [cryptomus](https://docs.ccxt.com/docs/exchanges/cryptomus#fetchopenorders)
- [deepcoin](https://docs.ccxt.com/docs/exchanges/deepcoin#fetchopenorders)
- [delta](https://docs.ccxt.com/docs/exchanges/delta#fetchopenorders)
- [deribit](https://docs.ccxt.com/docs/exchanges/deribit#fetchopenorders)
- [derive](https://docs.ccxt.com/docs/exchanges/derive#fetchopenorders)
- [digifinex](https://docs.ccxt.com/docs/exchanges/digifinex#fetchopenorders)
- [dydx](https://docs.ccxt.com/docs/exchanges/dydx#fetchopenorders)
- [extended](https://docs.ccxt.com/docs/exchanges/extended#fetchopenorders)
- [foxbit](https://docs.ccxt.com/docs/exchanges/foxbit#fetchopenorders)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#fetchopenorders)
- [gemini](https://docs.ccxt.com/docs/exchanges/gemini#fetchopenorders)
- [grvt](https://docs.ccxt.com/docs/exchanges/grvt#fetchopenorders)
- [hashkey](https://docs.ccxt.com/docs/exchanges/hashkey#fetchopenorders)
- [hibachi](https://docs.ccxt.com/docs/exchanges/hibachi#fetchopenorders)
- [hitbtc](https://docs.ccxt.com/docs/exchanges/hitbtc#fetchopenorders)
- [hollaex](https://docs.ccxt.com/docs/exchanges/hollaex#fetchopenorders)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#fetchopenorders)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#fetchopenorders)
- [independentreserve](https://docs.ccxt.com/docs/exchanges/independentreserve#fetchopenorders)
- [indodax](https://docs.ccxt.com/docs/exchanges/indodax#fetchopenorders)
- [kraken](https://docs.ccxt.com/docs/exchanges/kraken#fetchopenorders)
- [krakenfutures](https://docs.ccxt.com/docs/exchanges/krakenfutures#fetchopenorders)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchopenorders)
- [latoken](https://docs.ccxt.com/docs/exchanges/latoken#fetchopenorders)
- [lbank](https://docs.ccxt.com/docs/exchanges/lbank#fetchopenorders)
- [lighter](https://docs.ccxt.com/docs/exchanges/lighter#fetchopenorders)
- [luno](https://docs.ccxt.com/docs/exchanges/luno#fetchopenorders)
- [mercado](https://docs.ccxt.com/docs/exchanges/mercado#fetchopenorders)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#fetchopenorders)
- [modetrade](https://docs.ccxt.com/docs/exchanges/modetrade#fetchopenorders)
- [mudrex](https://docs.ccxt.com/docs/exchanges/mudrex#fetchopenorders)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#fetchopenorders)
- [ndax](https://docs.ccxt.com/docs/exchanges/ndax#fetchopenorders)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchopenorders)
- [onetrading](https://docs.ccxt.com/docs/exchanges/onetrading#fetchopenorders)
- [p2b](https://docs.ccxt.com/docs/exchanges/p2b#fetchopenorders)
- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#fetchopenorders)
- [paradex](https://docs.ccxt.com/docs/exchanges/paradex#fetchopenorders)
- [phemex](https://docs.ccxt.com/docs/exchanges/phemex#fetchopenorders)
- [poloniex](https://docs.ccxt.com/docs/exchanges/poloniex#fetchopenorders)
- [revolutx](https://docs.ccxt.com/docs/exchanges/revolutx#fetchopenorders)
- [tokocrypto](https://docs.ccxt.com/docs/exchanges/tokocrypto#fetchopenorders)
- [toobit](https://docs.ccxt.com/docs/exchanges/toobit#fetchopenorders)
- [upbit](https://docs.ccxt.com/docs/exchanges/upbit#fetchopenorders)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#fetchopenorders)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#fetchopenorders)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#fetchopenorders)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#fetchopenorders)
- [xt](https://docs.ccxt.com/docs/exchanges/xt#fetchopenorders)
- [zaif](https://docs.ccxt.com/docs/exchanges/zaif#fetchopenorders)
- [zebpay](https://docs.ccxt.com/docs/exchanges/zebpay#fetchopenorders)

* * *

## [fetchOpenOrdersWs](https://docs.ccxt.com/docs/base-spec\#fetchopenordersws)

fetch all unfilled currently open orders

**Kind**: instance

**Returns**: `Array<object>` \- a list of [order structures](https://docs.ccxt.com/docs/manual#order-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol |
| since | `int`, `undefined` | No | the earliest time in ms to fetch open orders for |
| limit | `int`, `undefined` | No | the maximum number of open orders structures to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-141)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchopenordersws)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#fetchopenordersws)
- [cex](https://docs.ccxt.com/docs/exchanges/cex#fetchopenordersws)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#fetchopenordersws)

* * *

## [fetchOption](https://docs.ccxt.com/docs/base-spec\#fetchoption)

fetches option data that is commonly found in an option chain

**Kind**: instance

**Returns**: `object` \- an [option chain structure](https://docs.ccxt.com/docs/manual#option-chain-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-142)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchoption)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchoption)
- [delta](https://docs.ccxt.com/docs/exchanges/delta#fetchoption)
- [deribit](https://docs.ccxt.com/docs/exchanges/deribit#fetchoption)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#fetchoption)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchoption)

* * *

## [fetchOptionChain](https://docs.ccxt.com/docs/base-spec\#fetchoptionchain)

fetches data for an underlying asset that is commonly found in an option chain

**Kind**: instance

**Returns**: `object` \- a list of [option chain structures](https://docs.ccxt.com/docs/manual#option-chain-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| code | `string` | Yes | base currency to fetch an option chain for |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-143)

- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchoptionchain)
- [deribit](https://docs.ccxt.com/docs/exchanges/deribit#fetchoptionchain)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#fetchoptionchain)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchoptionchain)

* * *

## [fetchOptionPositions](https://docs.ccxt.com/docs/base-spec\#fetchoptionpositions)

fetch data on open options positions

**Kind**: instance

**Returns**: `Array<object>` \- a list of [position structures](https://docs.ccxt.com/docs/manual#position-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>`, `undefined` | Yes | list of unified market symbols |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-144)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchoptionpositions)

* * *

## [fetchOrder](https://docs.ccxt.com/docs/base-spec\#fetchorder)

fetches information on an order made by the user

**Kind**: instance

**Returns**: `object` \- An [order structure](https://docs.ccxt.com/docs/manual#order-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| id | `string` | Yes | the order id |
| symbol | `string` | Yes | unified symbol of the market the order was made in |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-145)

- [alpaca](https://docs.ccxt.com/docs/exchanges/alpaca#fetchorder)
- [apex](https://docs.ccxt.com/docs/exchanges/apex#fetchorder)
- [aster](https://docs.ccxt.com/docs/exchanges/aster#fetchorder)
- [bigone](https://docs.ccxt.com/docs/exchanges/bigone#fetchorder)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchorder)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#fetchorder)
- [bit2c](https://docs.ccxt.com/docs/exchanges/bit2c#fetchorder)
- [bitbank](https://docs.ccxt.com/docs/exchanges/bitbank#fetchorder)
- [bitbns](https://docs.ccxt.com/docs/exchanges/bitbns#fetchorder)
- [bitfinex](https://docs.ccxt.com/docs/exchanges/bitfinex#fetchorder)
- [bitflyer](https://docs.ccxt.com/docs/exchanges/bitflyer#fetchorder)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#fetchorder)
- [bithumb](https://docs.ccxt.com/docs/exchanges/bithumb#fetchorder)
- [bitopro](https://docs.ccxt.com/docs/exchanges/bitopro#fetchorder)
- [bitrue](https://docs.ccxt.com/docs/exchanges/bitrue#fetchorder)
- [bitso](https://docs.ccxt.com/docs/exchanges/bitso#fetchorder)
- [bitstamp](https://docs.ccxt.com/docs/exchanges/bitstamp#fetchorder)
- [bitteam](https://docs.ccxt.com/docs/exchanges/bitteam#fetchorder)
- [bittrade](https://docs.ccxt.com/docs/exchanges/bittrade#fetchorder)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#fetchorder)
- [blockchaincom](https://docs.ccxt.com/docs/exchanges/blockchaincom#fetchorder)
- [btcbox](https://docs.ccxt.com/docs/exchanges/btcbox#fetchorder)
- [btcmarkets](https://docs.ccxt.com/docs/exchanges/btcmarkets#fetchorder)
- [bullish](https://docs.ccxt.com/docs/exchanges/bullish#fetchorder)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchorder)
- [coinbase](https://docs.ccxt.com/docs/exchanges/coinbase#fetchorder)
- [coinbaseexchange](https://docs.ccxt.com/docs/exchanges/coinbaseexchange#fetchorder)
- [coinbaseinternational](https://docs.ccxt.com/docs/exchanges/coinbaseinternational#fetchorder)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#fetchorder)
- [coinmate](https://docs.ccxt.com/docs/exchanges/coinmate#fetchorder)
- [coinone](https://docs.ccxt.com/docs/exchanges/coinone#fetchorder)
- [coinsph](https://docs.ccxt.com/docs/exchanges/coinsph#fetchorder)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#fetchorder)
- [delta](https://docs.ccxt.com/docs/exchanges/delta#fetchorder)
- [deribit](https://docs.ccxt.com/docs/exchanges/deribit#fetchorder)
- [digifinex](https://docs.ccxt.com/docs/exchanges/digifinex#fetchorder)
- [dydx](https://docs.ccxt.com/docs/exchanges/dydx#fetchorder)
- [extended](https://docs.ccxt.com/docs/exchanges/extended#fetchorder)
- [foxbit](https://docs.ccxt.com/docs/exchanges/foxbit#fetchorder)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#fetchorder)
- [gemini](https://docs.ccxt.com/docs/exchanges/gemini#fetchorder)
- [grvt](https://docs.ccxt.com/docs/exchanges/grvt#fetchorder)
- [hashkey](https://docs.ccxt.com/docs/exchanges/hashkey#fetchorder)
- [hibachi](https://docs.ccxt.com/docs/exchanges/hibachi#fetchorder)
- [hitbtc](https://docs.ccxt.com/docs/exchanges/hitbtc#fetchorder)
- [hollaex](https://docs.ccxt.com/docs/exchanges/hollaex#fetchorder)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#fetchorder)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#fetchorder)
- [independentreserve](https://docs.ccxt.com/docs/exchanges/independentreserve#fetchorder)
- [indodax](https://docs.ccxt.com/docs/exchanges/indodax#fetchorder)
- [kraken](https://docs.ccxt.com/docs/exchanges/kraken#fetchorder)
- [krakenfutures](https://docs.ccxt.com/docs/exchanges/krakenfutures#fetchorder)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchorder)
- [latoken](https://docs.ccxt.com/docs/exchanges/latoken#fetchorder)
- [lbank](https://docs.ccxt.com/docs/exchanges/lbank#fetchorder)
- [luno](https://docs.ccxt.com/docs/exchanges/luno#fetchorder)
- [mercado](https://docs.ccxt.com/docs/exchanges/mercado#fetchorder)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#fetchorder)
- [modetrade](https://docs.ccxt.com/docs/exchanges/modetrade#fetchorder)
- [mudrex](https://docs.ccxt.com/docs/exchanges/mudrex#fetchorder)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#fetchorder)
- [ndax](https://docs.ccxt.com/docs/exchanges/ndax#fetchorder)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchorder)
- [onetrading](https://docs.ccxt.com/docs/exchanges/onetrading#fetchorder)
- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#fetchorder)
- [paradex](https://docs.ccxt.com/docs/exchanges/paradex#fetchorder)
- [phemex](https://docs.ccxt.com/docs/exchanges/phemex#fetchorder)
- [poloniex](https://docs.ccxt.com/docs/exchanges/poloniex#fetchorder)
- [revolutx](https://docs.ccxt.com/docs/exchanges/revolutx#fetchorder)
- [tokocrypto](https://docs.ccxt.com/docs/exchanges/tokocrypto#fetchorder)
- [toobit](https://docs.ccxt.com/docs/exchanges/toobit#fetchorder)
- [upbit](https://docs.ccxt.com/docs/exchanges/upbit#fetchorder)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#fetchorder)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#fetchorder)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#fetchorder)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#fetchorder)
- [xt](https://docs.ccxt.com/docs/exchanges/xt#fetchorder)
- [zebpay](https://docs.ccxt.com/docs/exchanges/zebpay#fetchorder)

* * *

## [fetchOrderBook](https://docs.ccxt.com/docs/base-spec\#fetchorderbook)

fetches information on open orders with bid (buy) and ask (sell) prices, volumes and other data

**Kind**: instance

**Returns**: `object` \- an [order book structure](https://docs.ccxt.com/docs/manual#order-book-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to fetch the order book for |
| limit | `int` | No | the maximum amount of order book entries to return |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.loc | `string` | No | crypto location, default: us |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-146)

- [alpaca](https://docs.ccxt.com/docs/exchanges/alpaca#fetchorderbook)
- [apex](https://docs.ccxt.com/docs/exchanges/apex#fetchorderbook)
- [aster](https://docs.ccxt.com/docs/exchanges/aster#fetchorderbook)
- [backpack](https://docs.ccxt.com/docs/exchanges/backpack#fetchorderbook)
- [bigone](https://docs.ccxt.com/docs/exchanges/bigone#fetchorderbook)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchorderbook)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#fetchorderbook)
- [bit2c](https://docs.ccxt.com/docs/exchanges/bit2c#fetchorderbook)
- [bitbank](https://docs.ccxt.com/docs/exchanges/bitbank#fetchorderbook)
- [bitbns](https://docs.ccxt.com/docs/exchanges/bitbns#fetchorderbook)
- [bitfinex](https://docs.ccxt.com/docs/exchanges/bitfinex#fetchorderbook)
- [bitflyer](https://docs.ccxt.com/docs/exchanges/bitflyer#fetchorderbook)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#fetchorderbook)
- [bithumb](https://docs.ccxt.com/docs/exchanges/bithumb#fetchorderbook)
- [bitopro](https://docs.ccxt.com/docs/exchanges/bitopro#fetchorderbook)
- [bitrue](https://docs.ccxt.com/docs/exchanges/bitrue#fetchorderbook)
- [bitso](https://docs.ccxt.com/docs/exchanges/bitso#fetchorderbook)
- [bitstamp](https://docs.ccxt.com/docs/exchanges/bitstamp#fetchorderbook)
- [bitteam](https://docs.ccxt.com/docs/exchanges/bitteam#fetchorderbook)
- [bittrade](https://docs.ccxt.com/docs/exchanges/bittrade#fetchorderbook)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#fetchorderbook)
- [blockchaincom](https://docs.ccxt.com/docs/exchanges/blockchaincom#fetchorderbook)
- [blofin](https://docs.ccxt.com/docs/exchanges/blofin#fetchorderbook)
- [btcbox](https://docs.ccxt.com/docs/exchanges/btcbox#fetchorderbook)
- [btcmarkets](https://docs.ccxt.com/docs/exchanges/btcmarkets#fetchorderbook)
- [btcturk](https://docs.ccxt.com/docs/exchanges/btcturk#fetchorderbook)
- [btse](https://docs.ccxt.com/docs/exchanges/btse#fetchorderbook)
- [bullish](https://docs.ccxt.com/docs/exchanges/bullish#fetchorderbook)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchorderbook)
- [bydfi](https://docs.ccxt.com/docs/exchanges/bydfi#fetchorderbook)
- [cex](https://docs.ccxt.com/docs/exchanges/cex#fetchorderbook)
- [coinbase](https://docs.ccxt.com/docs/exchanges/coinbase#fetchorderbook)
- [coinbaseexchange](https://docs.ccxt.com/docs/exchanges/coinbaseexchange#fetchorderbook)
- [coincheck](https://docs.ccxt.com/docs/exchanges/coincheck#fetchorderbook)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#fetchorderbook)
- [coinmate](https://docs.ccxt.com/docs/exchanges/coinmate#fetchorderbook)
- [coinone](https://docs.ccxt.com/docs/exchanges/coinone#fetchorderbook)
- [coinsph](https://docs.ccxt.com/docs/exchanges/coinsph#fetchorderbook)
- [coinspot](https://docs.ccxt.com/docs/exchanges/coinspot#fetchorderbook)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#fetchorderbook)
- [cryptomus](https://docs.ccxt.com/docs/exchanges/cryptomus#fetchorderbook)
- [deepcoin](https://docs.ccxt.com/docs/exchanges/deepcoin#fetchorderbook)
- [delta](https://docs.ccxt.com/docs/exchanges/delta#fetchorderbook)
- [deribit](https://docs.ccxt.com/docs/exchanges/deribit#fetchorderbook)
- [digifinex](https://docs.ccxt.com/docs/exchanges/digifinex#fetchorderbook)
- [dydx](https://docs.ccxt.com/docs/exchanges/dydx#fetchorderbook)
- [extended](https://docs.ccxt.com/docs/exchanges/extended#fetchorderbook)
- [foxbit](https://docs.ccxt.com/docs/exchanges/foxbit#fetchorderbook)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#fetchorderbook)
- [gemini](https://docs.ccxt.com/docs/exchanges/gemini#fetchorderbook)
- [grvt](https://docs.ccxt.com/docs/exchanges/grvt#fetchorderbook)
- [hashkey](https://docs.ccxt.com/docs/exchanges/hashkey#fetchorderbook)
- [hibachi](https://docs.ccxt.com/docs/exchanges/hibachi#fetchorderbook)
- [hitbtc](https://docs.ccxt.com/docs/exchanges/hitbtc#fetchorderbook)
- [hollaex](https://docs.ccxt.com/docs/exchanges/hollaex#fetchorderbook)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#fetchorderbook)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#fetchorderbook)
- [independentreserve](https://docs.ccxt.com/docs/exchanges/independentreserve#fetchorderbook)
- [indodax](https://docs.ccxt.com/docs/exchanges/indodax#fetchorderbook)
- [kraken](https://docs.ccxt.com/docs/exchanges/kraken#fetchorderbook)
- [krakenfutures](https://docs.ccxt.com/docs/exchanges/krakenfutures#fetchorderbook)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchorderbook)
- [latoken](https://docs.ccxt.com/docs/exchanges/latoken#fetchorderbook)
- [lbank](https://docs.ccxt.com/docs/exchanges/lbank#fetchorderbook)
- [lighter](https://docs.ccxt.com/docs/exchanges/lighter#fetchorderbook)
- [luno](https://docs.ccxt.com/docs/exchanges/luno#fetchorderbook)
- [mercado](https://docs.ccxt.com/docs/exchanges/mercado#fetchorderbook)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#fetchorderbook)
- [modetrade](https://docs.ccxt.com/docs/exchanges/modetrade#fetchorderbook)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#fetchorderbook)
- [ndax](https://docs.ccxt.com/docs/exchanges/ndax#fetchorderbook)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchorderbook)
- [onetrading](https://docs.ccxt.com/docs/exchanges/onetrading#fetchorderbook)
- [p2b](https://docs.ccxt.com/docs/exchanges/p2b#fetchorderbook)
- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#fetchorderbook)
- [paradex](https://docs.ccxt.com/docs/exchanges/paradex#fetchorderbook)
- [paymium](https://docs.ccxt.com/docs/exchanges/paymium#fetchorderbook)
- [phemex](https://docs.ccxt.com/docs/exchanges/phemex#fetchorderbook)
- [poloniex](https://docs.ccxt.com/docs/exchanges/poloniex#fetchorderbook)
- [revolutx](https://docs.ccxt.com/docs/exchanges/revolutx#fetchorderbook)
- [tokocrypto](https://docs.ccxt.com/docs/exchanges/tokocrypto#fetchorderbook)
- [toobit](https://docs.ccxt.com/docs/exchanges/toobit#fetchorderbook)
- [upbit](https://docs.ccxt.com/docs/exchanges/upbit#fetchorderbook)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#fetchorderbook)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#fetchorderbook)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#fetchorderbook)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#fetchorderbook)
- [xt](https://docs.ccxt.com/docs/exchanges/xt#fetchorderbook)
- [zaif](https://docs.ccxt.com/docs/exchanges/zaif#fetchorderbook)
- [zebpay](https://docs.ccxt.com/docs/exchanges/zebpay#fetchorderbook)

* * *

## [fetchOrderBookWs](https://docs.ccxt.com/docs/base-spec\#fetchorderbookws)

fetches information on open orders with bid (buy) and ask (sell) prices, volumes and other data

**Kind**: instance

**Returns**: `object` \- A dictionary of [order book structures](https://docs.ccxt.com/docs/manual#order-book-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to fetch the order book for |
| limit | `int` | No | the maximum amount of order book entries to return |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-147)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchorderbookws)
- [lbank](https://docs.ccxt.com/docs/exchanges/lbank#fetchorderbookws)

* * *

## [fetchOrderBooks](https://docs.ccxt.com/docs/base-spec\#fetchorderbooks)

fetches information on open orders with bid (buy) and ask (sell) prices, volumes and other data for multiple markets

**Kind**: instance

**Returns**: `object` \- a dictionary of [order book structures](https://docs.ccxt.com/docs/manual#order-book-structure) indexed by market symbol

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>` | No | list of unified market symbols, all symbols fetched if undefined, default is undefined |
| limit | `int` | No | max number of entries per orderbook to return, default is undefined |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-148)

- [hitbtc](https://docs.ccxt.com/docs/exchanges/hitbtc#fetchorderbooks)
- [hollaex](https://docs.ccxt.com/docs/exchanges/hollaex#fetchorderbooks)
- [upbit](https://docs.ccxt.com/docs/exchanges/upbit#fetchorderbooks)

* * *

## [fetchOrderClassic](https://docs.ccxt.com/docs/base-spec\#fetchorderclassic)

fetches information on an order made by the user _classic accounts only_

**Kind**: instance

**Returns**: `object` \- An [order structure](https://docs.ccxt.com/docs/manual#order-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| id | `string` | Yes | the order id |
| symbol | `string` | Yes | unified symbol of the market the order was made in |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-149)

- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchorderclassic)

* * *

## [fetchOrderTrades](https://docs.ccxt.com/docs/base-spec\#fetchordertrades)

fetch all the trades made from a single order

**Kind**: instance

**Returns**: `Array<object>` \- a list of [trade structures](https://docs.ccxt.com/docs/manual#trade-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| id | `string` | Yes | order id |
| symbol | `string` | Yes | unified market symbol |
| since | `int` | No | the earliest time in ms to fetch trades for |
| limit | `int` | No | the maximum number of trades to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-150)

- [apex](https://docs.ccxt.com/docs/exchanges/apex#fetchordertrades)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchordertrades)
- [bitfinex](https://docs.ccxt.com/docs/exchanges/bitfinex#fetchordertrades)
- [bitso](https://docs.ccxt.com/docs/exchanges/bitso#fetchordertrades)
- [bittrade](https://docs.ccxt.com/docs/exchanges/bittrade#fetchordertrades)
- [btse](https://docs.ccxt.com/docs/exchanges/btse#fetchordertrades)
- [bullish](https://docs.ccxt.com/docs/exchanges/bullish#fetchordertrades)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchordertrades)
- [coinbaseexchange](https://docs.ccxt.com/docs/exchanges/coinbaseexchange#fetchordertrades)
- [coinsph](https://docs.ccxt.com/docs/exchanges/coinsph#fetchordertrades)
- [deepcoin](https://docs.ccxt.com/docs/exchanges/deepcoin#fetchordertrades)
- [deribit](https://docs.ccxt.com/docs/exchanges/deribit#fetchordertrades)
- [derive](https://docs.ccxt.com/docs/exchanges/derive#fetchordertrades)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#fetchordertrades)
- [hitbtc](https://docs.ccxt.com/docs/exchanges/hitbtc#fetchordertrades)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#fetchordertrades)
- [kraken](https://docs.ccxt.com/docs/exchanges/kraken#fetchordertrades)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchordertrades)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#fetchordertrades)
- [modetrade](https://docs.ccxt.com/docs/exchanges/modetrade#fetchordertrades)
- [ndax](https://docs.ccxt.com/docs/exchanges/ndax#fetchordertrades)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchordertrades)
- [onetrading](https://docs.ccxt.com/docs/exchanges/onetrading#fetchordertrades)
- [p2b](https://docs.ccxt.com/docs/exchanges/p2b#fetchordertrades)
- [poloniex](https://docs.ccxt.com/docs/exchanges/poloniex#fetchordertrades)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#fetchordertrades)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#fetchordertrades)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#fetchordertrades)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#fetchordertrades)
- [zebpatspot](https://docs.ccxt.com/docs/exchanges/zebpatspot#fetchordertrades)

* * *

## [fetchOrderWs](https://docs.ccxt.com/docs/base-spec\#fetchorderws)

fetches information on an order made by the user

**Kind**: instance

**Returns**: `object` \- An [order structure](https://docs.ccxt.com/docs/manual#order-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| id | `string` | Yes | order id |
| symbol | `string` | No | unified symbol of the market the order was made in |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-151)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchorderws)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#fetchorderws)
- [cex](https://docs.ccxt.com/docs/exchanges/cex#fetchorderws)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#fetchorderws)

* * *

## [fetchOrders](https://docs.ccxt.com/docs/base-spec\#fetchorders)

fetches information on multiple orders made by the user

**Kind**: instance

**Returns**: `Array<Order>` \- a list of [order structures](https://docs.ccxt.com/docs/manual#order-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol of the market orders were made in |
| since | `int` | No | the earliest time in ms to fetch orders for |
| limit | `int` | No | the maximum number of order structures to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.until | `int` | No | the latest time in ms to fetch orders for |
| params.direction | `string` | No | the ordering of the results, 'asc' or 'desc', defaults to 'asc' when since is set |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-152)

- [alpaca](https://docs.ccxt.com/docs/exchanges/alpaca#fetchorders)
- [apex](https://docs.ccxt.com/docs/exchanges/apex#fetchorders)
- [aster](https://docs.ccxt.com/docs/exchanges/aster#fetchorders)
- [backpack](https://docs.ccxt.com/docs/exchanges/backpack#fetchorders)
- [bigone](https://docs.ccxt.com/docs/exchanges/bigone#fetchorders)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchorders)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#fetchorders)
- [bitflyer](https://docs.ccxt.com/docs/exchanges/bitflyer#fetchorders)
- [bithumb](https://docs.ccxt.com/docs/exchanges/bithumb#fetchorders)
- [bitopro](https://docs.ccxt.com/docs/exchanges/bitopro#fetchorders)
- [bitteam](https://docs.ccxt.com/docs/exchanges/bitteam#fetchorders)
- [bittrade](https://docs.ccxt.com/docs/exchanges/bittrade#fetchorders)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#fetchorders)
- [blockchaincom](https://docs.ccxt.com/docs/exchanges/blockchaincom#fetchorders)
- [btcbox](https://docs.ccxt.com/docs/exchanges/btcbox#fetchorders)
- [btcmarkets](https://docs.ccxt.com/docs/exchanges/btcmarkets#fetchorders)
- [btcturk](https://docs.ccxt.com/docs/exchanges/btcturk#fetchorders)
- [bullish](https://docs.ccxt.com/docs/exchanges/bullish#fetchorders)
- [cex](https://docs.ccxt.com/docs/exchanges/cex#fetchorders)
- [coinbase](https://docs.ccxt.com/docs/exchanges/coinbase#fetchorders)
- [coinbaseexchange](https://docs.ccxt.com/docs/exchanges/coinbaseexchange#fetchorders)
- [coinmate](https://docs.ccxt.com/docs/exchanges/coinmate#fetchorders)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#fetchorders)
- [cryptomus](https://docs.ccxt.com/docs/exchanges/cryptomus#fetchorders)
- [derive](https://docs.ccxt.com/docs/exchanges/derive#fetchorders)
- [digifinex](https://docs.ccxt.com/docs/exchanges/digifinex#fetchorders)
- [dydx](https://docs.ccxt.com/docs/exchanges/dydx#fetchorders)
- [extended](https://docs.ccxt.com/docs/exchanges/extended#fetchorders)
- [foxbit](https://docs.ccxt.com/docs/exchanges/foxbit#fetchorders)
- [gemini](https://docs.ccxt.com/docs/exchanges/gemini#fetchorders)
- [grvt](https://docs.ccxt.com/docs/exchanges/grvt#fetchorders)
- [hollaex](https://docs.ccxt.com/docs/exchanges/hollaex#fetchorders)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#fetchorders)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#fetchorders)
- [krakenfutures](https://docs.ccxt.com/docs/exchanges/krakenfutures#fetchorders)
- [latoken](https://docs.ccxt.com/docs/exchanges/latoken#fetchorders)
- [lbank](https://docs.ccxt.com/docs/exchanges/lbank#fetchorders)
- [luno](https://docs.ccxt.com/docs/exchanges/luno#fetchorders)
- [mercado](https://docs.ccxt.com/docs/exchanges/mercado#fetchorders)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#fetchorders)
- [modetrade](https://docs.ccxt.com/docs/exchanges/modetrade#fetchorders)
- [mudrex](https://docs.ccxt.com/docs/exchanges/mudrex#fetchorders)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#fetchorders)
- [ndax](https://docs.ccxt.com/docs/exchanges/ndax#fetchorders)
- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#fetchorders)
- [paradex](https://docs.ccxt.com/docs/exchanges/paradex#fetchorders)
- [phemex](https://docs.ccxt.com/docs/exchanges/phemex#fetchorders)
- [revolutx](https://docs.ccxt.com/docs/exchanges/revolutx#fetchorders)
- [tokocrypto](https://docs.ccxt.com/docs/exchanges/tokocrypto#fetchorders)
- [toobit](https://docs.ccxt.com/docs/exchanges/toobit#fetchorders)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#fetchorders)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#fetchorders)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#fetchorders)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#fetchorders)
- [xt](https://docs.ccxt.com/docs/exchanges/xt#fetchorders)

* * *

## [fetchOrdersByIds](https://docs.ccxt.com/docs/base-spec\#fetchordersbyids)

fetch orders by the list of order id

**Kind**: instance

**Returns**: `Array<object>` \- a list of [order structure](https://docs.ccxt.com/docs/manual#order-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| ids | `Array<string>` | No | list of order id |
| symbol | `string` | No | unified ccxt market symbol |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-153)

- [kraken](https://docs.ccxt.com/docs/exchanges/kraken#fetchordersbyids)

* * *

## [fetchOrdersByStatus](https://docs.ccxt.com/docs/base-spec\#fetchordersbystatus)

fetch a list of orders

**Kind**: instance

**Returns**: `Array<Order>` \- a list of [order structures](https://docs.ccxt.com/docs/manual#order-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| status | `string` | Yes | order status to fetch for |
| symbol | `string` | Yes | unified market symbol of the market orders were made in |
| since | `int` | No | the earliest time in ms to fetch orders for |
| limit | `int` | No | the maximum number of order structures to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.trigger | `boolean` | No | set to true for fetching trigger orders |
| params.marginMode | `string` | No | 'cross' or 'isolated' for fetching spot margin orders |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-154)

- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#fetchordersbystatus)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchordersbystatus)

* * *

## [fetchOrdersClassic](https://docs.ccxt.com/docs/base-spec\#fetchordersclassic)

fetches information on multiple orders made by the user _classic accounts only_

**Kind**: instance

**Returns**: `Array<Order>` \- a list of [order structures](https://docs.ccxt.com/docs/manual#order-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol of the market orders were made in |
| since | `int` | No | the earliest time in ms to fetch orders for |
| limit | `int` | No | the maximum number of order structures to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.trigger | `boolean` | No | true if trigger order |
| params.stop | `boolean` | No | alias for trigger |
| params.type | `string` | No | market type, \['swap', 'option', 'spot'\] |
| params.subType | `string` | No | market subType, \['linear', 'inverse'\] |
| params.orderFilter | `string` | No | 'Order' or 'StopOrder' or 'tpslOrder' |
| params.until | `int` | No | the latest time in ms to fetch entries for |
| params.paginate | `boolean` | No | default false, when true will automatically paginate by calling this endpoint multiple times. See in the docs all the [availble parameters](https://docs.ccxt.com/docs/manual#pagination-params) |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-155)

- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchordersclassic)

* * *

## [fetchOrdersWs](https://docs.ccxt.com/docs/base-spec\#fetchordersws)

fetches information on multiple orders made by the user

**Kind**: instance

**Returns**: `Array<object>` \- a list of [order structures](https://docs.ccxt.com/docs/manual#order-structure)

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

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-156)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchordersws)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#fetchordersws)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#fetchordersws)

* * *

## [fetchPortfolioDetails](https://docs.ccxt.com/docs/base-spec\#fetchportfoliodetails)

Fetch details for a specific portfolio by UUID

**Kind**: instance

**Returns**: `Array<any>` \- An account structure </docs/manual#account-structure>

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| portfolioUuid | `string` | Yes | The unique identifier of the portfolio to fetch |
| params | `Dict` | No | Extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-157)

- [coinbase](https://docs.ccxt.com/docs/exchanges/coinbase#fetchportfoliodetails)

* * *

## [fetchPortfolios](https://docs.ccxt.com/docs/base-spec\#fetchportfolios)

fetch all the portfolios

**Kind**: instance

**Returns**: `object` \- a dictionary of [account structures](https://docs.ccxt.com/docs/manual#account-structure) indexed by the account type

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-158)

- [coinbase](https://docs.ccxt.com/docs/exchanges/coinbase#fetchportfolios)

* * *

## [fetchPosition](https://docs.ccxt.com/docs/base-spec\#fetchposition)

fetch data on an open position

**Kind**: instance

**Returns**: `object` \- a [position structure](https://docs.ccxt.com/docs/manual#position-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol of the market the position is held in |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-159)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchposition)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#fetchposition)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#fetchposition)
- [blofin](https://docs.ccxt.com/docs/exchanges/blofin#fetchposition)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchposition)
- [coinbase](https://docs.ccxt.com/docs/exchanges/coinbase#fetchposition)
- [coinbaseinternational](https://docs.ccxt.com/docs/exchanges/coinbaseinternational#fetchposition)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#fetchposition)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#fetchposition)
- [delta](https://docs.ccxt.com/docs/exchanges/delta#fetchposition)
- [deribit](https://docs.ccxt.com/docs/exchanges/deribit#fetchposition)
- [digifinex](https://docs.ccxt.com/docs/exchanges/digifinex#fetchposition)
- [dydx](https://docs.ccxt.com/docs/exchanges/dydx#fetchposition)
- [extended](https://docs.ccxt.com/docs/exchanges/extended#fetchposition)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#fetchposition)
- [hitbtc](https://docs.ccxt.com/docs/exchanges/hitbtc#fetchposition)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#fetchposition)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#fetchposition)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchposition)
- [lighter](https://docs.ccxt.com/docs/exchanges/lighter#fetchposition)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#fetchposition)
- [modetrade](https://docs.ccxt.com/docs/exchanges/modetrade#fetchposition)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchposition)
- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#fetchposition)
- [paradex](https://docs.ccxt.com/docs/exchanges/paradex#fetchposition)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#fetchposition)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#fetchposition)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#fetchposition)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#fetchposition)
- [xt](https://docs.ccxt.com/docs/exchanges/xt#fetchposition)

* * *

## [fetchPositionHistory](https://docs.ccxt.com/docs/base-spec\#fetchpositionhistory)

fetches historical positions

**Kind**: instance

**Returns**: `Array<object>` \- a list of [position structures](https://docs.ccxt.com/docs/manual#position-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified contract symbol |
| since | `int` | No | the earliest time in ms to fetch positions for |
| limit | `int` | No | the maximum amount of records to fetch |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.until | `int` | No | the latest time in ms to fetch positions for |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-160)

- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#fetchpositionhistory)
- [bydfi](https://docs.ccxt.com/docs/exchanges/bydfi#fetchpositionhistory)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#fetchpositionhistory)
- [phemex](https://docs.ccxt.com/docs/exchanges/phemex#fetchpositionhistory)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#fetchpositionhistory)

* * *

## [fetchPositionMode](https://docs.ccxt.com/docs/base-spec\#fetchpositionmode)

fetchs the position mode, hedged or one way, hedged for aster is set identically for all linear markets or all inverse markets

**Kind**: instance

**Returns**: `object` \- an object detailing whether the market is in hedged or one-way mode

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to fetch the order book for |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-161)

- [aster](https://docs.ccxt.com/docs/exchanges/aster#fetchpositionmode)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchpositionmode)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#fetchpositionmode)
- [blofin](https://docs.ccxt.com/docs/exchanges/blofin#fetchpositionmode)
- [btse](https://docs.ccxt.com/docs/exchanges/btse#fetchpositionmode)
- [bydfi](https://docs.ccxt.com/docs/exchanges/bydfi#fetchpositionmode)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchpositionmode)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#fetchpositionmode)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchpositionmode)
- [poloniex](https://docs.ccxt.com/docs/exchanges/poloniex#fetchpositionmode)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#fetchpositionmode)

* * *

## [fetchPositionWs](https://docs.ccxt.com/docs/base-spec\#fetchpositionws)

fetch data on an open position

**Kind**: instance

**Returns**: `object` \- a [position structure](https://docs.ccxt.com/docs/manual#position-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol of the market the position is held in |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-162)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchpositionws)

* * *

## [fetchPositions](https://docs.ccxt.com/docs/base-spec\#fetchpositions)

fetch all open positions

**Kind**: instance

**Returns**: `Array<object>` \- a list of [position structure](https://docs.ccxt.com/docs/manual#position-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>` | No | list of unified market symbols |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-163)

- [apex](https://docs.ccxt.com/docs/exchanges/apex#fetchpositions)
- [aster](https://docs.ccxt.com/docs/exchanges/aster#fetchpositions)
- [backpack](https://docs.ccxt.com/docs/exchanges/backpack#fetchpositions)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchpositions)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#fetchpositions)
- [bitfinex](https://docs.ccxt.com/docs/exchanges/bitfinex#fetchpositions)
- [bitflyer](https://docs.ccxt.com/docs/exchanges/bitflyer#fetchpositions)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#fetchpositions)
- [blofin](https://docs.ccxt.com/docs/exchanges/blofin#fetchpositions)
- [btse](https://docs.ccxt.com/docs/exchanges/btse#fetchpositions)
- [bullish](https://docs.ccxt.com/docs/exchanges/bullish#fetchpositions)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchpositions)
- [bydfi](https://docs.ccxt.com/docs/exchanges/bydfi#fetchpositions)
- [coinbase](https://docs.ccxt.com/docs/exchanges/coinbase#fetchpositions)
- [coinbaseinternational](https://docs.ccxt.com/docs/exchanges/coinbaseinternational#fetchpositions)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#fetchpositions)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#fetchpositions)
- [deepcoin](https://docs.ccxt.com/docs/exchanges/deepcoin#fetchpositions)
- [delta](https://docs.ccxt.com/docs/exchanges/delta#fetchpositions)
- [deribit](https://docs.ccxt.com/docs/exchanges/deribit#fetchpositions)
- [derive](https://docs.ccxt.com/docs/exchanges/derive#fetchpositions)
- [digifinex](https://docs.ccxt.com/docs/exchanges/digifinex#fetchpositions)
- [dydx](https://docs.ccxt.com/docs/exchanges/dydx#fetchpositions)
- [extended](https://docs.ccxt.com/docs/exchanges/extended#fetchpositions)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#fetchpositions)
- [grvt](https://docs.ccxt.com/docs/exchanges/grvt#fetchpositions)
- [hashkey](https://docs.ccxt.com/docs/exchanges/hashkey#fetchpositions)
- [hibachi](https://docs.ccxt.com/docs/exchanges/hibachi#fetchpositions)
- [hitbtc](https://docs.ccxt.com/docs/exchanges/hitbtc#fetchpositions)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#fetchpositions)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#fetchpositions)
- [kraken](https://docs.ccxt.com/docs/exchanges/kraken#fetchpositions)
- [krakenfutures](https://docs.ccxt.com/docs/exchanges/krakenfutures#fetchpositions)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchpositions)
- [lighter](https://docs.ccxt.com/docs/exchanges/lighter#fetchpositions)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#fetchpositions)
- [modetrade](https://docs.ccxt.com/docs/exchanges/modetrade#fetchpositions)
- [mudrex](https://docs.ccxt.com/docs/exchanges/mudrex#fetchpositions)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#fetchpositions)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchpositions)
- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#fetchpositions)
- [paradex](https://docs.ccxt.com/docs/exchanges/paradex#fetchpositions)
- [phemex](https://docs.ccxt.com/docs/exchanges/phemex#fetchpositions)
- [poloniex](https://docs.ccxt.com/docs/exchanges/poloniex#fetchpositions)
- [toobit](https://docs.ccxt.com/docs/exchanges/toobit#fetchpositions)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#fetchpositions)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#fetchpositions)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#fetchpositions)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#fetchpositions)
- [xt](https://docs.ccxt.com/docs/exchanges/xt#fetchpositions)
- [zebpay](https://docs.ccxt.com/docs/exchanges/zebpay#fetchpositions)

* * *

## [fetchPositionsADLRank](https://docs.ccxt.com/docs/base-spec\#fetchpositionsadlrank)

fetches the auto deleveraging rank and risk percentage for a list of symbols that have open positions

**Kind**: instance

**Returns**: `Array<object>` \- an array of [auto de leverage structure](https://docs.ccxt.com/docs/manual#auto-de-leverage-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>` | No | list of unified market symbols |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.portfolioMargin | `boolean` | No | set to true for the portfolio margin account |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-164)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchpositionsadlrank)
- [blofin](https://docs.ccxt.com/docs/exchanges/blofin#fetchpositionsadlrank)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchpositionsadlrank)
- [delta](https://docs.ccxt.com/docs/exchanges/delta#fetchpositionsadlrank)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#fetchpositionsadlrank)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchpositionsadlrank)
- [phemex](https://docs.ccxt.com/docs/exchanges/phemex#fetchpositionsadlrank)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#fetchpositionsadlrank)

* * *

## [fetchPositionsForSymbol](https://docs.ccxt.com/docs/base-spec\#fetchpositionsforsymbol)

fetch all open positions for specific symbol

**Kind**: instance

**Returns**: `Array<object>` \- a list of [position structure](https://docs.ccxt.com/docs/manual#position-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-165)

- [btse](https://docs.ccxt.com/docs/exchanges/btse#fetchpositionsforsymbol)
- [bydfi](https://docs.ccxt.com/docs/exchanges/bydfi#fetchpositionsforsymbol)
- [deepcoin](https://docs.ccxt.com/docs/exchanges/deepcoin#fetchpositionsforsymbol)
- [hashkey](https://docs.ccxt.com/docs/exchanges/hashkey#fetchpositionsforsymbol)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchpositionsforsymbol)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#fetchpositionsforsymbol)

* * *

## [fetchPositionsHistory](https://docs.ccxt.com/docs/base-spec\#fetchpositionshistory)

fetches historical positions

**Kind**: instance

**Returns**: `Array<object>` \- a list of [position structures](https://docs.ccxt.com/docs/manual#position-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>` | No | unified contract symbols |
| since | `int` | No | timestamp in ms of the earliest position to fetch, default=3 months ago, max range for params\["until"\] - since is 3 months |
| limit | `int` | No | the maximum amount of records to fetch, default=20, max=100 |
| params | `object` | Yes | extra parameters specific to the exchange API endpoint |
| params.until | `int` | No | timestamp in ms of the latest position to fetch, max range for params\["until"\] - since is 3 months |
| params.productType | `string` | No | USDT-FUTURES (default), COIN-FUTURES, USDC-FUTURES, SUSDT-FUTURES, SCOIN-FUTURES, or SUSDC-FUTURES |
| params.uta | `boolean` | No | set to true for the unified trading account (uta), defaults to false |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-166)

- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#fetchpositionshistory)
- [blofin](https://docs.ccxt.com/docs/exchanges/blofin#fetchpositionshistory)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchpositionshistory)
- [bydfi](https://docs.ccxt.com/docs/exchanges/bydfi#fetchpositionshistory)
- [extended](https://docs.ccxt.com/docs/exchanges/extended#fetchpositionshistory)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#fetchpositionshistory)
- [krakenfutures](https://docs.ccxt.com/docs/exchanges/krakenfutures#fetchpositionshistory)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchpositionshistory)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#fetchpositionshistory)
- [mudrex](https://docs.ccxt.com/docs/exchanges/mudrex#fetchpositionshistory)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchpositionshistory)
- [xt](https://docs.ccxt.com/docs/exchanges/xt#fetchpositionshistory)

* * *

## [fetchPositionsRisk](https://docs.ccxt.com/docs/base-spec\#fetchpositionsrisk)

fetch positions risk

**Kind**: instance

**Returns**: `object` \- data on the positions risk

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>`, `undefined` | Yes | list of unified market symbols |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-167)

- [aster](https://docs.ccxt.com/docs/exchanges/aster#fetchpositionsrisk)

* * *

## [fetchPositionsWs](https://docs.ccxt.com/docs/base-spec\#fetchpositionsws)

fetch all open positions

**Kind**: instance

**Returns**: `Array<object>` \- a list of [position structure](https://docs.ccxt.com/docs/manual#position-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>` | No | list of unified market symbols |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.returnRateLimits | `boolean` | No | set to true to return rate limit informations, defaults to false. |
| params.method | `string`, `undefined` | No | method to use. Can be account.position or v2/account.position |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-168)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchpositionsws)

* * *

## [fetchSettlementHistory](https://docs.ccxt.com/docs/base-spec\#fetchsettlementhistory)

fetches historical settlement records

**Kind**: instance

**Returns**: `Array<object>` \- a list of [settlement history objects](https://docs.ccxt.com/docs/manual#settlement-history-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol of the settlement history |
| since | `int` | No | timestamp in ms |
| limit | `int` | No | number of records, default 100, max 100 |
| params | `object` | No | exchange specific params |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-169)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchsettlementhistory)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchsettlementhistory)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#fetchsettlementhistory)
- [delta](https://docs.ccxt.com/docs/exchanges/delta#fetchsettlementhistory)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#fetchsettlementhistory)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#fetchsettlementhistory)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchsettlementhistory)

* * *

## [fetchSpotMarkets](https://docs.ccxt.com/docs/base-spec\#fetchspotmarkets)

retrieves data on all spot markets for hyperliquid

**Kind**: instance

**Returns**: `Array<object>` \- an array of objects representing market data

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-170)

- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#fetchspotmarkets)

* * *

## [fetchSpotOrder](https://docs.ccxt.com/docs/base-spec\#fetchspotorder)

fetch a spot order

**Kind**: instance

**Returns**: An [order structure](https://docs.ccxt.com/docs/manual#order-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| id | `string` | Yes | Order id |
| symbol | `string` | Yes | not sent to exchange except for trigger orders with clientOid, but used internally by CCXT to filter |
| params | `object` | No | exchange specific parameters |
| params.trigger | `bool` | No | true if fetching a trigger order |
| params.hf | `bool` | No | false, // true for hf order |
| params.clientOid | `bool` | No | unique order id created by users to identify their orders |
| params.marginMode | `object` | No | 'cross' or 'isolated' |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-171)

- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchspotorder)

* * *

## [fetchSpotOrdersByStatus](https://docs.ccxt.com/docs/base-spec\#fetchspotordersbystatus)

fetch a list of spot orders

**Kind**: instance

**Returns**: An [array of order structures](https://docs.ccxt.com/docs/manual#order-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| status | `string` | Yes | _not used for stop orders_ 'open' or 'closed' |
| symbol | `string` | Yes | unified market symbol |
| since | `int` | No | timestamp in ms of the earliest order |
| limit | `int` | No | max number of orders to return |
| params | `object` | No | exchange specific params |
| params.until | `int` | No | end time in ms |
| params.side | `string` | No | buy or sell |
| params.type | `string` | No | limit, market, limit\_stop or market\_stop |
| params.tradeType | `string` | No | TRADE for spot trading, MARGIN\_TRADE or MARGIN\_ISOLATED\_TRADE for Margin Trading |
| params.currentPage | `int` | No | _trigger orders only_ current page |
| params.orderIds | `string` | No | _trigger orders only_ comma separated order ID list |
| params.trigger | `bool` | No | True if fetching a trigger order |
| params.hf | `bool` | No | false, // true for hf order |
| params.marginMode | `string` | No | 'cross' or 'isolated', only for margin orders |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-172)

- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchspotordersbystatus)

* * *

## [fetchStatus](https://docs.ccxt.com/docs/base-spec\#fetchstatus)

the latest known information on the availability of the exchange API

**Kind**: instance

**Returns**: `object` \- a [status structure](https://docs.ccxt.com/docs/manual#exchange-status-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-173)

- [backpack](https://docs.ccxt.com/docs/exchanges/backpack#fetchstatus)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchstatus)
- [bitbns](https://docs.ccxt.com/docs/exchanges/bitbns#fetchstatus)
- [bitfinex](https://docs.ccxt.com/docs/exchanges/bitfinex#fetchstatus)
- [bitrue](https://docs.ccxt.com/docs/exchanges/bitrue#fetchstatus)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchstatus)
- [coincheck](https://docs.ccxt.com/docs/exchanges/coincheck#fetchstatus)
- [coinsph](https://docs.ccxt.com/docs/exchanges/coinsph#fetchstatus)
- [delta](https://docs.ccxt.com/docs/exchanges/delta#fetchstatus)
- [deribit](https://docs.ccxt.com/docs/exchanges/deribit#fetchstatus)
- [digifinex](https://docs.ccxt.com/docs/exchanges/digifinex#fetchstatus)
- [foxbit](https://docs.ccxt.com/docs/exchanges/foxbit#fetchstatus)
- [hashkey](https://docs.ccxt.com/docs/exchanges/hashkey#fetchstatus)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#fetchstatus)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#fetchstatus)
- [kraken](https://docs.ccxt.com/docs/exchanges/kraken#fetchstatus)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchstatus)
- [lighter](https://docs.ccxt.com/docs/exchanges/lighter#fetchstatus)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#fetchstatus)
- [modetrade](https://docs.ccxt.com/docs/exchanges/modetrade#fetchstatus)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#fetchstatus)
- [ndax](https://docs.ccxt.com/docs/exchanges/ndax#fetchstatus)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchstatus)
- [paradex](https://docs.ccxt.com/docs/exchanges/paradex#fetchstatus)
- [toobit](https://docs.ccxt.com/docs/exchanges/toobit#fetchstatus)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#fetchstatus)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#fetchstatus)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#fetchstatus)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#fetchstatus)
- [zebpay](https://docs.ccxt.com/docs/exchanges/zebpay#fetchstatus)

* * *

## [fetchSwapMarkets](https://docs.ccxt.com/docs/base-spec\#fetchswapmarkets)

retrieves data on all swap markets for hyperliquid

**Kind**: instance

**Returns**: `Array<object>` \- an array of objects representing market data

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-174)

- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#fetchswapmarkets)
- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#fetchswapmarkets)

* * *

## [fetchTicker](https://docs.ccxt.com/docs/base-spec\#fetchticker)

fetches a price ticker, a statistical calculation with the information calculated over the past 24 hours for a specific market

**Kind**: instance

**Returns**: `object` \- a [ticker structure](https://docs.ccxt.com/docs/manual#ticker-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to fetch the ticker for |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.loc | `string` | No | crypto location, default: us |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-175)

- [alpaca](https://docs.ccxt.com/docs/exchanges/alpaca#fetchticker)
- [apex](https://docs.ccxt.com/docs/exchanges/apex#fetchticker)
- [aster](https://docs.ccxt.com/docs/exchanges/aster#fetchticker)
- [backpack](https://docs.ccxt.com/docs/exchanges/backpack#fetchticker)
- [bigone](https://docs.ccxt.com/docs/exchanges/bigone#fetchticker)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchticker)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#fetchticker)
- [bit2c](https://docs.ccxt.com/docs/exchanges/bit2c#fetchticker)
- [bitbank](https://docs.ccxt.com/docs/exchanges/bitbank#fetchticker)
- [bitfinex](https://docs.ccxt.com/docs/exchanges/bitfinex#fetchticker)
- [bitflyer](https://docs.ccxt.com/docs/exchanges/bitflyer#fetchticker)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#fetchticker)
- [bithumb](https://docs.ccxt.com/docs/exchanges/bithumb#fetchticker)
- [bitopro](https://docs.ccxt.com/docs/exchanges/bitopro#fetchticker)
- [bitrue](https://docs.ccxt.com/docs/exchanges/bitrue#fetchticker)
- [bitso](https://docs.ccxt.com/docs/exchanges/bitso#fetchticker)
- [bitstamp](https://docs.ccxt.com/docs/exchanges/bitstamp#fetchticker)
- [bitteam](https://docs.ccxt.com/docs/exchanges/bitteam#fetchticker)
- [bittrade](https://docs.ccxt.com/docs/exchanges/bittrade#fetchticker)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#fetchticker)
- [blockchaincom](https://docs.ccxt.com/docs/exchanges/blockchaincom#fetchticker)
- [blofin](https://docs.ccxt.com/docs/exchanges/blofin#fetchticker)
- [btcbox](https://docs.ccxt.com/docs/exchanges/btcbox#fetchticker)
- [btcmarkets](https://docs.ccxt.com/docs/exchanges/btcmarkets#fetchticker)
- [btcturk](https://docs.ccxt.com/docs/exchanges/btcturk#fetchticker)
- [btse](https://docs.ccxt.com/docs/exchanges/btse#fetchticker)
- [bullish](https://docs.ccxt.com/docs/exchanges/bullish#fetchticker)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchticker)
- [bydfi](https://docs.ccxt.com/docs/exchanges/bydfi#fetchticker)
- [cex](https://docs.ccxt.com/docs/exchanges/cex#fetchticker)
- [coinbase](https://docs.ccxt.com/docs/exchanges/coinbase#fetchticker)
- [coinbaseexchange](https://docs.ccxt.com/docs/exchanges/coinbaseexchange#fetchticker)
- [coinbaseinternational](https://docs.ccxt.com/docs/exchanges/coinbaseinternational#fetchticker)
- [coincheck](https://docs.ccxt.com/docs/exchanges/coincheck#fetchticker)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#fetchticker)
- [coinmate](https://docs.ccxt.com/docs/exchanges/coinmate#fetchticker)
- [coinone](https://docs.ccxt.com/docs/exchanges/coinone#fetchticker)
- [coinsph](https://docs.ccxt.com/docs/exchanges/coinsph#fetchticker)
- [coinspot](https://docs.ccxt.com/docs/exchanges/coinspot#fetchticker)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#fetchticker)
- [delta](https://docs.ccxt.com/docs/exchanges/delta#fetchticker)
- [deribit](https://docs.ccxt.com/docs/exchanges/deribit#fetchticker)
- [derive](https://docs.ccxt.com/docs/exchanges/derive#fetchticker)
- [digifinex](https://docs.ccxt.com/docs/exchanges/digifinex#fetchticker)
- [extended](https://docs.ccxt.com/docs/exchanges/extended#fetchticker)
- [foxbit](https://docs.ccxt.com/docs/exchanges/foxbit#fetchticker)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#fetchticker)
- [gemini](https://docs.ccxt.com/docs/exchanges/gemini#fetchticker)
- [grvt](https://docs.ccxt.com/docs/exchanges/grvt#fetchticker)
- [hashkey](https://docs.ccxt.com/docs/exchanges/hashkey#fetchticker)
- [hibachi](https://docs.ccxt.com/docs/exchanges/hibachi#fetchticker)
- [hitbtc](https://docs.ccxt.com/docs/exchanges/hitbtc#fetchticker)
- [hollaex](https://docs.ccxt.com/docs/exchanges/hollaex#fetchticker)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#fetchticker)
- [independentreserve](https://docs.ccxt.com/docs/exchanges/independentreserve#fetchticker)
- [indodax](https://docs.ccxt.com/docs/exchanges/indodax#fetchticker)
- [kraken](https://docs.ccxt.com/docs/exchanges/kraken#fetchticker)
- [krakenfutures](https://docs.ccxt.com/docs/exchanges/krakenfutures#fetchticker)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchticker)
- [latoken](https://docs.ccxt.com/docs/exchanges/latoken#fetchticker)
- [lbank](https://docs.ccxt.com/docs/exchanges/lbank#fetchticker)
- [lighter](https://docs.ccxt.com/docs/exchanges/lighter#fetchticker)
- [luno](https://docs.ccxt.com/docs/exchanges/luno#fetchticker)
- [mercado](https://docs.ccxt.com/docs/exchanges/mercado#fetchticker)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#fetchticker)
- [mudrex](https://docs.ccxt.com/docs/exchanges/mudrex#fetchticker)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#fetchticker)
- [ndax](https://docs.ccxt.com/docs/exchanges/ndax#fetchticker)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchticker)
- [onetrading](https://docs.ccxt.com/docs/exchanges/onetrading#fetchticker)
- [p2b](https://docs.ccxt.com/docs/exchanges/p2b#fetchticker)
- [paradex](https://docs.ccxt.com/docs/exchanges/paradex#fetchticker)
- [paymium](https://docs.ccxt.com/docs/exchanges/paymium#fetchticker)
- [phemex](https://docs.ccxt.com/docs/exchanges/phemex#fetchticker)
- [poloniex](https://docs.ccxt.com/docs/exchanges/poloniex#fetchticker)
- [revolutx](https://docs.ccxt.com/docs/exchanges/revolutx#fetchticker)
- [tokocrypto](https://docs.ccxt.com/docs/exchanges/tokocrypto#fetchticker)
- [upbit](https://docs.ccxt.com/docs/exchanges/upbit#fetchticker)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#fetchticker)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#fetchticker)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#fetchticker)
- [xt](https://docs.ccxt.com/docs/exchanges/xt#fetchticker)
- [zaif](https://docs.ccxt.com/docs/exchanges/zaif#fetchticker)
- [zebpay](https://docs.ccxt.com/docs/exchanges/zebpay#fetchticker)

* * *

## [fetchTickerWs](https://docs.ccxt.com/docs/base-spec\#fetchtickerws)

fetches a price ticker, a statistical calculation with the information calculated over the past 24 hours for a specific market

**Kind**: instance

**Returns**: `object` \- a [ticker structure](https://docs.ccxt.com/docs/manual#ticker-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to fetch the ticker for |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.method | `string` | No | method to use can be ticker.price or ticker.book |
| params.returnRateLimits | `boolean` | No | return the rate limits for the exchange |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-176)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchtickerws)
- [cex](https://docs.ccxt.com/docs/exchanges/cex#fetchtickerws)
- [lbank](https://docs.ccxt.com/docs/exchanges/lbank#fetchtickerws)

* * *

## [fetchTickers](https://docs.ccxt.com/docs/base-spec\#fetchtickers)

fetches price tickers for multiple markets, statistical information calculated over the past 24 hours for each market

**Kind**: instance

**Returns**: `object` \- a dictionary of [ticker structures](https://docs.ccxt.com/docs/manual#ticker-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>` | No | unified symbols of the markets to fetch tickers for, defaults to all markets |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.loc | `string` | No | crypto location, default: us |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-177)

- [alpaca](https://docs.ccxt.com/docs/exchanges/alpaca#fetchtickers)
- [apex](https://docs.ccxt.com/docs/exchanges/apex#fetchtickers)
- [aster](https://docs.ccxt.com/docs/exchanges/aster#fetchtickers)
- [backpack](https://docs.ccxt.com/docs/exchanges/backpack#fetchtickers)
- [bigone](https://docs.ccxt.com/docs/exchanges/bigone#fetchtickers)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchtickers)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#fetchtickers)
- [bitbns](https://docs.ccxt.com/docs/exchanges/bitbns#fetchtickers)
- [bitfinex](https://docs.ccxt.com/docs/exchanges/bitfinex#fetchtickers)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#fetchtickers)
- [bithumb](https://docs.ccxt.com/docs/exchanges/bithumb#fetchtickers)
- [bitopro](https://docs.ccxt.com/docs/exchanges/bitopro#fetchtickers)
- [bitrue](https://docs.ccxt.com/docs/exchanges/bitrue#fetchtickers)
- [bitstamp](https://docs.ccxt.com/docs/exchanges/bitstamp#fetchtickers)
- [bitteam](https://docs.ccxt.com/docs/exchanges/bitteam#fetchtickers)
- [bittrade](https://docs.ccxt.com/docs/exchanges/bittrade#fetchtickers)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#fetchtickers)
- [blockchaincom](https://docs.ccxt.com/docs/exchanges/blockchaincom#fetchtickers)
- [blofin](https://docs.ccxt.com/docs/exchanges/blofin#fetchtickers)
- [btcbox](https://docs.ccxt.com/docs/exchanges/btcbox#fetchtickers)
- [btcturk](https://docs.ccxt.com/docs/exchanges/btcturk#fetchtickers)
- [btse](https://docs.ccxt.com/docs/exchanges/btse#fetchtickers)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchtickers)
- [bydfi](https://docs.ccxt.com/docs/exchanges/bydfi#fetchtickers)
- [cex](https://docs.ccxt.com/docs/exchanges/cex#fetchtickers)
- [coinbase](https://docs.ccxt.com/docs/exchanges/coinbase#fetchtickers)
- [coinbaseexchange](https://docs.ccxt.com/docs/exchanges/coinbaseexchange#fetchtickers)
- [coinbaseinternational](https://docs.ccxt.com/docs/exchanges/coinbaseinternational#fetchtickers)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#fetchtickers)
- [coinmate](https://docs.ccxt.com/docs/exchanges/coinmate#fetchtickers)
- [coinone](https://docs.ccxt.com/docs/exchanges/coinone#fetchtickers)
- [coinsph](https://docs.ccxt.com/docs/exchanges/coinsph#fetchtickers)
- [coinspot](https://docs.ccxt.com/docs/exchanges/coinspot#fetchtickers)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#fetchtickers)
- [cryptomus](https://docs.ccxt.com/docs/exchanges/cryptomus#fetchtickers)
- [deepcoin](https://docs.ccxt.com/docs/exchanges/deepcoin#fetchtickers)
- [delta](https://docs.ccxt.com/docs/exchanges/delta#fetchtickers)
- [deribit](https://docs.ccxt.com/docs/exchanges/deribit#fetchtickers)
- [digifinex](https://docs.ccxt.com/docs/exchanges/digifinex#fetchtickers)
- [extended](https://docs.ccxt.com/docs/exchanges/extended#fetchtickers)
- [foxbit](https://docs.ccxt.com/docs/exchanges/foxbit#fetchtickers)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#fetchtickers)
- [gemini](https://docs.ccxt.com/docs/exchanges/gemini#fetchtickers)
- [hashkey](https://docs.ccxt.com/docs/exchanges/hashkey#fetchtickers)
- [hitbtc](https://docs.ccxt.com/docs/exchanges/hitbtc#fetchtickers)
- [hollaex](https://docs.ccxt.com/docs/exchanges/hollaex#fetchtickers)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#fetchtickers)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#fetchtickers)
- [indodax](https://docs.ccxt.com/docs/exchanges/indodax#fetchtickers)
- [kraken](https://docs.ccxt.com/docs/exchanges/kraken#fetchtickers)
- [krakenfutures](https://docs.ccxt.com/docs/exchanges/krakenfutures#fetchtickers)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchtickers)
- [latoken](https://docs.ccxt.com/docs/exchanges/latoken#fetchtickers)
- [lbank](https://docs.ccxt.com/docs/exchanges/lbank#fetchtickers)
- [lighter](https://docs.ccxt.com/docs/exchanges/lighter#fetchtickers)
- [luno](https://docs.ccxt.com/docs/exchanges/luno#fetchtickers)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#fetchtickers)
- [mudrex](https://docs.ccxt.com/docs/exchanges/mudrex#fetchtickers)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#fetchtickers)
- [ndax](https://docs.ccxt.com/docs/exchanges/ndax#fetchtickers)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchtickers)
- [onetrading](https://docs.ccxt.com/docs/exchanges/onetrading#fetchtickers)
- [p2b](https://docs.ccxt.com/docs/exchanges/p2b#fetchtickers)
- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#fetchtickers)
- [paradex](https://docs.ccxt.com/docs/exchanges/paradex#fetchtickers)
- [phemex](https://docs.ccxt.com/docs/exchanges/phemex#fetchtickers)
- [poloniex](https://docs.ccxt.com/docs/exchanges/poloniex#fetchtickers)
- [revolutx](https://docs.ccxt.com/docs/exchanges/revolutx#fetchtickers)
- [tokocrypto](https://docs.ccxt.com/docs/exchanges/tokocrypto#fetchtickers)
- [toobit](https://docs.ccxt.com/docs/exchanges/toobit#fetchtickers)
- [upbit](https://docs.ccxt.com/docs/exchanges/upbit#fetchtickers)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#fetchtickers)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#fetchtickers)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#fetchtickers)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#fetchtickers)
- [xt](https://docs.ccxt.com/docs/exchanges/xt#fetchtickers)
- [zebpay](https://docs.ccxt.com/docs/exchanges/zebpay#fetchtickers)

* * *

## [fetchTime](https://docs.ccxt.com/docs/base-spec\#fetchtime)

fetches the current integer timestamp in milliseconds from the exchange server

**Kind**: instance

**Returns**: `int` \- the current integer timestamp in milliseconds from the exchange server

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-178)

- [alpaca](https://docs.ccxt.com/docs/exchanges/alpaca#fetchtime)
- [apex](https://docs.ccxt.com/docs/exchanges/apex#fetchtime)
- [aster](https://docs.ccxt.com/docs/exchanges/aster#fetchtime)
- [backpack](https://docs.ccxt.com/docs/exchanges/backpack#fetchtime)
- [bigone](https://docs.ccxt.com/docs/exchanges/bigone#fetchtime)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchtime)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#fetchtime)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#fetchtime)
- [bitrue](https://docs.ccxt.com/docs/exchanges/bitrue#fetchtime)
- [bittrade](https://docs.ccxt.com/docs/exchanges/bittrade#fetchtime)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#fetchtime)
- [btcmarkets](https://docs.ccxt.com/docs/exchanges/btcmarkets#fetchtime)
- [btse](https://docs.ccxt.com/docs/exchanges/btse#fetchtime)
- [bullish](https://docs.ccxt.com/docs/exchanges/bullish#fetchtime)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchtime)
- [cex](https://docs.ccxt.com/docs/exchanges/cex#fetchtime)
- [coinbase](https://docs.ccxt.com/docs/exchanges/coinbase#fetchtime)
- [coinbaseexchange](https://docs.ccxt.com/docs/exchanges/coinbaseexchange#fetchtime)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#fetchtime)
- [coinmate](https://docs.ccxt.com/docs/exchanges/coinmate#fetchtime)
- [coinsph](https://docs.ccxt.com/docs/exchanges/coinsph#fetchtime)
- [delta](https://docs.ccxt.com/docs/exchanges/delta#fetchtime)
- [deribit](https://docs.ccxt.com/docs/exchanges/deribit#fetchtime)
- [derive](https://docs.ccxt.com/docs/exchanges/derive#fetchtime)
- [digifinex](https://docs.ccxt.com/docs/exchanges/digifinex#fetchtime)
- [dydx](https://docs.ccxt.com/docs/exchanges/dydx#fetchtime)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#fetchtime)
- [hashkey](https://docs.ccxt.com/docs/exchanges/hashkey#fetchtime)
- [hibachi](https://docs.ccxt.com/docs/exchanges/hibachi#fetchtime)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#fetchtime)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#fetchtime)
- [indodax](https://docs.ccxt.com/docs/exchanges/indodax#fetchtime)
- [kraken](https://docs.ccxt.com/docs/exchanges/kraken#fetchtime)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchtime)
- [latoken](https://docs.ccxt.com/docs/exchanges/latoken#fetchtime)
- [lbank](https://docs.ccxt.com/docs/exchanges/lbank#fetchtime)
- [lighter](https://docs.ccxt.com/docs/exchanges/lighter#fetchtime)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#fetchtime)
- [modetrade](https://docs.ccxt.com/docs/exchanges/modetrade#fetchtime)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#fetchtime)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchtime)
- [onetrading](https://docs.ccxt.com/docs/exchanges/onetrading#fetchtime)
- [paradex](https://docs.ccxt.com/docs/exchanges/paradex#fetchtime)
- [poloniex](https://docs.ccxt.com/docs/exchanges/poloniex#fetchtime)
- [tokocrypto](https://docs.ccxt.com/docs/exchanges/tokocrypto#fetchtime)
- [toobit](https://docs.ccxt.com/docs/exchanges/toobit#fetchtime)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#fetchtime)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#fetchtime)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#fetchtime)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#fetchtime)
- [xt](https://docs.ccxt.com/docs/exchanges/xt#fetchtime)
- [zebpay](https://docs.ccxt.com/docs/exchanges/zebpay#fetchtime)

* * *

## [fetchTrades](https://docs.ccxt.com/docs/base-spec\#fetchtrades)

get the list of most recent trades for a particular symbol

**Kind**: instance

**Returns**: `Array<Trade>` \- a list of [trade structures](https://docs.ccxt.com/docs/manual#public-trades)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to fetch trades for |
| since | `int` | No | timestamp in ms of the earliest trade to fetch |
| limit | `int` | No | the maximum amount of trades to fetch |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.loc | `string` | No | crypto location, default: us |
| params.method | `string` | No | method, default: marketPublicGetV1beta3CryptoLocTrades |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-179)

- [alpaca](https://docs.ccxt.com/docs/exchanges/alpaca#fetchtrades)
- [apex](https://docs.ccxt.com/docs/exchanges/apex#fetchtrades)
- [aster](https://docs.ccxt.com/docs/exchanges/aster#fetchtrades)
- [backpack](https://docs.ccxt.com/docs/exchanges/backpack#fetchtrades)
- [bigone](https://docs.ccxt.com/docs/exchanges/bigone#fetchtrades)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchtrades)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#fetchtrades)
- [bit2c](https://docs.ccxt.com/docs/exchanges/bit2c#fetchtrades)
- [bitbank](https://docs.ccxt.com/docs/exchanges/bitbank#fetchtrades)
- [bitbns](https://docs.ccxt.com/docs/exchanges/bitbns#fetchtrades)
- [bitfinex](https://docs.ccxt.com/docs/exchanges/bitfinex#fetchtrades)
- [bitflyer](https://docs.ccxt.com/docs/exchanges/bitflyer#fetchtrades)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#fetchtrades)
- [bithumb](https://docs.ccxt.com/docs/exchanges/bithumb#fetchtrades)
- [bitopro](https://docs.ccxt.com/docs/exchanges/bitopro#fetchtrades)
- [bitrue](https://docs.ccxt.com/docs/exchanges/bitrue#fetchtrades)
- [bitso](https://docs.ccxt.com/docs/exchanges/bitso#fetchtrades)
- [bitstamp](https://docs.ccxt.com/docs/exchanges/bitstamp#fetchtrades)
- [bitteam](https://docs.ccxt.com/docs/exchanges/bitteam#fetchtrades)
- [bittrade](https://docs.ccxt.com/docs/exchanges/bittrade#fetchtrades)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#fetchtrades)
- [blofin](https://docs.ccxt.com/docs/exchanges/blofin#fetchtrades)
- [btcbox](https://docs.ccxt.com/docs/exchanges/btcbox#fetchtrades)
- [btcmarkets](https://docs.ccxt.com/docs/exchanges/btcmarkets#fetchtrades)
- [btcturk](https://docs.ccxt.com/docs/exchanges/btcturk#fetchtrades)
- [btse](https://docs.ccxt.com/docs/exchanges/btse#fetchtrades)
- [bullish](https://docs.ccxt.com/docs/exchanges/bullish#fetchtrades)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchtrades)
- [bydfi](https://docs.ccxt.com/docs/exchanges/bydfi#fetchtrades)
- [cex](https://docs.ccxt.com/docs/exchanges/cex#fetchtrades)
- [coinbase](https://docs.ccxt.com/docs/exchanges/coinbase#fetchtrades)
- [coinbaseexchange](https://docs.ccxt.com/docs/exchanges/coinbaseexchange#fetchtrades)
- [coincheck](https://docs.ccxt.com/docs/exchanges/coincheck#fetchtrades)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#fetchtrades)
- [coinmate](https://docs.ccxt.com/docs/exchanges/coinmate#fetchtrades)
- [coinone](https://docs.ccxt.com/docs/exchanges/coinone#fetchtrades)
- [coinsph](https://docs.ccxt.com/docs/exchanges/coinsph#fetchtrades)
- [coinspot](https://docs.ccxt.com/docs/exchanges/coinspot#fetchtrades)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#fetchtrades)
- [cryptomus](https://docs.ccxt.com/docs/exchanges/cryptomus#fetchtrades)
- [deepcoin](https://docs.ccxt.com/docs/exchanges/deepcoin#fetchtrades)
- [delta](https://docs.ccxt.com/docs/exchanges/delta#fetchtrades)
- [deribit](https://docs.ccxt.com/docs/exchanges/deribit#fetchtrades)
- [derive](https://docs.ccxt.com/docs/exchanges/derive#fetchtrades)
- [digifinex](https://docs.ccxt.com/docs/exchanges/digifinex#fetchtrades)
- [dydx](https://docs.ccxt.com/docs/exchanges/dydx#fetchtrades)
- [extended](https://docs.ccxt.com/docs/exchanges/extended#fetchtrades)
- [foxbit](https://docs.ccxt.com/docs/exchanges/foxbit#fetchtrades)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#fetchtrades)
- [gemini](https://docs.ccxt.com/docs/exchanges/gemini#fetchtrades)
- [grvt](https://docs.ccxt.com/docs/exchanges/grvt#fetchtrades)
- [hashkey](https://docs.ccxt.com/docs/exchanges/hashkey#fetchtrades)
- [hibachi](https://docs.ccxt.com/docs/exchanges/hibachi#fetchtrades)
- [hitbtc](https://docs.ccxt.com/docs/exchanges/hitbtc#fetchtrades)
- [hollaex](https://docs.ccxt.com/docs/exchanges/hollaex#fetchtrades)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#fetchtrades)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#fetchtrades)
- [independentreserve](https://docs.ccxt.com/docs/exchanges/independentreserve#fetchtrades)
- [indodax](https://docs.ccxt.com/docs/exchanges/indodax#fetchtrades)
- [kraken](https://docs.ccxt.com/docs/exchanges/kraken#fetchtrades)
- [krakenfutures](https://docs.ccxt.com/docs/exchanges/krakenfutures#fetchtrades)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchtrades)
- [latoken](https://docs.ccxt.com/docs/exchanges/latoken#fetchtrades)
- [lbank](https://docs.ccxt.com/docs/exchanges/lbank#fetchtrades)
- [luno](https://docs.ccxt.com/docs/exchanges/luno#fetchtrades)
- [mercado](https://docs.ccxt.com/docs/exchanges/mercado#fetchtrades)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#fetchtrades)
- [modetrade](https://docs.ccxt.com/docs/exchanges/modetrade#fetchtrades)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#fetchtrades)
- [ndax](https://docs.ccxt.com/docs/exchanges/ndax#fetchtrades)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchtrades)
- [p2b](https://docs.ccxt.com/docs/exchanges/p2b#fetchtrades)
- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#fetchtrades)
- [paradex](https://docs.ccxt.com/docs/exchanges/paradex#fetchtrades)
- [paymium](https://docs.ccxt.com/docs/exchanges/paymium#fetchtrades)
- [phemex](https://docs.ccxt.com/docs/exchanges/phemex#fetchtrades)
- [poloniex](https://docs.ccxt.com/docs/exchanges/poloniex#fetchtrades)
- [revolutx](https://docs.ccxt.com/docs/exchanges/revolutx#fetchtrades)
- [tokocrypto](https://docs.ccxt.com/docs/exchanges/tokocrypto#fetchtrades)
- [toobit](https://docs.ccxt.com/docs/exchanges/toobit#fetchtrades)
- [upbit](https://docs.ccxt.com/docs/exchanges/upbit#fetchtrades)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#fetchtrades)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#fetchtrades)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#fetchtrades)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#fetchtrades)
- [xt](https://docs.ccxt.com/docs/exchanges/xt#fetchtrades)
- [zaif](https://docs.ccxt.com/docs/exchanges/zaif#fetchtrades)
- [zebpay](https://docs.ccxt.com/docs/exchanges/zebpay#fetchtrades)

* * *

## [fetchTradesWs](https://docs.ccxt.com/docs/base-spec\#fetchtradesws)

fetch all trades made by the user

**Kind**: instance

**Returns**: `Array<object>` \- a list of [trade structures](https://docs.ccxt.com/docs/manual#trade-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol |
| since | `int` | No | the earliest time in ms to fetch trades for |
| limit | `int` | No | the maximum number of trades structures to retrieve, default=500, max=1000 |
| params | `object` | No | extra parameters specific to the exchange API endpoint EXCHANGE SPECIFIC PARAMETERS |
| params.fromId | `int` | No | trade ID to begin at |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-180)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchtradesws)
- [lbank](https://docs.ccxt.com/docs/exchanges/lbank#fetchtradesws)

* * *

## [fetchTradingFee](https://docs.ccxt.com/docs/base-spec\#fetchtradingfee)

fetch the trading fees for a market

**Kind**: instance

**Returns**: `object` \- a [fee structure](https://docs.ccxt.com/docs/manual#fee-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-181)

- [aster](https://docs.ccxt.com/docs/exchanges/aster#fetchtradingfee)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchtradingfee)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#fetchtradingfee)
- [bitflyer](https://docs.ccxt.com/docs/exchanges/bitflyer#fetchtradingfee)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#fetchtradingfee)
- [bitstamp](https://docs.ccxt.com/docs/exchanges/bitstamp#fetchtradingfee)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#fetchtradingfee)
- [btse](https://docs.ccxt.com/docs/exchanges/btse#fetchtradingfee)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchtradingfee)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#fetchtradingfee)
- [coinmate](https://docs.ccxt.com/docs/exchanges/coinmate#fetchtradingfee)
- [coinsph](https://docs.ccxt.com/docs/exchanges/coinsph#fetchtradingfee)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#fetchtradingfee)
- [digifinex](https://docs.ccxt.com/docs/exchanges/digifinex#fetchtradingfee)
- [extended](https://docs.ccxt.com/docs/exchanges/extended#fetchtradingfee)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#fetchtradingfee)
- [hashkey](https://docs.ccxt.com/docs/exchanges/hashkey#fetchtradingfee)
- [hitbtc](https://docs.ccxt.com/docs/exchanges/hitbtc#fetchtradingfee)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#fetchtradingfee)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#fetchtradingfee)
- [kraken](https://docs.ccxt.com/docs/exchanges/kraken#fetchtradingfee)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchtradingfee)
- [latoken](https://docs.ccxt.com/docs/exchanges/latoken#fetchtradingfee)
- [lbank](https://docs.ccxt.com/docs/exchanges/lbank#fetchtradingfee)
- [luno](https://docs.ccxt.com/docs/exchanges/luno#fetchtradingfee)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#fetchtradingfee)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchtradingfee)
- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#fetchtradingfee)
- [paradex](https://docs.ccxt.com/docs/exchanges/paradex#fetchtradingfee)
- [upbit](https://docs.ccxt.com/docs/exchanges/upbit#fetchtradingfee)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#fetchtradingfee)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#fetchtradingfee)
- [xt](https://docs.ccxt.com/docs/exchanges/xt#fetchtradingfee)
- [zebpay](https://docs.ccxt.com/docs/exchanges/zebpay#fetchtradingfee)

* * *

## [fetchTradingFees](https://docs.ccxt.com/docs/base-spec\#fetchtradingfees)

fetch the trading fees for multiple markets

**Kind**: instance

**Returns**: `object` \- a dictionary of [fee structures](https://docs.ccxt.com/docs/manual#fee-structure) indexed by market symbols

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.subType | `string` | No | "linear" or "inverse" |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-182)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchtradingfees)
- [bit2c](https://docs.ccxt.com/docs/exchanges/bit2c#fetchtradingfees)
- [bitbank](https://docs.ccxt.com/docs/exchanges/bitbank#fetchtradingfees)
- [bitfinex](https://docs.ccxt.com/docs/exchanges/bitfinex#fetchtradingfees)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#fetchtradingfees)
- [bitopro](https://docs.ccxt.com/docs/exchanges/bitopro#fetchtradingfees)
- [bitso](https://docs.ccxt.com/docs/exchanges/bitso#fetchtradingfees)
- [bitstamp](https://docs.ccxt.com/docs/exchanges/bitstamp#fetchtradingfees)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#fetchtradingfees)
- [blockchaincom](https://docs.ccxt.com/docs/exchanges/blockchaincom#fetchtradingfees)
- [btse](https://docs.ccxt.com/docs/exchanges/btse#fetchtradingfees)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchtradingfees)
- [cex](https://docs.ccxt.com/docs/exchanges/cex#fetchtradingfees)
- [coinbase](https://docs.ccxt.com/docs/exchanges/coinbase#fetchtradingfees)
- [coinbaseexchange](https://docs.ccxt.com/docs/exchanges/coinbaseexchange#fetchtradingfees)
- [coincheck](https://docs.ccxt.com/docs/exchanges/coincheck#fetchtradingfees)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#fetchtradingfees)
- [coinsph](https://docs.ccxt.com/docs/exchanges/coinsph#fetchtradingfees)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#fetchtradingfees)
- [cryptomus](https://docs.ccxt.com/docs/exchanges/cryptomus#fetchtradingfees)
- [deribit](https://docs.ccxt.com/docs/exchanges/deribit#fetchtradingfees)
- [extended](https://docs.ccxt.com/docs/exchanges/extended#fetchtradingfees)
- [foxbit](https://docs.ccxt.com/docs/exchanges/foxbit#fetchtradingfees)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#fetchtradingfees)
- [gemini](https://docs.ccxt.com/docs/exchanges/gemini#fetchtradingfees)
- [hashkey](https://docs.ccxt.com/docs/exchanges/hashkey#fetchtradingfees)
- [hibachi](https://docs.ccxt.com/docs/exchanges/hibachi#fetchtradingfees)
- [hitbtc](https://docs.ccxt.com/docs/exchanges/hitbtc#fetchtradingfees)
- [hollaex](https://docs.ccxt.com/docs/exchanges/hollaex#fetchtradingfees)
- [independentreserve](https://docs.ccxt.com/docs/exchanges/independentreserve#fetchtradingfees)
- [krakenfutures](https://docs.ccxt.com/docs/exchanges/krakenfutures#fetchtradingfees)
- [lbank](https://docs.ccxt.com/docs/exchanges/lbank#fetchtradingfees)
- [modetrade](https://docs.ccxt.com/docs/exchanges/modetrade#fetchtradingfees)
- [onetrading](https://docs.ccxt.com/docs/exchanges/onetrading#fetchtradingfees)
- [paradex](https://docs.ccxt.com/docs/exchanges/paradex#fetchtradingfees)
- [poloniex](https://docs.ccxt.com/docs/exchanges/poloniex#fetchtradingfees)
- [toobit](https://docs.ccxt.com/docs/exchanges/toobit#fetchtradingfees)
- [upbit](https://docs.ccxt.com/docs/exchanges/upbit#fetchtradingfees)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#fetchtradingfees)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#fetchtradingfees)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#fetchtradingfees)
- [xt](https://docs.ccxt.com/docs/exchanges/xt#fetchtradingfees)
- [zebpay](https://docs.ccxt.com/docs/exchanges/zebpay#fetchtradingfees)

* * *

## [fetchTradingFeesWs](https://docs.ccxt.com/docs/base-spec\#fetchtradingfeesws)

fetch the trading fees for multiple markets

**Kind**: instance

**Returns**: `object` \- a dictionary of [fee structures](https://docs.ccxt.com/docs/manual#fee-structure) indexed by market symbols

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-183)

- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#fetchtradingfeesws)

* * *

## [fetchTradingLimits](https://docs.ccxt.com/docs/base-spec\#fetchtradinglimits)

fetch the trading limits for a market

**Kind**: instance

**Returns**: `object` \- a [trading limits structure](https://docs.ccxt.com/docs/manual#trading-limits-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>`, `undefined` | Yes | unified market symbol |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-184)

- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#fetchtradinglimits)

* * *

## [fetchTransactionFee](https://docs.ccxt.com/docs/base-spec\#fetchtransactionfee)

fetch the fee for a transaction

**Kind**: instance

**Returns**: `object` \- a [fee structure](https://docs.ccxt.com/docs/manual#fee-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| code | `string` | Yes | unified currency code |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-185)

- [indodax](https://docs.ccxt.com/docs/exchanges/indodax#fetchtransactionfee)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchtransactionfee)

* * *

## [fetchTransactionFees](https://docs.ccxt.com/docs/base-spec\#fetchtransactionfees)

please use fetchDepositWithdrawFees instead

**Kind**: instance

**Returns**: `Array<object>` \- a list of [fee structures](https://docs.ccxt.com/docs/manual#fee-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| codes | `Array<string>`, `undefined` | Yes | not used by fetchTransactionFees () |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-186)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchtransactionfees)
- [bitso](https://docs.ccxt.com/docs/exchanges/bitso#fetchtransactionfees)
- [bitstamp](https://docs.ccxt.com/docs/exchanges/bitstamp#fetchtransactionfees)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#fetchtransactionfees)
- [lbank](https://docs.ccxt.com/docs/exchanges/lbank#fetchtransactionfees)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#fetchtransactionfees)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#fetchtransactionfees)

* * *

## [fetchTransactions](https://docs.ccxt.com/docs/base-spec\#fetchtransactions)

fetch history of deposits, withdrawals, and transfers

**Kind**: instance

**Returns**: `Array<Transaction>` \- a list of [transaction structures](https://docs.ccxt.com/docs/manual#transaction-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| code | `string` | No | unified currency code |
| since | `int` | No | the earliest time in ms to fetch transactions for |
| limit | `int` | No | the maximum number of transaction structures to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.paginate | `boolean` | No | default false, when true will automatically paginate by calling this endpoint multiple times. See in the docs all the [available parameters](https://docs.ccxt.com/docs/manual#pagination-params) |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-187)

- [extended](https://docs.ccxt.com/docs/exchanges/extended#fetchtransactions)
- [foxbit](https://docs.ccxt.com/docs/exchanges/foxbit#fetchtransactions)
- [latoken](https://docs.ccxt.com/docs/exchanges/latoken#fetchtransactions)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#fetchtransactions)

* * *

## [fetchTransfer](https://docs.ccxt.com/docs/base-spec\#fetchtransfer)

fetches a transfer

**Kind**: instance

**Returns**: `object` \- a [transfer structure](https://docs.ccxt.com/docs/manual#transfer-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| id | `string` | Yes | transfer id |
| code | `string` | No | unified currency code of the currency transferred |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-188)

- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#fetchtransfer)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#fetchtransfer)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchtransfer)

* * *

## [fetchTransfers](https://docs.ccxt.com/docs/base-spec\#fetchtransfers)

fetch a history of internal transfers made on an account

**Kind**: instance

**Returns**: `Array<object>` \- a list of [transfer structures](https://docs.ccxt.com/docs/manual#transfer-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| code | `string` | Yes | unified currency code of the currency transferred |
| since | `int` | No | the earliest time in ms to fetch transfers for |
| limit | `int` | No | the maximum number of transfers structures to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.until | `int` | No | the latest time in ms to fetch transfers for |
| params.paginate | `boolean` | No | default false, when true will automatically paginate by calling this endpoint multiple times. See in the docs all the [available parameters](https://docs.ccxt.com/docs/manual#pagination-params) |
| params.internal | `boolean` | No | default false, when true will fetch pay trade history |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-189)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchtransfers)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#fetchtransfers)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#fetchtransfers)
- [bitrue](https://docs.ccxt.com/docs/exchanges/bitrue#fetchtransfers)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#fetchtransfers)
- [bullish](https://docs.ccxt.com/docs/exchanges/bullish#fetchtransfers)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchtransfers)
- [bydfi](https://docs.ccxt.com/docs/exchanges/bydfi#fetchtransfers)
- [coinbaseinternational](https://docs.ccxt.com/docs/exchanges/coinbaseinternational#fetchtransfers)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#fetchtransfers)
- [deribit](https://docs.ccxt.com/docs/exchanges/deribit#fetchtransfers)
- [digifinex](https://docs.ccxt.com/docs/exchanges/digifinex#fetchtransfers)
- [dydx](https://docs.ccxt.com/docs/exchanges/dydx#fetchtransfers)
- [extended](https://docs.ccxt.com/docs/exchanges/extended#fetchtransfers)
- [grvt](https://docs.ccxt.com/docs/exchanges/grvt#fetchtransfers)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#fetchtransfers)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchtransfers)
- [latoken](https://docs.ccxt.com/docs/exchanges/latoken#fetchtransfers)
- [lighter](https://docs.ccxt.com/docs/exchanges/lighter#fetchtransfers)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#fetchtransfers)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchtransfers)
- [paradex](https://docs.ccxt.com/docs/exchanges/paradex#fetchtransfers)
- [phemex](https://docs.ccxt.com/docs/exchanges/phemex#fetchtransfers)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#fetchtransfers)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#fetchtransfers)

* * *

## [fetchUnderlyingAssets](https://docs.ccxt.com/docs/base-spec\#fetchunderlyingassets)

fetches the market ids of underlying assets for a specific contract market type

**Kind**: instance

**Returns**: `Array<object>` \- a list of [underlying assets](https://docs.ccxt.com/docs/manual#underlying-assets-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| params | `object` | No | exchange specific params |
| params.type | `string` | No | the contract market type, 'option', 'swap' or 'future', the default is 'option' |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-190)

- [gate](https://docs.ccxt.com/docs/exchanges/gate#fetchunderlyingassets)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchunderlyingassets)

* * *

## [fetchUtaBalance](https://docs.ccxt.com/docs/base-spec\#fetchutabalance)

helper method for fetching balance with unified trading account (uta) endpoint

**Kind**: instance

**Returns**: `object` \- a [balance structure](https://docs.ccxt.com/docs/manual#balance-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.type | `string` | No | 'unified', 'spot', 'funding', 'cross', 'isolated' or 'swap' (default is 'unified') |
| params.marginMode | `string` | No | 'cross' or 'isolated', margin type for fetching margin balance, only applicable if type is margin (default is cross) |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-191)

- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchutabalance)

* * *

## [fetchUtaOrder](https://docs.ccxt.com/docs/base-spec\#fetchutaorder)

fetch uta order

**Kind**: instance

**Returns**: `object` \- An [order structure](https://docs.ccxt.com/docs/manual#order-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| id | `string` | Yes | order id |
| symbol | `string` | Yes | unified symbol of the market the order was made in |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.accountMode | `string` | No | 'unified' or 'classic' (default is 'unified') |
| params.clientOrderId | `string` | No | client order id, required if id is not provided |
| params.marginMode | `string` | No | 'cross' or 'isolated', required if fetching a margin order (unified accountMode supports only cross margin) |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-192)

- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchutaorder)

* * *

## [fetchUtaOrdersByStatus](https://docs.ccxt.com/docs/base-spec\#fetchutaordersbystatus)

helper method for fetching orders by status with uta endpoint

**Kind**: instance

**Returns**: An [array of order structures](https://docs.ccxt.com/docs/manual#order-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| status | `string` | Yes | 'active' or 'closed', only 'active' is valid for stop orders |
| symbol | `string` | Yes | unified symbol for the market to retrieve orders from |
| since | `int` | No | timestamp in ms of the earliest order to retrieve |
| limit | `int` | No | The maximum number of orders to retrieve |
| params | `object` | No | exchange specific parameters |
| params.until | `int` | No | End time in ms |
| params.side | `string` | No | _closed orders only_ 'BUY' or 'SELL' |
| params.accountMode | `string` | No | 'unified' or 'classic' (default is unified) |
| params.marginMode | `string` | No | 'cross' or 'isolated', only for margin orders (unified accountMode supports only cross margin) |
| params.paginate | `boolean` | No | default false, when true will automatically paginate by calling this endpoint multiple times. See in the docs all the [availble parameters](https://docs.ccxt.com/docs/manual#pagination-params) |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-193)

- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchutaordersbystatus)

* * *

## [fetchVolatilityHistory](https://docs.ccxt.com/docs/base-spec\#fetchvolatilityhistory)

fetch the historical volatility of an option market based on an underlying asset

**Kind**: instance

**Returns**: `Array<object>` \- a list of [volatility history objects](https://docs.ccxt.com/docs/manual#volatility-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| code | `string` | Yes | unified currency code |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.period | `int` | No | the period in days to fetch the volatility for: 7,14,21,30,60,90,180,270 |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-194)

- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchvolatilityhistory)
- [deribit](https://docs.ccxt.com/docs/exchanges/deribit#fetchvolatilityhistory)

* * *

## [fetchWithdrawal](https://docs.ccxt.com/docs/base-spec\#fetchwithdrawal)

fetch data on a currency withdrawal via the withdrawal id, looks back 30 days for uta accounts and 90 days otherwise

**Kind**: instance

**Returns**: `object` \- a [transaction structure](https://docs.ccxt.com/docs/manual#transaction-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| id | `string` | Yes | withdrawal id |
| code | `string` | No | unified currency code |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.uta | `boolean` | No | set to true for the unified trading account (uta), defaults to false |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-195)

- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#fetchwithdrawal)
- [bithumb](https://docs.ccxt.com/docs/exchanges/bithumb#fetchwithdrawal)
- [bitopro](https://docs.ccxt.com/docs/exchanges/bitopro#fetchwithdrawal)
- [blockchaincom](https://docs.ccxt.com/docs/exchanges/blockchaincom#fetchwithdrawal)
- [hollaex](https://docs.ccxt.com/docs/exchanges/hollaex#fetchwithdrawal)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchwithdrawal)
- [upbit](https://docs.ccxt.com/docs/exchanges/upbit#fetchwithdrawal)

* * *

## [fetchWithdrawalWhitelist](https://docs.ccxt.com/docs/base-spec\#fetchwithdrawalwhitelist)

fetch a list of allowed withdrawal addresses

**Kind**: instance

**Returns**: `Array<object>` \- a list response from the exchange

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.generation | `int` | No | _only generation 2 is supported_ if you want to use the API generation 1 or 2, default is 2 |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-196)

- [bithumb](https://docs.ccxt.com/docs/exchanges/bithumb#fetchwithdrawalwhitelist)

* * *

## [fetchWithdrawals](https://docs.ccxt.com/docs/base-spec\#fetchwithdrawals)

fetch all withdrawals made from an account

**Kind**: instance

**Returns**: `Array<object>` \- a list of [transaction structures](https://docs.ccxt.com/docs/manual#transaction-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| code | `string` | No | unified currency code |
| since | `int` | No | the earliest time in ms to fetch withdrawals for |
| limit | `int` | No | the maximum number of withdrawal structures to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-197)

- [alpaca](https://docs.ccxt.com/docs/exchanges/alpaca#fetchwithdrawals)
- [backpack](https://docs.ccxt.com/docs/exchanges/backpack#fetchwithdrawals)
- [bigone](https://docs.ccxt.com/docs/exchanges/bigone#fetchwithdrawals)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#fetchwithdrawals)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#fetchwithdrawals)
- [bitbns](https://docs.ccxt.com/docs/exchanges/bitbns#fetchwithdrawals)
- [bitflyer](https://docs.ccxt.com/docs/exchanges/bitflyer#fetchwithdrawals)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#fetchwithdrawals)
- [bithumb](https://docs.ccxt.com/docs/exchanges/bithumb#fetchwithdrawals)
- [bitopro](https://docs.ccxt.com/docs/exchanges/bitopro#fetchwithdrawals)
- [bitrue](https://docs.ccxt.com/docs/exchanges/bitrue#fetchwithdrawals)
- [bitstamp](https://docs.ccxt.com/docs/exchanges/bitstamp#fetchwithdrawals)
- [bittrade](https://docs.ccxt.com/docs/exchanges/bittrade#fetchwithdrawals)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#fetchwithdrawals)
- [blockchaincom](https://docs.ccxt.com/docs/exchanges/blockchaincom#fetchwithdrawals)
- [blofin](https://docs.ccxt.com/docs/exchanges/blofin#fetchwithdrawals)
- [btcmarkets](https://docs.ccxt.com/docs/exchanges/btcmarkets#fetchwithdrawals)
- [btse](https://docs.ccxt.com/docs/exchanges/btse#fetchwithdrawals)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#fetchwithdrawals)
- [bydfi](https://docs.ccxt.com/docs/exchanges/bydfi#fetchwithdrawals)
- [coinbase](https://docs.ccxt.com/docs/exchanges/coinbase#fetchwithdrawals)
- [coinbaseexchange](https://docs.ccxt.com/docs/exchanges/coinbaseexchange#fetchwithdrawals)
- [coinbaseinternational](https://docs.ccxt.com/docs/exchanges/coinbaseinternational#fetchwithdrawals)
- [coincheck](https://docs.ccxt.com/docs/exchanges/coincheck#fetchwithdrawals)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#fetchwithdrawals)
- [coinsph](https://docs.ccxt.com/docs/exchanges/coinsph#fetchwithdrawals)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#fetchwithdrawals)
- [deepcoin](https://docs.ccxt.com/docs/exchanges/deepcoin#fetchwithdrawals)
- [deribit](https://docs.ccxt.com/docs/exchanges/deribit#fetchwithdrawals)
- [derive](https://docs.ccxt.com/docs/exchanges/derive#fetchwithdrawals)
- [digifinex](https://docs.ccxt.com/docs/exchanges/digifinex#fetchwithdrawals)
- [dydx](https://docs.ccxt.com/docs/exchanges/dydx#fetchwithdrawals)
- [extended](https://docs.ccxt.com/docs/exchanges/extended#fetchwithdrawals)
- [foxbit](https://docs.ccxt.com/docs/exchanges/foxbit#fetchwithdrawals)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#fetchwithdrawals)
- [grvt](https://docs.ccxt.com/docs/exchanges/grvt#fetchwithdrawals)
- [hashkey](https://docs.ccxt.com/docs/exchanges/hashkey#fetchwithdrawals)
- [hibachi](https://docs.ccxt.com/docs/exchanges/hibachi#fetchwithdrawals)
- [hitbtc](https://docs.ccxt.com/docs/exchanges/hitbtc#fetchwithdrawals)
- [hollaex](https://docs.ccxt.com/docs/exchanges/hollaex#fetchwithdrawals)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#fetchwithdrawals)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#fetchwithdrawals)
- [kraken](https://docs.ccxt.com/docs/exchanges/kraken#fetchwithdrawals)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#fetchwithdrawals)
- [lbank](https://docs.ccxt.com/docs/exchanges/lbank#fetchwithdrawals)
- [lighter](https://docs.ccxt.com/docs/exchanges/lighter#fetchwithdrawals)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#fetchwithdrawals)
- [modetrade](https://docs.ccxt.com/docs/exchanges/modetrade#fetchwithdrawals)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#fetchwithdrawals)
- [ndax](https://docs.ccxt.com/docs/exchanges/ndax#fetchwithdrawals)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#fetchwithdrawals)
- [paradex](https://docs.ccxt.com/docs/exchanges/paradex#fetchwithdrawals)
- [phemex](https://docs.ccxt.com/docs/exchanges/phemex#fetchwithdrawals)
- [poloniex](https://docs.ccxt.com/docs/exchanges/poloniex#fetchwithdrawals)
- [tokocrypto](https://docs.ccxt.com/docs/exchanges/tokocrypto#fetchwithdrawals)
- [toobit](https://docs.ccxt.com/docs/exchanges/toobit#fetchwithdrawals)
- [upbit](https://docs.ccxt.com/docs/exchanges/upbit#fetchwithdrawals)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#fetchwithdrawals)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#fetchwithdrawals)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#fetchwithdrawals)
- [xt](https://docs.ccxt.com/docs/exchanges/xt#fetchwithdrawals)

* * *

## [fetchWithdrawalsWs](https://docs.ccxt.com/docs/base-spec\#fetchwithdrawalsws)

fetch all withdrawals made from an account

**Kind**: instance

**Returns**: `Array<object>` \- a list of [transaction structures](https://docs.ccxt.com/docs/manual#transaction-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| code | `string` | Yes | unified currency code |
| since | `int` | No | the earliest time in ms to fetch withdrawals for |
| limit | `int` | No | the maximum number of withdrawals structures to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-198)

- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#fetchwithdrawalsws)

* * *

## [isUTAEnabled](https://docs.ccxt.com/docs/base-spec\#isutaenabled)

returns true or false so the user can check if unified account is enabled

**Kind**: instance

**Returns**: `boolean` \- true if unified account is enabled, false otherwise

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-199)

- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#isutaenabled)

* * *

## [isUnifiedEnabled](https://docs.ccxt.com/docs/base-spec\#isunifiedenabled)

returns \[enableUnifiedMargin, enableUnifiedAccount\] so the user can check if unified account is enabled

**Kind**: instance

**Returns**: `any` \- \[enableUnifiedMargin, enableUnifiedAccount\]

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-200)

- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#isunifiedenabled)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#isunifiedenabled)

* * *

## [loadMigrationStatus](https://docs.ccxt.com/docs/base-spec\#loadmigrationstatus)

loads the migration status for the account (hf or not)

**Kind**: instance

**Returns**: `any` \- ignore

| Param | Type | Description |
| --- | --- | --- |
| force | `boolean` | load account state for non hf |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-201)

- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#loadmigrationstatus)

* * *

## [loadUnifiedStatus](https://docs.ccxt.com/docs/base-spec\#loadunifiedstatus)

returns unifiedAccount so the user can check if the unified account is enabled

**Kind**: instance

**Returns**: `boolean` \- true or false if the enabled unified account is enabled or not and sets the unifiedAccount option if it is undefined

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-202)

- [gate](https://docs.ccxt.com/docs/exchanges/gate#loadunifiedstatus)

* * *

## [market](https://docs.ccxt.com/docs/base-spec\#market)

calculates the presumptive fee that would be charged for an order

**Kind**: instance

**Returns**: `object` \- contains the rate, the percentage multiplied to the order amount to obtain the fee amount, and cost, the total value of the fee in units of the quote currency, for the order

| Param | Type | Description |
| --- | --- | --- |
| symbol | `string` | unified market symbol |
| type | `string` | not used by btcmarkets.calculateFee |
| side | `string` | not used by btcmarkets.calculateFee |
| amount | `float` | how much you want to trade, in units of the base currency on most exchanges, or number of contracts |
| price | `float` | the price for the order to be filled at, in units of the quote currency |
| takerOrMaker | `string` | 'taker' or 'maker' |
| params | `object` |  |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-203)

- <anonymous>

* * *

## [preLoadLighterLibrary](https://docs.ccxt.com/docs/base-spec\#preloadlighterlibrary)

if the required credentials are available in options, it will pre-load the lighter Signer to avoid delaying sensitive calls like createOrder the first time they're executed

**Kind**: instance

**Returns**: `boolean` \- true if the signer was loaded, false otherwise

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-204)

- [lighter](https://docs.ccxt.com/docs/exchanges/lighter#preloadlighterlibrary)

* * *

## [redeemGiftCode](https://docs.ccxt.com/docs/base-spec\#redeemgiftcode)

redeem gift code

**Kind**: instance

**Returns**: `object` \- response from the exchange

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| giftcardCode | `string` | Yes |  |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-205)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#redeemgiftcode)

* * *

## [reduceMargin](https://docs.ccxt.com/docs/base-spec\#reducemargin)

remove margin from a position

**Kind**: instance

**Returns**: `object` \- a [margin structure](https://docs.ccxt.com/docs/manual#reduce-margin-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol |
| amount | `float` | Yes | the amount of margin to remove |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-206)

- [aster](https://docs.ccxt.com/docs/exchanges/aster#reducemargin)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#reducemargin)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#reducemargin)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#reducemargin)
- [delta](https://docs.ccxt.com/docs/exchanges/delta#reducemargin)
- [digifinex](https://docs.ccxt.com/docs/exchanges/digifinex#reducemargin)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#reducemargin)
- [hashkey](https://docs.ccxt.com/docs/exchanges/hashkey#reducemargin)
- [hitbtc](https://docs.ccxt.com/docs/exchanges/hitbtc#reducemargin)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#reducemargin)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#reducemargin)
- [lighter](https://docs.ccxt.com/docs/exchanges/lighter#reducemargin)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#reducemargin)
- [mudrex](https://docs.ccxt.com/docs/exchanges/mudrex#reducemargin)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#reducemargin)
- [poloniex](https://docs.ccxt.com/docs/exchanges/poloniex#reducemargin)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#reducemargin)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#reducemargin)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#reducemargin)
- [xt](https://docs.ccxt.com/docs/exchanges/xt#reducemargin)
- [zebpay](https://docs.ccxt.com/docs/exchanges/zebpay#reducemargin)

* * *

## [repayCrossMargin](https://docs.ccxt.com/docs/base-spec\#repaycrossmargin)

repay borrowed margin and interest

**Kind**: instance

**Returns**: `object` \- a [margin loan structure](https://docs.ccxt.com/docs/manual#margin-loan-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| code | `string` | Yes | unified currency code of the currency to repay |
| amount | `float` | Yes | the amount to repay |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.portfolioMargin | `boolean` | No | set to true if you would like to repay margin in a portfolio margin account |
| params.repayCrossMarginMethod | `string` | No | _portfolio margin only_ 'papiPostRepayLoan' (default), 'papiPostMarginRepayDebt' (alternative) |
| params.specifyRepayAssets | `string` | No | _portfolio margin papiPostMarginRepayDebt only_ specific asset list to repay debt |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-207)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#repaycrossmargin)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#repaycrossmargin)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#repaycrossmargin)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#repaycrossmargin)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#repaycrossmargin)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#repaycrossmargin)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#repaycrossmargin)

* * *

## [repayIsolatedMargin](https://docs.ccxt.com/docs/base-spec\#repayisolatedmargin)

repay borrowed margin and interest

**Kind**: instance

**Returns**: `object` \- a [margin loan structure](https://docs.ccxt.com/docs/manual#margin-loan-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol, required for isolated margin |
| code | `string` | Yes | unified currency code of the currency to repay |
| amount | `float` | Yes | the amount to repay |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-208)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#repayisolatedmargin)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#repayisolatedmargin)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#repayisolatedmargin)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#repayisolatedmargin)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#repayisolatedmargin)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#repayisolatedmargin)

* * *

## [repayMargin](https://docs.ccxt.com/docs/base-spec\#repaymargin)

repay borrowed margin and interest

**Kind**: instance

**Returns**: `object` \- a [margin loan structure](https://docs.ccxt.com/docs/manual#margin-loan-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| code | `string` | Yes | unified currency code of the currency to repay |
| amount | `float` | Yes | the amount to repay |
| symbol | `string` | Yes | not used by woo.repayMargin () |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-209)

- [woo](https://docs.ccxt.com/docs/exchanges/woo#repaymargin)

* * *

## [reserveRequestWeight](https://docs.ccxt.com/docs/base-spec\#reserverequestweight)

Instead of trading to increase the address based rate limits, this action allows reserving additional actions for 0.0005 USDC per request. The cost is paid from the Perps balance.

**Kind**: instance

**Returns**: `object` \- a response object

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| weight | `number` | Yes | the weight to reserve, 1 weight = 1 action, 0.0005 USDC per action |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-210)

- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#reserverequestweight)

* * *

## [setAgentAbstraction](https://docs.ccxt.com/docs/base-spec\#setagentabstraction)

set agent abstraction mode

**Kind**: instance

**Returns**: dictionary response from the exchange

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| abstraction | `string` | Yes | one of the strings \["i", "u", "p"\] where "i" is "disabled", "u" is "unifiedAccount", and "p" is "portfolioMargin" |
| params | `object` | No |  |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-211)

- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#setagentabstraction)

* * *

## [setContractLeverage](https://docs.ccxt.com/docs/base-spec\#setcontractleverage)

set the level of leverage for a market

**Kind**: instance

**Returns**: `object` \- response from the exchange

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| leverage | `float` | Yes | the rate of leverage |
| symbol | `string` | Yes | unified market symbol |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.uta | `boolean` | No | set to true for the unified trading account (uta) |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-212)

- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#setcontractleverage)

* * *

## [setLeverage](https://docs.ccxt.com/docs/base-spec\#setleverage)

set the level of leverage for a market

**Kind**: instance

**Returns**: `object` \- response from the exchange

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| leverage | `float` | Yes | the rate of leverage |
| symbol | `string` | Yes | unified market symbol |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-213)

- [apex](https://docs.ccxt.com/docs/exchanges/apex#setleverage)
- [aster](https://docs.ccxt.com/docs/exchanges/aster#setleverage)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#setleverage)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#setleverage)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#setleverage)
- [bitrue](https://docs.ccxt.com/docs/exchanges/bitrue#setleverage)
- [blofin](https://docs.ccxt.com/docs/exchanges/blofin#setleverage)
- [btse](https://docs.ccxt.com/docs/exchanges/btse#setleverage)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#setleverage)
- [bydfi](https://docs.ccxt.com/docs/exchanges/bydfi#setleverage)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#setleverage)
- [deepcoin](https://docs.ccxt.com/docs/exchanges/deepcoin#setleverage)
- [delta](https://docs.ccxt.com/docs/exchanges/delta#setleverage)
- [digifinex](https://docs.ccxt.com/docs/exchanges/digifinex#setleverage)
- [extended](https://docs.ccxt.com/docs/exchanges/extended#setleverage)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#setleverage)
- [grvt](https://docs.ccxt.com/docs/exchanges/grvt#setleverage)
- [hashkey](https://docs.ccxt.com/docs/exchanges/hashkey#setleverage)
- [hitbtc](https://docs.ccxt.com/docs/exchanges/hitbtc#setleverage)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#setleverage)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#setleverage)
- [krakenfutures](https://docs.ccxt.com/docs/exchanges/krakenfutures#setleverage)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#setleverage)
- [lighter](https://docs.ccxt.com/docs/exchanges/lighter#setleverage)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#setleverage)
- [modetrade](https://docs.ccxt.com/docs/exchanges/modetrade#setleverage)
- [mudrex](https://docs.ccxt.com/docs/exchanges/mudrex#setleverage)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#setleverage)
- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#setleverage)
- [paradex](https://docs.ccxt.com/docs/exchanges/paradex#setleverage)
- [phemex](https://docs.ccxt.com/docs/exchanges/phemex#setleverage)
- [poloniex](https://docs.ccxt.com/docs/exchanges/poloniex#setleverage)
- [toobit](https://docs.ccxt.com/docs/exchanges/toobit#setleverage)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#setleverage)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#setleverage)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#setleverage)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#setleverage)
- [xt](https://docs.ccxt.com/docs/exchanges/xt#setleverage)
- [zebpay](https://docs.ccxt.com/docs/exchanges/zebpay#setleverage)

* * *

## [setMargin](https://docs.ccxt.com/docs/base-spec\#setmargin)

Either adds or reduces margin in an isolated position in order to set the margin to a specific value

**Kind**: instance

**Returns**: `object` \- A [margin structure](https://docs.ccxt.com/docs/manual#margin-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol of the market to set margin in |
| amount | `float` | Yes | the amount to set the margin to |
| params | `object` | No | parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-214)

- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#setmargin)
- [bitfinex](https://docs.ccxt.com/docs/exchanges/bitfinex#setmargin)
- [bitrue](https://docs.ccxt.com/docs/exchanges/bitrue#setmargin)
- [coinbaseinternational](https://docs.ccxt.com/docs/exchanges/coinbaseinternational#setmargin)
- [lighter](https://docs.ccxt.com/docs/exchanges/lighter#setmargin)
- [phemex](https://docs.ccxt.com/docs/exchanges/phemex#setmargin)

* * *

## [setMarginMode](https://docs.ccxt.com/docs/base-spec\#setmarginmode)

set margin mode to 'cross' or 'isolated'

**Kind**: instance

**Returns**: `object` \- response from the exchange

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| marginMode | `string` | Yes | 'cross' or 'isolated' |
| symbol | `string` | Yes | unified market symbol |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-215)

- [aster](https://docs.ccxt.com/docs/exchanges/aster#setmarginmode)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#setmarginmode)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#setmarginmode)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#setmarginmode)
- [blofin](https://docs.ccxt.com/docs/exchanges/blofin#setmarginmode)
- [btse](https://docs.ccxt.com/docs/exchanges/btse#setmarginmode)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#setmarginmode)
- [bydfi](https://docs.ccxt.com/docs/exchanges/bydfi#setmarginmode)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#setmarginmode)
- [delta](https://docs.ccxt.com/docs/exchanges/delta#setmarginmode)
- [digifinex](https://docs.ccxt.com/docs/exchanges/digifinex#setmarginmode)
- [hashkey](https://docs.ccxt.com/docs/exchanges/hashkey#setmarginmode)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#setmarginmode)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#setmarginmode)
- [lighter](https://docs.ccxt.com/docs/exchanges/lighter#setmarginmode)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#setmarginmode)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#setmarginmode)
- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#setmarginmode)
- [paradex](https://docs.ccxt.com/docs/exchanges/paradex#setmarginmode)
- [phemex](https://docs.ccxt.com/docs/exchanges/phemex#setmarginmode)
- [toobit](https://docs.ccxt.com/docs/exchanges/toobit#setmarginmode)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#setmarginmode)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#setmarginmode)
- [xt](https://docs.ccxt.com/docs/exchanges/xt#setmarginmode)

* * *

## [setPositionMode](https://docs.ccxt.com/docs/base-spec\#setpositionmode)

set hedged to true or false for a market

**Kind**: instance

**Returns**: `object` \- response from the exchange

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| hedged | `bool` | Yes | set to true to use dualSidePosition |
| symbol | `string` | Yes | not used by setPositionMode () |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-216)

- [aster](https://docs.ccxt.com/docs/exchanges/aster#setpositionmode)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#setpositionmode)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#setpositionmode)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#setpositionmode)
- [blofin](https://docs.ccxt.com/docs/exchanges/blofin#setpositionmode)
- [btse](https://docs.ccxt.com/docs/exchanges/btse#setpositionmode)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#setpositionmode)
- [bydfi](https://docs.ccxt.com/docs/exchanges/bydfi#setpositionmode)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#setpositionmode)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#setpositionmode)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#setpositionmode)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#setpositionmode)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#setpositionmode)
- [phemex](https://docs.ccxt.com/docs/exchanges/phemex#setpositionmode)
- [poloniex](https://docs.ccxt.com/docs/exchanges/poloniex#setpositionmode)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#setpositionmode)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#setpositionmode)

* * *

## [setSandboxMode](https://docs.ccxt.com/docs/base-spec\#setsandboxmode)

enables or disables demo trading mode, if enabled will send PAPTRADING=1 in headers

**Kind**: instance

| Param |
| --- |
| enabled |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-217)

- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#setsandboxmode)

* * *

## [setUserAbstraction](https://docs.ccxt.com/docs/base-spec\#setuserabstraction)

set user abstraction mode

**Kind**: instance

**Returns**: dictionary response from the exchange

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| abstraction | `string` | Yes | one of the strings \["disabled", "unifiedAccount", "portfolioMargin"\], |
| params | `object` | No |  |
| params.type | `string` | No | 'userSetAbstraction' or 'agentSetAbstraction' default is 'userSetAbstraction' |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-218)

- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#setuserabstraction)

* * *

## [signIn](https://docs.ccxt.com/docs/base-spec\#signin)

sign in, must be called prior to using other authenticated methods

**Kind**: instance

**Returns**: response from exchange

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-219)

- [aster](https://docs.ccxt.com/docs/exchanges/aster#signin)
- [bullish](https://docs.ccxt.com/docs/exchanges/bullish#signin)
- [grvt](https://docs.ccxt.com/docs/exchanges/grvt#signin)
- [ndax](https://docs.ccxt.com/docs/exchanges/ndax#signin)

* * *

## [transfer](https://docs.ccxt.com/docs/base-spec\#transfer)

transfer currency internally between wallets on the same account

**Kind**: instance

**Returns**: `object` \- a [transfer structure](https://docs.ccxt.com/docs/manual#transfer-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| code | `string` | Yes | unified currency code |
| amount | `float` | Yes | amount to transfer |
| fromAccount | `string` | Yes | account to transfer from |
| toAccount | `string` | Yes | account to transfer to |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.transferId | `string` | No | UUID, which is unique across the platform |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-220)

- [apex](https://docs.ccxt.com/docs/exchanges/apex#transfer)
- [aster](https://docs.ccxt.com/docs/exchanges/aster#transfer)
- [bigone](https://docs.ccxt.com/docs/exchanges/bigone#transfer)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#transfer)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#transfer)
- [bitfinex](https://docs.ccxt.com/docs/exchanges/bitfinex#transfer)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#transfer)
- [bitrue](https://docs.ccxt.com/docs/exchanges/bitrue#transfer)
- [bitstamp](https://docs.ccxt.com/docs/exchanges/bitstamp#transfer)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#transfer)
- [blofin](https://docs.ccxt.com/docs/exchanges/blofin#transfer)
- [bullish](https://docs.ccxt.com/docs/exchanges/bullish#transfer)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#transfer)
- [budfi](https://docs.ccxt.com/docs/exchanges/budfi#transfer)
- [cex](https://docs.ccxt.com/docs/exchanges/cex#transfer)
- [coinbase](https://docs.ccxt.com/docs/exchanges/coinbase#transfer)
- [coinbaseinternational](https://docs.ccxt.com/docs/exchanges/coinbaseinternational#transfer)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#transfer)
- [deepcoin](https://docs.ccxt.com/docs/exchanges/deepcoin#transfer)
- [deribit](https://docs.ccxt.com/docs/exchanges/deribit#transfer)
- [digifinex](https://docs.ccxt.com/docs/exchanges/digifinex#transfer)
- [dydx](https://docs.ccxt.com/docs/exchanges/dydx#transfer)
- [extended](https://docs.ccxt.com/docs/exchanges/extended#transfer)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#transfer)
- [grvt](https://docs.ccxt.com/docs/exchanges/grvt#transfer)
- [hashkey](https://docs.ccxt.com/docs/exchanges/hashkey#transfer)
- [hitbtc](https://docs.ccxt.com/docs/exchanges/hitbtc#transfer)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#transfer)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#transfer)
- [kraken](https://docs.ccxt.com/docs/exchanges/kraken#transfer)
- [krakenfutures](https://docs.ccxt.com/docs/exchanges/krakenfutures#transfer)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#transfer)
- [kucoinfutures](https://docs.ccxt.com/docs/exchanges/kucoinfutures#transfer)
- [latoken](https://docs.ccxt.com/docs/exchanges/latoken#transfer)
- [lighter](https://docs.ccxt.com/docs/exchanges/lighter#transfer)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#transfer)
- [mudrex](https://docs.ccxt.com/docs/exchanges/mudrex#transfer)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#transfer)
- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#transfer)
- [paymium](https://docs.ccxt.com/docs/exchanges/paymium#transfer)
- [phemex](https://docs.ccxt.com/docs/exchanges/phemex#transfer)
- [poloniex](https://docs.ccxt.com/docs/exchanges/poloniex#transfer)
- [toobit](https://docs.ccxt.com/docs/exchanges/toobit#transfer)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#transfer)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#transfer)
- [xt](https://docs.ccxt.com/docs/exchanges/xt#transfer)

* * *

## [transferClassic](https://docs.ccxt.com/docs/base-spec\#transferclassic)

transfer currency internally between wallets on the same account with classic endpoints

**Kind**: instance

**Returns**: `object` \- a [transfer structure](https://docs.ccxt.com/docs/manual#transfer-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| code | `string` | Yes | unified currency code |
| amount | `float` | Yes | amount to transfer |
| fromAccount | `string` | Yes | account to transfer from |
| toAccount | `string` | Yes | account to transfer to |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.transferType | `string` | No | INTERNAL, PARENT\_TO\_SUB, SUB\_TO\_PARENT (default is INTERNAL) |
| params.fromUserId | `string` | No | required if transferType is SUB\_TO\_PARENT |
| params.toUserId | `string` | No | required if transferType is PARENT\_TO\_SUB |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-221)

- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#transferclassic)

* * *

## [transferOut](https://docs.ccxt.com/docs/base-spec\#transferout)

transfer from spot wallet to futures wallet

**Kind**: instance

**Returns**: a [transfer structure](https://docs.ccxt.com/docs/manual#transfer-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| code | `str` | Yes | Unified currency code |
| amount | `float` | Yes | Size of the transfer |
| params | `dict` | No | Exchange specific parameters |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-222)

- [kraken](https://docs.ccxt.com/docs/exchanges/kraken#transferout)
- [krakenfutures](https://docs.ccxt.com/docs/exchanges/krakenfutures#transferout)

* * *

## [transferUta](https://docs.ccxt.com/docs/base-spec\#transferuta)

transfer currency internally between wallets on the same account with uta endpoint

**Kind**: instance

**Returns**: `object` \- a [transfer structure](https://docs.ccxt.com/docs/manual#transfer-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| code | `string` | Yes | unified currency code |
| amount | `float` | Yes | amount to transfer |
| fromAccount | `string` | Yes | account to transfer from |
| toAccount | `string` | Yes | account to transfer to |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.transferType | `string` | No | INTERNAL, PARENT\_TO\_SUB, SUB\_TO\_PARENT, SUB\_TO\_SUB (default is INTERNAL) |
| params.fromUserId | `string` | No | required if transferType is SUB\_TO\_PARENT or SUB\_TO\_SUB |
| params.toUserId | `string` | No | required if transferType is PARENT\_TO\_SUB or SUB\_TO\_SUB |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-223)

- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#transferuta)

* * *

## [unWatchBalance](https://docs.ccxt.com/docs/base-spec\#unwatchbalance)

unWatches balance

**Kind**: instance

**Returns**: `object` \- status of the unwatch request

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-224)

- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#unwatchbalance)

* * *

## [unWatchBidsAsks](https://docs.ccxt.com/docs/base-spec\#unwatchbidsasks)

unWatches best bid & ask for symbols

**Kind**: instance

**Returns**: `object` \- a [ticker structure](https://docs.ccxt.com/docs/manual#ticker-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>` | Yes | unified symbol of the market to fetch the ticker for |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-225)

- [aster](https://docs.ccxt.com/docs/exchanges/aster#unwatchbidsasks)
- [backpack](https://docs.ccxt.com/docs/exchanges/backpack#unwatchbidsasks)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#unwatchbidsasks)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#unwatchbidsasks)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#unwatchbidsasks)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#unwatchbidsasks)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#unwatchbidsasks)

* * *

## [unWatchFundingRate](https://docs.ccxt.com/docs/base-spec\#unwatchfundingrate)

unWatches the current funding rate for a symbol

**Kind**: instance

**Returns**: `object` \- a [funding rate structure](https://docs.ccxt.com/docs/manual#funding-rate-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-226)

- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#unwatchfundingrate)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#unwatchfundingrate)

* * *

## [unWatchMarkPrice](https://docs.ccxt.com/docs/base-spec\#unwatchmarkprice)

unWatches a mark price for a specific market

**Kind**: instance

**Returns**: `object` \- a [ticker structure](https://docs.ccxt.com/docs/manual#ticker-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to fetch the ticker for |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.use1sFreq | `boolean` | No | _default is true_ if set to true, the mark price will be updated every second, otherwise every 3 seconds |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-227)

- [aster](https://docs.ccxt.com/docs/exchanges/aster#unwatchmarkprice)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#unwatchmarkprice)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#unwatchmarkprice)
- [lighter](https://docs.ccxt.com/docs/exchanges/lighter#unwatchmarkprice)

* * *

## [unWatchMarkPrices](https://docs.ccxt.com/docs/base-spec\#unwatchmarkprices)

watches the mark price for all markets

**Kind**: instance

**Returns**: `object` \- a [ticker structure](https://docs.ccxt.com/docs/manual#ticker-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>` | Yes | unified symbol of the market to fetch the ticker for |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.use1sFreq | `boolean` | No | _default is true_ if set to true, the mark price will be updated every second, otherwise every 3 seconds |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-228)

- [aster](https://docs.ccxt.com/docs/exchanges/aster#unwatchmarkprices)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#unwatchmarkprices)
- [lighter](https://docs.ccxt.com/docs/exchanges/lighter#unwatchmarkprices)

* * *

## [unWatchMyTrades](https://docs.ccxt.com/docs/base-spec\#unwatchmytrades)

unWatches information on multiple trades made by the user

**Kind**: instance

**Returns**: `Array<object>` \- a list of [order structures](https://docs.ccxt.com/docs/manual#order-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol of the market orders were made in |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.unifiedMargin | `boolean` | No | use unified margin account |
| params.executionFast | `boolean` | No | use fast execution |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-229)

- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#unwatchmytrades)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#unwatchmytrades)
- [lighter](https://docs.ccxt.com/docs/exchanges/lighter#unwatchmytrades)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#unwatchmytrades)
- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#unwatchmytrades)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#unwatchmytrades)

* * *

## [unWatchOHLCV](https://docs.ccxt.com/docs/base-spec\#unwatchohlcv)

unWatches historical candlestick data containing the open, high, low, and close price, and the volume of a market

**Kind**: instance

**Returns**: `Array<Array<int>>` \- A list of candles ordered as timestamp, open, high, low, close, volume

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to fetch OHLCV data for |
| timeframe | `string` | Yes | the length of time each candle represents |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-230)

- [aster](https://docs.ccxt.com/docs/exchanges/aster#unwatchohlcv)
- [backpack](https://docs.ccxt.com/docs/exchanges/backpack#unwatchohlcv)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#unwatchohlcv)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#unwatchohlcv)
- [bitfinex](https://docs.ccxt.com/docs/exchanges/bitfinex#unwatchohlcv)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#unwatchohlcv)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#unwatchohlcv)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#unwatchohlcv)
- [bydfi](https://docs.ccxt.com/docs/exchanges/bydfi#unwatchohlcv)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#unwatchohlcv)
- [deepcoin](https://docs.ccxt.com/docs/exchanges/deepcoin#unwatchohlcv)
- [dydx](https://docs.ccxt.com/docs/exchanges/dydx#unwatchohlcv)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#unwatchohlcv)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#unwatchohlcv)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#unwatchohlcv)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#unwatchohlcv)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#unwatchohlcv)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#unwatchohlcv)
- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#unwatchohlcv)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#unwatchohlcv)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#unwatchohlcv)

* * *

## [unWatchOHLCVForSymbols](https://docs.ccxt.com/docs/base-spec\#unwatchohlcvforsymbols)

unWatches historical candlestick data containing the open, high, low, and close price, and the volume of a market

**Kind**: instance

**Returns**: `Array<Array<int>>` \- A list of candles ordered as timestamp, open, high, low, close, volume

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbolsAndTimeframes | `Array<Array<string>>` | Yes | array of arrays containing unified symbols and timeframes to fetch OHLCV data for, example \[\['BTC/USDT', '1m'\], \['LTC/USDT', '5m'\]\] |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-231)

- [aster](https://docs.ccxt.com/docs/exchanges/aster#unwatchohlcvforsymbols)
- [backpack](https://docs.ccxt.com/docs/exchanges/backpack#unwatchohlcvforsymbols)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#unwatchohlcvforsymbols)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#unwatchohlcvforsymbols)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#unwatchohlcvforsymbols)
- [bydfi](https://docs.ccxt.com/docs/exchanges/bydfi#unwatchohlcvforsymbols)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#unwatchohlcvforsymbols)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#unwatchohlcvforsymbols)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#unwatchohlcvforsymbols)

* * *

## [unWatchOrderBook](https://docs.ccxt.com/docs/base-spec\#unwatchorderbook)

unsubscribe from the orderbook channel

**Kind**: instance

**Returns**: `object` \- A dictionary of [order book structures](https://docs.ccxt.com/docs/manual#order-book-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | symbol of the market to unwatch the trades for |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.limit | `int` | No | orderbook limit, default is undefined |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-232)

- [aster](https://docs.ccxt.com/docs/exchanges/aster#unwatchorderbook)
- [backpack](https://docs.ccxt.com/docs/exchanges/backpack#unwatchorderbook)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#unwatchorderbook)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#unwatchorderbook)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#unwatchorderbook)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#unwatchorderbook)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#unwatchorderbook)
- [bydfi](https://docs.ccxt.com/docs/exchanges/bydfi#unwatchorderbook)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#unwatchorderbook)
- [deepcoin](https://docs.ccxt.com/docs/exchanges/deepcoin#unwatchorderbook)
- [derive](https://docs.ccxt.com/docs/exchanges/derive#unwatchorderbook)
- [dydx](https://docs.ccxt.com/docs/exchanges/dydx#unwatchorderbook)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#unwatchorderbook)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#unwatchorderbook)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#unwatchorderbook)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#unwatchorderbook)
- [lighter](https://docs.ccxt.com/docs/exchanges/lighter#unwatchorderbook)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#unwatchorderbook)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#unwatchorderbook)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#unwatchorderbook)
- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#unwatchorderbook)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#unwatchorderbook)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#unwatchorderbook)

* * *

## [unWatchOrderBookForSymbols](https://docs.ccxt.com/docs/base-spec\#unwatchorderbookforsymbols)

unsubscribe from the orderbook channel

**Kind**: instance

**Returns**: `object` \- A dictionary of [order book structures](https://docs.ccxt.com/docs/manual#order-book-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>` | Yes | unified symbol of the market to unwatch the trades for |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.limit | `int` | No | orderbook limit, default is undefined |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-233)

- [aster](https://docs.ccxt.com/docs/exchanges/aster#unwatchorderbookforsymbols)
- [backpack](https://docs.ccxt.com/docs/exchanges/backpack#unwatchorderbookforsymbols)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#unwatchorderbookforsymbols)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#unwatchorderbookforsymbols)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#unwatchorderbookforsymbols)
- [bydfi](https://docs.ccxt.com/docs/exchanges/bydfi#unwatchorderbookforsymbols)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#unwatchorderbookforsymbols)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#unwatchorderbookforsymbols)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#unwatchorderbookforsymbols)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#unwatchorderbookforsymbols)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#unwatchorderbookforsymbols)

* * *

## [unWatchOrders](https://docs.ccxt.com/docs/base-spec\#unwatchorders)

unWatches information on multiple orders made by the user

**Kind**: instance

**Returns**: `Array<object>` \- a list of [order structures](https://docs.ccxt.com/docs/manual#order-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | No | unified market symbol of the market orders were made in |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-234)

- [backpack](https://docs.ccxt.com/docs/exchanges/backpack#unwatchorders)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#unwatchorders)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#unwatchorders)
- [lighter](https://docs.ccxt.com/docs/exchanges/lighter#unwatchorders)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#unwatchorders)
- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#unwatchorders)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#unwatchorders)

* * *

## [unWatchPositions](https://docs.ccxt.com/docs/base-spec\#unwatchpositions)

unWatches from the stream channel

**Kind**: instance

**Returns**: `Array<object>` \- a list of [position structure](https://docs.ccxt.com/docs/manual#position-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>` | No | list of unified market symbols to watch positions for |
| params | `object` | Yes | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-235)

- [backpack](https://docs.ccxt.com/docs/exchanges/backpack#unwatchpositions)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#unwatchpositions)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#unwatchpositions)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#unwatchpositions)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#unwatchpositions)

* * *

## [unWatchTicker](https://docs.ccxt.com/docs/base-spec\#unwatchticker)

unWatches a price ticker

**Kind**: instance

**Returns**: `object` \- a [ticker structure](https://docs.ccxt.com/docs/manual#ticker-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to fetch the ticker for |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-236)

- [aster](https://docs.ccxt.com/docs/exchanges/aster#unwatchticker)
- [backpack](https://docs.ccxt.com/docs/exchanges/backpack#unwatchticker)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#unwatchticker)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#unwatchticker)
- [bitfinex](https://docs.ccxt.com/docs/exchanges/bitfinex#unwatchticker)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#unwatchticker)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#unwatchticker)
- [bydfi](https://docs.ccxt.com/docs/exchanges/bydfi#unwatchticker)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#unwatchticker)
- [deepcoin](https://docs.ccxt.com/docs/exchanges/deepcoin#unwatchticker)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#unwatchticker)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#unwatchticker)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#unwatchticker)
- [lighter](https://docs.ccxt.com/docs/exchanges/lighter#unwatchticker)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#unwatchticker)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#unwatchticker)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#unwatchticker)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#unwatchticker)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#unwatchticker)

* * *

## [unWatchTickers](https://docs.ccxt.com/docs/base-spec\#unwatchtickers)

unWatches a price ticker, a statistical calculation with the information calculated over the past 24 hours for all markets of a specific list

**Kind**: instance

**Returns**: `object` \- a [ticker structure](https://docs.ccxt.com/docs/manual#ticker-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>` | Yes | unified symbol of the market to fetch the ticker for |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-237)

- [aster](https://docs.ccxt.com/docs/exchanges/aster#unwatchtickers)
- [backpack](https://docs.ccxt.com/docs/exchanges/backpack#unwatchtickers)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#unwatchtickers)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#unwatchtickers)
- [bydfi](https://docs.ccxt.com/docs/exchanges/bydfi#unwatchtickers)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#unwatchtickers)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#unwatchtickers)
- [lighter](https://docs.ccxt.com/docs/exchanges/lighter#unwatchtickers)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#unwatchtickers)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#unwatchtickers)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#unwatchtickers)
- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#unwatchtickers)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#unwatchtickers)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#unwatchtickers)

* * *

## [unWatchTrades](https://docs.ccxt.com/docs/base-spec\#unwatchtrades)

unsubscribe from the trades channel

**Kind**: instance

**Returns**: `Array<object>` \- a list of [trade structures](https://docs.ccxt.com/docs/manual#trade-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol of the market trades were made in |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-238)

- [aster](https://docs.ccxt.com/docs/exchanges/aster#unwatchtrades)
- [backpack](https://docs.ccxt.com/docs/exchanges/backpack#unwatchtrades)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#unwatchtrades)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#unwatchtrades)
- [bitfinex](https://docs.ccxt.com/docs/exchanges/bitfinex#unwatchtrades)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#unwatchtrades)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#unwatchtrades)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#unwatchtrades)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#unwatchtrades)
- [deepcoin](https://docs.ccxt.com/docs/exchanges/deepcoin#unwatchtrades)
- [derive](https://docs.ccxt.com/docs/exchanges/derive#unwatchtrades)
- [dydx](https://docs.ccxt.com/docs/exchanges/dydx#unwatchtrades)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#unwatchtrades)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#unwatchtrades)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#unwatchtrades)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#unwatchtrades)
- [lighter](https://docs.ccxt.com/docs/exchanges/lighter#unwatchtrades)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#unwatchtrades)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#unwatchtrades)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#unwatchtrades)
- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#unwatchtrades)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#unwatchtrades)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#unwatchtrades)

* * *

## [unWatchTradesForSymbols](https://docs.ccxt.com/docs/base-spec\#unwatchtradesforsymbols)

unsubscribe from the trades channel

**Kind**: instance

**Returns**: `Array<object>` \- a list of [trade structures](https://docs.ccxt.com/docs/manual#public-trades)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>` | Yes | unified symbol of the market to fetch trades for |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-239)

- [aster](https://docs.ccxt.com/docs/exchanges/aster#unwatchtradesforsymbols)
- [backpack](https://docs.ccxt.com/docs/exchanges/backpack#unwatchtradesforsymbols)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#unwatchtradesforsymbols)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#unwatchtradesforsymbols)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#unwatchtradesforsymbols)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#unwatchtradesforsymbols)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#unwatchtradesforsymbols)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#unwatchtradesforsymbols)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#unwatchtradesforsymbols)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#unwatchtradesforsymbols)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#unwatchtradesforsymbols)

* * *

## [upgradeUnifiedTradeAccount](https://docs.ccxt.com/docs/base-spec\#upgradeunifiedtradeaccount)

upgrades the account to unified trade account _warning_ this is irreversible

**Kind**: instance

**Returns**: `any` \- nothing

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-240)

- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#upgradeunifiedtradeaccount)

* * *

## [verifyGiftCode](https://docs.ccxt.com/docs/base-spec\#verifygiftcode)

verify gift code

**Kind**: instance

**Returns**: `object` \- response from the exchange

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| id | `string` | Yes | reference number id |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-241)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#verifygiftcode)

* * *

## [watchBalance](https://docs.ccxt.com/docs/base-spec\#watchbalance)

query for balance and get the amount of funds available for trading or funds locked in orders

**Kind**: instance

**Returns**: `object` \- a [balance structure](https://docs.ccxt.com/docs/manual#balance-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.type | `string` | No | 'spot' or 'swap', default is 'spot' |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-242)

- [aster](https://docs.ccxt.com/docs/exchanges/aster#watchbalance)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#watchbalance)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#watchbalance)
- [bitfinex](https://docs.ccxt.com/docs/exchanges/bitfinex#watchbalance)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#watchbalance)
- [bithumb](https://docs.ccxt.com/docs/exchanges/bithumb#watchbalance)
- [bitopro](https://docs.ccxt.com/docs/exchanges/bitopro#watchbalance)
- [bitrue](https://docs.ccxt.com/docs/exchanges/bitrue#watchbalance)
- [blockchaincom](https://docs.ccxt.com/docs/exchanges/blockchaincom#watchbalance)
- [blofin](https://docs.ccxt.com/docs/exchanges/blofin#watchbalance)
- [bullish](https://docs.ccxt.com/docs/exchanges/bullish#watchbalance)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#watchbalance)
- [bydfi](https://docs.ccxt.com/docs/exchanges/bydfi#watchbalance)
- [cex](https://docs.ccxt.com/docs/exchanges/cex#watchbalance)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#watchbalance)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#watchbalance)
- [deribit](https://docs.ccxt.com/docs/exchanges/deribit#watchbalance)
- [extended](https://docs.ccxt.com/docs/exchanges/extended#watchbalance)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#watchbalance)
- [hashkey](https://docs.ccxt.com/docs/exchanges/hashkey#watchbalance)
- [hollaex](https://docs.ccxt.com/docs/exchanges/hollaex#watchbalance)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#watchbalance)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#watchbalance)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#watchbalance)
- [lbank](https://docs.ccxt.com/docs/exchanges/lbank#watchbalance)
- [lighter](https://docs.ccxt.com/docs/exchanges/lighter#watchbalance)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#watchbalance)
- [modetrade](https://docs.ccxt.com/docs/exchanges/modetrade#watchbalance)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#watchbalance)
- [onetrading](https://docs.ccxt.com/docs/exchanges/onetrading#watchbalance)
- [phemex](https://docs.ccxt.com/docs/exchanges/phemex#watchbalance)
- [toobit](https://docs.ccxt.com/docs/exchanges/toobit#watchbalance)
- [upbit](https://docs.ccxt.com/docs/exchanges/upbit#watchbalance)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#watchbalance)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#watchbalance)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#watchbalance)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#watchbalance)

* * *

## [watchBidsAsks](https://docs.ccxt.com/docs/base-spec\#watchbidsasks)

watches best bid & ask for symbols

**Kind**: instance

**Returns**: `object` \- a [ticker structure](https://docs.ccxt.com/docs/manual#ticker-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>` | Yes | unified symbol of the market to fetch the ticker for |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-243)

- [aster](https://docs.ccxt.com/docs/exchanges/aster#watchbidsasks)
- [backpack](https://docs.ccxt.com/docs/exchanges/backpack#watchbidsasks)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#watchbidsasks)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#watchbidsasks)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#watchbidsasks)
- [blofin](https://docs.ccxt.com/docs/exchanges/blofin#watchbidsasks)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#watchbidsasks)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#watchbidsasks)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#watchbidsasks)
- [deribit](https://docs.ccxt.com/docs/exchanges/deribit#watchbidsasks)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#watchbidsasks)
- [gemini](https://docs.ccxt.com/docs/exchanges/gemini#watchbidsasks)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#watchbidsasks)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#watchbidsasks)
- [modetrade](https://docs.ccxt.com/docs/exchanges/modetrade#watchbidsasks)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#watchbidsasks)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#watchbidsasks)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#watchbidsasks)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#watchbidsasks)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#watchbidsasks)

* * *

## [watchFundingRate](https://docs.ccxt.com/docs/base-spec\#watchfundingrate)

watch the current funding rate

**Kind**: instance

**Returns**: `object` \- a [funding rate structure](https://docs.ccxt.com/docs/manual#funding-rate-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-244)

- [blofin](https://docs.ccxt.com/docs/exchanges/blofin#watchfundingrate)
- [extended](https://docs.ccxt.com/docs/exchanges/extended#watchfundingrate)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#watchfundingrate)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#watchfundingrate)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#watchfundingrate)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#watchfundingrate)

* * *

## [watchFundingRates](https://docs.ccxt.com/docs/base-spec\#watchfundingrates)

watch the funding rate for multiple markets

**Kind**: instance

**Returns**: `object` \- a dictionary of [funding rates structures](https://docs.ccxt.com/docs/manual#funding-rate-structure), indexed by market symbols

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>` | Yes | a list of unified market symbols |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-245)

- [okx](https://docs.ccxt.com/docs/exchanges/okx#watchfundingrates)

* * *

## [watchLiquidations](https://docs.ccxt.com/docs/base-spec\#watchliquidations)

watch the public liquidations of a trading pair

**Kind**: instance

**Returns**: `object` \- an array of [liquidation structures](https://docs.ccxt.com/docs/manual#liquidation-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified CCXT market symbol |
| since | `int` | No | the earliest time in ms to fetch liquidations for |
| limit | `int` | No | the maximum number of liquidation structures to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-246)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#watchliquidations)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#watchliquidations)
- [lighter](https://docs.ccxt.com/docs/exchanges/lighter#watchliquidations)

* * *

## [watchLiquidationsForSymbols](https://docs.ccxt.com/docs/base-spec\#watchliquidationsforsymbols)

watch the public liquidations of a trading pair

**Kind**: instance

**Returns**: `object` \- an array of [liquidation structures](https://docs.ccxt.com/docs/manual#liquidation-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>` | Yes | list of unified market symbols |
| since | `int` | No | the earliest time in ms to fetch liquidations for |
| limit | `int` | No | the maximum number of liquidation structures to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-247)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#watchliquidationsforsymbols)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#watchliquidationsforsymbols)

* * *

## [watchMarkPrice](https://docs.ccxt.com/docs/base-spec\#watchmarkprice)

watches a mark price for a specific market

**Kind**: instance

**Returns**: `object` \- a [ticker structure](https://docs.ccxt.com/docs/manual#ticker-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to fetch the ticker for |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.use1sFreq | `boolean` | No | _default is true_ if set to true, the mark price will be updated every second, otherwise every 3 seconds |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-248)

- [aster](https://docs.ccxt.com/docs/exchanges/aster#watchmarkprice)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#watchmarkprice)
- [extended](https://docs.ccxt.com/docs/exchanges/extended#watchmarkprice)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#watchmarkprice)
- [lighter](https://docs.ccxt.com/docs/exchanges/lighter#watchmarkprice)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#watchmarkprice)

* * *

## [watchMarkPrices](https://docs.ccxt.com/docs/base-spec\#watchmarkprices)

watches the mark price for all markets

**Kind**: instance

**Returns**: `object` \- a [ticker structure](https://docs.ccxt.com/docs/manual#ticker-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>` | Yes | unified symbol of the market to fetch the ticker for |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.use1sFreq | `boolean` | No | _default is true_ if set to true, the mark price will be updated every second, otherwise every 3 seconds |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-249)

- [aster](https://docs.ccxt.com/docs/exchanges/aster#watchmarkprices)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#watchmarkprices)
- [lighter](https://docs.ccxt.com/docs/exchanges/lighter#watchmarkprices)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#watchmarkprices)

* * *

## [watchMyLiquidations](https://docs.ccxt.com/docs/base-spec\#watchmyliquidations)

watch the private liquidations of a trading pair

**Kind**: instance

**Returns**: `object` \- an array of [liquidation structures](https://docs.ccxt.com/docs/manual#liquidation-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified CCXT market symbol |
| since | `int` | No | the earliest time in ms to fetch liquidations for |
| limit | `int` | No | the maximum number of liquidation structures to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-250)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#watchmyliquidations)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#watchmyliquidations)

* * *

## [watchMyLiquidationsForSymbols](https://docs.ccxt.com/docs/base-spec\#watchmyliquidationsforsymbols)

watch the private liquidations of a trading pair

**Kind**: instance

**Returns**: `object` \- an array of [liquidation structures](https://docs.ccxt.com/docs/manual#liquidation-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>` | Yes | list of unified market symbols |
| since | `int` | No | the earliest time in ms to fetch liquidations for |
| limit | `int` | No | the maximum number of liquidation structures to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-251)

- [binance](https://docs.ccxt.com/docs/exchanges/binance#watchmyliquidationsforsymbols)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#watchmyliquidationsforsymbols)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#watchmyliquidationsforsymbols)

* * *

## [watchMyTrades](https://docs.ccxt.com/docs/base-spec\#watchmytrades)

watches information on multiple trades made by the user

**Kind**: instance

**Returns**: `Array<object>` \- a list of [trade structures](https://docs.ccxt.com/docs/manual#trade-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol of the market trades were made in |
| since | `int` | No | the earliest time in ms to fetch trades for |
| limit | `int` | No | the maximum number of trade structures to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.unifiedMargin | `boolean` | No | use unified margin account |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-252)

- [alpaca](https://docs.ccxt.com/docs/exchanges/alpaca#watchmytrades)
- [apex](https://docs.ccxt.com/docs/exchanges/apex#watchmytrades)
- [aster](https://docs.ccxt.com/docs/exchanges/aster#watchmytrades)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#watchmytrades)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#watchmytrades)
- [bitfinex](https://docs.ccxt.com/docs/exchanges/bitfinex#watchmytrades)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#watchmytrades)
- [bitopro](https://docs.ccxt.com/docs/exchanges/bitopro#watchmytrades)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#watchmytrades)
- [bullish](https://docs.ccxt.com/docs/exchanges/bullish#watchmytrades)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#watchmytrades)
- [cex](https://docs.ccxt.com/docs/exchanges/cex#watchmytrades)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#watchmytrades)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#watchmytrades)
- [deepcoin](https://docs.ccxt.com/docs/exchanges/deepcoin#watchmytrades)
- [deribit](https://docs.ccxt.com/docs/exchanges/deribit#watchmytrades)
- [derive](https://docs.ccxt.com/docs/exchanges/derive#watchmytrades)
- [extended](https://docs.ccxt.com/docs/exchanges/extended#watchmytrades)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#watchmytrades)
- [grvt](https://docs.ccxt.com/docs/exchanges/grvt#watchmytrades)
- [hashkey](https://docs.ccxt.com/docs/exchanges/hashkey#watchmytrades)
- [hollaex](https://docs.ccxt.com/docs/exchanges/hollaex#watchmytrades)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#watchmytrades)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#watchmytrades)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#watchmytrades)
- [lighter](https://docs.ccxt.com/docs/exchanges/lighter#watchmytrades)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#watchmytrades)
- [modetrade](https://docs.ccxt.com/docs/exchanges/modetrade#watchmytrades)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#watchmytrades)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#watchmytrades)
- [onetrading](https://docs.ccxt.com/docs/exchanges/onetrading#watchmytrades)
- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#watchmytrades)
- [phemex](https://docs.ccxt.com/docs/exchanges/phemex#watchmytrades)
- [toobit](https://docs.ccxt.com/docs/exchanges/toobit#watchmytrades)
- [upbit](https://docs.ccxt.com/docs/exchanges/upbit#watchmytrades)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#watchmytrades)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#watchmytrades)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#watchmytrades)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#watchmytrades)

* * *

## [watchOHLCV](https://docs.ccxt.com/docs/base-spec\#watchohlcv)

watches historical candlestick data containing the open, high, low, and close price, and the volume of a market

**Kind**: instance

**Returns**: `Array<Array<int>>` \- A list of candles ordered as timestamp, open, high, low, close, volume

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to fetch OHLCV data for |
| timeframe | `string` | Yes | the length of time each candle represents |
| since | `int` | No | timestamp in ms of the earliest candle to fetch |
| limit | `int` | No | the maximum amount of candles to fetch |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-253)

- [alpaca](https://docs.ccxt.com/docs/exchanges/alpaca#watchohlcv)
- [apex](https://docs.ccxt.com/docs/exchanges/apex#watchohlcv)
- [aster](https://docs.ccxt.com/docs/exchanges/aster#watchohlcv)
- [backpack](https://docs.ccxt.com/docs/exchanges/backpack#watchohlcv)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#watchohlcv)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#watchohlcv)
- [bitfinex](https://docs.ccxt.com/docs/exchanges/bitfinex#watchohlcv)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#watchohlcv)
- [bitrue](https://docs.ccxt.com/docs/exchanges/bitrue#watchohlcv)
- [bittrade](https://docs.ccxt.com/docs/exchanges/bittrade#watchohlcv)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#watchohlcv)
- [blockchaincom](https://docs.ccxt.com/docs/exchanges/blockchaincom#watchohlcv)
- [blofin](https://docs.ccxt.com/docs/exchanges/blofin#watchohlcv)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#watchohlcv)
- [bydfi](https://docs.ccxt.com/docs/exchanges/bydfi#watchohlcv)
- [cex](https://docs.ccxt.com/docs/exchanges/cex#watchohlcv)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#watchohlcv)
- [deepcoin](https://docs.ccxt.com/docs/exchanges/deepcoin#watchohlcv)
- [deribit](https://docs.ccxt.com/docs/exchanges/deribit#watchohlcv)
- [dydx](https://docs.ccxt.com/docs/exchanges/dydx#watchohlcv)
- [extended](https://docs.ccxt.com/docs/exchanges/extended#watchohlcv)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#watchohlcv)
- [gemini](https://docs.ccxt.com/docs/exchanges/gemini#watchohlcv)
- [grvt](https://docs.ccxt.com/docs/exchanges/grvt#watchohlcv)
- [hashkey](https://docs.ccxt.com/docs/exchanges/hashkey#watchohlcv)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#watchohlcv)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#watchohlcv)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#watchohlcv)
- [lbank](https://docs.ccxt.com/docs/exchanges/lbank#watchohlcv)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#watchohlcv)
- [modetrade](https://docs.ccxt.com/docs/exchanges/modetrade#watchohlcv)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#watchohlcv)
- [ndax](https://docs.ccxt.com/docs/exchanges/ndax#watchohlcv)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#watchohlcv)
- [onetrading](https://docs.ccxt.com/docs/exchanges/onetrading#watchohlcv)
- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#watchohlcv)
- [phemex](https://docs.ccxt.com/docs/exchanges/phemex#watchohlcv)
- [toobit](https://docs.ccxt.com/docs/exchanges/toobit#watchohlcv)
- [upbit](https://docs.ccxt.com/docs/exchanges/upbit#watchohlcv)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#watchohlcv)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#watchohlcv)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#watchohlcv)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#watchohlcv)

* * *

## [watchOHLCVForSymbols](https://docs.ccxt.com/docs/base-spec\#watchohlcvforsymbols)

watches historical candlestick data containing the open, high, low, and close price, and the volume of a market

**Kind**: instance

**Returns**: `object` \- A list of candles ordered as timestamp, open, high, low, close, volume

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbolsAndTimeframes | `Array<Array<string>>` | Yes | array of arrays containing unified symbols and timeframes to fetch OHLCV data for, example \[\['BTC/USDT', '1m'\], \['LTC/USDT', '5m'\]\] |
| since | `int` | No | timestamp in ms of the earliest candle to fetch |
| limit | `int` | No | the maximum amount of candles to fetch |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-254)

- [apex](https://docs.ccxt.com/docs/exchanges/apex#watchohlcvforsymbols)
- [aster](https://docs.ccxt.com/docs/exchanges/aster#watchohlcvforsymbols)
- [backpack](https://docs.ccxt.com/docs/exchanges/backpack#watchohlcvforsymbols)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#watchohlcvforsymbols)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#watchohlcvforsymbols)
- [blofin](https://docs.ccxt.com/docs/exchanges/blofin#watchohlcvforsymbols)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#watchohlcvforsymbols)
- [bydfi](https://docs.ccxt.com/docs/exchanges/bydfi#watchohlcvforsymbols)
- [deribit](https://docs.ccxt.com/docs/exchanges/deribit#watchohlcvforsymbols)
- [grvt](https://docs.ccxt.com/docs/exchanges/grvt#watchohlcvforsymbols)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#watchohlcvforsymbols)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#watchohlcvforsymbols)
- [toobit](https://docs.ccxt.com/docs/exchanges/toobit#watchohlcvforsymbols)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#watchohlcvforsymbols)

* * *

## [watchOrderBook](https://docs.ccxt.com/docs/base-spec\#watchorderbook)

watches information on open orders with bid (buy) and ask (sell) prices, volumes and other data

**Kind**: instance

**Returns**: `object` \- an [order book structure](https://docs.ccxt.com/docs/manual#order-book-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to fetch the order book for |
| limit | `int` | No | the maximum amount of order book entries to return. |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-255)

- [alpaca](https://docs.ccxt.com/docs/exchanges/alpaca#watchorderbook)
- [apex](https://docs.ccxt.com/docs/exchanges/apex#watchorderbook)
- [aster](https://docs.ccxt.com/docs/exchanges/aster#watchorderbook)
- [backpack](https://docs.ccxt.com/docs/exchanges/backpack#watchorderbook)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#watchorderbook)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#watchorderbook)
- [bitfinex](https://docs.ccxt.com/docs/exchanges/bitfinex#watchorderbook)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#watchorderbook)
- [bithumb](https://docs.ccxt.com/docs/exchanges/bithumb#watchorderbook)
- [bitopro](https://docs.ccxt.com/docs/exchanges/bitopro#watchorderbook)
- [bittrade](https://docs.ccxt.com/docs/exchanges/bittrade#watchorderbook)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#watchorderbook)
- [blockchaincom](https://docs.ccxt.com/docs/exchanges/blockchaincom#watchorderbook)
- [blofin](https://docs.ccxt.com/docs/exchanges/blofin#watchorderbook)
- [bullish](https://docs.ccxt.com/docs/exchanges/bullish#watchorderbook)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#watchorderbook)
- [bydfi](https://docs.ccxt.com/docs/exchanges/bydfi#watchorderbook)
- [cex](https://docs.ccxt.com/docs/exchanges/cex#watchorderbook)
- [coincheck](https://docs.ccxt.com/docs/exchanges/coincheck#watchorderbook)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#watchorderbook)
- [coinone](https://docs.ccxt.com/docs/exchanges/coinone#watchorderbook)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#watchorderbook)
- [deepcoin](https://docs.ccxt.com/docs/exchanges/deepcoin#watchorderbook)
- [deribit](https://docs.ccxt.com/docs/exchanges/deribit#watchorderbook)
- [derive](https://docs.ccxt.com/docs/exchanges/derive#watchorderbook)
- [dydx](https://docs.ccxt.com/docs/exchanges/dydx#watchorderbook)
- [extended](https://docs.ccxt.com/docs/exchanges/extended#watchorderbook)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#watchorderbook)
- [gemini](https://docs.ccxt.com/docs/exchanges/gemini#watchorderbook)
- [grvt](https://docs.ccxt.com/docs/exchanges/grvt#watchorderbook)
- [hashkey](https://docs.ccxt.com/docs/exchanges/hashkey#watchorderbook)
- [hollaex](https://docs.ccxt.com/docs/exchanges/hollaex#watchorderbook)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#watchorderbook)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#watchorderbook)
- [independentreserve](https://docs.ccxt.com/docs/exchanges/independentreserve#watchorderbook)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#watchorderbook)
- [lbank](https://docs.ccxt.com/docs/exchanges/lbank#watchorderbook)
- [lighter](https://docs.ccxt.com/docs/exchanges/lighter#watchorderbook)
- [luno](https://docs.ccxt.com/docs/exchanges/luno#watchorderbook)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#watchorderbook)
- [modetrade](https://docs.ccxt.com/docs/exchanges/modetrade#watchorderbook)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#watchorderbook)
- [ndax](https://docs.ccxt.com/docs/exchanges/ndax#watchorderbook)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#watchorderbook)
- [onetrading](https://docs.ccxt.com/docs/exchanges/onetrading#watchorderbook)
- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#watchorderbook)
- [phemex](https://docs.ccxt.com/docs/exchanges/phemex#watchorderbook)
- [toobit](https://docs.ccxt.com/docs/exchanges/toobit#watchorderbook)
- [upbit](https://docs.ccxt.com/docs/exchanges/upbit#watchorderbook)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#watchorderbook)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#watchorderbook)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#watchorderbook)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#watchorderbook)

* * *

## [watchOrderBookForSymbols](https://docs.ccxt.com/docs/base-spec\#watchorderbookforsymbols)

watches information on open orders with bid (buy) and ask (sell) prices, volumes and other data

**Kind**: instance

**Returns**: `object` \- an [order book structure](https://docs.ccxt.com/docs/manual#order-book-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>` | Yes | unified array of symbols |
| limit | `int` | No | the maximum amount of order book entries to return. |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-256)

- [apex](https://docs.ccxt.com/docs/exchanges/apex#watchorderbookforsymbols)
- [aster](https://docs.ccxt.com/docs/exchanges/aster#watchorderbookforsymbols)
- [backpack](https://docs.ccxt.com/docs/exchanges/backpack#watchorderbookforsymbols)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#watchorderbookforsymbols)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#watchorderbookforsymbols)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#watchorderbookforsymbols)
- [blofin](https://docs.ccxt.com/docs/exchanges/blofin#watchorderbookforsymbols)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#watchorderbookforsymbols)
- [bydfi](https://docs.ccxt.com/docs/exchanges/bydfi#watchorderbookforsymbols)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#watchorderbookforsymbols)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#watchorderbookforsymbols)
- [deribit](https://docs.ccxt.com/docs/exchanges/deribit#watchorderbookforsymbols)
- [gemini](https://docs.ccxt.com/docs/exchanges/gemini#watchorderbookforsymbols)
- [grvt](https://docs.ccxt.com/docs/exchanges/grvt#watchorderbookforsymbols)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#watchorderbookforsymbols)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#watchorderbookforsymbols)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#watchorderbookforsymbols)
- [toobit](https://docs.ccxt.com/docs/exchanges/toobit#watchorderbookforsymbols)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#watchorderbookforsymbols)

* * *

## [watchOrders](https://docs.ccxt.com/docs/base-spec\#watchorders)

watches information on multiple orders made by the user

**Kind**: instance

**Returns**: `Array<object>` \- a list of [order structures](https://docs.ccxt.com/docs/manual#order-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol of the market orders were made in |
| since | `int` | No | the earliest time in ms to fetch orders for |
| limit | `int` | No | the maximum number of order structures to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-257)

- [alpaca](https://docs.ccxt.com/docs/exchanges/alpaca#watchorders)
- [apex](https://docs.ccxt.com/docs/exchanges/apex#watchorders)
- [aster](https://docs.ccxt.com/docs/exchanges/aster#watchorders)
- [backpack](https://docs.ccxt.com/docs/exchanges/backpack#watchorders)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#watchorders)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#watchorders)
- [bitfinex](https://docs.ccxt.com/docs/exchanges/bitfinex#watchorders)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#watchorders)
- [bithumb](https://docs.ccxt.com/docs/exchanges/bithumb#watchorders)
- [bitrue](https://docs.ccxt.com/docs/exchanges/bitrue#watchorders)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#watchorders)
- [biofin](https://docs.ccxt.com/docs/exchanges/biofin#watchorders)
- [bullish](https://docs.ccxt.com/docs/exchanges/bullish#watchorders)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#watchorders)
- [bydfi](https://docs.ccxt.com/docs/exchanges/bydfi#watchorders)
- [cex](https://docs.ccxt.com/docs/exchanges/cex#watchorders)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#watchorders)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#watchorders)
- [deepcoin](https://docs.ccxt.com/docs/exchanges/deepcoin#watchorders)
- [deribit](https://docs.ccxt.com/docs/exchanges/deribit#watchorders)
- [derive](https://docs.ccxt.com/docs/exchanges/derive#watchorders)
- [extended](https://docs.ccxt.com/docs/exchanges/extended#watchorders)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#watchorders)
- [grvt](https://docs.ccxt.com/docs/exchanges/grvt#watchorders)
- [hashkey](https://docs.ccxt.com/docs/exchanges/hashkey#watchorders)
- [hollaex](https://docs.ccxt.com/docs/exchanges/hollaex#watchorders)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#watchorders)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#watchorders)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#watchorders)
- [lbank](https://docs.ccxt.com/docs/exchanges/lbank#watchorders)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#watchorders)
- [modetrade](https://docs.ccxt.com/docs/exchanges/modetrade#watchorders)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#watchorders)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#watchorders)
- [onetrading](https://docs.ccxt.com/docs/exchanges/onetrading#watchorders)
- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#watchorders)
- [phemex](https://docs.ccxt.com/docs/exchanges/phemex#watchorders)
- [toobit](https://docs.ccxt.com/docs/exchanges/toobit#watchorders)
- [upbit](https://docs.ccxt.com/docs/exchanges/upbit#watchorders)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#watchorders)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#watchorders)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#watchorders)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#watchorders)

* * *

## [watchOrdersForSymbols](https://docs.ccxt.com/docs/base-spec\#watchordersforsymbols)

watches information on multiple orders made by the user across multiple symbols

**Kind**: instance

**Returns**: `Array<object>` \- a list of \[order structures\]{@link /docs/manual#order-structure

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>` | Yes |  |
| since | `int` | No | the earliest time in ms to fetch orders for |
| limit | `int` | No | the maximum number of order structures to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |
| params.trigger | `boolean` | No | set to true for trigger orders |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-258)

- [blofin](https://docs.ccxt.com/docs/exchanges/blofin#watchordersforsymbols)
- [bydfi](https://docs.ccxt.com/docs/exchanges/bydfi#watchordersforsymbols)

* * *

## [watchPosition](https://docs.ccxt.com/docs/base-spec\#watchposition)

watch open positions for a specific symbol

**Kind**: instance

**Returns**: `object` \- a [position structure](https://docs.ccxt.com/docs/manual#position-structure)

| Param | Type | Description |
| --- | --- | --- |
| symbol | `string`, `undefined` | unified market symbol |
| params | `object` | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-259)

- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#watchposition)

* * *

## [watchPositions](https://docs.ccxt.com/docs/base-spec\#watchpositions)

watch all open positions

**Kind**: instance

**Returns**: `Array<object>` \- a list of [position structure](https://docs.ccxt.com/docs/manual#position-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>` | No | list of unified market symbols |
| since | `int` | No | the earliest time in ms to fetch positions for |
| limit | `int` | No | the maximum number of positions to retrieve |
| params | `object` | Yes | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-260)

- [apex](https://docs.ccxt.com/docs/exchanges/apex#watchpositions)
- [aster](https://docs.ccxt.com/docs/exchanges/aster#watchpositions)
- [backpack](https://docs.ccxt.com/docs/exchanges/backpack#watchpositions)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#watchpositions)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#watchpositions)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#watchpositions)
- [blofin](https://docs.ccxt.com/docs/exchanges/blofin#watchpositions)
- [bullish](https://docs.ccxt.com/docs/exchanges/bullish#watchpositions)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#watchpositions)
- [bydfi](https://docs.ccxt.com/docs/exchanges/bydfi#watchpositions)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#watchpositions)
- [deepcoin](https://docs.ccxt.com/docs/exchanges/deepcoin#watchpositions)
- [extended](https://docs.ccxt.com/docs/exchanges/extended#watchpositions)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#watchpositions)
- [grvt](https://docs.ccxt.com/docs/exchanges/grvt#watchpositions)
- [hashkey](https://docs.ccxt.com/docs/exchanges/hashkey#watchpositions)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#watchpositions)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#watchpositions)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#watchpositions)
- [modetrade](https://docs.ccxt.com/docs/exchanges/modetrade#watchpositions)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#watchpositions)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#watchpositions)
- [toobit](https://docs.ccxt.com/docs/exchanges/toobit#watchpositions)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#watchpositions)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#watchpositions)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#watchpositions)

* * *

## [watchTicker](https://docs.ccxt.com/docs/base-spec\#watchticker)

watches a price ticker, a statistical calculation with the information calculated over the past 24 hours for a specific market

**Kind**: instance

**Returns**: `object` \- a [ticker structure](https://docs.ccxt.com/docs/manual#ticker-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified symbol of the market to fetch the ticker for |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-261)

- [alpaca](https://docs.ccxt.com/docs/exchanges/alpaca#watchticker)
- [apex](https://docs.ccxt.com/docs/exchanges/apex#watchticker)
- [aster](https://docs.ccxt.com/docs/exchanges/aster#watchticker)
- [backpack](https://docs.ccxt.com/docs/exchanges/backpack#watchticker)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#watchticker)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#watchticker)
- [bitfinex](https://docs.ccxt.com/docs/exchanges/bitfinex#watchticker)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#watchticker)
- [bithumb](https://docs.ccxt.com/docs/exchanges/bithumb#watchticker)
- [bitopro](https://docs.ccxt.com/docs/exchanges/bitopro#watchticker)
- [bitrue](https://docs.ccxt.com/docs/exchanges/bitrue#watchticker)
- [bittrade](https://docs.ccxt.com/docs/exchanges/bittrade#watchticker)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#watchticker)
- [blockchaincom](https://docs.ccxt.com/docs/exchanges/blockchaincom#watchticker)
- [blofin](https://docs.ccxt.com/docs/exchanges/blofin#watchticker)
- [bullish](https://docs.ccxt.com/docs/exchanges/bullish#watchticker)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#watchticker)
- [bydfi](https://docs.ccxt.com/docs/exchanges/bydfi#watchticker)
- [cex](https://docs.ccxt.com/docs/exchanges/cex#watchticker)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#watchticker)
- [coinone](https://docs.ccxt.com/docs/exchanges/coinone#watchticker)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#watchticker)
- [deepcoin](https://docs.ccxt.com/docs/exchanges/deepcoin#watchticker)
- [deribit](https://docs.ccxt.com/docs/exchanges/deribit#watchticker)
- [derive](https://docs.ccxt.com/docs/exchanges/derive#watchticker)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#watchticker)
- [grvt](https://docs.ccxt.com/docs/exchanges/grvt#watchticker)
- [hashkey](https://docs.ccxt.com/docs/exchanges/hashkey#watchticker)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#watchticker)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#watchticker)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#watchticker)
- [lbank](https://docs.ccxt.com/docs/exchanges/lbank#watchticker)
- [lighter](https://docs.ccxt.com/docs/exchanges/lighter#watchticker)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#watchticker)
- [modetrade](https://docs.ccxt.com/docs/exchanges/modetrade#watchticker)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#watchticker)
- [ndax](https://docs.ccxt.com/docs/exchanges/ndax#watchticker)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#watchticker)
- [onetrading](https://docs.ccxt.com/docs/exchanges/onetrading#watchticker)
- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#watchticker)
- [phemex](https://docs.ccxt.com/docs/exchanges/phemex#watchticker)
- [toobit](https://docs.ccxt.com/docs/exchanges/toobit#watchticker)
- [upbit](https://docs.ccxt.com/docs/exchanges/upbit#watchticker)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#watchticker)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#watchticker)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#watchticker)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#watchticker)

* * *

## [watchTickers](https://docs.ccxt.com/docs/base-spec\#watchtickers)

watches a price ticker, a statistical calculation with the information calculated over the past 24 hours for all markets of a specific list

**Kind**: instance

**Returns**: `object` \- a [ticker structure](https://docs.ccxt.com/docs/manual#ticker-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>` | Yes | unified symbol of the market to fetch the ticker for |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-262)

- [apex](https://docs.ccxt.com/docs/exchanges/apex#watchtickers)
- [aster](https://docs.ccxt.com/docs/exchanges/aster#watchtickers)
- [backpack](https://docs.ccxt.com/docs/exchanges/backpack#watchtickers)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#watchtickers)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#watchtickers)
- [bithumb](https://docs.ccxt.com/docs/exchanges/bithumb#watchtickers)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#watchtickers)
- [blofin](https://docs.ccxt.com/docs/exchanges/blofin#watchtickers)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#watchtickers)
- [bydfi](https://docs.ccxt.com/docs/exchanges/bydfi#watchtickers)
- [cex](https://docs.ccxt.com/docs/exchanges/cex#watchtickers)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#watchtickers)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#watchtickers)
- [deribit](https://docs.ccxt.com/docs/exchanges/deribit#watchtickers)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#watchtickers)
- [grvt](https://docs.ccxt.com/docs/exchanges/grvt#watchtickers)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#watchtickers)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#watchtickers)
- [lighter](https://docs.ccxt.com/docs/exchanges/lighter#watchtickers)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#watchtickers)
- [modetrade](https://docs.ccxt.com/docs/exchanges/modetrade#watchtickers)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#watchtickers)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#watchtickers)
- [onetrading](https://docs.ccxt.com/docs/exchanges/onetrading#watchtickers)
- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#watchtickers)
- [phemex](https://docs.ccxt.com/docs/exchanges/phemex#watchtickers)
- [toobit](https://docs.ccxt.com/docs/exchanges/toobit#watchtickers)
- [upbit](https://docs.ccxt.com/docs/exchanges/upbit#watchtickers)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#watchtickers)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#watchtickers)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#watchtickers)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#watchtickers)

* * *

## [watchTrades](https://docs.ccxt.com/docs/base-spec\#watchtrades)

watches information on multiple trades made in a market

**Kind**: instance

**Returns**: `Array<object>` \- a list of [trade structures](https://docs.ccxt.com/docs/manual#trade-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbol | `string` | Yes | unified market symbol of the market trades were made in |
| since | `int` | No | the earliest time in ms to fetch orders for |
| limit | `int` | No | the maximum number of trade structures to retrieve |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-263)

- [alpaca](https://docs.ccxt.com/docs/exchanges/alpaca#watchtrades)
- [apex](https://docs.ccxt.com/docs/exchanges/apex#watchtrades)
- [aster](https://docs.ccxt.com/docs/exchanges/aster#watchtrades)
- [backpack](https://docs.ccxt.com/docs/exchanges/backpack#watchtrades)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#watchtrades)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#watchtrades)
- [bitfinex](https://docs.ccxt.com/docs/exchanges/bitfinex#watchtrades)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#watchtrades)
- [bithumb](https://docs.ccxt.com/docs/exchanges/bithumb#watchtrades)
- [bitopro](https://docs.ccxt.com/docs/exchanges/bitopro#watchtrades)
- [bitrue](https://docs.ccxt.com/docs/exchanges/bitrue#watchtrades)
- [bittrade](https://docs.ccxt.com/docs/exchanges/bittrade#watchtrades)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#watchtrades)
- [blockchaincom](https://docs.ccxt.com/docs/exchanges/blockchaincom#watchtrades)
- [blofin](https://docs.ccxt.com/docs/exchanges/blofin#watchtrades)
- [bullish](https://docs.ccxt.com/docs/exchanges/bullish#watchtrades)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#watchtrades)
- [cex](https://docs.ccxt.com/docs/exchanges/cex#watchtrades)
- [coincheck](https://docs.ccxt.com/docs/exchanges/coincheck#watchtrades)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#watchtrades)
- [coinone](https://docs.ccxt.com/docs/exchanges/coinone#watchtrades)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#watchtrades)
- [deepcoin](https://docs.ccxt.com/docs/exchanges/deepcoin#watchtrades)
- [deribit](https://docs.ccxt.com/docs/exchanges/deribit#watchtrades)
- [derive](https://docs.ccxt.com/docs/exchanges/derive#watchtrades)
- [dydx](https://docs.ccxt.com/docs/exchanges/dydx#watchtrades)
- [extended](https://docs.ccxt.com/docs/exchanges/extended#watchtrades)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#watchtrades)
- [gemini](https://docs.ccxt.com/docs/exchanges/gemini#watchtrades)
- [grvt](https://docs.ccxt.com/docs/exchanges/grvt#watchtrades)
- [hashkey](https://docs.ccxt.com/docs/exchanges/hashkey#watchtrades)
- [hollaex](https://docs.ccxt.com/docs/exchanges/hollaex#watchtrades)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#watchtrades)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#watchtrades)
- [independentreserve](https://docs.ccxt.com/docs/exchanges/independentreserve#watchtrades)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#watchtrades)
- [lbank](https://docs.ccxt.com/docs/exchanges/lbank#watchtrades)
- [lighter](https://docs.ccxt.com/docs/exchanges/lighter#watchtrades)
- [luno](https://docs.ccxt.com/docs/exchanges/luno#watchtrades)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#watchtrades)
- [modetrade](https://docs.ccxt.com/docs/exchanges/modetrade#watchtrades)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#watchtrades)
- [ndax](https://docs.ccxt.com/docs/exchanges/ndax#watchtrades)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#watchtrades)
- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#watchtrades)
- [phemex](https://docs.ccxt.com/docs/exchanges/phemex#watchtrades)
- [toobit](https://docs.ccxt.com/docs/exchanges/toobit#watchtrades)
- [upbit](https://docs.ccxt.com/docs/exchanges/upbit#watchtrades)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#watchtrades)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#watchtrades)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#watchtrades)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#watchtrades)

* * *

## [watchTradesForSymbols](https://docs.ccxt.com/docs/base-spec\#watchtradesforsymbols)

get the list of most recent trades for a list of symbols

**Kind**: instance

**Returns**: `Array<object>` \- a list of [trade structures](https://docs.ccxt.com/docs/manual#public-trades)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| symbols | `Array<string>` | Yes | unified symbol of the market to fetch trades for |
| since | `int` | No | timestamp in ms of the earliest trade to fetch |
| limit | `int` | No | the maximum amount of trades to fetch |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-264)

- [apex](https://docs.ccxt.com/docs/exchanges/apex#watchtradesforsymbols)
- [aster](https://docs.ccxt.com/docs/exchanges/aster#watchtradesforsymbols)
- [backpack](https://docs.ccxt.com/docs/exchanges/backpack#watchtradesforsymbols)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#watchtradesforsymbols)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#watchtradesforsymbols)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#watchtradesforsymbols)
- [blofin](https://docs.ccxt.com/docs/exchanges/blofin#watchtradesforsymbols)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#watchtradesforsymbols)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#watchtradesforsymbols)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#watchtradesforsymbols)
- [deribit](https://docs.ccxt.com/docs/exchanges/deribit#watchtradesforsymbols)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#watchtradesforsymbols)
- [gemini](https://docs.ccxt.com/docs/exchanges/gemini#watchtradesforsymbols)
- [grvt](https://docs.ccxt.com/docs/exchanges/grvt#watchtradesforsymbols)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#watchtradesforsymbols)
- [nado](https://docs.ccxt.com/docs/exchanges/nado#watchtradesforsymbols)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#watchtradesforsymbols)
- [toobit](https://docs.ccxt.com/docs/exchanges/toobit#watchtradesforsymbols)
- [upbit](https://docs.ccxt.com/docs/exchanges/upbit#watchtradesforsymbols)
- [weex](https://docs.ccxt.com/docs/exchanges/weex#watchtradesforsymbols)

* * *

## [withdraw](https://docs.ccxt.com/docs/base-spec\#withdraw)

make a withdrawal

**Kind**: instance

**Returns**: `object` \- a [transaction structure](https://docs.ccxt.com/docs/manual#transaction-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| code | `string` | Yes | unified currency code |
| amount | `float` | Yes | the amount to withdraw |
| address | `string` | Yes | the address to withdraw to |
| tag | `string` | Yes | a memo for the transaction |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-265)

- [alpaca](https://docs.ccxt.com/docs/exchanges/alpaca#withdraw)
- [aster](https://docs.ccxt.com/docs/exchanges/aster#withdraw)
- [backpack](https://docs.ccxt.com/docs/exchanges/backpack#withdraw)
- [bigone](https://docs.ccxt.com/docs/exchanges/bigone#withdraw)
- [binance](https://docs.ccxt.com/docs/exchanges/binance#withdraw)
- [bingx](https://docs.ccxt.com/docs/exchanges/bingx#withdraw)
- [bitbank](https://docs.ccxt.com/docs/exchanges/bitbank#withdraw)
- [bitfinex](https://docs.ccxt.com/docs/exchanges/bitfinex#withdraw)
- [bitflyer](https://docs.ccxt.com/docs/exchanges/bitflyer#withdraw)
- [bitget](https://docs.ccxt.com/docs/exchanges/bitget#withdraw)
- [bithumb](https://docs.ccxt.com/docs/exchanges/bithumb#withdraw)
- [bitopro](https://docs.ccxt.com/docs/exchanges/bitopro#withdraw)
- [bitrue](https://docs.ccxt.com/docs/exchanges/bitrue#withdraw)
- [bitso](https://docs.ccxt.com/docs/exchanges/bitso#withdraw)
- [bitstamp](https://docs.ccxt.com/docs/exchanges/bitstamp#withdraw)
- [bittrade](https://docs.ccxt.com/docs/exchanges/bittrade#withdraw)
- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#withdraw)
- [blockchaincom](https://docs.ccxt.com/docs/exchanges/blockchaincom#withdraw)
- [blofin](https://docs.ccxt.com/docs/exchanges/blofin#withdraw)
- [btcmarkets](https://docs.ccxt.com/docs/exchanges/btcmarkets#withdraw)
- [bullish](https://docs.ccxt.com/docs/exchanges/bullish#withdraw)
- [bybit](https://docs.ccxt.com/docs/exchanges/bybit#withdraw)
- [coinbase](https://docs.ccxt.com/docs/exchanges/coinbase#withdraw)
- [coinbaseexchange](https://docs.ccxt.com/docs/exchanges/coinbaseexchange#withdraw)
- [coinbaseinternational](https://docs.ccxt.com/docs/exchanges/coinbaseinternational#withdraw)
- [coinex](https://docs.ccxt.com/docs/exchanges/coinex#withdraw)
- [coinmate](https://docs.ccxt.com/docs/exchanges/coinmate#withdraw)
- [coinsph](https://docs.ccxt.com/docs/exchanges/coinsph#withdraw)
- [cryptocom](https://docs.ccxt.com/docs/exchanges/cryptocom#withdraw)
- [deribit](https://docs.ccxt.com/docs/exchanges/deribit#withdraw)
- [digifinex](https://docs.ccxt.com/docs/exchanges/digifinex#withdraw)
- [dydx](https://docs.ccxt.com/docs/exchanges/dydx#withdraw)
- [extended](https://docs.ccxt.com/docs/exchanges/extended#withdraw)
- [foxbit](https://docs.ccxt.com/docs/exchanges/foxbit#withdraw)
- [gate](https://docs.ccxt.com/docs/exchanges/gate#withdraw)
- [gemini](https://docs.ccxt.com/docs/exchanges/gemini#withdraw)
- [grvt](https://docs.ccxt.com/docs/exchanges/grvt#withdraw)
- [hashkey](https://docs.ccxt.com/docs/exchanges/hashkey#withdraw)
- [hibachi](https://docs.ccxt.com/docs/exchanges/hibachi#withdraw)
- [hitbtc](https://docs.ccxt.com/docs/exchanges/hitbtc#withdraw)
- [hollaex](https://docs.ccxt.com/docs/exchanges/hollaex#withdraw)
- [htx](https://docs.ccxt.com/docs/exchanges/htx#withdraw)
- [hyperliquid](https://docs.ccxt.com/docs/exchanges/hyperliquid#withdraw)
- [independentreserve](https://docs.ccxt.com/docs/exchanges/independentreserve#withdraw)
- [indodax](https://docs.ccxt.com/docs/exchanges/indodax#withdraw)
- [kraken](https://docs.ccxt.com/docs/exchanges/kraken#withdraw)
- [kucoin](https://docs.ccxt.com/docs/exchanges/kucoin#withdraw)
- [lbank](https://docs.ccxt.com/docs/exchanges/lbank#withdraw)
- [lighter](https://docs.ccxt.com/docs/exchanges/lighter#withdraw)
- [mercado](https://docs.ccxt.com/docs/exchanges/mercado#withdraw)
- [mexc](https://docs.ccxt.com/docs/exchanges/mexc#withdraw)
- [modetrade](https://docs.ccxt.com/docs/exchanges/modetrade#withdraw)
- [ndax](https://docs.ccxt.com/docs/exchanges/ndax#withdraw)
- [okx](https://docs.ccxt.com/docs/exchanges/okx#withdraw)
- [pacifica](https://docs.ccxt.com/docs/exchanges/pacifica#withdraw)
- [phemex](https://docs.ccxt.com/docs/exchanges/phemex#withdraw)
- [poloniex](https://docs.ccxt.com/docs/exchanges/poloniex#withdraw)
- [tokocrypto](https://docs.ccxt.com/docs/exchanges/tokocrypto#withdraw)
- [toobit](https://docs.ccxt.com/docs/exchanges/toobit#withdraw)
- [upbit](https://docs.ccxt.com/docs/exchanges/upbit#withdraw)
- [whitebit](https://docs.ccxt.com/docs/exchanges/whitebit#withdraw)
- [woo](https://docs.ccxt.com/docs/exchanges/woo#withdraw)
- [woofipro](https://docs.ccxt.com/docs/exchanges/woofipro#withdraw)
- [xt](https://docs.ccxt.com/docs/exchanges/xt#withdraw)
- [zaif](https://docs.ccxt.com/docs/exchanges/zaif#withdraw)

* * *

## [withdrawWs](https://docs.ccxt.com/docs/base-spec\#withdrawws)

make a withdrawal

**Kind**: instance

**Returns**: `object` \- a [transaction structure](https://docs.ccxt.com/docs/manual#transaction-structure)

| Param | Type | Required | Description |
| --- | --- | --- | --- |
| code | `string` | Yes | unified currency code |
| amount | `float` | Yes | the amount to withdraw |
| address | `string` | Yes | the address to withdraw to |
| tag | `string` | Yes |  |
| params | `object` | No | extra parameters specific to the exchange API endpoint |

##### [Supported exchanges](https://docs.ccxt.com/docs/base-spec\#supported-exchanges-266)

- [bitvavo](https://docs.ccxt.com/docs/exchanges/bitvavo#withdrawws)

[Contributing\\
\\
Read the notes when opening a new issue on github and provide the requested details, so we can assist you better. You can also read the Troubleshooting section.](https://docs.ccxt.com/docs/contributing) [Supported Exchanges\\
\\
All cryptocurrency and prediction-market exchanges supported by CCXT.](https://docs.ccxt.com/docs/exchange-markets)

### On this page

[addMargin](https://docs.ccxt.com/docs/base-spec#addmargin) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges) [borrowCrossMargin](https://docs.ccxt.com/docs/base-spec#borrowcrossmargin) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-1) [borrowIsolatedMargin](https://docs.ccxt.com/docs/base-spec#borrowisolatedmargin) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-2) [calculatePricePrecision](https://docs.ccxt.com/docs/base-spec#calculatepriceprecision) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-3) [cancelAllContractOrders](https://docs.ccxt.com/docs/base-spec#cancelallcontractorders) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-4) [cancelAllOrders](https://docs.ccxt.com/docs/base-spec#cancelallorders) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-5) [cancelAllOrdersAfter](https://docs.ccxt.com/docs/base-spec#cancelallordersafter) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-6) [cancelAllOrdersWs](https://docs.ccxt.com/docs/base-spec#cancelallordersws) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-7) [cancelAllSpotOrders](https://docs.ccxt.com/docs/base-spec#cancelallspotorders) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-8) [cancelAllUtaOrders](https://docs.ccxt.com/docs/base-spec#cancelallutaorders) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-9) [cancelContractOrder](https://docs.ccxt.com/docs/base-spec#cancelcontractorder) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-10) [cancelOrder](https://docs.ccxt.com/docs/base-spec#cancelorder) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-11) [cancelOrderWs](https://docs.ccxt.com/docs/base-spec#cancelorderws) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-12) [cancelOrders](https://docs.ccxt.com/docs/base-spec#cancelorders) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-13) [cancelOrdersForSymbols](https://docs.ccxt.com/docs/base-spec#cancelordersforsymbols) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-14) [cancelOrdersRequest](https://docs.ccxt.com/docs/base-spec#cancelordersrequest) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-15) [cancelOrdersWs](https://docs.ccxt.com/docs/base-spec#cancelordersws) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-16) [cancelSpotOrder](https://docs.ccxt.com/docs/base-spec#cancelspotorder) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-17) [cancelTwapOrder](https://docs.ccxt.com/docs/base-spec#canceltwaporder) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-18) [cancelUtaOrder](https://docs.ccxt.com/docs/base-spec#cancelutaorder) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-19) [closeAllPositions](https://docs.ccxt.com/docs/base-spec#closeallpositions) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-20) [closePosition](https://docs.ccxt.com/docs/base-spec#closeposition) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-21) [closePositions](https://docs.ccxt.com/docs/base-spec#closepositions) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-22) [createAccount](https://docs.ccxt.com/docs/base-spec#createaccount) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-23) [createContractOrder](https://docs.ccxt.com/docs/base-spec#createcontractorder) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-24) [createContractOrders](https://docs.ccxt.com/docs/base-spec#createcontractorders) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-25) [createConvertTrade](https://docs.ccxt.com/docs/base-spec#createconverttrade) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-26) [createDepositAddress](https://docs.ccxt.com/docs/base-spec#createdepositaddress) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-27) [createGiftCode](https://docs.ccxt.com/docs/base-spec#creategiftcode) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-28) [createMarkeSellOrderWithCost](https://docs.ccxt.com/docs/base-spec#createmarkesellorderwithcost) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-29) [createMarketBuyOrderWithCost](https://docs.ccxt.com/docs/base-spec#createmarketbuyorderwithcost) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-30) [createMarketOrderWithCost](https://docs.ccxt.com/docs/base-spec#createmarketorderwithcost) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-31) [createMarketSellOrderWithCost](https://docs.ccxt.com/docs/base-spec#createmarketsellorderwithcost) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-32) [createOrder](https://docs.ccxt.com/docs/base-spec#createorder) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-33) [createOrderWs](https://docs.ccxt.com/docs/base-spec#createorderws) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-34) [createOrders](https://docs.ccxt.com/docs/base-spec#createorders) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-35) [createOrdersRequest](https://docs.ccxt.com/docs/base-spec#createordersrequest) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-36) [createOrdersWs](https://docs.ccxt.com/docs/base-spec#createordersws) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-37) [createSpotOrder](https://docs.ccxt.com/docs/base-spec#createspotorder) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-38) [createSpotOrders](https://docs.ccxt.com/docs/base-spec#createspotorders) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-39) [createSubAccount](https://docs.ccxt.com/docs/base-spec#createsubaccount) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-40) [createSwapOrder](https://docs.ccxt.com/docs/base-spec#createswaporder) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-41) [createTrailingAmountOrder](https://docs.ccxt.com/docs/base-spec#createtrailingamountorder) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-42) [createTrailingPercentOrder](https://docs.ccxt.com/docs/base-spec#createtrailingpercentorder) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-43) [createTwapOrder](https://docs.ccxt.com/docs/base-spec#createtwaporder) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-44) [createUtaOrder](https://docs.ccxt.com/docs/base-spec#createutaorder) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-45) [createVault](https://docs.ccxt.com/docs/base-spec#createvault) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-46) [deposit](https://docs.ccxt.com/docs/base-spec#deposit) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-47) [editContractOrder](https://docs.ccxt.com/docs/base-spec#editcontractorder) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-48) [editOrder](https://docs.ccxt.com/docs/base-spec#editorder) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-49) [editOrderWs](https://docs.ccxt.com/docs/base-spec#editorderws) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-50) [editOrders](https://docs.ccxt.com/docs/base-spec#editorders) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-51) [enableDemoTrading](https://docs.ccxt.com/docs/base-spec#enabledemotrading) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-52) [enableUserDexAbstraction](https://docs.ccxt.com/docs/base-spec#enableuserdexabstraction) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-53) [fetchADLRank](https://docs.ccxt.com/docs/base-spec#fetchadlrank) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-54) [fetchAccount](https://docs.ccxt.com/docs/base-spec#fetchaccount) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-55) [fetchAccountIdByType](https://docs.ccxt.com/docs/base-spec#fetchaccountidbytype) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-56) [fetchAccountSettings](https://docs.ccxt.com/docs/base-spec#fetchaccountsettings) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-57) [fetchAccounts](https://docs.ccxt.com/docs/base-spec#fetchaccounts) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-58) [fetchAllGreeks](https://docs.ccxt.com/docs/base-spec#fetchallgreeks) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-59) [fetchBalance](https://docs.ccxt.com/docs/base-spec#fetchbalance) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-60) [fetchBalanceWs](https://docs.ccxt.com/docs/base-spec#fetchbalancews) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-61) [fetchBidsAsks](https://docs.ccxt.com/docs/base-spec#fetchbidsasks) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-62) [fetchBorrowInterest](https://docs.ccxt.com/docs/base-spec#fetchborrowinterest) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-63) [fetchBorrowRateHistories](https://docs.ccxt.com/docs/base-spec#fetchborrowratehistories) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-64) [fetchBorrowRateHistory](https://docs.ccxt.com/docs/base-spec#fetchborrowratehistory) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-65) [fetchCanceledAndClosedOrders](https://docs.ccxt.com/docs/base-spec#fetchcanceledandclosedorders) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-66) [fetchCanceledOrders](https://docs.ccxt.com/docs/base-spec#fetchcanceledorders) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-67) [fetchClosedOrder](https://docs.ccxt.com/docs/base-spec#fetchclosedorder) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-68) [fetchClosedOrders](https://docs.ccxt.com/docs/base-spec#fetchclosedorders) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-69) [fetchClosedOrdersWs](https://docs.ccxt.com/docs/base-spec#fetchclosedordersws) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-70) [fetchContractBalance](https://docs.ccxt.com/docs/base-spec#fetchcontractbalance) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-71) [fetchContractDepositAddress](https://docs.ccxt.com/docs/base-spec#fetchcontractdepositaddress) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-72) [fetchContractDeposits](https://docs.ccxt.com/docs/base-spec#fetchcontractdeposits) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-73) [fetchContractOrder](https://docs.ccxt.com/docs/base-spec#fetchcontractorder) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-74) [fetchContractOrdersByStatus](https://docs.ccxt.com/docs/base-spec#fetchcontractordersbystatus) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-75) [fetchContractWithdrawals](https://docs.ccxt.com/docs/base-spec#fetchcontractwithdrawals) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-76) [fetchConvertCurrencies](https://docs.ccxt.com/docs/base-spec#fetchconvertcurrencies) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-77) [fetchConvertQuote](https://docs.ccxt.com/docs/base-spec#fetchconvertquote) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-78) [fetchConvertTrade](https://docs.ccxt.com/docs/base-spec#fetchconverttrade) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-79) [fetchConvertTradeHistory](https://docs.ccxt.com/docs/base-spec#fetchconverttradehistory) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-80) [fetchCrossBorrowRate](https://docs.ccxt.com/docs/base-spec#fetchcrossborrowrate) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-81) [fetchCrossBorrowRates](https://docs.ccxt.com/docs/base-spec#fetchcrossborrowrates) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-82) [fetchCurrencies](https://docs.ccxt.com/docs/base-spec#fetchcurrencies) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-83) [fetchCurrenciesWs](https://docs.ccxt.com/docs/base-spec#fetchcurrenciesws) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-84) [fetchDeposit](https://docs.ccxt.com/docs/base-spec#fetchdeposit) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-85) [fetchDepositAddress](https://docs.ccxt.com/docs/base-spec#fetchdepositaddress) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-86) [fetchDepositAddresses](https://docs.ccxt.com/docs/base-spec#fetchdepositaddresses) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-87) [fetchDepositAddressesByNetwork](https://docs.ccxt.com/docs/base-spec#fetchdepositaddressesbynetwork) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-88) [fetchDepositMethodId](https://docs.ccxt.com/docs/base-spec#fetchdepositmethodid) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-89) [fetchDepositMethodIds](https://docs.ccxt.com/docs/base-spec#fetchdepositmethodids) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-90) [fetchDepositMethods](https://docs.ccxt.com/docs/base-spec#fetchdepositmethods) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-91) [fetchDepositWithdrawFee](https://docs.ccxt.com/docs/base-spec#fetchdepositwithdrawfee) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-92) [fetchDepositWithdrawFees](https://docs.ccxt.com/docs/base-spec#fetchdepositwithdrawfees) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-93) [fetchDeposits](https://docs.ccxt.com/docs/base-spec#fetchdeposits) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-94) [fetchDepositsWithdrawals](https://docs.ccxt.com/docs/base-spec#fetchdepositswithdrawals) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-95) [fetchDepositsWs](https://docs.ccxt.com/docs/base-spec#fetchdepositsws) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-96) [fetchFundingHistory](https://docs.ccxt.com/docs/base-spec#fetchfundinghistory) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-97) [fetchFundingInterval](https://docs.ccxt.com/docs/base-spec#fetchfundinginterval) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-98) [fetchFundingIntervals](https://docs.ccxt.com/docs/base-spec#fetchfundingintervals) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-99) [fetchFundingLimits](https://docs.ccxt.com/docs/base-spec#fetchfundinglimits) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-100) [fetchFundingRate](https://docs.ccxt.com/docs/base-spec#fetchfundingrate) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-101) [fetchFundingRateHistory](https://docs.ccxt.com/docs/base-spec#fetchfundingratehistory) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-102) [fetchFundingRates](https://docs.ccxt.com/docs/base-spec#fetchfundingrates) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-103) [fetchGreeks](https://docs.ccxt.com/docs/base-spec#fetchgreeks) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-104) [fetchHip3Markets](https://docs.ccxt.com/docs/base-spec#fetchhip3markets) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-105) [fetchIsolatedBorrowRate](https://docs.ccxt.com/docs/base-spec#fetchisolatedborrowrate) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-106) [fetchIsolatedBorrowRates](https://docs.ccxt.com/docs/base-spec#fetchisolatedborrowrates) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-107) [fetchL3OrderBook](https://docs.ccxt.com/docs/base-spec#fetchl3orderbook) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-108) [fetchLastPrices](https://docs.ccxt.com/docs/base-spec#fetchlastprices) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-109) [fetchLedger](https://docs.ccxt.com/docs/base-spec#fetchledger) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-110) [fetchLedgerEntry](https://docs.ccxt.com/docs/base-spec#fetchledgerentry) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-111) [fetchLeverage](https://docs.ccxt.com/docs/base-spec#fetchleverage) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-112) [fetchLeverageTiers](https://docs.ccxt.com/docs/base-spec#fetchleveragetiers) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-113) [fetchLeverages](https://docs.ccxt.com/docs/base-spec#fetchleverages) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-114) [fetchLiquidations](https://docs.ccxt.com/docs/base-spec#fetchliquidations) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-115) [fetchLongShortRatioHistory](https://docs.ccxt.com/docs/base-spec#fetchlongshortratiohistory) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-116) [fetchMarginAdjustmentHistory](https://docs.ccxt.com/docs/base-spec#fetchmarginadjustmenthistory) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-117) [fetchMarginMode](https://docs.ccxt.com/docs/base-spec#fetchmarginmode) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-118) [fetchMarginModes](https://docs.ccxt.com/docs/base-spec#fetchmarginmodes) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-119) [fetchMarkOHLCV](https://docs.ccxt.com/docs/base-spec#fetchmarkohlcv) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-120) [fetchMarkPrice](https://docs.ccxt.com/docs/base-spec#fetchmarkprice) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-121) [fetchMarkPrices](https://docs.ccxt.com/docs/base-spec#fetchmarkprices) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-122) [fetchMarketLeverageTiers](https://docs.ccxt.com/docs/base-spec#fetchmarketleveragetiers) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-123) [fetchMarkets](https://docs.ccxt.com/docs/base-spec#fetchmarkets) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-124) [fetchMarketsWs](https://docs.ccxt.com/docs/base-spec#fetchmarketsws) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-125) [fetchMyContractTrades](https://docs.ccxt.com/docs/base-spec#fetchmycontracttrades) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-126) [fetchMyDustTrades](https://docs.ccxt.com/docs/base-spec#fetchmydusttrades) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-127) [fetchMyLiquidations](https://docs.ccxt.com/docs/base-spec#fetchmyliquidations) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-128) [fetchMySettlementHistory](https://docs.ccxt.com/docs/base-spec#fetchmysettlementhistory) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-129) [fetchMySpotTrades](https://docs.ccxt.com/docs/base-spec#fetchmyspottrades) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-130) [fetchMyTrades](https://docs.ccxt.com/docs/base-spec#fetchmytrades) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-131) [fetchMyTradesWs](https://docs.ccxt.com/docs/base-spec#fetchmytradesws) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-132) [fetchMyUtaTrades](https://docs.ccxt.com/docs/base-spec#fetchmyutatrades) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-133) [fetchOHLCV](https://docs.ccxt.com/docs/base-spec#fetchohlcv) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-134) [fetchOHLCVWs](https://docs.ccxt.com/docs/base-spec#fetchohlcvws) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-135) [fetchOpenInterest](https://docs.ccxt.com/docs/base-spec#fetchopeninterest) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-136) [fetchOpenInterestHistory](https://docs.ccxt.com/docs/base-spec#fetchopeninteresthistory) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-137) [fetchOpenInterests](https://docs.ccxt.com/docs/base-spec#fetchopeninterests) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-138) [fetchOpenOrder](https://docs.ccxt.com/docs/base-spec#fetchopenorder) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-139) [fetchOpenOrders](https://docs.ccxt.com/docs/base-spec#fetchopenorders) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-140) [fetchOpenOrdersWs](https://docs.ccxt.com/docs/base-spec#fetchopenordersws) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-141) [fetchOption](https://docs.ccxt.com/docs/base-spec#fetchoption) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-142) [fetchOptionChain](https://docs.ccxt.com/docs/base-spec#fetchoptionchain) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-143) [fetchOptionPositions](https://docs.ccxt.com/docs/base-spec#fetchoptionpositions) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-144) [fetchOrder](https://docs.ccxt.com/docs/base-spec#fetchorder) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-145) [fetchOrderBook](https://docs.ccxt.com/docs/base-spec#fetchorderbook) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-146) [fetchOrderBookWs](https://docs.ccxt.com/docs/base-spec#fetchorderbookws) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-147) [fetchOrderBooks](https://docs.ccxt.com/docs/base-spec#fetchorderbooks) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-148) [fetchOrderClassic](https://docs.ccxt.com/docs/base-spec#fetchorderclassic) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-149) [fetchOrderTrades](https://docs.ccxt.com/docs/base-spec#fetchordertrades) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-150) [fetchOrderWs](https://docs.ccxt.com/docs/base-spec#fetchorderws) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-151) [fetchOrders](https://docs.ccxt.com/docs/base-spec#fetchorders) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-152) [fetchOrdersByIds](https://docs.ccxt.com/docs/base-spec#fetchordersbyids) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-153) [fetchOrdersByStatus](https://docs.ccxt.com/docs/base-spec#fetchordersbystatus) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-154) [fetchOrdersClassic](https://docs.ccxt.com/docs/base-spec#fetchordersclassic) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-155) [fetchOrdersWs](https://docs.ccxt.com/docs/base-spec#fetchordersws) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-156) [fetchPortfolioDetails](https://docs.ccxt.com/docs/base-spec#fetchportfoliodetails) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-157) [fetchPortfolios](https://docs.ccxt.com/docs/base-spec#fetchportfolios) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-158) [fetchPosition](https://docs.ccxt.com/docs/base-spec#fetchposition) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-159) [fetchPositionHistory](https://docs.ccxt.com/docs/base-spec#fetchpositionhistory) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-160) [fetchPositionMode](https://docs.ccxt.com/docs/base-spec#fetchpositionmode) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-161) [fetchPositionWs](https://docs.ccxt.com/docs/base-spec#fetchpositionws) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-162) [fetchPositions](https://docs.ccxt.com/docs/base-spec#fetchpositions) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-163) [fetchPositionsADLRank](https://docs.ccxt.com/docs/base-spec#fetchpositionsadlrank) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-164) [fetchPositionsForSymbol](https://docs.ccxt.com/docs/base-spec#fetchpositionsforsymbol) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-165) [fetchPositionsHistory](https://docs.ccxt.com/docs/base-spec#fetchpositionshistory) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-166) [fetchPositionsRisk](https://docs.ccxt.com/docs/base-spec#fetchpositionsrisk) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-167) [fetchPositionsWs](https://docs.ccxt.com/docs/base-spec#fetchpositionsws) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-168) [fetchSettlementHistory](https://docs.ccxt.com/docs/base-spec#fetchsettlementhistory) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-169) [fetchSpotMarkets](https://docs.ccxt.com/docs/base-spec#fetchspotmarkets) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-170) [fetchSpotOrder](https://docs.ccxt.com/docs/base-spec#fetchspotorder) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-171) [fetchSpotOrdersByStatus](https://docs.ccxt.com/docs/base-spec#fetchspotordersbystatus) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-172) [fetchStatus](https://docs.ccxt.com/docs/base-spec#fetchstatus) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-173) [fetchSwapMarkets](https://docs.ccxt.com/docs/base-spec#fetchswapmarkets) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-174) [fetchTicker](https://docs.ccxt.com/docs/base-spec#fetchticker) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-175) [fetchTickerWs](https://docs.ccxt.com/docs/base-spec#fetchtickerws) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-176) [fetchTickers](https://docs.ccxt.com/docs/base-spec#fetchtickers) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-177) [fetchTime](https://docs.ccxt.com/docs/base-spec#fetchtime) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-178) [fetchTrades](https://docs.ccxt.com/docs/base-spec#fetchtrades) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-179) [fetchTradesWs](https://docs.ccxt.com/docs/base-spec#fetchtradesws) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-180) [fetchTradingFee](https://docs.ccxt.com/docs/base-spec#fetchtradingfee) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-181) [fetchTradingFees](https://docs.ccxt.com/docs/base-spec#fetchtradingfees) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-182) [fetchTradingFeesWs](https://docs.ccxt.com/docs/base-spec#fetchtradingfeesws) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-183) [fetchTradingLimits](https://docs.ccxt.com/docs/base-spec#fetchtradinglimits) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-184) [fetchTransactionFee](https://docs.ccxt.com/docs/base-spec#fetchtransactionfee) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-185) [fetchTransactionFees](https://docs.ccxt.com/docs/base-spec#fetchtransactionfees) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-186) [fetchTransactions](https://docs.ccxt.com/docs/base-spec#fetchtransactions) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-187) [fetchTransfer](https://docs.ccxt.com/docs/base-spec#fetchtransfer) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-188) [fetchTransfers](https://docs.ccxt.com/docs/base-spec#fetchtransfers) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-189) [fetchUnderlyingAssets](https://docs.ccxt.com/docs/base-spec#fetchunderlyingassets) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-190) [fetchUtaBalance](https://docs.ccxt.com/docs/base-spec#fetchutabalance) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-191) [fetchUtaOrder](https://docs.ccxt.com/docs/base-spec#fetchutaorder) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-192) [fetchUtaOrdersByStatus](https://docs.ccxt.com/docs/base-spec#fetchutaordersbystatus) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-193) [fetchVolatilityHistory](https://docs.ccxt.com/docs/base-spec#fetchvolatilityhistory) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-194) [fetchWithdrawal](https://docs.ccxt.com/docs/base-spec#fetchwithdrawal) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-195) [fetchWithdrawalWhitelist](https://docs.ccxt.com/docs/base-spec#fetchwithdrawalwhitelist) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-196) [fetchWithdrawals](https://docs.ccxt.com/docs/base-spec#fetchwithdrawals) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-197) [fetchWithdrawalsWs](https://docs.ccxt.com/docs/base-spec#fetchwithdrawalsws) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-198) [isUTAEnabled](https://docs.ccxt.com/docs/base-spec#isutaenabled) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-199) [isUnifiedEnabled](https://docs.ccxt.com/docs/base-spec#isunifiedenabled) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-200) [loadMigrationStatus](https://docs.ccxt.com/docs/base-spec#loadmigrationstatus) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-201) [loadUnifiedStatus](https://docs.ccxt.com/docs/base-spec#loadunifiedstatus) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-202) [market](https://docs.ccxt.com/docs/base-spec#market) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-203) [preLoadLighterLibrary](https://docs.ccxt.com/docs/base-spec#preloadlighterlibrary) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-204) [redeemGiftCode](https://docs.ccxt.com/docs/base-spec#redeemgiftcode) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-205) [reduceMargin](https://docs.ccxt.com/docs/base-spec#reducemargin) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-206) [repayCrossMargin](https://docs.ccxt.com/docs/base-spec#repaycrossmargin) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-207) [repayIsolatedMargin](https://docs.ccxt.com/docs/base-spec#repayisolatedmargin) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-208) [repayMargin](https://docs.ccxt.com/docs/base-spec#repaymargin) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-209) [reserveRequestWeight](https://docs.ccxt.com/docs/base-spec#reserverequestweight) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-210) [setAgentAbstraction](https://docs.ccxt.com/docs/base-spec#setagentabstraction) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-211) [setContractLeverage](https://docs.ccxt.com/docs/base-spec#setcontractleverage) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-212) [setLeverage](https://docs.ccxt.com/docs/base-spec#setleverage) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-213) [setMargin](https://docs.ccxt.com/docs/base-spec#setmargin) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-214) [setMarginMode](https://docs.ccxt.com/docs/base-spec#setmarginmode) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-215) [setPositionMode](https://docs.ccxt.com/docs/base-spec#setpositionmode) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-216) [setSandboxMode](https://docs.ccxt.com/docs/base-spec#setsandboxmode) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-217) [setUserAbstraction](https://docs.ccxt.com/docs/base-spec#setuserabstraction) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-218) [signIn](https://docs.ccxt.com/docs/base-spec#signin) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-219) [transfer](https://docs.ccxt.com/docs/base-spec#transfer) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-220) [transferClassic](https://docs.ccxt.com/docs/base-spec#transferclassic) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-221) [transferOut](https://docs.ccxt.com/docs/base-spec#transferout) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-222) [transferUta](https://docs.ccxt.com/docs/base-spec#transferuta) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-223) [unWatchBalance](https://docs.ccxt.com/docs/base-spec#unwatchbalance) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-224) [unWatchBidsAsks](https://docs.ccxt.com/docs/base-spec#unwatchbidsasks) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-225) [unWatchFundingRate](https://docs.ccxt.com/docs/base-spec#unwatchfundingrate) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-226) [unWatchMarkPrice](https://docs.ccxt.com/docs/base-spec#unwatchmarkprice) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-227) [unWatchMarkPrices](https://docs.ccxt.com/docs/base-spec#unwatchmarkprices) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-228) [unWatchMyTrades](https://docs.ccxt.com/docs/base-spec#unwatchmytrades) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-229) [unWatchOHLCV](https://docs.ccxt.com/docs/base-spec#unwatchohlcv) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-230) [unWatchOHLCVForSymbols](https://docs.ccxt.com/docs/base-spec#unwatchohlcvforsymbols) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-231) [unWatchOrderBook](https://docs.ccxt.com/docs/base-spec#unwatchorderbook) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-232) [unWatchOrderBookForSymbols](https://docs.ccxt.com/docs/base-spec#unwatchorderbookforsymbols) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-233) [unWatchOrders](https://docs.ccxt.com/docs/base-spec#unwatchorders) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-234) [unWatchPositions](https://docs.ccxt.com/docs/base-spec#unwatchpositions) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-235) [unWatchTicker](https://docs.ccxt.com/docs/base-spec#unwatchticker) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-236) [unWatchTickers](https://docs.ccxt.com/docs/base-spec#unwatchtickers) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-237) [unWatchTrades](https://docs.ccxt.com/docs/base-spec#unwatchtrades) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-238) [unWatchTradesForSymbols](https://docs.ccxt.com/docs/base-spec#unwatchtradesforsymbols) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-239) [upgradeUnifiedTradeAccount](https://docs.ccxt.com/docs/base-spec#upgradeunifiedtradeaccount) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-240) [verifyGiftCode](https://docs.ccxt.com/docs/base-spec#verifygiftcode) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-241) [watchBalance](https://docs.ccxt.com/docs/base-spec#watchbalance) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-242) [watchBidsAsks](https://docs.ccxt.com/docs/base-spec#watchbidsasks) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-243) [watchFundingRate](https://docs.ccxt.com/docs/base-spec#watchfundingrate) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-244) [watchFundingRates](https://docs.ccxt.com/docs/base-spec#watchfundingrates) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-245) [watchLiquidations](https://docs.ccxt.com/docs/base-spec#watchliquidations) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-246) [watchLiquidationsForSymbols](https://docs.ccxt.com/docs/base-spec#watchliquidationsforsymbols) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-247) [watchMarkPrice](https://docs.ccxt.com/docs/base-spec#watchmarkprice) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-248) [watchMarkPrices](https://docs.ccxt.com/docs/base-spec#watchmarkprices) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-249) [watchMyLiquidations](https://docs.ccxt.com/docs/base-spec#watchmyliquidations) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-250) [watchMyLiquidationsForSymbols](https://docs.ccxt.com/docs/base-spec#watchmyliquidationsforsymbols) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-251) [watchMyTrades](https://docs.ccxt.com/docs/base-spec#watchmytrades) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-252) [watchOHLCV](https://docs.ccxt.com/docs/base-spec#watchohlcv) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-253) [watchOHLCVForSymbols](https://docs.ccxt.com/docs/base-spec#watchohlcvforsymbols) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-254) [watchOrderBook](https://docs.ccxt.com/docs/base-spec#watchorderbook) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-255) [watchOrderBookForSymbols](https://docs.ccxt.com/docs/base-spec#watchorderbookforsymbols) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-256) [watchOrders](https://docs.ccxt.com/docs/base-spec#watchorders) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-257) [watchOrdersForSymbols](https://docs.ccxt.com/docs/base-spec#watchordersforsymbols) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-258) [watchPosition](https://docs.ccxt.com/docs/base-spec#watchposition) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-259) [watchPositions](https://docs.ccxt.com/docs/base-spec#watchpositions) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-260) [watchTicker](https://docs.ccxt.com/docs/base-spec#watchticker) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-261) [watchTickers](https://docs.ccxt.com/docs/base-spec#watchtickers) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-262) [watchTrades](https://docs.ccxt.com/docs/base-spec#watchtrades) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-263) [watchTradesForSymbols](https://docs.ccxt.com/docs/base-spec#watchtradesforsymbols) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-264) [withdraw](https://docs.ccxt.com/docs/base-spec#withdraw) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-265) [withdrawWs](https://docs.ccxt.com/docs/base-spec#withdrawws) [Supported exchanges](https://docs.ccxt.com/docs/base-spec#supported-exchanges-266)