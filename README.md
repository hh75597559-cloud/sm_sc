 # 🧪 반도체 공정 학습 튜터 (Semiconductor Process Tutor)

![Streamlit](https://img.shields.io/badge/Framework-Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LLM-LangChain-blue?logo=chainlink&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.9%2B-yellow?logo=python&logoColor=white)


📘 AI 기반 반도체 공정 학습 지원 플랫폼
이 프로젝트는 Streamlit + LangChain 을 기반으로 반도체 공정 학습을 보다 직관적이고 체계적으로 지원하기 위해 제작되었습니다.
사용자는 PDF 학습 자료 업로드 → 벡터 검색 기반 Q&A → 단계별 공정 학습 → 랜덤 문제 풀이까지
하나의 흐름 속에서 자율적이고 몰입감 있는 학습 경험을 얻을 수 있습니다.                          

페이지 사진

---                                  

## 👨‍💻 팀원

| 이름 |  학번 |

| 유태건 | 시스템반도체공학과 | 202321562
| 박세현 | 시스템반도체공학과 | 202321571
| 박수현 | 시스템반도체공학과 | 202321561

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

app.py: 네비게이션/사이드바(임베딩 생성)·페이지 라우팅

LLM.py: 백엔드 선택, RAG 유틸, 퀴즈/채점 파서, 멀티모달 질의, STT/TTS 헬퍼

1~8.py: 공정별 학습(개요/핵심/가로스크롤 프로세스/진도관리/RAG/퀴즈)

9.py: 접근성+ (음성/카메라/이미지 → 멀티모달 질의)



✨ 주요 기능

📘 공정 학습 모듈
+ 주요 특징 : 공정별 개요 · 핵심 포인트 학습 지원
! 세부 기능 : 단계별 프로세스 다이어그램
!              공정별 핵심 포인트 정리
!              학습 진도 관리 (완료율 표시)
- 강점      : 시각적 이해도 향상, 자기주도 학습 가능

🔎 Q&A (RAG)
+ 주요 특징 : 업로드한 PDF 기반 지능형 질의응답
! 세부 기능 : FAISS 벡터 검색
!              OpenAI/Gemini 응답 선택 및 생성
!              출처 문서 표시
- 강점      : 신뢰성 있는 학습자료 기반 답변 제공

🎲 랜덤 문제 생성기
+ 주요 특징 : 실습형 학습 강화
! 세부 기능 : 난이도 선택 (초급/고급)
!              랜덤 문제 자동 생성
!              학습 점검용 피드백 제공
- 강점      : 시험 대비, 자기 점검 학습에 효과적

🎯 맞춤형 학습 경험
+ 주요 특징 : 학습자료 ↔ Q&A ↔ 문제풀이 선순환 구조
! 세부 기능 : 사용자가 선택한 학습자료 활용
!              자율적 질문·답변 학습
!              복습 및 시험 준비 최적화
- 강점      : AI 기반 개인 맞춤 학습 경험 제공

🎤 Q&A 확장 기능 (멀티모달 입력)
+ 주요 특징 : 음성 / 이미지 / 카메라 / 채팅 입력 지원
! 세부 기능 : 음성 인식 → 질문/응답/음성 출력
!              이미지 업로드 (공정 사진·도표)
!              카메라 촬영 (실시간 전송)
!              채팅 입력 (자유로운 질문)
- 강점      : 다양한 입력 채널로 몰입형 학습 경험 제공
  
📊 공정 프로세스 시각화

카드 기반 시각화를 통해 각 공정의 진행 과정을 단계적으로 쉽게 파악할 수 있습니다.

<img width="1169" height="78" alt="image" src="https://github.com/user-attachments/assets/b30acdd8-ea46-40bb-af5d-260e27b5ef1a" />

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
🗂 디렉토리 구조 (Directory Tree)
C:.
|   .env
|   .gitignore
|   myllm.zip
|   requirements.txt
|
+---.idea
|   |   .gitignore
|   |   misc.xml
|   |   modules.xml
|   |   myproject.iml
|   |   sm_sc.iml
|   |   vcs.xml
|   |   workspace.xml
|   |
|   \---inspectionProfiles
|           profiles_settings.xml
|           Project_Default.xml
|
+---data
+---myllm
|       Myapi.py
|       __init__.py
|
+---project
|   |   1.py
|   |   2.py
|   |   3.py
|   |   4.py
|   |   5.py
|   |   6.py
|   |   7.py
|   |   8.py
|   |   9.py
|   |   app.py
|   |   cate.py
|   |   LLM.py
|   |   main.py
|   |
|   \---__pycache__
|           LLM.cpython-310.pyc
|
\---__pycache__
        LLM.cpython-310.pyc
        MyLCH.cpython-310.pyc

---

## 🚀 시작하기
스트림잇 주소
### 1. 설치
```bash
git clone https://github.com/사용자명/sm_sc.git
cd sm_sc/project
