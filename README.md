# 🧪 반도체 공정 학습 튜터 (Semiconductor Process Tutor)

> Streamlit + LangChain 기반의 **반도체 공정 학습 보조 애플리케이션**  
> PDF 학습자료를 업로드하여 **임베딩/검색 기반 질의응답(RAG)**과  
> **포토리소그래피, 식각, 산화, 확산, 이온주입, 증착, 금속배선, CMP** 등  
> 주요 공정을 단계별 다이어그램 + 핵심 포인트 + Q&A로 학습할 수 있습니다.

---

## ✨ 주요 기능

### 1. 메인 기능
- **PDF 업로드 및 임베딩 생성**  
  - OpenAI / Gemini / HuggingFace 임베딩 선택 가능  
  - 업로드한 자료를 FAISS 벡터DB로 변환 → 검색 가능
- **LLM 백엔드 선택**  
  - OpenAI GPT 계열 (기본: `gpt-4o`)  
  - Google Gemini (예: `gemini-1.5-flash`)  
- **질의응답 (RAG)**  
  - 업로드한 학습자료 기반으로 질문 → AI 답변 + 출처 표시  

### 2. 학습 페이지 (pages/*)
각 공정별 페이지는 **개요 → 핵심 포인트 → 공정 다이어그램 → 질의응답** 구성으로 되어 있습니다.

- `1_포토리소그래피.py` : PR 코팅 → 노광 → 현상 → 베이크 공정  
- `2_식각.py` : Wet/Dry Etching, RIE, ICP  
- `3_산화.py` : Dry/Wet Thermal Oxidation, Deal-Grove 모델  
- `4_확산.py` : Pre-Deposition, Drive-in, 농도 프로파일  
- `5_이온주입.py` : Ion Beam Implantation, 채널링 방지, 어닐  
- `6_증착.py` : PVD / CVD / ALD 증착 기술  
- `7_금속배선.py` : 구리 배선, 배리어/시드, 전해도금, EM 신뢰성  
- `8_CMP.py` : Chemical Mechanical Polishing, 디싱·스크래치 제어  

각 단계는 **Graphviz 다이어그램**으로 시각화되어 이해를 돕습니다.

---

## 🛠️ 기술 스택

- **Frontend / UI**
  - [Streamlit](https://streamlit.io)  

- **LLM & 임베딩**
  - [LangChain](https://www.langchain.com/)  
  - OpenAI GPT (예: `gpt-4o`)  
  - Google Gemini (`gemini-1.5-flash`)  
  - HuggingFace Sentence Transformers (`all-MiniLM-L6-v2`)  

- **Vector Database**
  - FAISS (문서 임베딩 검색)  

- **Document Loader**
  - PyPDFLoader (PDF 텍스트 분할 & 로딩)  

---

## 🚀 실행 방법

### 1. 프로젝트 클론
```bash
git clone https://github.com/사용자명/sm_sc.git
cd sm_sc/project
