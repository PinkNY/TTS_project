import os
import librosa
import sudfile as sf
from tqdm import tqdm

def preprocess_audio(input_dir, output_dir, sample_rate=22050):
    """음성 데이터를 전처리 하여 저장한다."""
    os.makedirs(output_dir, exist_ok=True)
    