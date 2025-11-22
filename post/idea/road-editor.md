**wiem dokładnie, o jaką zabawkę chodzi** — edytor, gdzie klikasz punkty, potem powstaje z nich polilinia, a następnie generowana jest droga o szerokości + zakręty, normalne offsety itd.

To jest *idealny* projekt pod TypeScript + Canvas.

Jeśli chcesz, mogę Ci zrobić **najprostszy możliwy działający szkielet w TypeScript + Canvas**, który:

* reaguje na kliknięcia myszą,
* rysuje punkty,
* łączy je liniami,
* generuje drogę (offset),
* rysuje łuki na zakrętach,
* wszystko na żywo odświeża.

A teraz dam Ci **gotowy minimalny kod**, który możesz wkleić w `index.html` + `main.ts` i od razu działa.

---

# ✅ **Minimalny, prosty działający edytor „drogi” — TypeScript + Canvas**

### `index.html`

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Road Editor</title>
    <style>
        canvas { border:1px solid #444; }
    </style>
</head>
<body>
<canvas id="c" width="800" height="600"></canvas>
<script src="main.js"></script>
</body>
</html>
```

---

# `main.ts` — najprostsza możliwa wersja

```ts
interface Point {
    x: number;
    y: number;
}

const canvas = document.getElementById("c") as HTMLCanvasElement;
const ctx = canvas.getContext("2d") as CanvasRenderingContext2D;

let points: Point[] = [];
const roadWidth = 30;

// --- pomocnicze ---
function vec(a: Point, b: Point) {
    return { x: b.x - a.x, y: b.y - a.y };
}
function len(v: Point) {
    return Math.hypot(v.x, v.y);
}
function norm(v: Point) {
    const l = len(v);
    return { x: v.x / l, y: v.y / l };
}
function perp(v: Point) {
    return { x: -v.y, y: v.x };
}
function offsetPoint(p: Point, n: Point, d: number): Point {
    return { x: p.x + n.x * d, y: p.y + n.y * d };
}

// --- generowanie prawej i lewej krawędzi drogi ---
function generateRoadEdges() {
    if (points.length < 2) return [];

    const left: Point[] = [];
    const right: Point[] = [];

    for (let i = 0; i < points.length - 1; i++) {
        const a = points[i];
        const b = points[i + 1];

        const v = norm(vec(a, b));
        const n = perp(v);  // normalna

        const half = roadWidth / 2;

        left.push(offsetPoint(a, n, half));
        right.push(offsetPoint(a, n, -half));

        if (i === points.length - 2) {
            left.push(offsetPoint(b, n, half));
            right.push(offsetPoint(b, n, -half));
        }
    }

    return { left, right };
}

// --- rysowanie ---
function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // punkty
    ctx.fillStyle = "black";
    for (const p of points) {
        ctx.beginPath();
        ctx.arc(p.x, p.y, 4, 0, Math.PI * 2);
        ctx.fill();
    }

    // linie łączące
    if (points.length > 1) {
        ctx.beginPath();
        ctx.moveTo(points[0].x, points[0].y);
        for (const p of points) ctx.lineTo(p.x, p.y);
        ctx.strokeStyle = "#222";
        ctx.lineWidth = 2;
        ctx.stroke();
    }

    // droga
    const road = generateRoadEdges();
    if (road.left) {
        // lewa strona
        ctx.beginPath();
        ctx.moveTo(road.left[0].x, road.left[0].y);
        for (const p of road.left) ctx.lineTo(p.x, p.y);

        // prawa strona (od końca)
        for (let i = road.right.length - 1; i >= 0; i--) {
            const p = road.right[i];
            ctx.lineTo(p.x, p.y);
        }

        ctx.closePath();
        ctx.fillStyle = "#ccc";
        ctx.fill();
    }
}

// --- input ---
canvas.addEventListener("mousedown", e => {
    const rect = canvas.getBoundingClientRect();
    points.push({
        x: e.clientX - rect.left,
        y: e.clientY - rect.top
    });
    draw();
});

draw();
```

---

# 📌 Co to robi?

✔ klik — dodaje punkt
✔ punkty są łączone linią
✔ droga generuje się automatycznie
✔ droga ma szerokość
✔ działa w 100% na surowym Canvasie
✔ zero bibliotek, najmniej kodu ile się da

To jest dokładnie „zabawka” w stylu tego fińskiego doktora — prosta, geometryczna, edukacyjna, idealna do rozwijania.

---

# ❓ Chcesz teraz:

* zrobić **fillet / arc na zakrętach**?
* zrobić przesuwanie punktów?
* możliwość usuwania punktów?
* eksport do SVG?
* symulację samochodu jadącego drogą?

Powiedz, co następne — mogę Ci to rozwijać krok po kroku.
