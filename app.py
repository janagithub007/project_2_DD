import os
import pandas as pd
import streamlit as st
import plotly.express as px


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Data-Driven Stock Analysis",
    page_icon="📈",
    layout="wide"
)


# ============================================================
# FILE PATHS
# ============================================================



APP_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FOLDER = os.path.join(APP_DIR, "powerbi_data")

MARKET_FILE = os.path.join(DATA_FOLDER, "stock_market_data.csv")
SUMMARY_FILE = os.path.join(DATA_FOLDER, "stock_summary.csv")
CUMULATIVE_FILE = os.path.join(DATA_FOLDER, "cumulative_returns.csv")
GAINERS_FILE = os.path.join(DATA_FOLDER, "monthly_top_5_gainers.csv")
LOSERS_FILE = os.path.join(DATA_FOLDER, "monthly_top_5_loosers.csv")
CORRELATION_FILE = os.path.join(DATA_FOLDER, "correlation_long.csv")


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():

    market = pd.read_csv(MARKET_FILE)
    summary = pd.read_csv(SUMMARY_FILE)
    cumulative = pd.read_csv(CUMULATIVE_FILE)
    gainers = pd.read_csv(GAINERS_FILE)
    losers = pd.read_csv(LOSERS_FILE)
    correlation = pd.read_csv(CORRELATION_FILE)

    market["date"] = pd.to_datetime(market["date"])
    cumulative["date"] = pd.to_datetime(cumulative["date"])

    return (
        market,
        summary,
        cumulative,
        gainers,
        losers,
        correlation
    )


(
    df,
    stock_summary,
    cumulative_df,
    monthly_gainers,
    monthly_losers,
    correlation_long
) = load_data()


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("📊 Dashboard Navigation")

page = st.sidebar.radio(
    "Select Page",
    [
        "Market Overview",
        "Stock Analysis",
        "Monthly Analysis",
        "Correlation Analysis",
        "Power BI Dashboard",
        "About"
    ]
)


# ============================================================
# MAIN TITLE
# ============================================================

st.title("📈 Data-Driven Stock Analysis")

st.caption(
    "Interactive analysis of stock market performance, "
    "returns, volatility, sectors and correlations."
)

st.divider()


# ============================================================
# PAGE 1 - MARKET OVERVIEW
# ============================================================

if page == "Market Overview":

    st.header("📊 Market Overview")

    # ---------------- KPI CALCULATIONS ----------------

    green_count = (
        stock_summary["Yearly_Return"] > 0
    ).sum()

    red_count = (
        stock_summary["Yearly_Return"] < 0
    ).sum()

    total_stocks = stock_summary["Ticker"].nunique()

    average_price = df["close"].mean()

    average_volume = df["volume"].mean()


    # ---------------- KPI CARDS ----------------

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric(
        "Total Stocks",
        total_stocks
    )

    col2.metric(
        "Green Stocks",
        green_count
    )

    col3.metric(
        "Red Stocks",
        red_count
    )

    col4.metric(
        "Average Price",
        f"{average_price:,.2f}"
    )

    col5.metric(
        "Average Volume",
        f"{average_volume:,.0f}"
    )

    st.divider()


    # ========================================================
    # TOP / BOTTOM STOCKS
    # ========================================================

    left, right = st.columns(2)


    # ---------------- TOP 10 ----------------

    with left:

        st.subheader("🟢 Top 10 Performing Stocks")

        top_10 = (
            stock_summary
            .sort_values(
                "Yearly_Return",
                ascending=False
            )
            .head(10)
        )

        fig_top = px.bar(
            top_10,
            x="Yearly_Return",
            y="Ticker",
            orientation="h",
            text_auto=".2%",
            title="Top 10 Stocks by Yearly Return"
        )

        fig_top.update_layout(
            yaxis={
                "categoryorder": "total ascending"
            },
            xaxis_tickformat=".0%"
        )

        st.plotly_chart(
            fig_top,
            use_container_width=True
        )


    # ---------------- BOTTOM 10 ----------------

    with right:

        st.subheader("🔴 Bottom 10 Performing Stocks")

        bottom_10 = (
            stock_summary
            .sort_values(
                "Yearly_Return",
                ascending=True
            )
            .head(10)
        )

        fig_bottom = px.bar(
            bottom_10,
            x="Yearly_Return",
            y="Ticker",
            orientation="h",
            text_auto=".2%",
            title="Bottom 10 Stocks by Yearly Return"
        )

        fig_bottom.update_layout(
            yaxis={
                "categoryorder": "total descending"
            },
            xaxis_tickformat=".0%"
        )

        st.plotly_chart(
            fig_bottom,
            use_container_width=True
        )


    # ========================================================
    # VOLATILITY
    # ========================================================

    st.divider()

    st.header("⚡ Volatility Analysis")

    if "daily_return" not in df.columns:

        df = df.sort_values(
            ["Ticker", "date"]
        )

        df["daily_return"] = (
            df.groupby("Ticker")["close"]
            .pct_change()
        )


    volatility_df = (
        df.groupby("Ticker")["daily_return"]
        .std()
        .reset_index(name="Volatility")
    )


    top_volatility = (
        volatility_df
        .sort_values(
            "Volatility",
            ascending=False
        )
        .head(10)
    )


    fig_volatility = px.bar(
        top_volatility,
        x="Ticker",
        y="Volatility",
        text_auto=".2%",
        title="Top 10 Highly Volatile Stocks"
    )

    fig_volatility.update_layout(
        yaxis_tickformat=".0%"
    )

    st.plotly_chart(
        fig_volatility,
        use_container_width=True
    )


    # ========================================================
    # SECTOR PERFORMANCE
    # ========================================================

    st.divider()

    st.header("🏢 Sector-wise Performance")

    sector_performance = (
        stock_summary
        .groupby("Sector")["Yearly_Return"]
        .mean()
        .sort_values(ascending=False)
        .reset_index()
    )


    fig_sector = px.bar(
        sector_performance,
        x="Sector",
        y="Yearly_Return",
        text_auto=".2%",
        title="Average Yearly Return by Sector"
    )

    fig_sector.update_layout(
        yaxis_tickformat=".0%"
    )

    st.plotly_chart(
        fig_sector,
        use_container_width=True
    )


# ============================================================
# PAGE 2 - INDIVIDUAL STOCK ANALYSIS
# ============================================================

elif page == "Stock Analysis":

    st.header("📈 Individual Stock Analysis")


    # ---------------- STOCK SELECTOR ----------------

    ticker_list = sorted(
        df["Ticker"].dropna().unique()
    )

    selected_ticker = st.selectbox(
        "Select a Stock",
        ticker_list
    )


    selected_stock = (
        df[
            df["Ticker"] == selected_ticker
        ]
        .sort_values("date")
        .copy()
    )


    selected_summary = stock_summary[
        stock_summary["Ticker"] == selected_ticker
    ]


    # ========================================================
    # STOCK KPIs
    # ========================================================

    first_price = selected_stock.iloc[0]["close"]
    last_price = selected_stock.iloc[-1]["close"]

    yearly_return = (
        last_price - first_price
    ) / first_price


    if "daily_return" not in selected_stock.columns:

        selected_stock["daily_return"] = (
            selected_stock["close"]
            .pct_change()
        )


    volatility = (
        selected_stock["daily_return"]
        .std()
    )


    k1, k2, k3, k4 = st.columns(4)

    k1.metric(
        "First Close",
        f"{first_price:,.2f}"
    )

    k2.metric(
        "Latest Close",
        f"{last_price:,.2f}"
    )

    k3.metric(
        "Yearly Return",
        f"{yearly_return:.2%}"
    )

    k4.metric(
        "Volatility",
        f"{volatility:.2%}"
    )


    # ========================================================
    # PRICE TREND
    # ========================================================

    st.subheader(
        f"Price Trend - {selected_ticker}"
    )


    fig_price = px.line(
        selected_stock,
        x="date",
        y="close",
        title=f"{selected_ticker} Closing Price Trend"
    )


    st.plotly_chart(
        fig_price,
        use_container_width=True
    )


    # ========================================================
    # CUMULATIVE RETURN
    # ========================================================

    st.subheader(
        f"Cumulative Return - {selected_ticker}"
    )


    selected_cumulative = cumulative_df[
        cumulative_df["Ticker"]
        == selected_ticker
    ].sort_values("date")


    fig_cumulative = px.line(
        selected_cumulative,
        x="date",
        y="cumulative_return",
        title=f"{selected_ticker} Cumulative Return"
    )


    fig_cumulative.update_layout(
        yaxis_tickformat=".0%"
    )


    st.plotly_chart(
        fig_cumulative,
        use_container_width=True
    )


    # ========================================================
    # SIMPLE DYNAMIC INSIGHT
    # ========================================================

    st.subheader("💡 Stock Insight")

    if yearly_return > 0:

        st.success(
            f"{selected_ticker} gained "
            f"{yearly_return:.2%} during the analysis period."
        )

    elif yearly_return < 0:

        st.error(
            f"{selected_ticker} declined "
            f"{abs(yearly_return):.2%} during the analysis period."
        )

    else:

        st.info(
            f"{selected_ticker} showed no major overall change."
        )


    st.info(
        f"Volatility of {selected_ticker}: "
        f"{volatility:.2%}. "
        "Higher volatility indicates larger fluctuations "
        "in daily returns."
    )


# ============================================================
# PAGE 3 - MONTHLY ANALYSIS
# ============================================================

elif page == "Monthly Analysis":

    st.header("📅 Monthly Top Gainers & Losers")


    available_months = sorted(
        monthly_gainers["month"]
        .dropna()
        .unique()
    )


    selected_month = st.selectbox(
        "Select Month",
        available_months
    )


    month_gainers = monthly_gainers[
        monthly_gainers["month"]
        == selected_month
    ].sort_values(
        "Monthly_Return",
        ascending=False
    )


    month_losers = monthly_losers[
        monthly_losers["month"]
        == selected_month
    ].sort_values(
        "Monthly_Return",
        ascending=True
    )


    left, right = st.columns(2)


    # ---------------- GAINERS ----------------

    with left:

        st.subheader(
            f"🟢 Top 5 Gainers - {selected_month}"
        )


        fig_gainers = px.bar(
            month_gainers,
            x="Ticker",
            y="Monthly_Return",
            text_auto=".2%"
        )


        fig_gainers.update_layout(
            yaxis_tickformat=".0%"
        )


        st.plotly_chart(
            fig_gainers,
            use_container_width=True
        )


    # ---------------- LOSERS ----------------

    with right:

        st.subheader(
            f"🔴 Top 5 Losers - {selected_month}"
        )


        fig_losers = px.bar(
            month_losers,
            x="Ticker",
            y="Monthly_Return",
            text_auto=".2%"
        )


        fig_losers.update_layout(
            yaxis_tickformat=".0%"
        )


        st.plotly_chart(
            fig_losers,
            use_container_width=True
        )


    # ========================================================
    # MONTHLY TABLES
    # ========================================================

    st.divider()

    t1, t2 = st.columns(2)

    with t1:

        st.write("### Top 5 Gainers Data")

        display_gainers = (
            month_gainers[
                ["Ticker", "Monthly_Return"]
            ]
            .copy()
        )

        display_gainers["Monthly_Return"] = (
            display_gainers["Monthly_Return"]
            .map(lambda x: f"{x:.2%}")
        )

        st.dataframe(
            display_gainers,
            use_container_width=True,
            hide_index=True
        )


    with t2:

        st.write("### Top 5 Losers Data")

        display_losers = (
            month_losers[
                ["Ticker", "Monthly_Return"]
            ]
            .copy()
        )

        display_losers["Monthly_Return"] = (
            display_losers["Monthly_Return"]
            .map(lambda x: f"{x:.2%}")
        )

        st.dataframe(
            display_losers,
            use_container_width=True,
            hide_index=True
        )


# ============================================================
# PAGE 4 - CORRELATION ANALYSIS
# ============================================================

elif page == "Correlation Analysis":

    st.header("🔥 Stock Correlation Analysis")

    st.write(
        """
        Correlation measures how closely the price movements
        of two stocks are related.

        **+1:** Strong positive relationship  
        **0:** Little or no linear relationship  
        **-1:** Strong negative relationship
        """
    )


    # ========================================================
    # CREATE MATRIX FROM LONG FORMAT
    # ========================================================

    correlation_matrix = (
        correlation_long
        .pivot(
            index="Ticker",
            columns="Ticker_2",
            values="Correlation"
        )
    )


    fig_corr = px.imshow(
        correlation_matrix,
        zmin=-1,
        zmax=1,
        color_continuous_scale="RdYlGn",
        aspect="auto",
        title="Stock Correlation Heatmap"
    )


    fig_corr.update_layout(
        height=850
    )


    st.plotly_chart(
        fig_corr,
        use_container_width=True
    )


    st.info(
        "Stocks with correlation values closer to +1 tend "
        "to move in a similar direction, while values closer "
        "to -1 indicate opposite movements."
    )
elif page == "Power BI Dashboard":

    st.header("📊 Power BI Dashboard")

    st.write(
        """
        The following dashboards were developed using Microsoft Power BI
        as part of the Data-Driven Stock Analysis project.
        """
    )

    # Get the folder where app.py is located
    APP_DIR = os.path.dirname(os.path.abspath(__file__))

    page1_image = os.path.join(
        APP_DIR,
        "powerbi_images",
        "powerbi_page1.png"
    )

    page2_image = os.path.join(
        APP_DIR,
        "powerbi_images",
        "powerbi_page2.png"
    )

    st.subheader("Page 1 - Market Overview")

    st.image(
        page1_image,
        caption="Power BI - Market Overview",
        use_container_width=True
    )

    st.write(
        """
        The Market Overview dashboard presents total stocks,
        green and red stocks, average price, average volume,
        top and bottom performers, sector-wise performance
        and volatility analysis.
        """
    )

    st.divider()

    st.subheader("Page 2 - Detailed Analysis")

    st.image(
        page2_image,
        caption="Power BI - Detailed Analysis",
        use_container_width=True
    )

    st.write(
        """
        The Detailed Analysis dashboard presents stock price trends,
        cumulative returns, monthly top gainers and losers,
        and stock correlation analysis.
        """
    )
# ============================================================
# PAGE 5 - ABOUT / DEFINITIONS
# ============================================================

elif page == "About":

    st.header("📘 About the Project")

    st.write(
        """
        This project analyzes historical stock market data
        to identify market trends, stock performance,
        volatility, cumulative returns, sector performance,
        monthly gainers and losers, and relationships
        between stocks.
        """
    )


    st.subheader("📌 Key Definitions")


    with st.expander("What is Yearly Return?"):

        st.write(
            """
            Yearly Return measures the percentage change
            between the first closing price and the final
            closing price of a stock during the analysis period.
            """
        )


    with st.expander("What is Daily Return?"):

        st.write(
            """
            Daily Return measures the percentage change in
            a stock's closing price compared with the
            previous trading day.
            """
        )


    with st.expander("What is Volatility?"):

        st.write(
            """
            Volatility measures how much a stock's returns
            fluctuate. In this project, volatility is measured
            using the standard deviation of daily returns.

            Higher volatility means larger price fluctuations.
            """
        )


    with st.expander("What is Cumulative Return?"):

        st.write(
            """
            Cumulative Return represents the total compounded
            return generated by a stock over the analysis period.
            """
        )


    with st.expander("What is Correlation?"):

        st.write(
            """
            Correlation measures the relationship between
            the price movements of two stocks.

            A value near +1 indicates similar movement,
            while a value near -1 indicates opposite movement.
            """
        )


    with st.expander("What are Green and Red Stocks?"):

        st.write(
            """
            Green Stocks have positive returns over the
            analysis period.

            Red Stocks have negative returns over the
            analysis period.
            """
        )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Data-Driven Stock Analysis | "
    "Python • Pandas • Streamlit • Power BI"
)