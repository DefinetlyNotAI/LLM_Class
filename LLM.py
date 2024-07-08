import logging
from transformers import pipeline, set_seed
import random
import yfinance as yf
from bs4 import BeautifulSoup
import requests


class LLM:
    def __init__(self):
        """
        Initializes the object and sets up the logger.

        Parameters:
            self (object): The instance of the class.

        Returns:
            None
        """
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(
            level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
        )

    def get_stock_headline(self, Company_Code):
        """
        Retrieves the headlines of news articles related to a given stock ticker.

        Args:
            Company_Code (str): The stock ticker symbol.

        Returns:
            list: A list of strings representing the headlines of the news articles.

        Raises:
            requests.exceptions.RequestException: If there is an error making the HTTP request.
        """
        url = f"https://finance.yahoo.com/quote/{Company_Code}?p={Company_Code}&.tsrc=fin-srch"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Check for HTTP errors
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Error fetching stock news: {e}")
            raise

        soup = BeautifulSoup(response.text, "html.parser")
        headlines = [
            headline.text for headline in soup.find_all("h3", class_="Mb(5px)")
        ]
        return headlines

    def get_stock_history(self, Company_Code):
        """
        Retrieves historical stock data for a given ticker symbol.

        Parameters:
            Company_Code (str): The ticker symbol of the stock.

        Returns:
            pandas.DataFrame: The historical stock data for the given ticker symbol.
        """
        try:
            stock = yf.Ticker(Company_Code)
            data = stock.history(period="1y")
            return data
        except Exception as e:
            self.logger.error(f"Error fetching stock data: {e}")
            raise

    def complete_text(
        self,
        prompt="What",
        seed=random.randint(1, 1000),
        model="gpt2",
        revision=None,
        device=-1,
        max_length=100,
        min_length=30,
        do_sample=True,
        temperature=0.7,
        top_k=50,
        top_p=0.95,
        num_return_sequences=1,
        truncation=True,
    ):
        """
        Generate text based on a given prompt using a customizable text generation pipeline, Basically
        Continues on the prompt given.

        Parameters:
            prompt (str): The starting sentence or prompt for text generation.
            model (str): The model identifier from Hugging Face Model Hub.
            revision (str, optional): The revision of the model to use. Defaults to None.
            device (int): Device to run the model on. -1 for GPU, 0 for CPU. Defaults to -1.
            max_length (int): Maximum length of the sequence to be generated.
            min_length (int, optional): Minimum length of the sequence to be generated. Defaults to None.
            do_sample (bool): Whether to sample the tokens randomly. Defaults to True.
            temperature (float): Controls the randomness of predictions. Higher values result in more random outputs. Defaults to 0.7.
            top_k (int): Number of highest probability vocabulary tokens to keep for top-k filtering. Defaults to 50.
            top_p (float): Cumulative probability of parameter tokens to keep for nucleus sampling. Defaults to 0.95.
            num_return_sequences (int): The number of independently computed sequences to generate. Defaults to 1.
            truncation (bool): Whether to truncate the generated text. Defaults to True.
            seed (int): Seed value for reproducibility. Defaults to 42.

        Returns:
            str: The generated text based on the prompt.
        """
        # Validate parameters
        if not isinstance(prompt, str) or not prompt.strip():
            raise ValueError("Prompt cannot be empty.")
        if not isinstance(model, str) or not model.strip():
            raise ValueError("Model name cannot be empty.")

        # Initialize the text generation pipeline with the specified options
        try:
            text_generator = pipeline(
                "text-generation", model=model, revision=revision, device=device
            )
        except Exception as e:
            self.logger.error(f"Failed to initialize the text generator: {e}")
            raise

        # Set seed for reproducibility
        set_seed(seed)

        # Generate text based on the prompt and specified parameters
        try:
            generated_text = text_generator(
                prompt,
                max_length=max_length,
                min_length=min_length,
                do_sample=do_sample,
                temperature=temperature,
                top_k=top_k,
                top_p=top_p,
                num_return_sequences=num_return_sequences,
                truncation=truncation,
            )
        except Exception as e:
            self.logger.error(f"Failed to generate text: {e}")
            raise

        # Return the generated text
        return generated_text[0][
            "generated_text"
        ]  # Assuming the output is a list of dictionaries

    @staticmethod
    def analyze_sentiment(
        text, model="distilbert-base-uncased-finetuned-sst-2-english", device=-1
    ):
        """
        Analyzes the sentiment of the given text using the sentiment-analysis pipeline.

        Parameters and Returns are the same as in the original function.
        """
        # Initialize the sentiment analysis pipeline with the specified options
        sentiment_analyzer = pipeline("sentiment-analysis", model=model, device=device)

        # Perform sentiment analysis on the text
        result = sentiment_analyzer(text)[
            0
        ]  # We take the first result since sentiment analysis usually returns a single prediction

        # Return the sentiment label
        return result["label"]


# Example usage:
llm = LLM()
llm.complete_text("Test_Text", max_length=100, min_length=50)
llm.get_stock_headline("AAPL")
llm.get_stock_history("AAPL")
llm.analyze_sentiment("Test_Text")
