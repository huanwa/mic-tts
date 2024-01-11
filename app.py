from tts_voice import tts_order_voice
import edge_tts
import gradio as gr
import tempfile
import anyio

language_dict = tts_order_voice

async def text_to_speech_edge(text, language_code):
    voice = language_dict[language_code]
    communicate = edge_tts.Communicate(text, voice)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
        tmp_path = tmp_file.name

    await communicate.save(tmp_path)

    return "语音合成完成：{}".format(text), tmp_path



input_text = gr.inputs.Textbox(lines=5, label="输入文本")
output_text = gr.outputs.Textbox(label="输出文本")
output_audio = gr.outputs.Audio(type="filepath", label="导出文件")
default_language = list(language_dict.keys())[0]
language = gr.inputs.Dropdown(choices=list(language_dict.keys()), default=default_language, label="语言")


interface = gr.Interface(fn=text_to_speech_edge, inputs=[input_text, language], outputs=[output_text, output_audio], title="Edge TTS 文字转语音")


if __name__ == "__main__":
    anyio.run(interface.launch, backend="asyncio")
