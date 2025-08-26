# 🧪 반도체 공정 학습 튜터 (Semiconductor Process Tutor)

![Streamlit](https://img.shields.io/badge/Framework-Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LLM-LangChain-blue?logo=chainlink&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.9%2B-yellow?logo=python&logoColor=white)

> 📘 **Streamlit + LangChain 기반 반도체 공정 학습 보조 애플리케이션**  
> 업로드한 PDF 학습 자료를 **벡터 검색 기반 질의응답(RAG)**으로 활용하고,  
> 📊 **공정별 개요 · 핵심 포인트 · 단계별 다이어그램 · 질의응답**을 통해 쉽게 학습할 수 있습니다.

---

## 👨‍💻 팀원 및 역할

| 이름 | 담당 역할 |
|:----:|:----------|
| 손형 | Backend / DB |
| 신영 | Frontend / UI |
| 문건 | AI 모델 연동 / RAG |
| 김진 | 문서화 / 테스트 |

---

## ✨ 주요 기능

✅ **PDF 업로드 & 임베딩**  
- OpenAI, Gemini, HuggingFace 임베딩 선택 가능  
- 업로드한 문서를 FAISS 벡터 DB로 변환하여 검색  

✅ **LLM 백엔드 선택**  
- OpenAI GPT 계열 (`gpt-4o` 등)  
- Google Gemini (`gemini-1.5-flash`)  

✅ **공정별 학습 페이지**  
- **포토리소그래피** : 노광, 현상, 해상도 공식  
- **식각(Etching)** : Wet / Dry, RIE, ICP  
- **산화(Oxidation)** : Dry / Wet, Deal-Grove 모델  
- **확산(Diffusion)** : Pre-Depo, Drive-in, 농도 프로파일  
- **이온주입(Ion Implantation)** : 채널링 방지, 어닐링  
- **증착(Deposition)** : PVD / CVD / ALD  
- **금속배선(Metallization)** : 구리 도금, EM 신뢰성  
- **CMP (평탄화)** : 디싱, 스크래치 제어  

✅ **인터랙티브 Q&A (RAG)**  
- 업로드한 자료 기반으로 질문 → 답변 + 출처 문서 표시  

✅ **시각화**  
- 각 공정은 **Graphviz 다이어그램**으로 단계별 시각화  

---

## 🛠 개발환경 및 개발도구

- **협업도구** : GitHub, ERD Cloud  
- **개발도구** : IntelliJ, VS Code  
- **프로그래밍 언어** : Python 3.9+, Java, JavaScript, HTML5, CSS, SQL  
- **Database** : MySQL  
- **Framework** : Streamlit, Spring Boot, MyBatis, Bootstrap  
- **AI/ML** : LangChain, OpenAI API, Google Gemini API  
- **Vector DB** : FAISS  

---

## 🚀 시작하기

### 1. 설치
```bash
git clone https://github.com/사용자명/sm_sc.git
cd sm_sc/project
