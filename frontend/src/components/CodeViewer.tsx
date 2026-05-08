import Editor from "@monaco-editor/react";

export default function CodeViewer({ code }: any) {
  return (
    <Editor
      height="100%"
      defaultLanguage="python"
      value={code || "# Select code to view"}
      theme="vs-dark"
    />
  );
}