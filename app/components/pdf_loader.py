import os
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from app.config.config import DATA_PATH, CHUNK_SIZE, CHUNK_OVERLAP
from app.common.logger import get_logger
from app.common.custom_exception import CustomException


logger = get_logger(__name__)

def load_pdf_files(data_path=DATA_PATH):
    try:
        if not os.path.exists(data_path):
            raise CustomException(f"The specified data path does not exist: {data_path}")
        logger.info(f"Loading PDF files from directory: {data_path}")
        loader = DirectoryLoader(data_path, glob="**/*.pdf", loader_cls=PyPDFLoader)
        documents = loader.load()
        if not documents:
            logger.warning
        logger.info(f"Loaded {len(documents)} documents from {data_path}")
        return documents
    except Exception as e:
        error_message = f"Failed to load PDF files from {data_path}: {str(e)}"
        logger.error(str(error_message))
        return []

def create_text_chunks(documents, chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP):
    try:
        if not documents:
            raise CustomException("No documents provided for text chunking.")
        logger.info(f"Creating text chunks with chunk size {chunk_size} and overlap {chunk_overlap}")
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        texts = text_splitter.split_documents(documents)
        logger.info(f"Created {len(texts)} text chunks")
        return texts
    except Exception as e:
        error_message = f"Failed to create text chunks: {str(e)}"
        logger.error(str(error_message))
        return []