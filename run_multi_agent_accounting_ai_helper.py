import ast
import pathlib

SOURCE_FILE = pathlib.Path(__file__).with_name('multi_agent_bert_accounting_ai_lab.py')

if not SOURCE_FILE.exists():
    raise FileNotFoundError(f"Source file not found: {SOURCE_FILE}")

source_text = SOURCE_FILE.read_text(encoding='utf-8')
lines = source_text.splitlines()
clean_lines = []
for line in lines:
    stripped = line.lstrip()
    if stripped.startswith('!pip '):
        continue
    if stripped.startswith('from google.colab import'):
        continue
    if 'files.download(' in line:
        continue
    if stripped.startswith('import google.colab'):
        continue
    if stripped.startswith('from google.colab import sheets'):
        continue
    if stripped.startswith('from google.colab import ai'):
        continue
    clean_lines.append(line)
clean_source = '\n'.join(clean_lines)

module_ast = ast.parse(clean_source)
selected_segments = []
for node in module_ast.body:
    if isinstance(node, (ast.Import, ast.ImportFrom, ast.FunctionDef, ast.ClassDef)):
        segment = ast.get_source_segment(clean_source, node)
        if segment:
            selected_segments.append(segment)
    elif isinstance(node, ast.Assign):
        if isinstance(node.value, (ast.Constant, ast.Tuple, ast.List, ast.Dict, ast.Set)):
            segment = ast.get_source_segment(clean_source, node)
            if segment:
                selected_segments.append(segment)

# Add any required support definitions.
selected_segments.insert(0, 'from pathlib import Path')
selected_segments.insert(0, 'import pathlib')
selected_segments.insert(0, 'import os')
selected_segments.append('Path("data").mkdir(exist_ok=True)')
selected_segments.append('if __name__ == "__main__":\n    if "run_multi_agent_accounting_ai" not in globals():\n        raise RuntimeError(\"run_multi_agent_accounting_ai function not found\")\n    final = run_multi_agent_accounting_ai(show_dashboard=False)\n    print(\"Workflow completed. Output rows:\", len(final) if hasattr(final, \"__len__\") else final)')

output_text = '\n\n'.join(selected_segments)

helper_file = pathlib.Path(__file__)
helper_file.write_text(output_text, encoding='utf-8')
print(f"Created helper script: {helper_file}")
