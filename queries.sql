USE stock_analysis;

-- 1. Check total number of records
SELECT COUNT(*) AS total_records
FROM stock_data;

-- 2. Check total number of stocks
SELECT COUNT(DISTINCT Ticker) AS total_stocks
FROM stock_data;

-- 3. Average closing price and trading volume
SELECT
    AVG(close) AS average_price,
    AVG(volume) AS average_volume
FROM stock_data;

-- 4. Average closing price for each stock
SELECT
    Ticker,
    AVG(close) AS average_close_price
FROM stock_data
GROUP BY Ticker
ORDER BY average_close_price DESC;

-- 5. Average trading volume for each stock
SELECT
    Ticker,
    AVG(volume) AS average_volume
FROM stock_data
GROUP BY Ticker
ORDER BY average_volume DESC;

-- 6. Highest daily return
SELECT
    Ticker,
    date,
    daily_return
FROM stock_data
WHERE daily_return IS NOT NULL
ORDER BY daily_return DESC
LIMIT 10;

-- 7. Highest volatility stocks
SELECT
    Ticker,
    STDDEV_SAMP(daily_return) AS volatility
FROM stock_data
WHERE daily_return IS NOT NULL
GROUP BY Ticker
ORDER BY volatility DESC
LIMIT 10;

-- 8. View sample stock data
SELECT *
FROM stock_data
LIMIT 10;