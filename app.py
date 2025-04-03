from flask import Flask, request, render_template, jsonify
from utils import generate_xiaohongshu
import os

app = Flask(__name__)

# 首页：输入主题的表单
@app.route('/')
def index():
    return render_template('index.html')

# 处理生成请求的API
@app.route('/generate', methods=['POST'])
def generate():
    theme = request.form.get('theme')
    openai_api_key = os.getenv("OPENAI_API_KEY")  # 从环境变量读取API密钥
    if not openai_api_key:
        return jsonify({"error": "OpenAI API Key未配置"}), 500
    try:
        result = generate_xiaohongshu(theme, openai_api_key)
        return jsonify({
            "titles": result.titles,
            "content": result.content
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5100)