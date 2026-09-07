---
description: Browse Veda Online input data in a pivot cube, and open the source Excel workbook at the matching sheet and cell.
---

# Browse

## Introduction

- Browse shows the **assembled model input** after Synchronize — the data Veda actually read from Excel, in one pivot cube.
- Use it to check declarations, compare scenarios or regions, and jump from a number to the source workbook in **Excel Viewer**.

<img src="../images/Browse.png" class="align-center" alt="Browse" />

## Common tasks

Jump to the step you need:

- Load data into the pivot → [Load data](#load-data)
- Filter Process or Commodity by set → [Filter using sets](#filter-using-sets)
- Open the Excel behind a number → [Open source Excel from a pivot cell](#open-source-excel-from-a-pivot-cell)
- Save or Push that workbook → [Excel Viewer](Navigator.md#excel-viewer)

## How to use it?

### Load data

1. Select at least one item in any dimension list (scenario, region, process, commodity, attribute, or user constraint).
2. Click **Browse** (shortcut **Alt + G**).
3. The pivot fills in the lower pane. Rearrange rows and columns as needed.

**Reset** (**Alt + R**) clears the dimension selections.

If the lists are empty, Synchronize the model first.

### Filter using sets

- In the Process and Commodity lists, choose **User Set** or **TIMES Set** from the dropdown.
- The list then shows only members of that set.

<img src="../images/browse_set.png" class="align-center" alt="Browse set filter" />

### Open source Excel from a pivot cell

After the pivot loads, double-click a **number** in the grid (not a year or attribute name). Hover first — the tooltip shows workbook, sheet, and cell. You can also select the number and press **Enter**.

The workbook opens in **Excel Viewer**:

<figure class="align-center">
<img src="../images/excel_viewer.png" alt="Excel Viewer" width="700" />
</figure>

Excel Viewer does not open when several records are combined in one number, or when the tooltip has no file location. If the tooltip also lists a second (seed) workbook, both files open.

This action is not available in Results or Reports.

**Save** writes the file on the KanORS server only. It does **not** Push to GitHub and does **not** Synchronize the database. Full Save / Push / Pull rules: [Excel Viewer](Navigator.md#excel-viewer).

## Why Browse

All model declarations live in Excel. Use Browse (or Items detail) to **see** what was imported, not to replace Excel as the place you specify data.

- A syntax problem can mean a declaration was ignored or read differently from what you intended.
- One item can be declared in several workbooks; Browse shows those values together.
- The cube is the data in the Veda database after the last Synchronize.
