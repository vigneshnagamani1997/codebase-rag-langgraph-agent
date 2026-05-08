import ReactFlow from "reactflow";
import "reactflow/dist/style.css";
import { useEffect, useState } from "react";

export default function GraphView() {
  const [elements, setElements] = useState<any[]>([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/graph")
      .then(res => res.json())
      .then(data => {
        const nodes = data.nodes.map((n: any, i: number) => ({
          id: n.id,
          data: { label: n.id },
          position: { x: Math.random() * 400, y: Math.random() * 400 }
        }));

        const edges = data.edges.map((e: any, i: number) => ({
          id: `e-${i}`,
          source: e.source,
          target: e.target
        }));

        setElements([...nodes, ...edges]);
      })
      .catch(() => {
        setElements([]);
      });
  }, []);

  return <ReactFlow nodes={elements} edges={[]} />;
}