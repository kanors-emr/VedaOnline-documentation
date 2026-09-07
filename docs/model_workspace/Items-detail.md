---
description: Items View in Veda Online — topology and parameters for processes and commodities, and open source Excel from pivot value cells.
---

# Items detail

## Introduction

Items View (Items detail) shows **one item at a time**: process, commodity, user constraint, or commodity group — its parameters, topology, and diagrams.

<img src="../images/new_items_detail.png" class="align-center" width="600" alt="Items View" />

## Common tasks

Jump to the step you need:

- Select a region and item → [Select an item](#select-an-item)
- See parameters in a cube → [Pivot View](#pivot-view)
- Open the Excel behind a number → [Open source Excel from a pivot cell](#open-source-excel-from-a-pivot-cell)
- See name, description, and a parameter table → [Detailed View](#detailed-view)
- See inputs and outputs around a process → [Basic View](#basic-view)
- Draw topology → [Network Diagram](#network-diagram) / [New RES Diagram](#new-res-diagram)
- Save or Push the workbook → [Excel Viewer](Navigator.md#excel-viewer)

What a TIMES process is: [TIMES process](#times-process).

## How to use it?

### Select an item

1. Choose **Region** (and **Framework** if that dropdown is shown).
2. In the left list, pick a type: **Prc** (process), **Com** (commodity), **UC** (user constraint), or **CG** (commodity group). Search the list if needed.
3. Click one item. The right-hand views update for that item.

### Pivot View

Pivot View shows the assembled parameters for the selected item. Rearrange rows and columns the same way as in [Browse](Browse.md).

<figure class="align-center">
<img src="../images/items_view_pivot.png" alt="Items View pivot grid" />
</figure>

### Open source Excel from a pivot cell

Double-click a **number** in the pivot (not a year or attribute name). Hover first — the tooltip shows workbook, sheet, and cell. You can also select the number and press **Enter**.

The workbook opens in **Excel Viewer**:

<figure class="align-center">
<img src="../images/excel_viewer.png" alt="Excel Viewer" width="700" />
</figure>

Excel Viewer does not open when several records are combined in one number, or when the tooltip has no file location. If the tooltip also lists a second (seed) workbook, both files open.

**Save** writes the file on the KanORS server only. It does **not** Push to GitHub and does **not** Synchronize the database. Full Save / Push / Pull rules: [Excel Viewer](Navigator.md#excel-viewer).

### Detailed View

Shows the selected item’s name, description, and a table of its parameters.

<img src="../images/items_view_detail_view.png" class="align-center" height="200" alt="Detailed View" />

A video overview is linked from the camera icon in this panel: [Items View on YouTube](https://youtu.be/ds4iRFE69Ag).

### Basic View

Shows how the selected process (or commodity) sits in the RES: user constraints, input commodities, the process, output commodities, and auxiliary flows.

<img src="../images/items_view_input_output.png" class="align-center" height="250" alt="Basic View" />

The same panel has two tabs:

- **Grid Map** — items on a map (where coordinates exist).
- **RES** — the input / process / output schematic above.

Click a name in Basic View to jump to that item in the left list.

### Network Diagram

**Network Diagram** (**Alt + N + D**) opens a window of topology around the selected item, up to five input/output levels. You can open more items as extra tabs in that window.

<img src="../images/items_view_network_diag.png" class="align-center" height="300" alt="Network Diagram" />

Network diagram is **not** available for user constraints or commodity groups.

### New RES Diagram

**New RES Diagram** opens a RES-style topology window for the current process or commodity. The button is hidden for user constraints and commodity groups.

<img src="../images/items_view_new_res_diag.png" class="align-center" height="300" alt="New RES Diagram" />

## TIMES process

- A process converts input commodity(ies) to output commodity(ies).
- Each process is linear (for example output proportional to input; investment and fixed O&M scale with capacity; variable O&M scale with activity).
    - A power plant converts input fuel (coal, oil, gas, nuclear, or a renewable source) to electricity.
    - A plug-in diesel hybrid car can be modelled as a process that converts electricity and/or diesel to passenger-miles.
- A typical national model may have about 1000 processes.

<img src="../images/TIMES_process.png" class="align-center" alt="TIMES process" />
