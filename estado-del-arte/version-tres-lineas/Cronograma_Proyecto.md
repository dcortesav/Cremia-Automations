# Cronograma — Proyecto de Transformación Digital Industrial de la Planta de Derivados Lácteos

> **Alcance:** cronograma de ejecución del proyecto de automatización de las tres líneas de la planta (yogur, queso campesino y kumis), construido a partir de la `EDT_Proyecto.md`.

> **Supuestos:** inicio el 18 de enero de 2027, después de la aceptación de la oferta. La planta sigue en producción durante el proyecto; el montaje se hace por línea, en paradas programadas.

> **Duración estimada:** 43 semanas (10 meses), del 18 de enero al 12 de noviembre de 2027.

---

## 1. Diagrama de Gantt

```mermaid
gantt
    title Proyecto TDI - Planta de derivados lácteos
    dateFormat YYYY-MM-DD
    axisFormat %b %Y

    section 1.1 Gestión
    Plan del proyecto y línea base           :g1, 2027-01-18, 2w
    Seguimiento y control                    :g2, after g1, 2027-10-29
    Cierre administrativo                    :g3, 2027-11-01, 2w

    section 1.2 Ingeniería básica
    Levantamiento y caracterización          :b1, 2027-01-18, 3w
    VSM, simulación y cuellos de botella     :b2, after b1, 3w
    Arquitectura ISA-95 y red OT/IT          :b3, after b1, 3w
    Modelos ISA-88 y recetas                 :b4, after b1, 3w
    P&ID e índice de instrumentos            :b5, after b1, 5w
    Aprobación de la ingeniería básica       :milestone, m1, 2027-03-12, 0d

    section 1.3 Ingeniería de detalle
    Especificación de equipos                :d1, 2027-03-01, 4w
    Lista de E/S y arquitectura de control   :d3, 2027-03-15, 3w
    Diseño eléctrico y de tableros           :d2, after d3, 5w
    Celda robotizada y análisis de riesgos   :d4, 2027-03-01, 6w
    Diseño de la interfaz HMI                :d5, 2027-03-15, 4w
    Distribución en planta                   :d6, after d1, 4w
    Aprobación de la ingeniería de detalle   :milestone, m2, 2027-05-07, 0d

    section 1.4 Procura
    Cotizaciones y selección de proveedores  :p1, 2027-03-29, 4w
    Órdenes de compra y fabricación          :p2, after p1, 10w
    Pruebas FAT de equipos                   :p3, after p2, 2w
    FAT aprobadas                            :milestone, m3, 2027-07-16, 0d

    section 1.5 Software
    PLC de recursos compartidos              :s4, 2027-04-12, 5w
    PLC de la línea de yogur                 :s1, 2027-04-26, 7w
    PLC de la línea de queso                 :s2, 2027-05-10, 7w
    PLC de la línea de kumis                 :s3, 2027-05-24, 7w
    SCADA                                    :s5, 2027-05-10, 10w
    MES e integración con ERP                :s6, 2027-05-24, 11w

    section 1.6 Gemelo digital
    Gemelo digital                           :t1, 2027-05-24, 8w
    Simulación de la celda robotizada        :t2, 2027-05-10, 6w
    Puesta en marcha virtual                 :t3, 2027-07-19, 5w
    Puesta en marcha virtual aprobada        :milestone, m4, 2027-08-20, 0d

    section 1.7 Montaje
    Montaje mecánico                         :i1, 2027-07-19, 7w
    Instalación eléctrica e instrumentación  :i2, 2027-08-02, 7w
    Red industrial y servidores              :i3, 2027-07-19, 4w
    Instalación de la celda robotizada       :i4, 2027-08-23, 4w

    section 1.8 Pruebas y arranque
    Pruebas de lazo y de E/S                 :q1, 2027-09-20, 3w
    Pruebas SAT por línea                    :q2, after q1, 3w
    Arranque con producto y ajuste           :q3, 2027-10-11, 3w
    Validación de calidad e inocuidad        :q4, 2027-10-18, 2w
    SAT aprobadas                            :milestone, m5, 2027-10-29, 0d

    section 1.9 Cierre
    Capacitación                             :c1, 2027-10-11, 3w
    Documentación as-built y manuales        :c2, 2027-10-18, 3w
    Acta de entrega y soporte inicial        :c3, 2027-11-01, 2w
    Entrega del proyecto                     :milestone, m6, 2027-11-12, 0d
```

---

## 2. Hitos

| Hito | Fecha | Pago asociado |
|---|---|---:|
| Inicio del proyecto (firma del contrato) | 18 de enero de 2027 | 30 % |
| Aprobación de la ingeniería básica | 12 de marzo de 2027 | — |
| Aprobación de la ingeniería de detalle | 7 de mayo de 2027 | — |
| Pruebas FAT aprobadas | 16 de julio de 2027 | 30 % |
| Puesta en marcha virtual aprobada | 20 de agosto de 2027 | — |
| Pruebas SAT aprobadas | 29 de octubre de 2027 | 30 % |
| Entrega del proyecto | 12 de noviembre de 2027 | 10 % |

---

## 3. Ruta crítica

`Levantamiento → P&ID → Especificación de equipos → Cotizaciones → Fabricación de equipos → FAT → Montaje → Pruebas de lazo → SAT → Entrega`

El plazo lo determina la fabricación y entrega de los equipos (10 semanas). La programación de PLC, el SCADA y el gemelo digital avanzan en paralelo con la procura, y la puesta en marcha virtual permite llegar al montaje con el software ya probado.

---

## 4. Carga de trabajo por fase

| Fase | Semanas | Horas (EDT) |
|---|---:|---:|
| 1.1 Gestión | 43 | 560 |
| 1.2 Ingeniería conceptual y básica | 8 | 960 |
| 1.3 Ingeniería de detalle | 10 | 1.120 |
| 1.4 Procura | 16 | 400 |
| 1.5 Software | 17 | 1.680 |
| 1.6 Gemelo digital y puesta en marcha virtual | 15 | 720 |
| 1.7 Montaje e instalación | 9 | 960 |
| 1.8 Pruebas y puesta en marcha | 6 | 720 |
| 1.9 Capacitación, documentación y cierre | 5 | 360 |
| **Total** | **43** | **7.480** |

La capacidad del equipo es de 6 personas × 43 semanas × 42 h = 10.836 h, de modo que la ocupación media es del 69 %.
