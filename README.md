 # 🧪 반도체 공정 학습 튜터 (Semiconductor Process Tutor)

![Streamlit](https://img.shields.io/badge/Framework-Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LLM-LangChain-blue?logo=chainlink&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.9%2B-yellow?logo=python&logoColor=white)


📘 AI 기반 반도체 공정 학습 지원 플랫폼
                        
**복잡한 반도체 공정, 누구나 따라가는 학습 여정으로.**  
**PDF 하나로 시작해 RAG·퀴즈·멀티모달로 완성하는 AI 튜터.**

Streamlit + LangChain 기반의 반도체 공정 학습 지원 애플리케이션입니다.
PDF 학습 자료를 업로드하면 텍스트를 분할·벡터화(FAISS)하여 RAG 파이프라인(OpenAI/Gemini)을 통해 질의응답을 수행하고, 답변과 함께 출처를 제공합니다.
각 공정은 개요·핵심 포인트·단계 다이어그램으로 구조화되어 있으며, 동일 형식으로 페이지를 구성해 흐름 파악과 비교 학습이 쉽습니다.
학습 평가는 난이도 선택형 랜덤 문제와 간단 해설, 진도율 표시로 이루어져 이해 수준을 정량적으로 확인할 수 있습니다.
전체 학습 흐름은 자료 업로드 → RAG 질의응답 → 단계별 학습 → 퀴즈 평가로 설계되어, 반복 가능한 자기주도 학습 사이클을 제공합니다.

---                                  

## 👨‍💻 팀원


**| 유태건 | 시스템반도체공학과 | 202321562 |**

**| 박세현 | 시스템반도체공학과 | 202321571 |**

**| 박수현 | 시스템반도체공학과 | 202321561 |**

---
## 🛠 개발환경 및 개발도구

- **협업도구** : GitHub  
- **개발도구** : VS Code, Streamlit CLI  
- **프로그래밍 언어** : Python 3.10 
- **Framework / Library** : Streamlit, LangChain  
- **LLM API** : OpenAI API, Google Gemini API  
- **Vector DB** : FAISS  
- **문서 처리** : PyPDFLoader (langchain_community)  

# Installation
1) 프로젝트 클론
git clone https://github.com/사용자명/semiconductor-tutor.git
cd semiconductor-tutor/project

2) 가상환경 (권장)
python -m venv .venv
 //Windows//
.venv\Scripts\activate
//macOS/Linux//
source .venv/bin/activate

4) 의존성 설치

   pip install -r requirements.txt

   or

   pip install streamlit langchain langchain-community langchain-openai langchain-google-genai \
            faiss-cpu pypdf python-dotenv google-generativeai openai pillow faster-whisper

6) 실행
 
    streamlit run app.py

7) Environment Variables (.env 권장)
OpenAI 사용 시
OPENAI_API_KEY=sk-xxxx
Google Gemini 사용 시
GOOGLE_API_KEY=AIza-xxxx

# 🏗 아키텍처 (Architecture)

**app.py**: 네비게이션 / 사이드바(임베딩 생성) · 페이지 라우팅  
**LLM.py**: 백엔드 선택, RAG 유틸, 퀴즈/채점 파서, 멀티모달 질의, STT/TTS 헬퍼  
**1~8.py**: 공정별 학습 (개요 / 핵심 / 가로 스크롤 프로세스 / 진도 관리 / RAG / 퀴즈)  
**9.py**: 접근성+ (음성 / 카메라 / 이미지 → 멀티모달 질의)


# ✨ 주요 기능

### 📘 공정 학습 모듈
- **주요 특징**: 공정별 개요와 핵심 포인트 학습 지원
- **세부 기능**:
  - 단계별 프로세스 다이어그램
  - 공정별 핵심 포인트 정리
  - 학습 진도 관리(완료율 표시)
- **강점**: 시각적 이해도 향상, 자기주도 학습 가능

### 🔎 Q&A (RAG)
- **주요 특징**: 업로드한 PDF 기반 지능형 질의응답
- **세부 기능**:
  - **FAISS 벡터 검색**
  - **OpenAI/Gemini** 모델 응답 생성
  - **출처 문서 표시**
- **강점**: 신뢰성 있는 학습자료 기반 답변 제공


### 🎲 랜덤 문제 생성기
- **주요 특징**: 실습형 학습 강화
- **세부 기능**:
  - **난이도 선택(초급/고급)**
  - **랜덤 문제 자동 생성**
  - **학습 점검용 피드백 제공**
- **강점**: 시험 대비 및 자기 점검 학습에 효과적


### 🎯 맞춤형 학습 경험
- **주요 특징**: **학습자료 ↔ Q&A ↔ 문제풀이** 선순환 구조
- **세부 기능**:
  - **사용자가 선택한 학습자료** 활용
  - 자율적 질문·답변 학습
  - 복습 및 시험 준비 최적화
- **강점**: **AI 기반 개인 맞춤 학습 경험 제공**

### 🎤 Q&A 확장 기능 (멀티모달 입력)
- **주요 특징**: **음성 / 이미지 / 카메라 / 채팅** 입력 지원
- **세부 기능**:
  - 음성 인식 → 답변 생성 → 음성 출력
  - 이미지 업로드(공정 사진·도표)
  - 카메라 촬영(실시간 전송)
  - 채팅 입력(자유로운 질문)
- **강점**: 다양한 입력 채널을 통한 **몰입형 학습 경험** 제공




**📊 공정 프로세스 시각화**

카드 기반 시각화를 통해 각 공정의 진행 과정을 단계적으로 쉽게 파악할 수 있습니다.


<!-- ✅ 4 columns x 2 rows gallery for GitHub README -->
<table>
  <!-- Row 1: Titles -->
  <tr>
    <td align="center" width="25%" style="font-weight:700;font-size:16px;padding:6px 4px;">공정 학습 모듈</td>
    <td align="center" width="25%" style="font-weight:700;font-size:16px;padding:6px 4px;">Q&A (RAG)</td>
    <td align="center" width="25%" style="font-weight:700;font-size:16px;padding:6px 4px;">랜덤 문제 생성</td>
    <td align="center" width="25%" style="font-weight:700;font-size:16px;padding:6px 4px;">랜덤 문제 생성</td>
  </tr>
  <!-- Row 1: Images -->
  <tr>
    <td align="center"><img src="https://github.com/user-attachments/assets/b0830e4e-b862-4ee0-90c6-a8032db32de9" alt="공정 학습 모듈" width="230"></td>
    <td align="center"><img src="https://github.com/user-attachments/assets/9f235334-be6d-480e-b4fc-019b38bccae9" alt="Q&A (RAG)" width="230"></td>
    <td align="center"><img src="https://github.com/user-attachments/assets/a4cfb0f8-1af0-45d9-ba01-462a9eab9f23" alt="랜덤 문제 생성" width="230"></td>
    <td align="center"><img src="https://github.com/user-attachments/assets/cbcd9717-deca-4de0-90d8-ef9150265932" alt="랜덤 문제 생성" width="230"></td>
  </tr>

  <!-- Row 2: Titles -->
  <tr>
    <td align="center" width="25%" style="font-weight:700;font-size:16px;padding:6px 4px;">멀티모달-음성인식&이미지 업로드</td>
    <td align="center" width="25%" style="font-weight:700;font-size:16px;padding:6px 4px;">멀티모달-카메라촬영</td>
    <td align="center" width="25%" style="font-weight:700;font-size:16px;padding:6px 4px;">멀티모달-챗봇</td>
    <td align="center" width="25%" style="font-weight:700;font-size:16px;padding:6px 4px;">단계별 카드</td>
  </tr>
  <!-- Row 2: Images -->
  <tr>
    <td align="center"><img src="https://github.com/user-attachments/assets/428b2440-73c2-41d4-9db9-2c4ee0be72ac" alt="멀티모달-음성인식&이미지 업로드" width="230"></td>
    <td align="center"><img src="https://github.com/user-attachments/assets/cad23eaf-626a-435d-9a4c-365897cacd3c" alt="멀티모달-카메라촬영" width="230"></td>
    <td align="center"><img src="https://github.com/user-attachments/assets/d591cbe8-68fb-47c5-bf79-a3a1cba5fd68" alt="멀티모달-챗봇" width="230"></td>
    <td align="center"><img src="https://github.com/user-attachments/assets/b30acdd8-ea46-40bb-af5d-260e27b5ef1a" alt="단계별 카드" width="230"></td>
  </tr>
</table>

## 🎥 시연 영상 (Demo Video)

[![시연 영상 보기](https://img.shields.io/badge/YouTube-시연영상-red?logo=youtube&logoColor=white)](https://youtube.com/예시링크)

---

### 1️⃣ 포토리소그래피 (Photolithography)
- **키워드** : 노광, 현상, 해상도 공식 (R = k1·λ/NA)  
- **설명** : 웨이퍼 표면에 감광막(PR)을 바르고 노광/현상 과정을 거쳐 미세 패턴을 형성하는 공정  

---

### 2️⃣ 식각 (Etching)
- **키워드** : Wet / Dry, RIE, ICP, 선택비(Selectivity)  
- **설명** : 포토 공정에서 만든 패턴을 실제 기판/박막에 전사하여 불필요한 물질을 제거하는 공정  

---

### 3️⃣ 산화 (Oxidation)
- **키워드** : Dry vs Wet, Deal-Grove 모델, 게이트 산화막  
- **설명** : 실리콘 표면에 SiO₂ 절연막을 성장시켜 트랜지스터 게이트 절연막 등으로 활용  

---

### 4️⃣ 확산 (Diffusion)
- **키워드** : Pre-Deposition, Drive-in, 가우시안/에러펑션 프로파일  
- **설명** : 고온에서 도펀트를 웨이퍼 내부로 확산시켜 농도 프로파일과 접합 깊이를 형성  

---

### 5️⃣ 이온주입 (Ion Implantation)
- **키워드** : 이온 주입, 채널링 방지(tilt), 어닐링(활성화)  
- **설명** : 고속 이온 빔을 주입하여 원하는 농도/깊이로 도핑하는 현대 반도체 핵심 도핑 공정  

---

### 6️⃣ 증착 (Deposition)
- **키워드** : PVD, CVD, ALD, 박막 두께 균일도  
- **설명** : 웨이퍼 표면에 절연막, 도전막, 배리어막 등을 증착하여 소자 및 배선 구조를 형성  

---

### 7️⃣ 금속배선 (Metallization)
- **키워드** : 배리어/시드층, 구리 도금, EM 신뢰성  
- **설명** : 트랜지스터 간 신호 연결을 위한 금속 배선을 형성하고 RC Delay를 최소화  

---

### 8️⃣ CMP (Chemical Mechanical Polishing)
- **키워드** : 평탄화, 디싱, 스크래치, 오버폴리시  
- **설명** : 패드와 슬러리를 이용해 표면을 평탄화하여 다층 배선과 후속 공정의 기반을 마련  

✅ **인터랙티브 Q&A (RAG)**  
- 업로드한 자료 기반으로 질문 → 답변 + 출처 문서 표시  

✅ **시각화**  
- 각 공정은 **Graphviz 다이어그램**으로 단계별 시각화  
---
details> <summary><b>🔧 RAG 초기화 (ConversationalRetrievalChain) — 클릭하여 펼치기</b></summary>
# RAG 초기화 (README 예제)
import streamlit as st
from langchain.chains import ConversationalRetrievalChain
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from LLM import get_llm_backend, get_chat_llm

st.subheader("질의응답 (RAG)")

if "vectorstore" not in st.session_state:
    st.info("임베딩 자료가 없습니다. PDF 업로드 → 임베딩 생성 후 이용하세요.")
else:
    # LLM 선택(OpenAI/Gemini) 및 생성
    if "qa_chain" not in st.session_state:
        backend, model = get_llm_backend()             # 예: ("openai", "gpt-4o-mini")
        llm = get_chat_llm(backend=backend, model=model, temperature=0.2)
        retriever = st.session_state.vectorstore.as_retriever(search_kwargs={"k": 4})

        # PDF 우선 답변 프롬프트
        prompt = ChatPromptTemplate.from_messages([
            ("system",
             "당신의 1차 정보원은 업로드된 PDF입니다. "
             "가능하면 PDF 근거를 우선하여 답하고, 부족하면 일반지식으로 보완하되 그 사실을 한 문장으로 표시하십시오. "
             "항상 정중한 한국어(존댓말)로 답하십시오."),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{question}")
        ])

        st.session_state.qa_chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=retriever,
            return_source_documents=True,
            combine_docs_chain_kwargs={"prompt": prompt},
        )
        st.session_state.llm = llm
        st.session_state.retriever = retriever
        st.session_state.qa_mode = "crc"    # CRC 사용 플래그

</details> ::contentReference[oaicite:0]{index=0}













---
# 🗂 디렉토리 구조 (Directory Tree)

```plaintext
C:.
│   .env
│   .gitignore
│   myllm.zip
│   requirements.txt
│
+---.idea
│   │   .gitignore
│   │   misc.xml
│   │   modules.xml
│   │   myproject.iml
│   │   sm_sc.iml
│   │   vcs.xml
│   │   workspace.xml
│   │
│   \---inspectionProfiles
│           profiles_settings.xml
│           Project_Default.xml
│
+---data
│
+---myllm
│   │   Myapi.py
│   │   __init__.py
│
+---project
│   │   1.py
│   │   2.py
│   │   3.py
│   │   4.py
│   │   5.py
│   │   6.py
│   │   7.py
│   │   8.py
│   │   9.py
│   │   app.py
│   │   cate.py
│   │   LLM.py
│   │   main.py
│   │
│   \---__pycache__
│           LLM.cpython-310.pyc
│           MyLCH.cpython-310.pyc
```
