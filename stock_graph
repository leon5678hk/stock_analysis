import matplotlib.pyplot as plt
import pandas as pd

def make_graph(data, company_name):
    data['Date'] = pd.to_datetime(data['Date'])

    # stock price data
    plt.figure(figsize=(12, 6))
    plt.plot(data['Date'], data['Close'], label='Stock Price', color='blue', linewidth=2)

    # title and labels
    plt.title(f"{company_name} Stock Price Over Time", fontsize=16)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Stock Price (USD)', fontsize=12)
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Display
    plt.tight_layout()
    plt.show()

make_graph(tesla_data, 'Tesla')
make_graph(gme_data, 'Tesla')
