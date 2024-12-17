# TTS_project
내 목소리 TTS 만들어서 방송할거임.

TTS_project/
│
├── venv/                # 가상환경 (예외 처리됨)
├── data/                # 음성 데이터 저장 폴더
│   ├── raw/             # 원본 음성 데이터
│   └── processed/       # 전처리된 음성 데이터
├── models/              # 학습된 모델 저장 폴더
│   └── checkpoints/     # 체크포인트 저장
├── src/                 # 소스코드 폴더
│   ├── preprocess.py    # 데이터 전처리 코드
│   ├── train.py         # 모델 학습 코드
│   ├── synthesize.py    # 음성 합성 코드 (추론)
│   └── utils.py         # 유틸리티 함수 모음
├── requirements.txt     # 의존성 패키지 목록
└── README.md            # 프로젝트 설명서
