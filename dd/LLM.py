import os
import tempfile
from typing import List
import streamlit as st

# LangChain / Vector DB
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader

def build_vectorstore_from_pdfs(files: List[st.runtime.uploaded_file_manager.UploadedFile],
                                embed_backend: str = "openai",
                                ollama_embed_model: str = "nomic-embed-text"):
    docs = []
    with st.spinner("PDF를 로딩 중…"):
        for f in files:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                tmp.write(f.read())
                tmp_path = tmp.name
            loader = PyPDFLoader(tmp_path)
            docs.extend(loader.load())
            os.remove(tmp_path)

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = splitter.split_documents(docs)

    if embed_backend == "openai":
        if not HAS_OPENAI:
            raise RuntimeError("langchain-openai가 필요합니다.")
        embedding = OpenAIEmbeddings()
    elif embed_backend == "ollama":
        if not HAS_OLLAMA:
            raise RuntimeError("Ollama 임베딩 사용 불가 (설치 필요)")
        embedding = OllamaEmbeddings(model=ollama_embed_model)
    else:
        from langchain_community.embeddings import HuggingFaceEmbeddings
        embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    vs = FAISS.from_documents(splits, embedding)
    return vs


def set_llm_settings():
    st.sidebar.subheader("LLM · 임베딩 설정")
    backend = st.sidebar.selectbox("LLM 백엔드", ["openai", "ollama"], index=0)
    if backend == "openai":
        if HAS_OPENAI:
            _api = st.sidebar.text_input("OpenAI API Key", type="password", placeholder="sk-…")
            if _api:
                os.environ["OPENAI_API_KEY"] = _api
            model = st.sidebar.text_input("OpenAI 모델", value="gpt-4o-mini")
        else:
            st.sidebar.error("langchain-openai 미설치")
            model = "gpt-4o-mini"
    else:
        if HAS_OLLAMA:
            model = st.sidebar.text_input("Ollama 모델", value="llama3.1:8b")
        else:
            st.sidebar.error("Ollama 미설치")
            model = "llama3.1:8b"

    st.session_state["llm_backend"] = backend
    st.session_state["llm_model"] = model

    st.sidebar.divider()
    st.sidebar.subheader("자료 업로드 · 임베딩")
    uploaded = st.sidebar.file_uploader("PDF 업로드 (여러 개)", type=["pdf"], accept_multiple_files=True)
    embed_backend = st.sidebar.selectbox("임베딩 백엔드", ["openai", "ollama", "hf"], index=0)

    colA, colB = st.sidebar.columns(2)
    if colA.button("임베딩 생성", use_container_width=True):
        if not uploaded:
            st.sidebar.warning("PDF를 먼저 업로드하세요.")
        else:
            try:
                st.session_state.vectorstore = build_vectorstore_from_pdfs(uploaded, embed_backend)
                st.sidebar.success("벡터스토어 생성 완료")
                st.session_state.pop("qa_chain", None)
            except Exception as e:
                st.sidebar.error(f"임베딩 실패: {e}")

    if colB.button("임베딩 초기화", use_container_width=True):
        st.session_state.pop("vectorstore", None)
        st.session_state.pop("qa_chain", None)
        st.sidebar.info("임베딩을 비웠습니다.")


def dot_pipeline(title: str, steps):
    lines = ["digraph G {",
             "rankdir=LR;",
             "node [shape=box, style=rounded, fontsize=12, fontname=\"Pretendard, NanumGothic, Arial\"];",
             f"labelloc=t; label=\"{title}\";"]
    for i, step in enumerate(steps):
        lines.append(f"n{i} [label=\"{step}\"];")
    for i in range(len(steps) - 1):
        lines.append(f"n{i} -> n{i + 1};")
    lines.append("}")
    return "\n".join(lines)