import pyupbit
import keys

upbit = pyupbit.Upbit(keys.access, keys.secret)

print(upbit.get_balance("KRW-DOGE"))
# print(upbit.get_balance("KRW-BTT"))
# print(upbit.get_balance("KRW"))
# print(pyupbit.get_tickers())
# print(pyupbit.get_tickers(fiat="KRW"))
print(pyupbit.get_current_price("KRW-DOGE"))

df = pyupbit.get_ohlcv("KRW-DOGE")
print(df.tail())