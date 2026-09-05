---
description: Browse Veda Online input data in a pivot cube, and open the source Excel workbook at the matching sheet and cell.
---

# Browse

## Introduction

!!! note

    All data declarations for Veda models are done in Excel files. To *visualize* the model, use the interface instead of relying on Excel files. Excel should be used for initial and additional data specification. To check declarations or topology for a particular item, use Browse (or Items detail).

Browsing model input is **necessary** for two reasons:

- You may have a syntax error and some of your declarations may have been ignored, or read differently from what you intended.
- The declarations for a single item may be spread across several Excel files, and you will see them all in one place in this interface.
- Browse presents the actual model data.

<img src="../images/Browse.png" class="align-center" alt="image" />

The Browser thereby enables the user to view subsets of the assembled data in a cube by selecting the scenario(s), region(s), process(es), commodity(ies), and/or the attribute(s) of interest. It is possible to rearrange the layout of the cube by adding/removing dimensions (columns and rows) to/from the table.

## How to use it?

### Load data in Pivot Grid

- Select at least one element from any element list.
- Click **Browse** to load data in the Pivot Grid.

### Filter using sets

- In the Process and Commodity element lists, select **User Set** or **TIMES Set** from the dropdown (as shown below).
- The selected set filters the linked elements.

<img src="../images/browse_set.png" class="align-center" alt="image" />

### Open source Excel from a pivot cell

When **Excel Viewer** is enabled for your account, you can jump from a Browse pivot **value** (the number) to the template that supplied it.

- Hover the cell first. The tooltip shows workbook, sheet, and cell. If the value also has a **seed** source, the tooltip lists that workbook too.
- Openable value cells use a pointer cursor. Click once to select the cell (blue outline).
- **Double-click** the value cell, or press **Enter** on the selected cell, to open **Excel Viewer** at that sheet and cell.
- If the cell has a seed source, both workbooks open (primary first, then seed).

Excel Viewer does **not** open from:

- Row or column labels (attribute names, years, and other dimension text)
- Aggregated cells (more than one underlying record) — the tooltip already says the location is unavailable
- Cells with no file path or cell address

GitHub save rules are the same as Navigator: if GitHub is ahead, or no token is saved on a linked model, the workbook opens **view only**. See [Excel Viewer](Navigator.md#excel-viewer) and [Push Excel files to GitHub](Navigator.md#push-excel-files-to-github).

This open-from-cell action is not available in Results or Reports.
