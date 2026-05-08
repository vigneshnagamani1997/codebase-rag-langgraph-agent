from app.agent.tools.search import search_code
from app.agent.tools.file_reader import read_file
from app.agent.tools.code_analyzer import analyze_code
from app.agent.prompts import AGENT_PROMPT
from anthropic import Anthropic
import os

client = Anthropic(api_key=os.getenv("CLAUDE_API_KEY"))

TOOLS = {
    "search_code": search_code,
    "read_file": read_file,
    "analyze_code": analyze_code,
}

def run_agent(query, max_steps=5):
    context = ""
    
    for step in range(max_steps):
        prompt = AGENT_PROMPT.format(query=query, context=context)

        response = client.messages.create(
            model="claude-3-sonnet-20240229",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        output = response.content[0].text

        if "FINAL_ANSWER:" in output:
            return output.split("FINAL_ANSWER:")[1].strip()

        # Tool call parsing (simple version)
        if "TOOL:" in output:
            tool_name = output.split("TOOL:")[1].split("\n")[0].strip()
            tool_input = output.split("INPUT:")[1].strip()

            tool_fn = TOOLS.get(tool_name)
            if tool_fn:
                result = tool_fn(tool_input)
                context += f"\nTool {tool_name} result:\n{result}\n"

    return "Agent failed to converge."