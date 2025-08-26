# =============================================
# File: app.py  (메인 페이지)
# =============================================
import os
import tempfile
from typing import List
import streamlit as st
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader

st.title("반도체 공정 학습 튜터")
st.markdown("다쳤을 땐 쎄쎄")

try:
    from langchain_openai import ChatOpenAI, OpenAIEmbeddings

    HAS_OPENAI = True
except Exception:
    HAS_OPENAI = False

try:
    from langchain_community.chat_models import ChatOllama
    from langchain_community.embeddings import OllamaEmbeddings

    HAS_OLLAMA = True
except Exception:
    HAS_OLLAMA = False

from langchain.chains import RetrievalQA

st.set_page_config(page_title="반도체 공정 학습 튜터 · 메인", layout="wide")

# --- Sidebar: LLM & Embeddings 설정 + PDF 임베딩 ---
st.sidebar.subheader("LLM · 임베딩 설정")

# LLM 백엔드 선택
backend = st.sidebar.selectbox("LLM 백엔드", ["openai", "gemini"], index=0)

if backend == "openai":
    if HAS_OPENAI:
        openai_key = st.sidebar.text_input("OpenAI API Key", type="password", placeholder="sk-...")
        if openai_key:
            os.environ["OPENAI_API_KEY"] = openai_key
        model = st.sidebar.text_input("OpenAI 모델", value="gpt-4o-mini")
    else:
        st.sidebar.error("langchain-openai 미설치")
        model = "gpt-4o-mini"
else:  # gemini
    if HAS_GEMINI:
        google_key = st.sidebar.text_input("Google API Key", type="password", placeholder="AIza...")
        if google_key:
            os.environ["GOOGLE_API_KEY"] = google_key
        model = st.sidebar.text_input("Gemini 모델", value="gemini-1.5-pro")
    else:
        st.sidebar.error("langchain-google-genai 미설치 (`pip install langchain-google-genai`)")
        model = "gemini-1.5-pro"

# 세션에 보관
st.session_state["llm_backend"] = backend
st.session_state["llm_model"] = model

st.sidebar.divider()
st.sidebar.subheader("자료 업로드 · 임베딩")

# 임베딩 백엔드 선택
embed_backend = st.sidebar.selectbox("임베딩 백엔드", ["openai", "gemini", "hf"], index=0)

# PDF 업로드
uploaded = st.sidebar.file_uploader("PDF 업로드 (여러 개 가능)", type=["pdf"], accept_multiple_files=True)

colA, colB = st.sidebar.columns(2)
if colA.button("임베딩 생성", use_container_width=True):
    if not uploaded:
        st.sidebar.warning("PDF를 먼저 업로드하세요.")
    else:
        try:
            st.session_state.vectorstore = build_vectorstore_from_pdfs(uploaded, embed_backend)
            st.sidebar.success("벡터스토어 생성 완료")
            # 모델 변경 대비 체인 초기화
            st.session_state.pop("qa_chain", None)
        except Exception as e:
            st.sidebar.error(f"임베딩 실패: {e}")

if colB.button("임베딩 초기화", use_container_width=True):
    st.session_state.pop("vectorstore", None)
    st.session_state.pop("qa_chain", None)
    st.sidebar.info("임베딩을 비웠습니다.")


