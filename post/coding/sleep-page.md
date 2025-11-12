## Code something that will put me to sleep now

Nice — I’ll give you a **ready-to-run, self-contained** webpage you can open in any modern browser. It implements the breathing cycles, progressive muscle relaxation, countdown-to-sleep visualization, optional speech guidance (Web Speech API), gentle ambient sound (Web Audio pink noise + slow low-frequency oscillator), simple animations, and controls (start/pause/stop, speech on/off, volume, speed).

Copy the entire code below into a file named `sleep.html` and open it in Chrome/Firefox/Edge/Safari. No internet required.

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Sleep Guide — Breathing + Relaxation</title>
  <style>
    :root{
      --bg:#0b1020;
      --card:#0f1724;
      --muted:#9aa7b2;
      --accent:#7fb3c9;
      --accent-2:#98d4c6;
      --glass: rgba(255,255,255,0.04);
      --radius:16px;
      font-family: Inter, "Helvetica Neue", Arial, sans-serif;
      color-scheme: dark;
    }
    *{box-sizing:border-box}
    html,body{height:100%;margin:0;background:radial-gradient(circle at 30% 10%, rgba(40,60,80,0.12), transparent 10%), var(--bg); color:#e8f1f4}
    .wrap{min-height:100%;display:flex;align-items:center;justify-content:center;padding:28px}
    .card{
      width:980px; max-width:98vw; background:linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));
      border:1px solid rgba(255,255,255,0.04); border-radius:var(--radius); padding:22px; display:grid; gap:18px;
      grid-template-columns: 1fr 360px;
      box-shadow: 0 10px 40px rgba(0,0,0,0.6);
    }
    .left{padding:18px 10px}
    h1{margin:0 0 6px;font-weight:600;font-size:20px}
    p.lead{margin:0;color:var(--muted);font-size:13px}
    .visual{
      margin-top:18px; height:420px; border-radius:12px; background: linear-gradient(180deg, rgba(255,255,255,0.012), rgba(255,255,255,0.008));
      display:flex; align-items:center; justify-content:center; position:relative; overflow:hidden;
      border:1px solid rgba(255,255,255,0.03);
    }
    /* breathing circle */
    .breath-circle{
      width:220px; height:220px; border-radius:50%; display:flex; align-items:center; justify-content:center;
      backdrop-filter: blur(6px);
      transition: transform 1s ease-in-out, box-shadow 1s ease-in-out;
      box-shadow: 0 8px 30px rgba(10,20,30,0.7);
    }
    .breath-text{ text-align:center; }
    .big{font-size:40px; font-weight:600; margin:0}
    .small{font-size:14px; color:var(--muted); margin-top:6px}
    /* right column controls */
    .right{padding:18px; border-left:1px dashed rgba(255,255,255,0.02)}
    .controls{display:flex; gap:8px; margin-bottom:12px; flex-wrap:wrap}
    button{background:var(--glass); border:1px solid rgba(255,255,255,0.04); color:inherit; padding:10px 12px; border-radius:10px; cursor:pointer}
    button.primary{background:linear-gradient(90deg,var(--accent),var(--accent-2)); color:#072227; font-weight:700}
    .slider{width:100%}
    label{display:block;font-size:13px;color:var(--muted); margin-bottom:6px}
    .row{display:flex; gap:8px; align-items:center}
    .script{font-size:14px; line-height:1.5; color:#dfeef2; background: rgba(255,255,255,0.02); padding:10px; border-radius:8px; max-height:220px; overflow:auto}
    .footer{font-size:12px; color:var(--muted); margin-top:10px}
    /* countdown */
    .countdown{position:absolute; right:18px; top:18px; background:rgba(0,0,0,0.28); padding:6px 10px;border-radius:8px;font-size:18px}
    /* small screens */
    @media (max-width:900px){
      .card{grid-template-columns: 1fr; padding:16px}
      .right{border-left:none;border-top:1px dashed rgba(255,255,255,0.02)}
      .visual{height:360px}
    }
  </style>
</head>
<body>
  <div class="wrap">
    <main class="card" role="main" aria-labelledby="title">
      <section class="left">
        <h1 id="title">Sleep Guide — breathing + progressive relaxation</h1>
        <p class="lead">Start the session below. Use speech on/off — the guide will gently speak each step. If speech isn't available, read the displayed lines slowly.</p>

        <div class="visual" aria-hidden="false">
          <div class="countdown" id="countDisplay" aria-live="polite">Ready</div>
          <div id="breathCircle" class="breath-circle" aria-hidden="true">
            <div class="breath-text">
              <div id="phaseLabel" class="big">Breathe</div>
              <div id="phaseSub" class="small">Press Start</div>
            </div>
          </div>
        </div>

        <div style="margin-top:14px; display:flex; gap:10px; align-items:center; justify-content:space-between; flex-wrap:wrap">
          <div style="max-width:65%">
            <label for="sessionSelect">Session pattern</label>
            <select id="sessionSelect" aria-label="Session pattern">
              <option value="short">2-minute Reset (4 rounds) — 4/7/8</option>
              <option value="relax">12-minute Progressive Relaxation</option>
              <option value="float">Float Visualization + 20→1 countdown (about 8 minutes)</option>
              <option value="full" selected>Full Guided (breathing + progressive + countdown, ~16–20 min)</option>
            </select>
          </div>
          <div style="min-width:220px">
            <label for="speed">Speech Speed</label>
            <input id="speed" class="slider" type="range" min="0.6" max="1.4" step="0.05" value="1" />
          </div>
        </div>

        <div style="margin-top:10px; display:flex; gap:10px; align-items:center; flex-wrap:wrap">
          <div class="controls" role="group" aria-label="Playback controls">
            <button id="startBtn" class="primary">Start</button>
            <button id="pauseBtn">Pause</button>
            <button id="stopBtn">Stop</button>
            <button id="voiceToggle">Speech: On</button>
          </div>
          <div style="display:flex; gap:8px; align-items:center;">
            <label for="volume" style="margin:0">Ambient volume</label>
            <input id="volume" type="range" min="0" max="1" step="0.01" value="0.18" style="width:120px" />
          </div>
        </div>

        <div style="margin-top:16px">
          <label>Live script (spoken lines)</label>
          <div id="script" class="script" aria-live="polite">
            Press <strong>Start</strong> to begin. Spoken lines will appear here in order.
          </div>
          <div class="footer">Tip: Lie down, dim lights, and allow your breathing to match the circle animation. If you prefer silence, turn Speech Off.</div>
        </div>
      </section>

      <aside class="right" aria-label="Settings and quick actions">
        <div>
          <label>Quick actions</label>
          <div class="row" style="margin-bottom:12px">
            <button id="twoMin">2-min Reset</button>
            <button id="prog">Start Progressive</button>
            <button id="countOnly">Countdown Only</button>
          </div>

          <label for="voiceSelect">Voice (speech)</label>
          <select id="voiceSelect" style="width:100%" aria-label="Choose voice"></select>

          <div style="margin-top:12px">
            <label>Ambient sound options</label>
            <div class="row" style="margin-top:6px">
              <button id="toggleNoise">Toggle Noise</button>
              <button id="toggleTone">Toggle Tone</button>
            </div>
            <div style="margin-top:8px">
              <label for="toneHz">Tone frequency (Hz)</label>
              <input id="toneHz" type="range" min="40" max="220" value="80" />
            </div>
          </div>

        </div>
      </aside>
    </main>
  </div>

  <script>
  // Sleep Guide — self-contained browser implementation
  // - uses Web Speech API (if available) for spoken guidance
  // - uses Web Audio API for gentle ambient sound (pink-ish noise + slow LFO)
  // - patterns: short 4/7/8, progressive muscle relaxation, float visualization with countdown

  // ---------- Utilities ----------
  const el = id => document.getElementById(id);
  const scriptEl = el('script');
  const phaseLabel = el('phaseLabel');
  const phaseSub = el('phaseSub');
  const breathCircle = el('breathCircle');
  const countDisplay = el('countDisplay');

  let running = false;
  let paused = false;
  let queueTimer = null;
  let currentUtter = null;
  let speechOn = true;
  let voices = [];
  let synth = window.speechSynthesis || null;
  const sessionSelect = el('sessionSelect');
  const speedInput = el('speed');
  const volumeInput = el('volume');

  // ---------- Speech helpers ----------
  function speakLine(text, opts = {}) {
    // Adds text to script area and optionally speaks it
    const node = document.createElement('div');
    node.textContent = text;
    scriptEl.appendChild(node);
    scriptEl.scrollTop = scriptEl.scrollHeight;

    if (!speechOn || !synth) return Promise.resolve();
    return new Promise((resolve) => {
      const u = new SpeechSynthesisUtterance(text);
      u.rate = parseFloat(speedInput.value) || 1;
      if (voices[0]) u.voice = voices.find(v => v.name === el('voiceSelect').value) || voices[0];
      currentUtter = u;
      u.onend = () => { currentUtter = null; resolve(); };
      u.onerror = () => { currentUtter = null; resolve(); };
      synth.speak(u);
    });
  }

  if (synth) {
    // populate voices
    function refreshVoices(){
      voices = synth.getVoices().filter(v => v.lang && v.lang.startsWith('en')) // prefer english voices
      const sel = el('voiceSelect');
      sel.innerHTML = '';
      (voices.length ? voices : synth.getVoices()).forEach(v=>{
        const opt = document.createElement('option');
        opt.value = v.name; opt.textContent = `${v.name} — ${v.lang}`;
        sel.appendChild(opt);
      });
    }
    refreshVoices();
    if (synth.onvoiceschanged !== undefined) synth.onvoiceschanged = refreshVoices;
  } else {
    el('voiceSelect').style.display='none';
  }

  // ---------- Audio: gentle noise + tone ----------
  let audioCtx, noiseNode, noiseGain, lfoGain, toneOsc, toneGain;
  function initAudio() {
    if (audioCtx) return;
    audioCtx = new (window.AudioContext || window.webkitAudioContext)();

    // Noise (colored) using buffer: create simple "pink-ish" by filtering white
    const bufferSize = 2 * audioCtx.sampleRate;
    const noiseBuffer = audioCtx.createBuffer(1, bufferSize, audioCtx.sampleRate);
    const output = noiseBuffer.getChannelData(0);
    for (let i = 0; i < bufferSize; i++) {
      output[i] = Math.random() * 2 - 1;
    }
    noiseNode = audioCtx.createBufferSource();
    noiseNode.buffer = noiseBuffer;
    noiseNode.loop = true;

    // Create a lowpass to reduce harshness (make it warmer)
    const lp = audioCtx.createBiquadFilter();
    lp.type = 'lowpass';
    lp.frequency.value = 1200;

    noiseGain = audioCtx.createGain();
    noiseGain.gain.value = Number(volumeInput.value) || 0.18;

    noiseNode.connect(lp);
    lp.connect(noiseGain);
    noiseGain.connect(audioCtx.destination);

    // tone oscillator + slow amplitude LFO for subtle pulsing
    toneOsc = audioCtx.createOscillator();
    toneOsc.type = 'sine';
    toneOsc.frequency.value = Number(el('toneHz').value) || 80;
    toneGain = audioCtx.createGain();
    toneGain.gain.value = 0.0; // start quiet
    toneOsc.connect(toneGain);
    toneGain.connect(audioCtx.destination);

    // LFO to gently pulse the tone volume
    const lfo = audioCtx.createOscillator();
    lfo.type = 'sine';
    lfo.frequency.value = 0.05; // very slow pulse (20s cycle)
    lfoGain = audioCtx.createGain();
    lfoGain.gain.value = 0.01; // small depth
    lfo.connect(lfoGain);
    lfoGain.connect(toneGain.gain);

    noiseNode.start();
    toneOsc.start();
    lfo.start();
  }

  function setAmbientVolume(v){
    if (noiseGain) noiseGain.gain.value = v;
  }

  el('volume').addEventListener('input', (e)=> {
    setAmbientVolume(Number(e.target.value));
  });
  el('toneHz').addEventListener('input', (e)=>{
    if (toneOsc) toneOsc.frequency.setValueAtTime(Number(e.target.value), audioCtx.currentTime);
  });

  let noiseEnabled = true, toneEnabled = false;
  el('toggleNoise').addEventListener('click', () => {
    initAudio();
    noiseEnabled = !noiseEnabled;
    noiseGain.gain.setValueAtTime(noiseEnabled ? Number(volumeInput.value) : 0, audioCtx.currentTime);
    el('toggleNoise').textContent = noiseEnabled ? 'Noise: On' : 'Noise: Off';
  });
  el('toggleTone').addEventListener('click', () => {
    initAudio();
    toneEnabled = !toneEnabled;
    toneGain.gain.setValueAtTime(toneEnabled ? 0.02 : 0.0, audioCtx.currentTime);
    el('toggleTone').textContent = toneEnabled ? 'Tone: On' : 'Tone: Off';
  });

  // ---------- Animation helpers ----------
  function animateBreath(scale, shadowSize=30){
    breathCircle.style.transform = `scale(${scale})`;
    breathCircle.style.boxShadow = `0 ${shadowSize}px ${shadowSize*1.5}px rgba(5,20,30,0.6)`;
  }

  // ---------- Session sequences ----------
  // Each sequence: array of {label, sub, durationSec, speakText}
  function buildTwoMinuteReset(){
    // 4 rounds of 4/7/8 breathing; each round ~ (4+7+8)=19s including small pauses => ~76s, but we'll run 4 rounds exactly as in the guide
    const rounds = 4;
    const seq = [];
    for(let r=1;r<=rounds;r++){
      seq.push({label:`Inhale`, sub:`Count 1–4`, duration:4, speak:`Breathe in for four seconds.`});
      seq.push({label:`Hold`, sub:`Count 1–7`, duration:7, speak:`Hold for seven seconds.`});
      seq.push({label:`Exhale`, sub:`Count 1–8`, duration:8, speak:`Exhale fully for eight seconds.`});
      seq.push({label:``, sub:`Pause`, duration:1, speak:``});
    }
    seq.push({label:`Complete`, sub:`Two-minute reset finished`, duration:0, speak:`Good. If you feel calmer, continue to lie still and notice the heaviness.`});
    return seq;
  }

  function buildProgressive(){
    // progressive muscle relaxation — major muscle groups with 5s tension/relax transitions + breathing
    const groups = [
      {name:'Head & face', speak:'Tense your face: clench jaw, screw eyes shut, lift eyebrows. Hold five seconds then release.'},
      {name:'Neck & shoulders', speak:'Shrug shoulders up, hold five seconds, then drop them away from your ears.'},
      {name:'Arms & hands', speak:'Clench fists, tense forearms and biceps. Hold five seconds, then relax.'},
      {name:'Chest & belly', speak:'Take a full gentle breath and hold for three seconds, then exhale slowly.'},
      {name:'Back', speak:'Arch slightly to feel the muscles, hold five seconds, then let them soften.'},
      {name:'Hips & buttocks', speak:'Tighten your glutes for five seconds, then let go.'},
      {name:'Legs & feet', speak:'Tense thighs, calves, and point toes for five seconds, then release.'}
    ];
    const seq = [];
    seq.push({label:'Settle', sub:'Breathe slowly', duration:6, speak:'Make yourself comfortable on your back. Take a few slow, grounding breaths.'});
    for(const g of groups){
      seq.push({label:g.name, sub:'Tighten for 5s', duration:5, speak:g.speak});
      seq.push({label:g.name, sub:'Relax', duration:6, speak:`Now relax ${g.name.toLowerCase()}. Notice warmth and heaviness.`});
    }
    seq.push({label:'Finish', sub:'Deep breath', duration:8, speak:'Now take two slow breaths and feel your whole body sink into the surface beneath you.'});
    return seq;
  }

  function buildFloatCountdown(){
    // Float + countdown 20→1, each number = a breath (approx 4-6s each) — we'll use 5s per count to be gentle
    const seq = [];
    seq.push({label:'Float', sub:'Imagine a cloud', duration:8, speak:'Imagine lying on a warm, soft cloud. Let it hold you.'});
    let count = 20;
    for(let i=0;i<count;i++){
      seq.push({label:`Count ${count-i}`, sub:`Breathe`, duration:5, speak:`${count-i}`});
    }
    seq.push({label:'Done', sub:'Stay with the feeling', duration:0, speak:'Let go of counting now. Stay with the floating sensation and breathe gently.'});
    return seq;
  }

  function buildFull(){
    // combine breathing, progressive, countdown
    return [
      ...buildTwoMinuteReset().slice(0,-1),
      ...buildProgressive(),
      ...buildFloatCountdown()
    ];
  }

  // ---------- Runner ----------
  let sequence = [];
  let seqIndex = 0;
  let phaseRemaining = 0;
  function loadSession(name){
    if (name==='short') sequence = buildTwoMinuteReset();
    else if (name==='relax') sequence = buildProgressive();
    else if (name==='float') sequence = buildFloatCountdown();
    else sequence = buildFull();
  }
  function startSession(nameOverride){
    if (running) return;
    // ensure audio context started by user gesture
    try { initAudio(); } catch(e){}
    const name = nameOverride || sessionSelect.value;
    loadSession(name);
    running = true; paused = false;
    seqIndex = 0;
    scriptEl.innerHTML = '';
    runNext();
    el('startBtn').textContent = 'Running...';
  }

  function runNext(){
    if (!running || paused) return;
    if (seqIndex >= sequence.length){
      finishAll();
      return;
    }
    const item = sequence[seqIndex];
    seqIndex++;
    phaseLabel.textContent = item.label || '';
    phaseSub.textContent = item.sub || '';
    // animate circle depending on inhale/exhale or neutral
    // simple heuristic:
    const txt = (item.label || '').toLowerCase();
    if (txt.includes('inhale') || txt.includes('in')) animateBreath(1.18, 12);
    else if (txt.includes('exhale') || txt.includes('out') || txt.includes('relax')) animateBreath(0.86, 4);
    else animateBreath(1.0, 8);

    // set countdown display for phases with duration
    if (item.duration && item.duration > 0){
      phaseRemaining = item.duration;
      countDisplay.textContent = `${phaseRemaining}s`;
      // speak then start per-second countdown
      speakLine(item.speak || item.label || '').then(()=> {
        // per-second tick
        const tick = () => {
          if (!running || paused) return;
          phaseRemaining--;
          countDisplay.textContent = `${phaseRemaining}s`;
          if (phaseRemaining <= 0){
            // small pause before next
            countDisplay.textContent = '';
            setTimeout(()=> runNext(), 350);
          } else {
            queueTimer = setTimeout(tick, 1000);
          }
        };
        queueTimer = setTimeout(tick, 1000);
      });
    } else {
      // zero-duration: just display and speak once
      countDisplay.textContent = '';
      speakLine(item.speak || item.label || '').then(()=> setTimeout(()=> runNext(), 350));
    }
  }

  function pauseSession(){
    if (!running) return;
    paused = !paused;
    if (paused){
      clearTimeout(queueTimer);
      el('pauseBtn').textContent = 'Resume';
      phaseSub.textContent = 'Paused';
      if (synth && currentUtter) synth.pause();
    } else {
      el('pauseBtn').textContent = 'Pause';
      if (synth && currentUtter) synth.resume();
      runNext();
    }
  }

  function stopSession(){
    running = false;
    paused = false;
    clearTimeout(queueTimer);
    if (synth) { try { synth.cancel(); } catch(e){} }
    seqIndex = 0;
    phaseLabel.textContent = 'Breathe';
    phaseSub.textContent = 'Press Start';
    countDisplay.textContent = 'Stopped';
    animateBreath(1.0, 8);
    el('startBtn').textContent = 'Start';
  }

  function finishAll(){
    running = false;
    paused = false;
    el('startBtn').textContent = 'Start';
    phaseLabel.textContent = 'Complete';
    phaseSub.textContent = 'You may relax here';
    countDisplay.textContent = '';
    animateBreath(1.0,8);
    speakLine('Session complete. Allow yourself to drift into sleep.').then(()=>{});
  }

  // ---------- UI wiring ----------
  el('startBtn').addEventListener('click', ()=> {
    if (!running) {
      // resume audio ctx if suspended (some browsers require resume on gesture)
      if (audioCtx && audioCtx.state === 'suspended') audioCtx.resume();
      startSession();
    }
  });
  el('pauseBtn').addEventListener('click', pauseSession);
  el('stopBtn').addEventListener('click', stopSession);

  el('voiceToggle').addEventListener('click', ()=> {
    speechOn = !speechOn;
    el('voiceToggle').textContent = `Speech: ${speechOn ? 'On' : 'Off'}`;
  });

  // quick action buttons
  el('twoMin').addEventListener('click', ()=> { stopSession(); startSession('short'); });
  el('prog').addEventListener('click', ()=> { stopSession(); startSession('relax'); });
  el('countOnly').addEventListener('click', ()=> { stopSession(); startSession('float'); });

  // sessionSelect change resets UI script
  sessionSelect.addEventListener('change', ()=> {
    scriptEl.innerHTML = 'Press Start to begin this session.';
  });

  // speed input updates spoken rate; show small feedback
  speedInput.addEventListener('input', ()=> {
    const v = Number(speedInput.value).toFixed(2);
    speedInput.title = `Speech rate ${v}x`;
  });

  // clean up on unload
  window.addEventListener('beforeunload', ()=> {
    stopSession();
    if (audioCtx) try { audioCtx.close(); } catch(e){}
  });

  // ensure Start is labeled correctly if autoplayed
  (function initUIDefaults(){
    phaseLabel.textContent = 'Breathe';
    phaseSub.textContent = 'Press Start';
    animateBreath(1,8);
    el('toggleNoise').textContent = 'Noise: On';
    el('toggleTone').textContent = 'Tone: Off';
  })();

  // Accessibility: keyboard shortcuts
  window.addEventListener('keydown', (e)=>{
    if (e.key === ' ') { e.preventDefault(); if (!running) el('startBtn').click(); else pauseSession(); }
    if (e.key.toLowerCase() === 's') el('stopBtn').click();
  });

  // Pre-warm audio on first user gesture so sound plays smoothly
  document.addEventListener('click', function once(){
    try { initAudio(); if (audioCtx && audioCtx.state === 'suspended') audioCtx.resume(); } catch(e){}
    document.removeEventListener('click', once);
  }, {once:true});

  </script>
</body>
</html>
```

How to use

* Save as `sleep.html` on your device and open in a browser (desktop or mobile).
* Lie down, dim lights, and press **Start**. Toggle **Speech** if you want spoken guidance. Use volume/tone controls to set gentle background sound.
* Keyboard: space to start/pause, `s` to stop.

Notes & safety

* This tool is a **relaxation aid** — not a medical device. If you have chronic insomnia, severe anxiety, or a medical condition, please consult a healthcare professional.
* If you prefer, I can also: produce a shorter audio-ready script (optimized for recording), or convert this into a minimal mobile-friendly page, or add multilingual voice selections. Want any of that?
