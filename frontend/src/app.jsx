import { useEffect, useState } from "react";
import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import { setToken } from "./api";

export default function App() {
  const [authed, setAuthed] = useState(false);

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (token) {
      setToken(token);
      setAuthed(true);
    }
  }, []);

  function logout() {
    localStorage.removeItem("token");
    setToken(null);
    setAuthed(false);
  }

  return (
    <div style={{ minHeight: "100vh", background: "radial-gradient(circle at top, #2b6cb0, #111)" }}>
      {authed ? <Dashboard onLogout={logout} /> : <Login onAuth={() => setAuthed(true)} />}
    </div>
  );
}
