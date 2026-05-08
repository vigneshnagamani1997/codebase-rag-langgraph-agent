import { useState } from "react";
import Chat from "./components/Chat";
import CodeViewer from "./components/CodeViewer";
import GraphView from "./components/GraphView";

export default function App() {
  const [code, setCode] = useState("");

  return (
    <div style={{ display: "flex", height: "100vh" }}>
      <div style={{ width: "30%", borderRight: "1px solid #333" }}>
        <Chat onSelectCode={setCode} />
      </div>

      <div style={{ width: "40%", borderRight: "1px solid #333" }}>
        <CodeViewer code={code} />
      </div>

      <div style={{ width: "30%" }}>
        <GraphView />
      </div>
    </div>
  );
}