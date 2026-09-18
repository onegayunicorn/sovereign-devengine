import React, { useEffect, useState } from 'react'

const PHI = 1.61803399
const SCHUMANN = 7.83
const HANDSHAKE_URL = import.meta.env.VITE_HANDSHAKE_URL || 'http://127.0.0.1:5000'

const CHANNELS = [
  { name: 'Base',   freq: SCHUMANN,             color: '#3b82f6' },
  { name: 'Violet', freq: SCHUMANN * PHI,       color: '#a855f7' },
  { name: 'Life',   freq: SCHUMANN * 2,         color: '#22c55e' },
  { name: 'Gold',   freq: SCHUMANN * PHI * PHI, color: '#eab308' },
  { name: 'Field',  freq: SCHUMANN / PHI,       color: '#34d399' },
]

export default function App() {
  const [pairing, setPairing] = useState({ paired: false, reachable: false })
  const [deploying, setDeploying] = useState(false)
  const [log, setLog] = useState([{ t: 'boot', m: 'Sovereign Dev Engine online.' }])

  const push = (m) => setLog(p => [...p.slice(-80), { t: new Date().toLocaleTimeString(), m }])

  useEffect(() => {
    let alive = true
    const poll = async () => {
      try {
        const r = await fetch(`${HANDSHAKE_URL}/status`)
        const j = await r.json()
        if (alive) setPairing({ ...j, reachable: true })
      } catch {
        if (alive) setPairing(p => ({ ...p, reachable: false }))
      }
    }
    poll()
    const id = setInterval(poll, 3000)
    return () => { alive = false; clearInterval(id) }
  }, [])

  const deploy = async () => {
    setDeploying(true)
    push('▶ Deploy → Xbox :11443 …')
    try {
      const r = await fetch(`${HANDSHAKE_URL}/paean/deploy`, { method: 'POST' })
      const j = await r.json()
      push(j.msg || '✔ Deploy triggered — check your Xbox')
    } catch {
      push('✖ Bridge offline — run handshake.py first')
    } finally {
      setDeploying(false)
    }
  }

  const paired = pairing.reachable && pairing.paired

  return (
    <div className="shell">
      <header className="topbar">
        <h1>⚡ Sovereign <span>Dev Engine</span></h1>
        <div className="pills">
          <span className={`pill ${paired ? 'ok' : 'bad'}`}>
            {paired ? '● Paired' : '○ Unpaired'}
          </span>
          <span className={`pill ${pairing.reachable ? 'ok' : 'bad'}`}>
            {pairing.reachable ? '● Daemon Live' : '○ Offline'}
          </span>
        </div>
      </header>

      <section className="channels">
        <h2>PHOTONIC-Ω · 5-Channel Resonance</h2>
        <div className="grid">
          {CHANNELS.map(c => (
            <div className="chan" key={c.name}>
              <i className="dot" style={{
                background: c.color,
                animationDuration: `${(1/(c.freq/4)).toFixed(2)}s`
              }} />
              <span className="cname">{c.name}</span>
              <span className="cfreq">{c.freq.toFixed(2)} Hz</span>
            </div>
          ))}
        </div>
      </section>

      <section className="deploy">
        <button onClick={deploy} disabled={deploying}>
          {deploying ? 'Deploying…' : '🎮 Deploy to Xbox'}
        </button>
      </section>

      <section className="terminal">
        <div className="tbar">Build Log</div>
        <div className="tbody">
          {log.map((l, i) => (
            <div key={i}><span className="ts">[{l.t}]</span> {l.m}</div>
          ))}
        </div>
      </section>
    </div>
  )
}
