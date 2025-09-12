import os
from app.components.pdf_loader import load_pdf_files, create_text_chunks
from app.components.vector_store import loa_vector_store, save_vector_store
from app.config.config import DB_FAISS_PATH
from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger = get_logger(__name__)


def process_and_store_pdfs():
    try:
        logger.info("Starting PDF processing and vector store creation")
        
        # Load PDF files
        documents = load_pdf_files()
        if not documents:
            raise CustomException("No documents loaded. Please check the data path and ensure it contains PDF files.")
        
        # Create text chunks
        text_chunks = create_text_chunks(documents)
        if not text_chunks:
            raise CustomException("Text chunking failed. No chunks created from the documents.")
        
        # Save to vector store
        save_vector_store(text_chunks)

        logger.info("PDF processing and vector store creation completed successfully")
    except Exception as e:
        error_message = f"Error in processing and storing PDFs: {str(e)}"
        logger.error(str(error_message))

if __name__ == "__main__":
    process_and_store_pdfs() 
    