from app.agent.tools.search import search_code
from app.agent.tools.file_reader import read_file
from app.agent.tools.code_analyzer import analyze_code
from app.agent.prompts import AGENT_PROMPT

import ollama

TOOLS = {
    "search_code": search_code,
    "read_file": read_file,
    "analyze_code": analyze_code,
}

def call_llm(prompt):
    response = ollama.chat(
        model="llama3",   # or mistral, codellama, etc.
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response["message"]["content"]


def run_agent(query, max_steps=5):
    context = ""

    for step in range(max_steps):
        prompt = AGENT_PROMPT.format(query=query, context=context)

        output = call_llm(prompt)

        # Debug (optional)
        print(f"\nStep {step} output:\n", output)

        if "FINAL_ANSWER:" in output:
            return output.split("FINAL_ANSWER:")[1].strip()

        # Tool call parsing
        if "TOOL:" in output:
            try:
                tool_name = output.split("TOOL:")[1].split("\n")[0].strip()
                tool_input = output.split("INPUT:")[1].strip()

                tool_fn = TOOLS.get(tool_name)

                if tool_fn:
                    result = tool_fn(tool_input)
                    context += f"\nTool {tool_name} result:\n{result}\n"
            except Exception as e:
                context += f"\nTool execution error: {str(e)}\n"

    return "Agent failed to converge."