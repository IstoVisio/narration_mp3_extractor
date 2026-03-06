import syglass
from syglass import pyglass
import whisper
import json
import os

SRC = ".\\narrations"
AUDIO_DST = ".\\audio_files"

def ExtractAndTranscribeNarrationFile(narration: pyglass.PresentationFile, dst: str):
    scene: pyglass.Narration
    transcription = {}
    print(f"Starting narration: {narration.header.title}")
    for i, scene in enumerate(narration.narrations):
        print(f"Starting scene: {i}")
        dstFile = f'{dst}\\{narration.header.title}_{i}.mp3'
        pyglass.NarrationFileWriter.WriteFileHandle(scene.narrationAudioTrack, pyglass.path(dstFile))
        transcription[i] = TranscribeFile(dstFile)
    return transcription
    

def TranscribeFile(path: str):
    loaded_audio = whisper.load_audio(path)
    model = whisper.load_model("medium.en", device="cuda")
    captions = model.transcribe(loaded_audio)
    segments = captions["segments"]
    segment: dict
    for segment in segments:
        segment.pop("tokens")
        segment.pop("avg_logprob")
        segment.pop("compression_ratio")
        segment.pop("temperature")
    return segments


if __name__ == "__main__":
    syp_files = [f for f in os.listdir(SRC) if f.endswith('.syp')]
    label_dict = {}
    for syp in syp_files:
        src = SRC + f'/{syp}'
        narration = syglass.get_presentation(src)
        transcription = ExtractAndTranscribeNarrationFile(narration, AUDIO_DST)
        with open(src.replace(".syp", ".json"), "w") as transcription_file:
            json.dump(transcription, transcription_file)
    print("Finished!")