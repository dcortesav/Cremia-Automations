// Genera las variantes del logo de Cremia Automations — ejecutar: node generar_logo.js
const fs = require("fs");
const AZUL = "#0b4f6c", CELESTE = "#3aa6c9", CREMA = "#f6f1e3";
// Isotipo: gota de leche con un engranaje interior y un nodo de datos
function isotipo(cx, cy, k, fondo, tinta, acento) {
  const dientes = [];
  for (let i = 0; i < 8; i++) {
    const a = (i * Math.PI) / 4;
    const x = cx + Math.cos(a) * 19 * k, y = cy + 14 * k + Math.sin(a) * 19 * k;
    dientes.push(`<rect x="${(x - 4 * k).toFixed(1)}" y="${(y - 4 * k).toFixed(1)}" width="${8 * k}" height="${8 * k}" fill="${fondo}" transform="rotate(${i * 45} ${x.toFixed(1)} ${y.toFixed(1)})"/>`);
  }
  return `
  <path d="M${cx} ${cy - 52 * k} C${cx + 14 * k} ${cy - 26 * k} ${cx + 40 * k} ${cy - 8 * k} ${cx + 40 * k} ${cy + 18 * k} A${40 * k} ${40 * k} 0 0 1 ${cx - 40 * k} ${cy + 18 * k} C${cx - 40 * k} ${cy - 8 * k} ${cx - 14 * k} ${cy - 26 * k} ${cx} ${cy - 52 * k} Z" fill="${tinta}"/>
  <circle cx="${cx}" cy="${cy + 14 * k}" r="${17 * k}" fill="${fondo}"/>
  ${dientes.join("\n  ")}
  <circle cx="${cx}" cy="${cy + 14 * k}" r="${8 * k}" fill="${acento}"/>`;
}
const svg = (w, h, body, bg) => `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${w} ${h}" width="${w}" height="${h}" font-family="'Segoe UI', Arial, Helvetica, sans-serif">\n<rect width="${w}" height="${h}" fill="${bg}"/>${body}\n</svg>\n`;
const texto = (x, y, tinta, acento) => `
  <text x="${x}" y="${y}" font-size="64" font-weight="700" fill="${tinta}" letter-spacing="1">Cremia</text>
  <text x="${x + 3}" y="${y + 38}" font-size="24" font-weight="600" fill="${acento}" letter-spacing="9">AUTOMATIONS</text>`;

fs.writeFileSync(__dirname + "/logo_horizontal.svg", svg(520, 180, isotipo(90, 88, 1.25, "#ffffff", AZUL, CELESTE) + texto(175, 96, AZUL, CELESTE), "#ffffff"));
fs.writeFileSync(__dirname + "/logo_horizontal_oscuro.svg", svg(520, 180, isotipo(90, 88, 1.25, AZUL, CREMA, CELESTE) + texto(175, 96, CREMA, CELESTE), AZUL));
fs.writeFileSync(__dirname + "/isotipo.svg", svg(200, 200, isotipo(100, 98, 1.5, "#ffffff", AZUL, CELESTE), "#ffffff"));
console.log("ok");
