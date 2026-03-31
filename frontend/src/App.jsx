import React, { useState, useEffect } from 'react';

function App() {
  const [networkState, setNetworkState] = useState(null);

  useEffect(() => {
    const ws = new WebSocket('ws://localhost:8000/ws/dashboard');
    
    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      setNetworkState(data);
    };

    return () => {
      ws.close();
    };
  }, []);

  return (
    <div className="min-h-screen w-full bg-slate-900 text-slate-100 p-8 font-sans">
      <header className="mb-12 text-center">
        <h1 className="text-4xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-emerald-400">
          AutoLedgerAI
        </h1>
        <p className="text-slate-400 mt-2">Self-Healing Blockchain Network</p>
      </header>

      {networkState ? (
        <div className="max-w-6xl mx-auto space-y-8">
          
          <div className="bg-slate-800 rounded-xl p-6 shadow-xl border border-slate-700">
            <h2 className="text-2xl font-bold mb-4 flex items-center justify-between">
              <span>Network Consensus Health</span>
              <span className="text-emerald-400">{networkState.consensus_health.toFixed(1)}%</span>
            </h2>
            <div className="w-full bg-slate-700 rounded-full h-4">
              <div 
                className="bg-emerald-400 h-4 rounded-full transition-all duration-500"
                style={{ width: `${networkState.consensus_health}%` }}
              ></div>
            </div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            {networkState.nodes.map(node => (
              <div 
                key={node.id} 
                className={`p-6 rounded-xl border shadow-lg transition-all duration-500
                  ${node.status === 'isolated' ? 'bg-red-900/20 border-red-500/50' : 'bg-slate-800 border-slate-700'}
                `}
              >
                <div className="flex justify-between items-start mb-4">
                  <h3 className="text-lg font-bold text-slate-200">{node.id}</h3>
                  <span className={`px-2 py-1 rounded text-xs font-semibold
                    ${node.status === 'active' ? 'bg-emerald-500/20 text-emerald-400' : 'bg-red-500/20 text-red-400'}
                  `}>
                    {node.status.toUpperCase()}
                  </span>
                </div>
                
                <div className="space-y-2">
                  <div className="flex justify-between text-sm">
                    <span className="text-slate-400">Trust Score</span>
                    <span className={`font-mono font-medium
                      ${node.trust_score > 70 ? 'text-emerald-400' : node.trust_score > 40 ? 'text-amber-400' : 'text-red-400'}
                    `}>
                      {node.trust_score.toFixed(1)}
                    </span>
                  </div>
                  
                  <div className="w-full bg-slate-700 rounded-full h-2">
                    <div 
                      className={`h-2 rounded-full transition-all duration-500
                        ${node.trust_score > 70 ? 'bg-emerald-400' : node.trust_score > 40 ? 'bg-amber-400' : 'bg-red-400'}
                      `}
                      style={{ width: `${node.trust_score}%` }}
                    ></div>
                  </div>
                  
                  {node.is_malicious && (
                    <div className="mt-4 text-xs font-semibold text-red-400 bg-red-400/10 py-1 px-2 rounded w-max inline-block">
                      Malicious Activity Detected
                    </div>
                  )}
                </div>
              </div>
            ))}
          </div>
          
        </div>
      ) : (
        <div className="flex justify-center items-center h-64">
          <div className="animate-pulse flex space-x-4">
            <div className="h-12 w-12 bg-slate-700 rounded-full"></div>
            <div className="space-y-3">
              <div className="h-4 w-48 bg-slate-700 rounded"></div>
              <div className="h-4 w-32 bg-slate-700 rounded"></div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
