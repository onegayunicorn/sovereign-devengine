import React, { useState, useEffect } from 'react'

const CHANNELS = [
  { name: 'Base',  freq: '7.83 Hz',   color: '#336699' },
  { name: 'Violet', freq: '7.83×φ',  color: '#b333e6' },
  { name: 'Life',  freq: '15.66 Hz',  color: '#33e666' },
  { name: 'Gold',  freq: '7.83×φ²', color: '#ffd933' },
  { name: 'Field', freq: '7.83÷φ',  color: '#80e6b3' },
]

export default function App() {
  const [paired, setPaired] = useState(false)
  const [timeLeft, setTimeLeft] = useState(0)
  const [log, setLog] = useState(['Sovereign Dev Engine ready.'])

  useEffect(() => {
    // Poll handshake status if available
    const id = setInterval(async () => {
      try {
        const r = await fetch('http://localhost:5000/status')
        const d = await r.json()
        setPaired(d.paired)
        setTimeLeft(d.time_remaining)
      } catch {}
    }, 2000)
    return () => clearInterval(id)
  }, [])

  const addLog = (msg) => setLog(prev => [...prev.slice(-20), msg])

  return (
    <div className="app">
      <header>
        <h1>⚡ SOVEREIGN DEV ENGINE</h1>
        <p className="tagline">Zero-Cloud · Local-First · PHOTONIC-Ω</p>
      </header>

      <section className="status-grid">
        <div className={`card ${paired ? 'ok' : 'warn'}`}>
          <h3>Handshake</h3>
          <p>{paired ? '✅ Paired' : '⏳ Awaiting PIN'}</p>
          {!paired && timeLeft > 0 && <small>{timeLeft}s remaining</small>}
        </div>
        <div className="card">
          <h3>Xbox Portal</h3>
          <p>Port 11443</p>
          <button onClick={() => addLog('Deploy triggered — check console')}>Deploy</button>
        </div>
        <div className="card">
          <h3>Build</h3>
          <p>Ready</p>
          <button onClick={() => addLog('Build started...')}>Build</button>
        </div>
      </section>

      <section className="channels">
        <h2>PHOTONIC-Ω Channels</h2>
        <div className="channel-row">
          {CHANNELS.map(c => (
            <div key={c.name} className="channel" style={{ borderColor: c.color }}>
              <span className="dot" style={{ background: c.color }} />
              <strong>{c.name}</strong>
              <small>{c.freq}</small>
            </div>
          ))}
        </div>
      </section>

      <section className="terminal">
        <h3>Log</h3>
        <pre>{log.join('\n')}</pre>
      </section>
    </div>
  )
}
