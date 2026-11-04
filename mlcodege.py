"""ML Code Generator — polished Gradio UI.

Set GOOGLE_API_KEY before launching. The AI-agent workflow remains intentionally
close to the original project; this update focuses on UI/UX and concise prompts.
"""
import os
import gradio as gr
from smolagents import CodeAgent, DuckDuckGoSearchTool, LiteLLMModel

# Configure your API key in the environment; never hard-code secrets here.
import os

api_key = "AIzaSyDd28a4fuS6QWH01Sx6EXVMMcM3MXhHgSo"  # Replace with your actual Google API key

if not api_key:
    raise ValueError(
        "GOOGLE_API_KEY is missing. "
        "Set it in PowerShell before running the app."
    )

# Keep the project's existing model ID. If it is unavailable for your account,
# replace it with a currently supported Gemini model ID in LiteLLM format.
model = LiteLLMModel(
    model_id="gemini/gemini-3.5-flash-lite",
    api_key=api_key
)

ml_code_agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()],
    additional_authorized_imports=["pandas", "numpy", "sklearn", "json"],
    model=model,
)


def generate_ml_code(dataset_file, user_prompt):
    """Validate inputs and ask the existing agent for one focused ML solution."""
    if dataset_file is None:
        return "## Dataset needed\nUpload a CSV or Excel file, then generate your solution."
    if not user_prompt or not user_prompt.strip():
        return "## Task needed\nDescribe one machine-learning task in the prompt box."

    file_path = dataset_file if isinstance(dataset_file, str) else dataset_file.name
    full_prompt = f"""
You are a practical Python machine-learning coding assistant.
Dataset path: {file_path}
User task: {user_prompt.strip()}

Requirements:
- Load the supplied dataset using pandas and inspect its columns before selecting features.
- Complete only the requested task; keep the solution simple and concise.
- Use scikit-learn where appropriate and include necessary preprocessing.
- Avoid web searches unless the user explicitly asks for them.
- Do not use names, emails, phone numbers, or other direct personal identifiers as features.
- Do not invent evaluation scores or claim code was executed unless it was actually executed.
- Return readable Python code with brief explanations and appropriate evaluation metrics.
"""
    try:
        return str(ml_code_agent.run(full_prompt))
    except Exception as exc:
        # User-facing message stays concise; detailed tracebacks should be logged privately.
        return (
            "## Generation failed\n"
            f"**{type(exc).__name__}:** {exc}\n\n"
            "Check your API key, model ID, network connection, and package versions, then try again."
        )


PROMPT_SPENDING = (
    "Using the uploaded customer dataset, build a simple Linear Regression model "
    "to predict total spending. Split the data into training and testing sets, "
    "and report MAE and R². Keep the code concise and avoid web searches."
)
PROMPT_TIER = (
    "Using the uploaded customer dataset, build a simple Decision Tree Classifier "
    "to predict customer tier from relevant features. Split the data into training "
    "and testing sets and report accuracy. Exclude personal identifiers. Avoid web searches."
)
PROMPT_SEGMENTS = (
    "Using the uploaded customer dataset, apply K-Means clustering to total spending "
    "and total orders. Scale the features, create three customer segments, and show "
    "a simple visualization. Keep the code concise and avoid web searches."
)

CUSTOM_CSS = r"""
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap');
:root {
  --bg: #080d18; --surface: #101a2b; --surface-2: #131f33;
  --line: rgba(156, 177, 211, .16); --text: #edf3ff; --muted: #9baac2;
  --blue: #7195ff; --teal: #53e0cb;
}
.gradio-container {
  max-width: 1480px !important; margin: 0 auto !important;
  font-family: 'DM Sans', Inter, system-ui, sans-serif !important;
  background: transparent !important;
}
body {
  background:
    radial-gradient(ellipse at 8% -8%, rgba(70, 104, 210, .20), transparent 34%),
    radial-gradient(ellipse at 96% 8%, rgba(34, 188, 169, .10), transparent 27%),
    #080d18 !important;
}
#main-shell { gap: 22px !important; padding: 18px 8px 8px !important; }
.hero {
  position: relative; isolation: isolate; overflow: hidden;
  padding: clamp(26px, 4vw, 48px); border: 1px solid var(--line);
  border-radius: 28px;
  background: linear-gradient(118deg, rgba(19, 34, 61, .98), rgba(13, 25, 43, .97) 60%, rgba(12, 36, 48, .94));
  box-shadow: 0 28px 90px rgba(0,0,0,.22);
}
.hero:before { content:''; position:absolute; z-index:-1; width:360px; height:360px; right:-100px; top:-170px; border-radius:50%; border:1px solid rgba(83,224,203,.16); box-shadow:0 0 0 35px rgba(83,224,203,.025),0 0 0 75px rgba(83,224,203,.018); }
.hero:after { content:''; position:absolute; z-index:-1; width:220px; height:220px; right:7%; bottom:-170px; border-radius:50%; background:rgba(77,116,255,.15); filter:blur(18px); }
.eyebrow { display:flex; align-items:center; gap:9px; color:var(--teal); font-size:11px; font-weight:700; letter-spacing:.19em; text-transform:uppercase; margin-bottom:15px; }
.eyebrow:before { content:''; width:24px; height:2px; background:var(--teal); border-radius:2px; }
.hero h1 { margin:0 0 13px; color:#f5f8ff; font-family:'Space Grotesk',sans-serif; font-size:clamp(34px,5vw,54px); font-weight:700; letter-spacing:-.045em; line-height:1.05; }
.hero h1 span { background:linear-gradient(95deg,#8daaff,#57e1d0); -webkit-background-clip:text; background-clip:text; color:transparent; }
.hero p { max-width:780px; margin:0; color:#b1bfd6; font-size:15px; line-height:1.8; }
.hero-bottom { display:flex; flex-wrap:wrap; justify-content:space-between; align-items:center; gap:18px; margin-top:25px; }
.tech-pills { display:flex; flex-wrap:wrap; gap:8px; }
.tech-pill { border:1px solid rgba(173,193,225,.17); background:rgba(255,255,255,.035); color:#d7e3f7; padding:7px 11px; border-radius:9px; font-size:11px; font-weight:600; }
.hero-note { color:#8fa1bd; font-size:12px; }
.section-kicker { color:var(--teal); font-size:10px; font-weight:700; letter-spacing:.16em; text-transform:uppercase; margin-bottom:8px; }
.section-heading { color:#f1f5ff; font-family:'Space Grotesk',sans-serif; font-size:20px; font-weight:600; letter-spacing:-.025em; margin:0 0 5px; }
.section-desc { color:var(--muted); font-size:12px; line-height:1.65; margin:0 0 18px; }
.panel { background:linear-gradient(160deg,rgba(17,28,47,.97),rgba(12,21,36,.97)) !important; border:1px solid var(--line) !important; border-radius:22px !important; padding:clamp(17px,2.3vw,26px) !important; box-shadow:0 16px 45px rgba(0,0,0,.15) !important; }
label, .label-wrap span { color:#dce6f8 !important; font-weight:600 !important; }
textarea, input, .file-preview, .wrap { border-radius:12px !important; }
textarea, input { background:#0a1322 !important; border:1px solid rgba(148,169,204,.22) !important; color:#edf3ff !important; }
textarea:focus, input:focus { border-color:#7195ff !important; box-shadow:0 0 0 3px rgba(113,149,255,.13) !important; }
.file-preview, .upload-container { border-color:rgba(148,169,204,.25) !important; border-radius:14px !important; }
#generate-btn button { min-height:51px; border:0 !important; border-radius:13px !important; background:linear-gradient(105deg,#6488ff,#5274ee 55%,#20bba9) !important; color:white !important; font-weight:700 !important; box-shadow:0 9px 25px rgba(72,111,238,.22); transition:transform .18s ease,filter .18s ease; }
#generate-btn button:hover { transform:translateY(-2px); filter:brightness(1.08); }
#clear-btn button { min-height:48px; border-radius:12px !important; border:1px solid var(--line) !important; background:rgba(255,255,255,.035) !important; }
.quick-label { color:#9baac2; font-size:11px; font-weight:700; letter-spacing:.08em; text-transform:uppercase; margin:18px 0 9px; }
#quick-btn button { border:1px solid rgba(148,169,204,.19) !important; border-radius:10px !important; background:rgba(255,255,255,.025) !important; color:#d5e2f7 !important; font-size:11px !important; min-height:38px; }
#quick-btn button:hover { border-color:rgba(83,224,203,.45) !important; background:rgba(83,224,203,.06) !important; }
.tip { display:flex; gap:10px; align-items:flex-start; border:1px solid rgba(83,224,203,.15); background:rgba(83,224,203,.045); padding:13px 14px; border-radius:12px; color:#aabbd2; font-size:11px; line-height:1.65; margin-top:15px; }
.tip strong { color:#c7f7ee; }
#output-panel { min-height:600px; }
.output-top { display:flex; justify-content:space-between; align-items:center; gap:12px; margin-bottom:17px; }
.output-status { display:inline-flex; align-items:center; gap:7px; padding:6px 10px; border:1px solid rgba(83,224,203,.19); background:rgba(83,224,203,.055); border-radius:999px; color:#9eeadd; font-size:10px; font-weight:700; white-space:nowrap; }
.status-dot { width:6px; height:6px; border-radius:50%; background:#53e0cb; box-shadow:0 0 9px rgba(83,224,203,.55); }
#output-text { color:#dce6f8 !important; line-height:1.75 !important; }
#output-text .prose { color:#dce6f8 !important; }
#output-text pre { background:#080f1b !important; border:1px solid rgba(148,169,204,.16) !important; border-radius:13px !important; }
#output-text code { color:#b8d4ff; }
#output-text h1, #output-text h2, #output-text h3 { color:#f0f5ff !important; font-family:'Space Grotesk',sans-serif; }
.empty-state { min-height:380px; display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; border:1px dashed rgba(148,169,204,.20); border-radius:16px; padding:24px; background:rgba(4,11,21,.22); }
.empty-icon { display:flex; align-items:center; justify-content:center; width:60px; height:60px; border-radius:18px; border:1px solid rgba(113,149,255,.24); background:rgba(113,149,255,.08); color:#91adff; font-size:26px; margin-bottom:17px; }
.empty-title { color:#e7efff; font-family:'Space Grotesk',sans-serif; font-size:16px; font-weight:600; margin-bottom:8px; }
.empty-copy { max-width:300px; color:#8799b4; font-size:12px; line-height:1.8; }
.footer { display:flex; flex-wrap:wrap; justify-content:space-between; gap:10px; padding:7px 4px 2px; color:#71819c; font-size:11px; }
.footer strong { color:#9eafca; font-weight:600; }
@media (max-width: 850px) { #main-shell { padding:8px 0 !important; } .hero { border-radius:20px; } .panel { border-radius:17px !important; } #output-panel { min-height:400px; } }
"""

with gr.Blocks(theme=gr.themes.Soft(), css=CUSTOM_CSS, title="ML Code Generator | AI Data Science Workspace") as iface:
    with gr.Column(elem_id="main-shell"):
        gr.HTML(
            """
            <header class="hero">
              <div class="eyebrow">Intelligent data science workspace</div>
              <h1>From dataset to <span>ML solution.</span></h1>
              <p>Generate practical Python machine-learning code from a real dataset and a clear objective. Built for fast experiments, readable code, and data-driven decisions.</p>
              <div class="hero-bottom">
                <div class="tech-pills">
                  <span class="tech-pill">PYTHON</span><span class="tech-pill">GEMINI AI</span>
                  <span class="tech-pill">SMOLAGENTS</span><span class="tech-pill">SCIKIT-LEARN</span>
                </div>
                <div class="hero-note">Upload · Describe · Generate</div>
              </div>
            </header>
            """
        )

        with gr.Row(equal_height=False):
            with gr.Column(scale=5, min_width=300, elem_classes=["panel"]):
                gr.HTML(
                    '<div class="section-kicker">Workspace / 01</div>'
                    '<div class="section-heading">Configure your task</div>'
                    '<div class="section-desc">Start with a dataset, then describe one focused machine-learning objective.</div>'
                )
                dataset_input = gr.File(
                    label="Your dataset",
                    file_types=[".csv", ".xlsx", ".xls"],
                    type="filepath",
                )
                prompt_input = gr.Textbox(
                    label="What do you want to predict or discover?",
                    lines=4,
                    max_lines=7,
                    placeholder="Example: Predict customer spending using Linear Regression. Report MAE and R². Keep the code simple and avoid web searches.",
                )
                gr.HTML('<div class="quick-label">Quick-start prompts</div>')
                with gr.Row():
                    spending_btn = gr.Button("Spending prediction", elem_id="quick-btn", size="sm")
                    tier_btn = gr.Button("Tier classification", elem_id="quick-btn", size="sm")
                with gr.Row():
                    segment_btn = gr.Button("Customer segmentation", elem_id="quick-btn", size="sm")
                with gr.Row():
                    submit_btn = gr.Button("✦  Generate ML solution", variant="primary", elem_id="generate-btn", scale=4)
                    clear_btn = gr.ClearButton([dataset_input, prompt_input], value="Reset", elem_id="clear-btn", scale=1)
                gr.HTML(
                    '<div class="tip"><span>✦</span><span><strong>Pro tip</strong><br>'
                    'One objective per request usually gives faster, clearer results. Generated code should be reviewed before use.</span></div>'
                )

            with gr.Column(scale=7, min_width=320, elem_classes=["panel"], elem_id="output-panel"):
                gr.HTML(
                    '<div class="output-top"><div>'
                    '<div class="section-kicker">Workspace / 02</div>'
                    '<div class="section-heading">Solution workspace</div>'
                    '<div class="section-desc" style="margin-bottom:0">Your generated code and explanation will appear here.</div>'
                    '</div><span class="output-status"><span class="status-dot"></span> AI WORKSPACE</span></div>'
                )
                output_text = gr.Markdown(
                    value=(
                        '<div class="empty-state">'
                        '<div class="empty-icon">⌘</div>'
                        '<div class="empty-title">Your next idea starts here</div>'
                        '<div class="empty-copy">Upload your dataset, choose a quick-start prompt or write your own task, then generate a focused ML solution.</div>'
                        '</div>'
                    ),
                    elem_id="output-text",
                )

        gr.HTML(
            '<footer class="footer"><span><strong>ML Code Generator</strong> · AI-assisted machine learning</span>'
            '<span>Built with Gradio · smolagents · Gemini</span></footer>'
        )

    submit_btn.click(
        fn=generate_ml_code,
        inputs=[dataset_input, prompt_input],
        outputs=output_text,
        show_progress="minimal",
    )
    spending_btn.click(fn=lambda: PROMPT_SPENDING, inputs=None, outputs=prompt_input)
    tier_btn.click(fn=lambda: PROMPT_TIER, inputs=None, outputs=prompt_input)
    segment_btn.click(fn=lambda: PROMPT_SEGMENTS, inputs=None, outputs=prompt_input)

if __name__ == "__main__": 
    iface.launch()
