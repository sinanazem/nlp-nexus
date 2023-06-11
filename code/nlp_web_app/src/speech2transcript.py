import whisper
import librosa

def audio_to_transcript(audio_file_path):

    # Load the audio file
    signal, sr = librosa.load(audio_file_path, sr=16000)

    # Load the English base model
    model = whisper.load_model("base")

    # Transcribe the audio using the model
    result = model.transcribe(signal)
    return result["text"]


