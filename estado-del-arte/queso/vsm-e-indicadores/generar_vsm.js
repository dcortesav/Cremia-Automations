// Genera VSM_Queso_Actual.svg y VSM_Queso_Propuesto.svg — ejecutar: node generar_vsm.js
const fs = require("fs");
const W = 1640, H = 800;
const esc = (v) => String(v).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

function vsm(cfg) {
  const s = [];
  const add = (x) => s.push(x);
  const t = (x, y, txt, o = {}) =>
    add(`<text x="${x}" y="${y}" font-size="${o.size || 12}" text-anchor="${o.anchor || "middle"}"${o.bold ? ' font-weight="700"' : ""} fill="${o.fill || "#000"}">${esc(txt)}</text>`);
  add(`<defs><marker id="a" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto"><path d="M0 0 L10 4 L0 8 Z" fill="#000"/></marker>
<marker id="ai" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto"><path d="M0 0 L10 4 L0 8 Z" fill="#1f5fa8"/></marker></defs>`);
  add(`<rect width="${W}" height="${H}" fill="#fff"/>`);
  add(`<rect x="8" y="8" width="${W - 16}" height="${H - 16}" fill="none" stroke="#000" stroke-width="1.5"/>`);
  t(24, 36, cfg.title, { size: 17, bold: true, anchor: "start" });
  t(24, 56, cfg.subtitle, { size: 12, anchor: "start", fill: "#333" });

  // Entidades externas (forma de fábrica)
  const factory = (x, y, w, name, sub) => {
    add(`<path d="M${x} ${y + 70} L${x} ${y + 20} L${x + w / 3} ${y + 35} L${x + w / 3} ${y + 20} L${x + (2 * w) / 3} ${y + 35} L${x + (2 * w) / 3} ${y + 20} L${x + w} ${y + 35} L${x + w} ${y + 70} Z" fill="#f2f2f2" stroke="#000" stroke-width="1.5"/>`);
    t(x + w / 2, y + 56, name, { bold: true });
    sub.forEach((l, i) => t(x + w / 2, y + 88 + i * 15, l, { size: 11, fill: "#333" }));
  };
  factory(40, 80, 170, "Acopio de leche", cfg.supplier);
  factory(W - 210, 80, 170, "Distribución", cfg.customer);
  // Control de producción
  add(`<rect x="${W / 2 - 150}" y="80" width="300" height="70" fill="#eaf1fb" stroke="#1f5fa8" stroke-width="1.5"/>`);
  t(W / 2, 108, "Control de producción", { bold: true });
  t(W / 2, 128, cfg.control, { size: 11, fill: "#1f5fa8" });
  // Flujos de información con cliente y proveedor
  const info = (pts, label, lx, ly, dashed) => {
    add(`<path d="${pts.map((p, i) => (i ? "L" : "M") + p[0] + " " + p[1]).join(" ")}" fill="none" stroke="#1f5fa8" stroke-width="1.3"${dashed ? ' stroke-dasharray="6 4"' : ""} marker-end="url(#ai)"/>`);
    if (label) t(lx, ly, label, { size: 10.5, fill: "#1f5fa8" });
  };
  info([[W - 210, 115], [W / 2 + 150, 115]], cfg.infoCustomer, W - 330, 106, cfg.electronic ? false : true);
  info([[W / 2 - 150, 115], [210, 115]], cfg.infoSupplier, 330, 106, cfg.electronic ? false : true);

  // Procesos
  const n = cfg.procs.length, bw = 150, gap = (W - 80 - n * bw) / (n - 1), y0 = 290;
  cfg.procs.forEach((p, i) => {
    const x = 40 + i * (bw + gap);
    add(`<rect x="${x}" y="${y0}" width="${bw}" height="58" fill="${p.bottleneck ? "#fde2e0" : "#fff"}" stroke="${p.bottleneck ? "#b3261e" : "#000"}" stroke-width="${p.bottleneck ? 2.5 : 1.5}"/>`);
    t(x + bw / 2, y0 + 24, p.name, { bold: true, size: 12.5 });
    t(x + bw / 2, y0 + 44, p.sub || "", { size: 10.5, fill: "#444" });
    // operarios
    t(x + bw - 8, y0 - 8, p.op + " op.", { size: 10.5, anchor: "end", fill: "#333" });
    // caja de datos
    add(`<rect x="${x}" y="${y0 + 58}" width="${bw}" height="${p.data.length * 17 + 8}" fill="#fafafa" stroke="#000" stroke-width="1"/>`);
    p.data.forEach((d, k) => t(x + 8, y0 + 76 + k * 17, d, { size: 10.5, anchor: "start" }));
    // información desde control
    info([[W / 2 - 120 + (i * 240) / (n - 1), 150], [x + bw / 2, y0 - 26]], "", 0, 0, !cfg.electronic);
    // flujo de material e inventario
    if (i < n - 1) {
      const xa = x + bw, xb = x + bw + gap;
      add(`<line x1="${xa}" y1="${y0 + 29}" x2="${xb}" y2="${y0 + 29}" stroke="#000" stroke-width="2.5" ${cfg.push ? 'stroke-dasharray="10 5"' : ""} marker-end="url(#a)"/>`);
      const inv = cfg.inv[i];
      if (inv) {
        const cx = (xa + xb) / 2;
        add(`<path d="M${cx - 13} ${y0 + 12} L${cx + 13} ${y0 + 12} L${cx} ${y0 - 12} Z" fill="#fff3bf" stroke="#000" stroke-width="1.2"/>`);
        t(cx, y0 + 7, "I", { size: 10, bold: true });
        t(cx, y0 - 18, inv, { size: 10 });
      }
    }
  });
  add(`<rect x="${W / 2 - 330}" y="203" width="660" height="18" fill="#fff" opacity="0.92"/>`);
  t(W / 2, 216, cfg.infoPlant, { size: 11, fill: "#1f5fa8" });
  // Material: proveedor → primer proceso; último → cliente
  add(`<path d="M125 190 L125 ${y0 - 2}" fill="none" stroke="#000" stroke-width="2.5" marker-end="url(#a)"/>`);
  t(118, 262, cfg.inbound, { size: 10.5, anchor: "end" });
  add(`<path d="M${W - 115} ${y0 - 2} L${W - 115} 192" fill="none" stroke="#000" stroke-width="2.5" marker-end="url(#a)"/>`);
  t(W - 108, 262, cfg.outbound, { size: 10.5, anchor: "start" });

  // Línea de tiempo
  const yt = 560;
  t(40, yt - 18, "Línea de tiempo (min por lote, desde la leche pasteurizada en el tanque pulmón)", { size: 12, bold: true, anchor: "start" });
  cfg.procs.forEach((p, i) => {
    const x = 40 + i * (bw + gap);
    add(`<path d="M${x} ${yt + 30} L${x + bw} ${yt + 30}" stroke="#000" stroke-width="1.5" fill="none"/>`);
    t(x + bw / 2, yt + 48, "VA " + p.va, { size: 11, fill: "#207245", bold: true });
    if (i < n - 1) {
      add(`<path d="M${x + bw} ${yt + 30} L${x + bw} ${yt} L${x + bw + gap} ${yt} L${x + bw + gap} ${yt + 30}" stroke="#000" stroke-width="1.5" fill="none"/>`);
      t(x + bw + gap / 2, yt - 6, "NVA " + cfg.nva[i], { size: 11, fill: "#b3261e", bold: true });
    }
  });
  // Resumen
  add(`<rect x="40" y="640" width="${W - 80}" height="120" fill="#fafafa" stroke="#000" stroke-width="1"/>`);
  cfg.summary.forEach((col, i) => {
    const cx = 60 + i * ((W - 120) / cfg.summary.length);
    t(cx, 664, col[0], { size: 11, anchor: "start", fill: "#444" });
    t(cx, 692, col[1], { size: 19, anchor: "start", bold: true });
    t(cx, 714, col[2] || "", { size: 10.5, anchor: "start", fill: "#444" });
    t(cx, 730, col[3] || "", { size: 10.5, anchor: "start", fill: "#444" });
  });
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" font-family="Arial, Helvetica, sans-serif">\n${s.join("\n")}\n</svg>\n`;
}

const actual = vsm({
  title: "VSM actual — Línea 2: Queso campesino (familia QC-250, cuña de 250 g)",
  subtitle: "Demanda: 7 lotes/día (35.000 L de leche; 4.667 kg de queso) · 2 turnos · 900 min disponibles/día · Takt = 128,6 min/lote",
  supplier: ["Carrotanques de 10.000 L", "Entrega diaria"],
  customer: ["4.667 kg/día", "Despacho diario"],
  control: "Programación manual (hojas de cálculo)",
  infoCustomer: "Pedidos semanales", infoSupplier: "Plan de acopio semanal",
  infoPlant: "Órdenes de producción en papel, por turno · registros manuales de lote",
  electronic: false, push: true,
  inbound: "Silo ≤ 48 h", outbound: "Cámara 1–2 días",
  procs: [
    { name: "Pasteurización", sub: "HTST compartido", op: 1, va: "—", data: ["TC = 30 min/lote", "C/O = 30 min", "Disp. = 95 %", "Compartido L1-L2-L3"] },
    { name: "Tina quesera", sub: "2 tinas de 5.000 L", op: 2, va: 107, data: ["TC = 212 min (con CIP)", "106 min/lote (2 tinas)", "Disp. = 95 %", "Punto de corte manual"] },
    { name: "Moldeo", sub: "manual", op: 3, va: 25, data: ["TC = 25 min/lote", "222 moldes de 3 kg", "Llenado manual", "Variación de peso"] },
    { name: "Prensado", sub: "2 prensas · volteo manual", op: 3, va: 75, bottleneck: true, data: ["TC = 190 min/lote", "2 ciclos de 95 min", "400 kg por ciclo", "Disp. = 90 %"] },
    { name: "Oreo", sub: "cuarto frío 4–6 °C", op: 0, va: 0, data: ["600 min/lote", "Capacidad: 4 lotes", "Espera técnica", ""] },
    { name: "Porcionado y empaque", sub: "termoformado al vacío", op: 3, va: 95, data: ["TC = 95 min/lote", "28 und/min", "C/O = 20 min", "Rechazo = 4 %"] },
    { name: "Paletizado", sub: "manual", op: 2, va: 0, data: ["TC = 22 min/lote", "111 cajas", "5 cajas/min", ""] },
  ],
  inv: ["Pulmón 10.000 L", "", "Moldes en espera", "", "4 lotes", ""],
  nva: [30, 0, 115, 15, 610, 22],
  summary: [
    ["MLT (lead time de fabricación)", "1.094 min (18,2 h)", "Leche pasteurizada → estiba en cámara", ""],
    ["Tiempo de valor agregado", "302 min", "27,6 % del MLT", ""],
    ["Recurso limitante", "Prensado: 190 min/lote", "Takt = 128,6 min/lote", "No cumple la demanda"],
    ["Producción real", "3,97 lotes/día", "2.650 kg/día (57 % de la demanda)", ""],
    ["OEE", "54,5 %", "A = 85 % · PE = 66,8 % · Q = 96 %", ""],
    ["Operarios por turno", "14", "", ""],
  ],
});

const futuro = vsm({
  title: "VSM propuesto — Línea 2: Queso campesino (familia QC-250, cuña de 250 g)",
  subtitle: "Demanda: 7 lotes/día (35.000 L de leche; 4.667 kg de queso) · 2 turnos · 900 min disponibles/día · Takt = 128,6 min/lote",
  supplier: ["Carrotanques de 10.000 L", "Entrega diaria"],
  customer: ["4.667 kg/día", "Despacho diario"],
  control: "ERP (plan) → MES (órdenes y recetas ISA-88)",
  infoCustomer: "Pedidos electrónicos (ERP)", infoSupplier: "Plan de acopio (ERP)",
  infoPlant: "Órdenes y recetas electrónicas MES → PLC / SCADA · registro automático de lote, paradas y calidad",
  electronic: true, push: false,
  inbound: "Silo ≤ 48 h", outbound: "Cámara 1 día",
  procs: [
    { name: "Pasteurización", sub: "HTST compartido", op: 1, va: "—", data: ["TC = 30 min/lote", "Campañas por producto", "Disp. = 97 %", "PCC con registro"] },
    { name: "Tina quesera", sub: "2 tinas · receta automática", op: 2, va: 107, bottleneck: true, data: ["TC = 212 min (con CIP)", "106 min/lote (2 tinas)", "Disp. = 97 %", "Sensor de coagulación"] },
    { name: "Moldeo", sub: "moldeadora multicabezal", op: 1, va: 15, data: ["TC = 15 min/lote", "Dosificación por peso", "WT-201", ""] },
    { name: "Prensado", sub: "4 prensas · volteo automático", op: 1, va: 75, data: ["TC = 80 min/lote", "1 ciclo", "800 kg por ciclo", "Disp. = 95 %"] },
    { name: "Enfriamiento", sub: "túnel de aire forzado", op: 0, va: 0, data: ["150 min/lote", "0–2 °C", "Flujo continuo", ""] },
    { name: "Porcionado y empaque", sub: "termoformado al vacío", op: 2, va: 95, data: ["TC = 95 min/lote", "28 und/min", "C/O = 10 min", "Rechazo = 1,5 %"] },
    { name: "Paletizado", sub: "celda robotizada", op: 1, va: 0, data: ["TC = 11 min/lote", "111 cajas", "10 cajas/min", "Compartido L1-L2-L3"] },
  ],
  inv: ["Pulmón 10.000 L", "", "", "", "", ""],
  nva: [30, 0, 5, 10, 155, 11],
  summary: [
    ["MLT (lead time de fabricación)", "503 min (8,4 h)", "−54 % frente al actual", ""],
    ["Tiempo de valor agregado", "292 min", "58,1 % del MLT", ""],
    ["Recurso limitante", "Tina: 106 min/lote", "Takt = 128,6 min/lote", "Cumple la demanda (U = 92 %)"],
    ["Producción real", "7 lotes/día", "4.667 kg/día (100 % de la demanda)", "Capacidad: 7,6 lotes/día"],
    ["OEE", "87,9 %", "A = 92 % · PE = 97 % · Q = 98,5 %", ""],
    ["Operarios por turno", "8", "", ""],
  ],
});

fs.writeFileSync(__dirname + "/VSM_Queso_Actual.svg", actual);
fs.writeFileSync(__dirname + "/VSM_Queso_Propuesto.svg", futuro);
console.log("OK", actual.length, futuro.length);
