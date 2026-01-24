import { useState } from 'react'
import './Navbar.css'

function Navbar({ isAuthenticated, onLogout }) {
  const [showMenu, setShowMenu] = useState(false)

  return (
    <nav className="navbar">
      <div className="navbar-container">
        <div className="navbar-brand">
          <h2>DevMatch AI</h2>
        </div>
        
        <div className="navbar-menu">
          {isAuthenticated ? (
            <>
              <a href="/dashboard">Dashboard</a>
              <a href="/history">Histórico</a>
              <button className="logout-btn" onClick={onLogout}>
                Sair
              </button>
            </>
          ) : (
            <>
              <a href="/login">Login</a>
              <a href="/register">Cadastro</a>
            </>
          )}
        </div>
      </div>
    </nav>
  )
}

export default Navbar
