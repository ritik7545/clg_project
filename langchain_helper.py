
import os
import logging
from dotenv import load_dotenv
from urllib.parse import quote_plus

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.prompts import SemanticSimilarityExampleSelector
from langchain.embeddings import HuggingFaceEmbeddings

from langchain.prompts import FewShotPromptTemplate
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX
from langchain.prompts.prompt import PromptTemplate
from few_shots import few_shots
from langchain_core.caches import BaseCache  
 
from langchain_core.callbacks import Callbacks
from langchain_core.caches import InMemoryCache
from langchain_community.vectorstores import Chroma




load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MyCache(BaseCache):
    """Custom cache for SQLDatabaseChain."""
    pass  

SQLDatabaseChain.model_rebuild()

def get_few_shot_db_chain():
    try:
        db_user = os.getenv("DB_USER", "ritik")
        db_password = os.getenv("DB_PASSWORD", "ritiksaras")  
        db_host = os.getenv("DB_HOST", "localhost")
        db_name = os.getenv("DB_NAME", "retail_sales_db")
        google_api_key = os.getenv("GOOGLE_API_KEY")

        if not google_api_key:
            raise ValueError("GOOGLE_API_KEY is missing. Please set it in your environment variables.")

        password = quote_plus(db_password)

        try:
            import pymysql
        except ImportError:
            raise ImportError("pymysql module is missing. Install it using `pip install pymysql`.")

        connection_string = f"mysql+pymysql://{db_user}:{password}@{db_host}/{db_name}"
        db = SQLDatabase.from_uri(connection_string, sample_rows_in_table_info=3)

        llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=google_api_key, temperature=0.1)


        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={"device": "cpu"},
            encode_kwargs={"normalize_embeddings": True}
        )

        to_vectorize = [" ".join(str(v) for v in example.values()) for example in few_shots]

        persist_directory = "db"
        os.makedirs(persist_directory, exist_ok=True)

        vectorstore = Chroma.from_texts(
            texts=to_vectorize,
            embedding=embeddings,
            metadatas=few_shots,
            persist_directory=persist_directory
        )

        example_selector = SemanticSimilarityExampleSelector(
            vectorstore=vectorstore,
            k=2
        )

        mysql_prompt = """You are a MySQL expert. Given an input question, generate the best SQL query..."""

        example_prompt = PromptTemplate(
            input_variables=["Question", "SQLQuery", "SQLResult", "Answer"],
            template="\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}"
        )

        few_shot_prompt = FewShotPromptTemplate(
            example_selector=example_selector,
            example_prompt=example_prompt,
            prefix=mysql_prompt,
            suffix=PROMPT_SUFFIX,
            input_variables=["input", "table_info", "top_k"]
        )

        chain = SQLDatabaseChain.from_llm(
                llm=llm,
                db=db,
                verbose=True,
                prompt=few_shot_prompt  
        )

        logger.info("SQLDatabaseChain successfully initialized.")
        return chain

    except Exception as e:
        logger.error(f"Error in get_few_shot_db_chain: {str(e)}", exc_info=True)
        raise
