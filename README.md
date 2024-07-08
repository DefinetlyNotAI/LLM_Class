# LLM_Class 📎

Welcome to `LLM_Class` 🌐,
Crafted with python and Hugging Face 🐍, by DefinetlyNotAI 🤗.
This comprehensive guide is here to equip you with everything you need to use `LLM_Class` effectively.

<div align="center">
    <a href="https://github.com/DefinetlyNotAI/LLM_Class/issues"><img src="https://img.shields.io/github/issues/DefinetlyNotAI/LLM_Class" alt="GitHub Issues"></a>
    <a href="https://github.com/DefinetlyNotAI/LLM_Class/tags"><img src="https://img.shields.io/github/v/tag/DefinetlyNotAI/LLM_Class" alt="GitHub Tag"></a>
    <a href="https://github.com/DefinetlyNotAI/LLM_Class/graphs/commit-activity"><img src="https://img.shields.io/github/commit-activity/t/DefinetlyNotAI/LLM_Class" alt="GitHub Commit Activity"></a>
    <a href="https://github.com/DefinetlyNotAI/LLM_Class/languages"><img src="https://img.shields.io/github/languages/count/DefinetlyNotAI/LLM_Class" alt="GitHub Language Count"></a>
    <a href="https://github.com/DefinetlyNotAI/LLM_Class/actions"><img src="https://img.shields.io/github/check-runs/DefinetlyNotAI/LLM_Class/main" alt="GitHub Branch Check Runs"></a>
    <a href="https://github.com/DefinetlyNotAI/LLM_Class"><img src="https://img.shields.io/github/repo-size/DefinetlyNotAI/LLM_Class" alt="GitHub Repo Size"></a>
</div>

# LLM_Class

The `LLM_Class` is a Python class designed to provide financial market insights through
various functionalities including retrieving stock news,
fetching historical stock data, generating text based on prompts,
and analyzing the sentiment of given texts as well as act like a basic language model.
It leverages external libraries such as `requests`, `BeautifulSoup`, `yfinance`, and `transformers` 
from Hugging Face to perform these tasks efficiently.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed Python 3.8 or later.
- You have installed the required Python packages from the [requirements.ps1](requirements.ps1) file.
- You are using windows
- You have at least 6GB of Storage available
- You have a dedicated nvidea GPU supporting CUDA 11.8

## Installation

If you plan to modify or extend the functionality of the `LLM_Class`, clone the repository and install the required packages locally.

```bash
git clone https://github.com/DefinetlyNotAI/LLM_Class.git
cd LLM_Class
.\requirements.ps1
```

## Usage

### Initialization

First, import the `LLM_Class` class and create an instance of it:

```python
from LLM import LLM

llm = LLM()
```

### Getting Stock News

To retrieve the latest news headlines for a specific stock ticker, use the `get_stock_news` method:

```python
news_headlines = llm.get_stock_news('AAPL')
print("News Headlines:", news_headlines)
```

This is the most unsupported feature of the `LLM_Class`.

### Fetching Historical Stock Data

To fetch historical stock data for a given ticker symbol over the past year, use the `get_stock_data` method:

```python
stock_data = llm.get_stock_data('AAPL')
print(stock_data)
```

### Generating Text

To generate text based on a given prompt using a customizable text generation pipeline, 
use the `generate_text` method:

```python
generated_text = llm.generate_text(prompt="What is the future of AI in finance?")
print(generated_text)
```

### Analyzing Sentiment

To analyze the sentiment of a given text, use the `analyze_sentiment` method:

```python
sentiment = llm.analyze_sentiment(text="The stock market is volatile today.")
print(sentiment)
```

## Contributing

Contributions are what make the open-source community such an amazing place to learn,
inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

But don't hesitate to [open an Issue](https://github.com/DefinetlyNotAI/LLM_Class/issues) 
if you have any questions or encounter any issues.

Most importantly, **don't forget to follow us!** and read our [Contributing Guide](CONTRIBUTING.md).

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

## Contact

Shahm Najeeb - Nirt_12023@outlook.com

Project Link: [https://github.com/DefinetlyNotAI/LLM_Class](https://github.com/DefinetlyNotAI/LLM_Class)
