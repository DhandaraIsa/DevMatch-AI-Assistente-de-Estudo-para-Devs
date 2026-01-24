import { useState } from "react";
import { api, setToken } from "../api";

export default function Login({ onAuth }) {
  const [mode, setMode] = useState("login");
  const [name, setName] = useState("Dhandara");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  async function submit(e) {
    e.preventDefault();
    const url = mode === "login" ? "/auth/login" : "/auth/register";
    const payload = mode === "login" ? { email, password } : { name, email, password };
    const { data } = await api.post(url, payload);
    localStorage.setItem("token", data.access_token);
    setToken(data.access_token);
    onAuth();
  }

  return (
    <div style={{ maxWidth: 420, margin: "50px auto", color: "white" }}>
      <h1>DevMatch AI</h1>
      <p style={{ opacity: 0.85 }}>Seu assistente de estudo para devs (Python + React + IA)</p>

      <form onSubmit={submit} style={{ display: "grid", gap: 10 }}>
        {mode === "register" && (
          <input value={name} onChange={(e) => setName(e.target.value)} placeholder="Nome" />
        )}
        <input value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Email" />
        <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Senha" />
        <button type="submit">{mode === "login" ? "Entrar" : "Criar conta"}</button>
      </form>

      <button
        onClick={() => setMode(mode === "login" ? "register" : "login")}
        style={{ marginTop: 10, background: "transparent", color: "#9ae6b4", border: "none", cursor: "pointer" }}
      >
        {mode === "login" ? "Criar conta" : "Já tenho conta"}
      </button>
    </div>
  );
}
