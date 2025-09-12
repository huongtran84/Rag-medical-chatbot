from langchain_community.vectorstores import FAISS
from app.common.logger import get_logger
from app.common.custom_exception import CustomException
from app.config.config import DB_FAISS_PATH
from app.components.embedings import get_embedding_model

logger = get_logger(__name__)

def load_vector_store():
    try:
        logger.info("Loading FAISS vector store from disk")
        embedding_model = get_embedding_model()
        if isinstance(embedding_model, str):
            raise CustomException(f"Embedding model initialization failed: {embedding_model}")
        vector_store = FAISS.load_local(DB_FAISS_PATH, embedding_model,allow_dangerous_deserialization=True)
        logger.info("FAISS vector store loaded successfully")
        return vector_store
    except Exception as e:
        error_message = f"Failed to load FAISS vector store: {str(e)}"
        logger.error(str(error_message))
        return None

def save_vector_store(text_chunks):
    try:
        if not text_chunks:
            raise CustomException("No text chunks provided to save to vector store.")
        logger.info("Creating and saving FAISS vector store to disk")
        embedding_model = get_embedding_model()
        if isinstance(embedding_model, str):
            raise CustomException(f"Embedding model initialization failed: {embedding_model}")
        vector_store = FAISS.from_documents(text_chunks, embedding_model)
        vector_store.save_local(DB_FAISS_PATH)
        logger.info(f"FAISS vector store saved successfully at {DB_FAISS_PATH}")
        return vector_store
    except Exception as e:
        error_message = f"Failed to save FAISS vector store: {str(e)}"
        logger.error(str(error_message))
        return None