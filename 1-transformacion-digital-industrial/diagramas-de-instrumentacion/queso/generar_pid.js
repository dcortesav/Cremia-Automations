// Genera P&ID_Queso.svg (ISA-5.1 simplificado) — ejecutar: node generar_pid.js
const fs = require("fs");
const W = 1800, H = 1200;
let s = [];
const add = (x) => s.push(x);
const esc = (v) => String(v).replace(/</g, "&lt;").replace(/>/g, "&gt;");
const t = (x, y, txt, o = {}) =>
  add(`<text x="${x}" y="${y}" font-size="${o.size || 11}" text-anchor="${o.anchor || "middle"}"${o.bold ? ' font-weight="700"' : ""}${o.fill ? ` fill="${o.fill}"` : ""}>${esc(txt)}</text>`);

// ---------- primitivas ----------
function line(pts, kind = "proc") {
  const d = pts.map((p, i) => (i ? "L" : "M") + p[0] + " " + p[1]).join(" ");
  const cls = { proc: 'stroke="#000" stroke-width="2"', util: 'stroke="#1f5fa8" stroke-width="1.6"', sig: 'stroke="#000" stroke-width="1" stroke-dasharray="6 4"', whey: 'stroke="#2b7a3d" stroke-width="2"' }[kind];
  const mk = kind === "sig" ? "" : ` marker-end="url(#arr-${kind})"`;
  add(`<path d="${d}" fill="none" ${cls}${mk}/>`);
}
function pump(x, y, tag) {
  add(`<circle cx="${x}" cy="${y}" r="16" fill="#fff" stroke="#000" stroke-width="2"/>`);
  add(`<path d="M${x - 9} ${y + 10} L${x} ${y - 12} L${x + 9} ${y + 10}" fill="none" stroke="#000" stroke-width="1.5"/>`);
  t(x, y + 32, tag, { bold: true });
}
function valve(x, y, tag, vert = false, actuated = true) {
  if (!vert) add(`<path d="M${x - 10} ${y - 7} L${x + 10} ${y + 7} L${x + 10} ${y - 7} L${x - 10} ${y + 7} Z" fill="#fff" stroke="#000" stroke-width="1.5"/>`);
  else add(`<path d="M${x - 7} ${y - 10} L${x + 7} ${y + 10} L${x - 7} ${y + 10} L${x + 7} ${y - 10} Z" fill="#fff" stroke="#000" stroke-width="1.5"/>`);
  if (actuated) {
    add(`<line x1="${x}" y1="${y}" x2="${x}" y2="${y - 18}" stroke="#000" stroke-width="1.2"/>`);
    add(`<path d="M${x - 9} ${y - 18} A9 9 0 0 1 ${x + 9} ${y - 18} Z" fill="#fff" stroke="#000" stroke-width="1.2"/>`);
  }
  if (tag) t(x + (vert ? -14 : 0), y + (vert ? 4 : 22), tag, { size: 10, anchor: vert ? "end" : "middle" });
}
// Instrumento: field = campo; plc = función en PLC/SCADA (círculo con línea)
function inst(x, y, letters, num, loc = "field") {
  add(`<circle cx="${x}" cy="${y}" r="19" fill="#fff" stroke="#000" stroke-width="1.4"/>`);
  if (loc === "plc") add(`<line x1="${x - 19}" y1="${y}" x2="${x + 19}" y2="${y}" stroke="#000" stroke-width="1.2"/>`);
  if (loc === "plc") add(`<rect x="${x - 19}" y="${y - 19}" width="38" height="38" fill="none" stroke="#000" stroke-width="1"/>`);
  t(x, y - 4, letters, { size: 10, bold: true });
  t(x, y + 12, num, { size: 10 });
}
function box(x, y, w, h, title, tag, sub) {
  add(`<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="4" fill="#fff" stroke="#000" stroke-width="2"/>`);
  t(x + w / 2, y + h / 2 - (sub ? 6 : 0), title, { size: 11 });
  if (sub) t(x + w / 2, y + h / 2 + 10, sub, { size: 9, fill: "#444" });
  if (tag) t(x + w / 2, y + h + 16, tag, { bold: true });
}
function tank(x, y, w, h, tag, title) {
  add(`<path d="M${x} ${y + 14} Q${x} ${y} ${x + w / 2} ${y} Q${x + w} ${y} ${x + w} ${y + 14} L${x + w} ${y + h - 14} Q${x + w} ${y + h} ${x + w / 2} ${y + h} Q${x} ${y + h} ${x} ${y + h - 14} Z" fill="#fff" stroke="#000" stroke-width="2"/>`);
  String(title).split("|").forEach((ln, i, a) => t(x + w / 2, y + h / 2 + (i - (a.length - 1) / 2) * 13, ln, { size: 10 }));
  t(x + w / 2, y + h + 16, tag, { bold: true });
}
function motor(x, y, tag) {
  add(`<circle cx="${x}" cy="${y}" r="12" fill="#fff" stroke="#000" stroke-width="1.5"/>`);
  t(x, y + 4, "M", { size: 11, bold: true });
  if (tag) t(x + 18, y + 4, tag, { size: 10, anchor: "start" });
}
const sig = (a, b) => line([a, b], "sig");

// ---------- defs y marco ----------
add(`<defs>
<marker id="arr-proc" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto"><path d="M0 0 L10 4 L0 8 Z" fill="#000"/></marker>
<marker id="arr-util" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto"><path d="M0 0 L10 4 L0 8 Z" fill="#1f5fa8"/></marker>
<marker id="arr-whey" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto"><path d="M0 0 L10 4 L0 8 Z" fill="#2b7a3d"/></marker>
</defs>`);
add(`<rect x="0" y="0" width="${W}" height="${H}" fill="#fff"/>`);
add(`<rect x="10" y="10" width="${W - 20}" height="${H - 20}" fill="none" stroke="#000" stroke-width="2"/>`);
t(30, 42, "P&amp;ID — LÍNEA 2: QUESO CAMPESINO · Recepción, tratamiento de la leche y elaboración en tina", { size: 16, bold: true, anchor: "start" });
t(30, 62, "Área 100: recepción y almacenamiento · Área 150: tratamiento térmico (compartida L1-L2-L3) · Área 200: quesería · Área 300: suero", { size: 11, anchor: "start", fill: "#333" });

// Separadores de área
add(`<line x1="20" y1="400" x2="${W - 20}" y2="400" stroke="#888" stroke-dasharray="3 5"/>`);
t(30, 392, "ÁREA 100 — RECEPCIÓN Y ALMACENAMIENTO (COMPARTIDA)", { size: 10, anchor: "start", fill: "#666", bold: true });
t(30, 420, "ÁREA 150 — TRATAMIENTO TÉRMICO (COMPARTIDA) · ÁREA 200 — QUESERÍA · ÁREA 300 — SUERO", { size: 10, anchor: "start", fill: "#666", bold: true });

// ================= FILA 1 (y=230) =================
const y1 = 230;
box(40, y1 - 40, 110, 80, "Carrotanque", "TK-100", "leche cruda ≤6 °C");
line([[150, y1], [214, y1]]);
pump(230, y1, "P-101");
line([[246, y1], [300, y1]]);
box(300, y1 - 22, 60, 44, "Filtro", "F-101", "100–200 µm");
line([[360, y1], [480, y1]]);
// FT-101 en línea
add(`<rect x="400" y="${y1 - 10}" width="30" height="20" fill="#fff" stroke="#000" stroke-width="1.5"/>`);
inst(415, y1 - 70, "FT", "101");
sig([415, y1 - 51], [415, y1 - 10]);
inst(415, y1 - 140, "FQI", "101", "plc");
sig([415, y1 - 121], [415, y1 - 89]);
box(480, y1 - 45, 90, 90, "Enfriador", "E-101", "de placas");
line([[480, y1 + 30], [440, y1 + 30], [440, y1 + 90]], "util");
t(446, y1 + 102, "Retorno agua helada", { size: 9, anchor: "start", fill: "#1f5fa8" });
line([[640, y1 + 90], [600, y1 + 90], [600, y1 + 30], [570, y1 + 30]], "util");
t(646, y1 + 94, "Agua helada 1 °C", { size: 9, anchor: "start", fill: "#1f5fa8" });
valve(600, y1 + 60, "TV-101", true);
line([[570, y1], [680, y1]]);
inst(630, y1 - 60, "TT", "101");
sig([630, y1 - 41], [630, y1]);
inst(700, y1 - 110, "TIC", "101", "plc");
sig([649, y1 - 60], [681, y1 - 110]);
sig([719, y1 - 110], [760, y1 - 110]);
sig([760, y1 - 110], [760, y1 + 60]);
sig([760, y1 + 60], [618, y1 + 60]);
// Silo
line([[680, y1], [800, y1], [800, y1 - 70], [820, y1 - 70]]);
tank(820, y1 - 110, 90, 230, "T-101", "Silo leche|cruda|25.000 L");
motor(865, y1 - 128, "M-101");
add(`<line x1="865" y1="${y1 - 116}" x2="865" y2="${y1 + 60}" stroke="#000" stroke-width="1.5"/>`);
add(`<path d="M845 ${y1 + 60} L885 ${y1 + 60}" stroke="#000" stroke-width="2"/>`);
inst(950, y1 - 60, "LT", "101");
sig([931, y1 - 60], [910, y1 - 60]);
inst(950, y1 + 10, "TT", "102");
sig([931, y1 + 10], [910, y1 + 10]);
inst(1020, y1 - 60, "LAHL", "101", "plc");
sig([969, y1 - 60], [1001, y1 - 60]);
// Salida silo → P-102 → clarificadora → estandarizadora
line([[865, y1 + 120], [865, y1 + 150], [1050, y1 + 150]]);
pump(1066, y1 + 150, "P-102");
line([[1082, y1 + 150], [1110, y1 + 150], [1110, y1 + 40], [1140, y1 + 40]]);
box(1140, y1 - 5, 100, 90, "Clarificadora", "CF-101", "bactofugadora");
line([[1240, y1 + 40], [1300, y1 + 40]]);
box(1300, y1 - 5, 110, 90, "Estandarizadora", "SE-101", "grasa 3,0 %");
inst(1355, y1 - 75, "AT", "101");
sig([1355, y1 - 56], [1355, y1 - 5]);
inst(1440, y1 - 75, "AIC", "101", "plc");
sig([1374, y1 - 75], [1421, y1 - 75]);
line([[1410, y1 + 10], [1520, y1 + 10]], "proc");
valve(1470, y1 + 10, "FV-101");
sig([1459, y1 - 75], [1470, y1 - 75]);
sig([1470, y1 - 75], [1470, y1 - 8]);
t(1528, y1 + 14, "Crema a L1 / L3", { size: 10, anchor: "start" });
// Leche estandarizada baja a fila 2
line([[1410, y1 + 60], [1680, y1 + 60], [1680, 445], [120, 445], [120, 520]]);
t(1670, y1 + 52, "Leche estandarizada", { size: 10, anchor: "end" });

// ================= FILA 2 (y=600) =================
const y2 = 700;
tank(80, 520, 80, 90, "BT-101", "Tanque|balance");
inst(200, 540, "LT", "150");
sig([181, 540], [160, 540]);
line([[120, 610], [120, 650], [190, 650]]);
pump(206, 650, "P-150");
line([[222, 650], [260, 650], [260, y2], [290, y2]]);
// Pasteurizador con 3 secciones
add(`<rect x="290" y="${y2 - 70}" width="240" height="140" rx="4" fill="#fff" stroke="#000" stroke-width="2"/>`);
[["Regeneración", 290], ["Calentamiento", 370], ["Enfriamiento", 450]].forEach(([n, x]) => {
  add(`<rect x="${x + 6}" y="${y2 - 60}" width="68" height="120" fill="none" stroke="#000" stroke-width="1" stroke-dasharray="2 2"/>`);
  t(x + 40, y2 + 4, n, { size: 9 });
});
t(410, y2 - 80, "Pasteurizador HTST 10.000 L/h — 72–75 °C / 15–20 s", { size: 11, bold: true });
t(450, y2 + 88, "PA-101", { bold: true });
// Vapor/agua caliente a sección calentamiento
line([[410, y2 + 170], [410, y2 + 70]], "util");
valve(410, y2 + 125, "TV-103", true);
t(416, y2 + 185, "Agua caliente / vapor", { size: 9, fill: "#1f5fa8" });
line([[490, y2 + 170], [490, y2 + 70]], "util");
t(496, y2 + 185, "Agua helada", { size: 9, fill: "#1f5fa8", anchor: "start" });
// Tubo de retención
line([[530, y2 - 30], [560, y2 - 30]]);
add(`<path d="M560 ${y2 - 30} h80 v-20 h-80 v-20 h80" fill="none" stroke="#000" stroke-width="3"/>`);
t(600, y2 - 8, "Tubo de retención HT-101", { size: 10 });
inst(680, y2 - 120, "TT", "103");
sig([680, y2 - 101], [680, y2 - 70]);
line([[640, y2 - 70], [720, y2 - 70]]);
inst(760, y2 - 175, "TIC", "103", "plc");
sig([699, y2 - 120], [741, y2 - 175]);
inst(840, y2 - 175, "TR", "103", "plc");
sig([779, y2 - 175], [821, y2 - 175]);
sig([760, y2 - 156], [760, y2 - 130]);
sig([760, y2 - 130], [550, y2 - 130]);
sig([550, y2 - 130], [550, y2 + 95]);
sig([550, y2 + 95], [410, y2 + 95]);
// FDV
valve(740, y2 - 70, "XV-101 (FDV)");
inst(840, y2 - 110, "TSL", "103", "plc");
sig([821, y2 - 110], [740, y2 - 88]);
// Desvío regresa al tanque balance
line([[740, y2 - 60], [740, y2 - 40], [700, y2 - 40], [700, 500], [60, 500], [60, 565], [80, 565]]);
t(360, 492, "Retorno por desvío XV-101 (T < 72 °C)", { size: 10, anchor: "start" });
// Retorno a regeneración/enfriamiento y salida
line([[760, y2 - 70], [790, y2 - 70], [790, y2 + 40], [530, y2 + 40]]);
t(795, y2 + 10, "a regeneración", { size: 9, anchor: "start", fill: "#444" });
line([[530, y2 + 60], [870, y2 + 60]]);
inst(830, y2 + 110, "TT", "104");
sig([830, y2 + 91], [830, y2 + 60]);
t(700, y2 + 76, "Leche pasteurizada 32–35 °C", { size: 10 });
// Tanque pulmón
tank(870, y2 - 10, 80, 120, "T-102", "Pulmón");
inst(990, y2 + 10, "LT", "102");
sig([971, y2 + 10], [950, y2 + 10]);
line([[910, y2 + 110], [910, y2 + 150], [990, y2 + 150]]);
pump(1006, y2 + 150, "P-201");
line([[1022, y2 + 150], [1060, y2 + 150], [1060, y2 - 30], [1110, y2 - 30]]);
inst(1060, y2 - 90, "FQ", "201", "field");
sig([1060, y2 - 71], [1060, y2 - 30]);

// Tina quesera
add(`<path d="M1110 ${y2 - 60} L1110 ${y2 + 60} Q1110 ${y2 + 110} 1170 ${y2 + 110} L1290 ${y2 + 110} Q1350 ${y2 + 110} 1350 ${y2 + 60} L1350 ${y2 - 60}" fill="#fff" stroke="#000" stroke-width="2.5"/>`);
add(`<path d="M1100 ${y2 - 40} L1100 ${y2 + 64} Q1100 ${y2 + 120} 1170 ${y2 + 120} L1290 ${y2 + 120} Q1360 ${y2 + 120} 1360 ${y2 + 64} L1360 ${y2 - 40}" fill="none" stroke="#000" stroke-width="1" stroke-dasharray="5 3"/>`);
t(1230, y2 + 62, "Tina quesera 5.000 L", { size: 11, bold: true });
t(1230, y2 + 76, "doble camisa · liras corte/agitación", { size: 9, fill: "#444" });
t(1230, y2 + 96, "V-201 (y V-202 en paralelo)", { bold: true });
motor(1230, y2 - 95, "M-201");
add(`<line x1="1230" y1="${y2 - 83}" x2="1230" y2="${y2 - 30}" stroke="#000" stroke-width="1.5"/>`);
add(`<rect x="1200" y="${y2 - 30}" width="60" height="70" fill="none" stroke="#000" stroke-width="1"/>`);
add(`<line x1="1200" y1="${y2 + 5}" x2="1260" y2="${y2 + 5}" stroke="#000" stroke-width="1"/>`);
add(`<line x1="1230" y1="${y2 - 30}" x2="1230" y2="${y2 + 40}" stroke="#000" stroke-width="1"/>`);
inst(1160, y2 - 145, "SIC", "201", "plc");
sig([1179, y2 - 145], [1218, y2 - 100]);
t(1182, y2 - 162, "VFD", { size: 9, fill: "#444", anchor: "start" });
inst(1400, y2 - 20, "TT", "201");
sig([1381, y2 - 20], [1350, y2 - 20]);
inst(1470, y2 - 20, "TIC", "201", "plc");
sig([1419, y2 - 20], [1451, y2 - 20]);
inst(1400, y2 + 50, "LT", "201");
sig([1381, y2 + 50], [1350, y2 + 50]);
// Camisa: agua caliente con TV-201
line([[1560, y2 + 90], [1440, y2 + 90], [1360, y2 + 90]], "util");
valve(1500, y2 + 90, "TV-201");
sig([1489, y2 - 20], [1500, y2 - 20]);
sig([1500, y2 - 20], [1500, y2 + 72]);
t(1566, y2 + 94, "Agua caliente 40 °C", { size: 9, anchor: "start", fill: "#1f5fa8" });
// Dosificación (a la derecha de la tina)
const dos = [["CaCl₂", "P-204", "204", y2 - 230, 1340], ["Cuajo", "P-205", "205", y2 - 180, 1320]];
dos.forEach(([n, p, num, yy, xin]) => {
  box(1560, yy - 17, 70, 34, n, "", "");
  line([[1560, yy], [xin, yy], [xin, y2 - 60]]);
  add(`<circle cx="1470" cy="${yy}" r="10" fill="#fff" stroke="#000" stroke-width="1.5"/>`);
  t(1470, yy - 14, p, { size: 9 });
  inst(1680, yy, "FQ", num, "plc");
  sig([1661, yy], [1630, yy]);
});
t(1595, y2 - 142, "Dosificación por receta (ISA-88)", { size: 10, bold: true });
// Sal (manual / tornillo)
t(1270, y2 - 70, "Sal ↓", { size: 10, anchor: "start" });

// Descargas de la tina
// Suero
line([[1170, y2 + 110], [1170, y2 + 200], [1060, y2 + 200]], "whey");
valve(1170, y2 + 160, "XV-202", true);
pump(1044, y2 + 200, "P-202");
line([[1028, y2 + 200], [980, y2 + 200], [980, y2 + 250]], "whey");
tank(930, y2 + 250, 100, 90, "T-301", "Tanque|suero");
inst(1080, y2 + 290, "LT", "301");
sig([1061, y2 + 290], [1030, y2 + 290]);
inst(1080, y2 + 345, "TT", "301");
sig([1061, y2 + 345], [1030, y2 + 330]);
t(1100, y2 + 205, "Suero", { size: 10, fill: "#2b7a3d", anchor: "start" });
// Cuajada
line([[1290, y2 + 110], [1290, y2 + 220], [1380, y2 + 220]]);
valve(1290, y2 + 165, "XV-203", true);
pump(1396, y2 + 220, "P-203");
line([[1412, y2 + 220], [1450, y2 + 220]]);
box(1450, y2 + 185, 90, 70, "Moldeadora", "ML-201", "moldes 1 kg / 3 kg");
inst(1620, y2 + 175, "WT", "201");
sig([1601, y2 + 175], [1540, y2 + 200]);
line([[1540, y2 + 220], [1570, y2 + 220], [1570, y2 + 290], [1450, y2 + 290]]);
box(1360, y2 + 265, 90, 60, "Prensas", "PR-201…204", "neumáticas");
inst(1560, y2 + 330, "PIC", "201", "plc");
sig([1541, y2 + 330], [1450, y2 + 310]);
line([[1360, y2 + 295], [1300, y2 + 295], [1300, y2 + 340]]);
t(1310, y2 + 352, "A desmoldeo, oreo y empaque (sección discreta)", { size: 10, anchor: "start" });

// ---------- Leyenda ----------
const lx = 30, ly = H - 200;
add(`<rect x="${lx}" y="${ly}" width="560" height="170" fill="#fff" stroke="#000" stroke-width="1"/>`);
t(lx + 10, ly + 18, "LEYENDA (ISA-5.1)", { size: 11, bold: true, anchor: "start" });
line([[lx + 10, ly + 40], [lx + 60, ly + 40]]); t(lx + 70, ly + 44, "Línea de proceso (leche / cuajada)", { anchor: "start", size: 10 });
line([[lx + 10, ly + 62], [lx + 60, ly + 62]], "whey"); t(lx + 70, ly + 66, "Línea de suero", { anchor: "start", size: 10 });
line([[lx + 10, ly + 84], [lx + 60, ly + 84]], "util"); t(lx + 70, ly + 88, "Servicio (agua helada / caliente, vapor)", { anchor: "start", size: 10 });
line([[lx + 10, ly + 106], [lx + 60, ly + 106]], "sig"); t(lx + 70, ly + 110, "Señal eléctrica / de control", { anchor: "start", size: 10 });
inst(lx + 330, ly + 55, "TT", "xxx"); t(lx + 356, ly + 59, "Instrumento de campo", { anchor: "start", size: 10 });
inst(lx + 330, ly + 115, "TIC", "xxx", "plc"); t(lx + 356, ly + 119, "Función en PLC / SCADA", { anchor: "start", size: 10 });
t(lx + 10, ly + 140, "T: temperatura · L: nivel · F: flujo · A: análisis (grasa) · P: presión · S: velocidad · W: peso", { anchor: "start", size: 9.5 });
t(lx + 10, ly + 156, "T/I/C/R/Q/SL/AHL: transmisor / indicador / controlador / registrador / totalizador / interruptor bajo / alarma alta-baja", { anchor: "start", size: 9.5 });

// ---------- Cajetín ----------
const bx = W - 430, by = H - 125;
add(`<rect x="${bx}" y="${by}" width="410" height="110" fill="#fff" stroke="#000" stroke-width="1.5"/>`);
add(`<line x1="${bx}" y1="${by + 36}" x2="${bx + 410}" y2="${by + 36}" stroke="#000"/>`);
t(bx + 205, by + 24, "PROYECTO INTEGRADOR APM 2026-2S — UNAL", { size: 12, bold: true });
t(bx + 10, by + 56, "Plano: P&amp;ID-L2-001 · Línea 2 Queso campesino", { anchor: "start", size: 10.5 });
t(bx + 10, by + 74, "Elaboró: C. S. Hoyos P. · J. A. Zapata P.", { anchor: "start", size: 10.5 });
t(bx + 10, by + 92, "Norma: ANSI/ISA-5.1 · Rev. A · Sin escala", { anchor: "start", size: 10.5 });

const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" font-family="Arial, Helvetica, sans-serif">\n${s.join("\n")}\n</svg>\n`;
fs.writeFileSync(__dirname + "/PID_Queso.svg", svg);
console.log("OK", svg.length);
