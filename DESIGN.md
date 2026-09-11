---
name: QR Absen Harian Skomda
description: Stamped attendance ledger - QR Datang green and QR Pulang blue on ruled paper
colors:
  stamp-green: "#059669"
  stamp-green-deep: "#047857"
  stamp-blue: "#2563EB"
  stamp-blue-deep: "#1D4ED8"
  ledger-ink: "#182420"
  ledger-muted: "#5C665F"
  rule-line: "#DFDCD0"
  paper: "#FAFAF6"
  card-white: "#FFFFFF"
  errata-red: "#DC2626"
typography:
  display:
    fontFamily: "Archivo, system-ui, sans-serif"
    fontSize: "clamp(3.4rem, 11vw, 6.5rem)"
    fontWeight: 700
    lineHeight: 1
    letterSpacing: "-0.02em"
  title:
    fontFamily: "Archivo, system-ui, sans-serif"
    fontSize: "1.45rem"
    fontWeight: 800
    lineHeight: 1.2
    letterSpacing: "0.05em"
  body:
    fontFamily: "Archivo, system-ui, sans-serif"
    fontSize: "0.92rem"
    fontWeight: 400
    lineHeight: 1.5
  data:
    fontFamily: "JetBrains Mono, ui-monospace, monospace"
    fontSize: "0.85rem"
    fontWeight: 500
    lineHeight: 1.5
  label:
    fontFamily: "Archivo, system-ui, sans-serif"
    fontSize: "0.72rem"
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: "0.22em"
rounded:
  stamp: "6px"
  pad: "10px"
  card: "14px"
  rail: "999px"
spacing:
  sm: "8px"
  md: "16px"
  lg: "24px"
components:
  retry-datang:
    backgroundColor: "{colors.stamp-green-deep}"
    textColor: "{colors.card-white}"
    rounded: "{rounded.pad}"
    padding: "0.65rem 1.2rem"
  retry-pulang:
    backgroundColor: "{colors.stamp-blue-deep}"
    textColor: "{colors.card-white}"
    rounded: "{rounded.pad}"
    padding: "0.65rem 1.2rem"
---

# Design System: QR Absen Harian Skomda

## Overview

**Creative North Star: "The Stamped Ledger"**

A school attendance journal, validated in ink. The page is a ruled ledger sheet on stark paper; each QR code sits inside a rubber-stamp frame in full-strength section color, as if the day itself stamped its approval. Nothing floats, nothing glows: ink, rules, tabs, and tabular numerals do all the work. Density is deliberate, a gate-side board read at a glance and at arm's length.

**Key Characteristics:**
- Ruled paper ground with ink-black structure lines.
- Two full-strength section hues that own whole regions, never scattered accents.
- Tabular mono reserved strictly for measured data: clock, IDs, countdown.
- Motion is a single stamp-in moment plus a live clock; everything else stands still.

## Colors

Two working inks on paper white; each section hue owns its gate outright.

### Primary
- **Stamp Green** (#059669): the Datang gate. Header bands, QR stamp frames, LIVE stamp, retry buttons (deep variant). Owns the left half of the page.

### Secondary
- **Stamp Blue** (#2563EB): the Pulang gate. Same duties as green, right half of the page.

### Neutral
- **Ledger Paper** (#FAFAF6): page ground, barely warm white.
- **Card White** (#FFFFFF): gate and ledger cards sitting on the paper.
- **Ledger Ink** (#182420): green-black ink for text, borders, rails, masthead rules.
- **Sage Muted** (#5C665F): secondary text on paper or white.
- **Rule Line** (#DFDCD0): ledger rules, dividers, perforation.

### Named Rules
**The Full-Strength Section Rule.** Green and blue appear at full saturation in whole regions (header bands, stamp frames), never as scattered small accents. Tints of the same hues may fill the day-phase rail bands only.
**The Errata Slip Rule.** Errors use signal red (#DC2626) on pale wash (#FEF2F2) with deep red text (#991B1B), formatted as a labeled slip, never a toast.

## Typography

**Display Font:** Archivo (with system-ui fallback)
**Body Font:** Archivo (with system-ui fallback)
**Label/Mono Font:** JetBrains Mono (with ui-monospace fallback)

**Character:** A workhorse grotesque for words, a technical mono for measurements. Caps with wide tracking name things; mono with tabular figures counts things. Serif display never enters this world.

### Hierarchy
- **Display** (700, clamp(3.4rem, 11vw, 6.5rem), 1): the giant WIB clock, tabular numerals, with a small muted WIB suffix.
- **Title** (800, 1.45rem, 1.2): white caps on full-hue gate bands.
- **Body** (400, 0.92rem, 1.5): gate descriptions, footer notes.
- **Data** (500, 0.85rem, mono): register numbers, timestamps, dates.
- **Label** (700, 0.72rem, 0.22em tracking, uppercase): section labels, rail legend, error tags.

### Named Rules
**The Mono Measures Rule.** JetBrains Mono appears only for clock time, IDs, dates, countdowns, and register codes. Words about the product are always Archivo. Mono as decoration is a defect.

## Layout

Ledger desk: centered column (max 72rem), masthead rule on top, hero row (giant clock beside the next-QR ledger card), twin stamp gates separated by a dashed perforation line on desktop, footer rule at the close. More space between sections (about 2rem) than inside cards (about 1.2rem). Below 768px the gates stack; below 860px the hero stacks; below 520px the masthead wraps. Day-phase rail bands keep true hour proportions (PAGI 5, SIANG 5, SORE 4, MALAM 10 of 24).

## Elevation & Depth

Depth is one soft lifted shadow, used identically on ledger cards and gates.

### Shadow Vocabulary
- **Lifted sheet** (`box-shadow: 5px 9px 18px rgba(24, 36, 32, 0.14)`): ledger cards and gate cards at rest.

### Named Rules
**The Offset-Plus-Blur Rule.** Every shadow carries both an offset and a soft blur. Zero-blur block shadows never ship in this world.

## Shapes

Ink-bordered rectangles with a 14px card radius; 10px on pads, buttons, and slips; 6px on stamps and chips; full-round pill only for the day rail. QR pads carry a 3px double-rule stamp frame in the gate's section hue. The perforation divider is a 2px dashed rule. Border radius never exceeds 14px; pills are reserved for the rail.

## Components

### Buttons
- **Shape:** rounded pads (10px radius), bold 0.95rem type.
- **Primary:** deep section hue (Datang #047857, Pulang #1D4ED8) with white text; AA-safe on both.
- **Active:** inverts to ink background with paper text, like a pressed stamp.
- **Focus:** 3px ink outline with 2px offset, always visible.

### Stamp Gates
- **Corner Style:** 14px card radius with 1.5px ink border.
- **Background:** white card on paper ground.
- **Shadow Strategy:** the lifted-sheet shadow.
- **Anatomy:** full-hue header band with white title, muted description line, mono register row ruled top and bottom, double-rule QR pad, mono timestamp.

### Day Rail
- Pill rail with four labeled phase bands in true hour proportion, etched tick overlay, and a stepped now-tab carrying the current HH:MM. Color never travels alone: every band is labeled.

### Error Slips
- Red-bordered slip with a tracked mono tag naming the failure, plain-language recovery sentence, and the gate's retry button. One per gate, hidden until its fetch fails.

## Do's and Don'ts

### Do:
- **Do** keep both gates visible together at every viewport; the admin reads two validations at once.
- **Do** render QR codes at 220px minimum on pure white pads with a quiet zone; scanability outranks decoration.
- **Do** label every color-coded element in words (gate titles, phase names, register numbers).
- **Do** use tabular numerals for all times, IDs, and countdowns so digits never jitter.

### Don't:
- **Don't** show the raw JSON payload on the page (owner decision); it lives inside the QR only.
- **Don't** use serif display, cream nostalgia styling, glow, gradients-as-decoration, or purple anywhere.
- **Don't** use mono for prose or headlines; mono measures, Archivo speaks.
- **Don't** add a third gate, a map, a marquee, or decorative illustration; the ledger stays a ledger.
- **Don't** ship zero-blur shadows, kickers above headings, or Unicode glyphs as icons.
