import { useState } from "react";

export default function Chat({ onSelectCode }: any) {
  const [messages, setMessages] = useState<any[]>([]);
  const [input, setInput] = useState("");

  const sendMessage = async () => {
    if (!input) return;

    const userMsg = { role: "user", content: input };
    setMessages(prev => [...prev, userMsg]);

    const res = await fetch(
      `http://127.0.0.1:8000/query?q=${encodeURIComponent(input)}`
    );
    const data = await res.json();

    const botMsg = {
      role: "assistant",
      content: data.answer,
      sources: data.sources || []
    };

    setMessages(prev => [...prev, botMsg]);
    setInput("");
  };

  return (
    <div style={{ padding: 10 }}>
      <h3>AI Assistant</h3>

      <div style={{ height: "80vh", overflowY: "auto" }}>
        {messages.map((m, i) => (
          <div key={i}>
            <b>{m.role}</b>: {m.content}
            {m.sources?.length > 0 && (
              <button onClick={() => onSelectCode(m.sources[0])}>
                View Code
              </button>
            )}
          </div>
        ))}
      </div>

      <input
        value={input}
        onChange={(e) => setInput(e.target.value)}
        style={{ width: "80%" }}
      />
      <button onClick={sendMessage}>Send</button>
    </div>
  );
}