# pip install git+https://github.com/openai/whisper.git -q 

import whisper 

model = whisper.load_model('base') 

model.device 

# RUN git clone https://github.com/petewarden/openai-whisper-webapp

from IPython.display import Audio 
Audio('/content/openai-whisper-webapp/mary.mp3') 

from IPython.display import Audio 
Audio('/content/openai-whisper-webapp/daisy_HAL_9000.mp3') 

def transcribe(audio):

    # load audio and pad/trim it to fit 30 seconds 
    audio = whisper.load_audio(audio) 
    audio = whisper.pad_or_trim(audio) 

    # make log-Mel spectrogram and move to the same device as the model 
    mel = whisper.log_mel_spectrogram(audio).to(model.device) 

    # detect the spoken language 
    _, probs = model.detect_language(mel) 
    print(f'Detected language: {max(probs, key=probs.get)}')

    # decode the audio 
    options = whisper.DecodingOptions() 
    result = whisper.decode(model, mel, options) 
    return result.text 

easy_text = transcribe('/content/openai-whisper-webapp/mary.mp3') 
print(easy_text) 

hard_text = transcribe('/content/openai-whisper-webapp/daisy_HAL_9000.mp3')
print(hard_text) 

# pip install gradio -q

import gradio as gr 
import time 

gr.Interface(
    title = 'OpenAI Whisper ASR Gradio Web UI',
    fn=transcribe,
    inputs=[
        gr.inputs.Audio(source="microphone", type='filepath') 

    ],
    outputs=[
        'textbox'
    ],
    live=True
).launch()




