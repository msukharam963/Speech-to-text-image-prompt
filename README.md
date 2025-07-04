<!DOCTYPE html>
<html lang="en">
  
<body style="font-family: Arial; line-height: 1.6; margin: 2em; background: #fafafa; color: #333;">

<h1 color: #007acc;>🎤🖼️ Voice-to-Image Generator</h1>

<p>
A web-based app that takes either typed text or spoken input and generates an image using Stable Diffusion.
Built with Streamlit, Diffusers, and optional voice support using <code>speech_recognition</code>.
</p>

<h2 color: #007acc;>🌟 Features</h2>
<ul>
  <li>🎙️ Voice-to-text (optional)</li>
  <li>📝 Text input for prompts</li>
  <li>🎨 Style filters (Realistic, Anime, Sketch, etc.)</li>
  <li>📏 Resolution slider</li>
  <li>🔁 Seed control for repeatable images</li>
  <li>🧠 Inference step adjustment</li>
  <li>📥 Download image button</li>
</ul>

<h2 color: #007acc;>📷 Screenshots</h2>
<p><em>Replace with your actual screenshots:</em></p>
<table>
  <tr>
    <td><img src="Screenshots/Input.png" alt="Prompt Input" width="400"></td>
    <td><img src="Screenshots/Output.png" alt="Generated Image" width="400"></td>
  </tr>
</table>

<h2 color: #007acc;>🧰 Tech Stack</h2>
<ul>
  <li><strong>UI:</strong> Streamlit</li>
  <li><strong>Speech Input:</strong> speech_recognition (local only)</li>
  <li><strong>Image Generation:</strong> Hugging Face Diffusers + Stable Diffusion</li>
  <li><strong>Audio:</strong> HTML + base64</li>
</ul>

<h2 color: #007acc;>🚀 How to Run Locally</h2>

<h3 color: #007acc;>🛠️ Prerequisites</h3>
<ul>
  <li>Python 3.9+</li>
  <li>pip</li>
  <li>GPU recommended (CPU also works)</li>
</ul>

<h3 color: #007acc;>🔧 Clone the Repo</h3>
<pre background: #f4f4f4; padding: 1em; border-left: 5px solid #007acc; overflow-x: auto;><code background: #f4f4f4; padding: 2px 4px; border-radius: 4px;>git clone https://github.com/yourusername/voice-to-image-generator.git
cd voice-to-image-generator</code></pre>

<h3 color: #007acc;>📦 Install Requirements</h3>
<pre background: #f4f4f4; padding: 1em; border-left: 5px solid #007acc; overflow-x: auto;><code background: #f4f4f4; padding: 2px 4px; >pip install -r requirements.txt</code></pre>

<h3 color: #007acc;>▶️ Run the App</h3>
<pre background: #f4f4f4; padding: 1em; border-left: 5px solid #007acc; overflow-x: auto;><code background: #f4f4f4; padding: 2px 4px; >streamlit run app.py</code></pre>

<p>Then open your browser to <a href="http://localhost:8501">http://localhost:8501</a></p>

<h2 color: #007acc;>☁️ Deploying to Streamlit Cloud</h2>
<ol>
  <li>Push to GitHub</li>
  <li>Go to <a href="https://share.streamlit.io">https://share.streamlit.io</a></li>
  <li>Connect your repo and deploy</li>
</ol>

<p><strong>Note:</strong> Voice input only works locally. For online, use the text input version.</p>

<h2 color: #007acc;>📁 Project Structure</h2>
<pre background: #f4f4f4; padding: 1em; border-left: 5px solid #007acc; overflow-x: auto;><code background: #f4f4f4; padding: 2px 4px; >
├── app.py
├── speech_to_text.py
├── image_gen.py
├── beep.mp3
├── requirements.txt
├── README.html
└── screenshots/
</code></pre>

<h2 color: #007acc;>🙌 Acknowledgements</h2>
<ul>
  <li>Hugging Face Diffusers</li>
  <li>Streamlit</li>
  <li>Stable Diffusion by Stability AI</li>
</ul>

</body>
</html>
