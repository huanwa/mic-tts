from tts_voice import tts_order_voice
import edge_tts
import gradio as gr
import tempfile
import anyio
from wsgidav.wsgi_dav_app import DEFAULT_CONFIG, WsgiDavApp


# 增加一行，定义WSGI的入口函数
def app(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'application/json')]
    start_response(status, headers)
    return [b'Hello World']


if __name__ == "__main__":
    anyio.run(app, backend="asyncio")
