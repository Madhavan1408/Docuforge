import io
import pypdf
from langchain_text_splitters import RecursiveCharacterTextSplitter
def extract_text(file_bytes : bytes ,file_type :str) ->str:
    try:
        if file_type =="pdf":
            pdf_reader=pypdf.PdfReader(io.BytesIO(file_bytes))
            chunk=[]
            for page in pdf_reader.pages:
                text=extract_text()
                if text:
                    chunk.append(text)
            return "\n".join(chunk)
        elif file_type =="txt":
            return file_bytes.decode("utf-8")
        else:
            raise ValueError("Unsupported File System")
    except Exception as e:
        print(f"Error Extracting Text: {e}")
        return ""
def chunk_split(text :str):
    chunk=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=100,separators=["\n\n","\n","."," ",""])
    return chunk.split_text(text)