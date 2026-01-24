import { useEffect, useState } from "react";
import { api } from "../api";
import Card from "../components/Card";

export default function Dashboard({ onLogout }) {
  const [topic, setTopic] = useState("React");
  const [level, setLevel] = useState("medium");
  const [errorText, setErrorText] = useState("");
  const [result, setResult] = useState("");
  const [history, setHistory] = useState([]);

  async function loadHistory() {
    const { data } = await api.get("/history");
    setHistory(data);
  }

  useEffect(() => { loadHistory(); }, []);

  async function ask(kind) {
    setResult("Gerando resposta...");
    const payload =
      kind === "plan" ? { topic, level } :
      kind === "questions" ? { topic, level } :
      { topic, level, error_text: errorText };

    const { data } = await api.post(`/ai/${kind}`, payload);
    setResult(data.content);
    loadHistory();
  }

  return (
    <div style={{ color: "white", maxWidth: 1100, margin: "24px auto", padding: 12 }}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
        <h2>DevMatch AI — Dashboard</h2>
        <button onClick={onLogout}>Sair</button>
      </div>

      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 12 }}>
        <Card title="Configurar seu estudo">
          <div style={{ display: "grid", gap: 10 }}>
            <input value={topic} onChange={(e) => setTopic(e.target.value)} placeholder="Tema (ex: SQL, React, Python)" />
            <select value={level} onChange={(e) => setLevel(e.target.value)}>
              <option value="beginner">Iniciante</option>
              <option value="medium">Médio</option>
              <option value="advanced">Avançado</option>
            </select>
            <div style={{ display: "flex", gap: 8, flexWrap: "wrap" }}>
              <button onClick={() => ask("plan")}>Gerar plano 7 dias</button>
              <button onClick={() => ask("questions")}>Gerar perguntas</button>
            </div>
          </div>
        </Card>

        <Card title="Explicar erro">
          <textarea
            rows={7}
            value={errorText}
            onChange={(e) => setErrorText(e.target.value)}
            placeholder="Cole aqui seu erro/código..."
            style={{ width: "100%" }}
          />
          <button onClick={() => ask("explain")} style={{ marginTop: 10 }}>Explicar e corrigir</button>
        </Card>

        <Card title="Resultado (Markdown)">
          <pre style={{ whiteSpace: "pre-wrap" }}>{result}</pre>
        </Card>

        <Card title="Histórico">
          <div style={{ display: "grid", gap: 8, maxHeight: 360, overflow: "auto" }}>
            {history.map((h) => (
              <div key={h.id} style={{ border: "1px solid rgba(255,255,255,0.15)", borderRadius: 12, padding: 10 }}>
                <strong>{h.kind.toUpperCase()}</strong> — {h.topic} ({h.level})
                <div style={{ opacity: 0.8, fontSize: 12 }}>{new Date(h.created_at).toLocaleString()}</div>
              </div>
            ))}
          </div>
        </Card>
      </div>
    </div>
  );
}
