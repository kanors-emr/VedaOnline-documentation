---
description: Navigator for Veda Online — Excel templates, GitHub Pull/Push, file status, Synchronize, and Excel Viewer.
---

# Navigator

## Introduction

- The Navigator provides a comprehensive view of all the templates in the various folders managed by Veda for the current model.
- The Navigator is the main vehicle for accessing, importing, and coordinating the various templates that make up a model.
- Its main screen is divided into sub-windows according to the various types of templates managed by Veda.
- For GitHub-linked models, use **Pull**, **Push**, and **Commits** to keep the server folder aligned with GitHub. Double-click a file row to open it in the browser **Excel Viewer**.

<img src="../images/navigator.png" class="align-center" alt="image" />

## Common tasks

Jump to the step you need:

- Open or edit Excel in the browser → [Excel Viewer](#excel-viewer)
- Excel Viewer keyboard shortcuts → [Keyboard shortcuts](#keyboard-shortcuts)
- Save Excel edits to the KanORS server → **Save** in [Excel Viewer](#excel-viewer). Saving does **not** send the file to GitHub or update the Veda database.
- Send saved Excel edits from the KanORS server to GitHub → [Push Excel files to GitHub](#push-excel-files-to-github)
- Get the latest files from GitHub → **Pull** on the toolbar. Then **Synchronize** if you also need the Veda database to match those files.
- Undo local Excel edits without sending them to GitHub → **Discard** in the [Push](#push-excel-files-to-github) window (model owner)
- Save or update your GitHub token → [User Profile](../User-Profile.md#github-credentials)

### Edit, Save, Push, and Synchronize

For Excel files edited in Veda Online, remember this workflow:

**Edit → Save to KanORS server → Push to GitHub**

**Synchronize** is separate. It reads the selected Excel files from the KanORS server into the **Veda database**.

- **Save** → saves the edited workbook on the **KanORS server** only.
- **Push** → sends the saved server copy to **GitHub**.
- **Synchronize** → imports the selected workbook data into the **Veda database**.
- Saving a workbook does **not** automatically Push it to GitHub and does **not** automatically Synchronize it with the database.

Template types (SysSettings, SubRES, scenarios, and so on) are listed under [Quadrants](#quadrants).

## How to use it?

### Toolbar actions

<img src="../images/navigator_toolbar.png" class="align-center" alt="Navigator toolbar" />

**Push** and the **?** Excel Viewer help appear only if Excel Viewer is available on your account.

1.  **Options Menu** – Extra Navigator features (NoSeedValue, Tag Details, Model Trade Links, Sync Logs, Delete Logs). See [Options menu](#options-menu).
2.  **Start from Scratch** – Deletes model data from the database (Reports are kept), then Pulls files from GitHub. You must **Synchronize** again afterwards. Private repository: saved token required ([GitHub credentials](#github-credentials)).
3.  **Pull** – Replaces the model folder on the server with GitHub. Local folder edits on the server are discarded. The database does **not** change until you **Synchronize**. Private repository: saved token required. If another git action is already running, wait and try again.
4.  **Push** – Sends selected Navigator Excel files that are saved on the KanORS server to GitHub. Full steps: [Push Excel files to GitHub](#push-excel-files-to-github).
5.  **Commits** – Lets you review your GitHub commits directly in Veda Online.
6.  **File Status** – Colour legend for each template:
    - **NotImported** – not yet read into the database
    - **ToImport** – selected for importing with the next Synchronize (orange)
    - **Consistent** – template is in sync with the database
    - **InConsistent** – file has been modified after the last Synchronize
    - **ToRemove** – previously imported template now flagged for removal from the database
    - **FileMissing** – a previously imported template that no longer exists in the template folder
    - **Error** – the file has thrown an error
    - **NotOnGitHub** – local Excel changes not yet sent to GitHub. A **golden yellow** dot on the file row and a yellow count on **Push** mean the same thing.
7.  **Email** – If this checkbox is cleared, Veda Online will not send an email after synchronization finishes.
8.  **Synchronize** – Reads selected Excel files (**ToImport**, orange) from the KanORS server into the Veda database. This is **not** Push: GitHub does not change.
    - Watch progress in the right-hand log or on the **Jobs Dashboard**.
    - If you edited Excel in Navigator and have not Pushed yet, Veda Online warns you. **Continue Sync** still loads the files into the database, but GitHub will not have those edits yet. **Cancel** if you want to Push first.
    - An email is sent when sync finishes (unless you cleared the Email checkbox).
    - After synchronizing a model, you can return to the Navigator.

### Push Excel files to GitHub

Use **Push** (shortcut **Alt + U**) after you edit and **Save** Navigator Excel (`.xlsx` / `.xlsm`) and want those saved workbooks on GitHub.

When you save a workbook in Excel Viewer, the edited file is saved on the **KanORS server**. It is **not** sent to GitHub automatically. Push sends that saved server copy to GitHub.

You need a GitHub token that can **update that repository**. Save it on [User Profile](../User-Profile.md#github-credentials). When you click **Push**, Veda Online checks the token first. If none is saved, or it cannot update the repository, you get an error and the Push window does **not** open.

1. Click **Push**. A **yellow** badge shows how many Excel files have local changes.
2. Select the files to send.
3. Enter a **commit message** (required).
4. Click **Push**.

If GitHub already has newer files than this model folder, Push is blocked. **Pull** first. The window lists Excel files that Pull will replace. Veda Online does not Pull automatically when you click Push.

After success you get a confirmation and a link to the commit on GitHub. **Last Synced** on the model still shows the last **Synchronize**, not this Push.

**Discard** uses the same checkboxes. It is for the **model owner**. It restores or deletes the selected local Excel files from what you last Pulled. It does not change GitHub. Confirm first; this cannot be undone. Discard is hidden when GitHub already has newer files — use **Pull** instead. Unchecked files stay as they are.

### GitHub credentials

GitHub-linked models use the token saved on [User Profile](../User-Profile.md#github-credentials).

- **Public** repositories: Pull and Start from Scratch do not need a token. **Push** always needs a token that can update the repository.
- **Private** repositories: Pull, Start from Scratch, and Push need a valid saved token.
- You can **open** Excel Viewer without a token. **Save** needs a saved token, and GitHub must not have newer files than this folder.

### Excel Viewer

Use **Excel Viewer** to view and edit a model Excel file in the browser.

<figure class="align-center">
<img src="../images/excel_viewer.png" alt="Excel Viewer" width="700" />
</figure>

#### How to open

- **Navigator:** Double-click a file row in any scenario grid.
- **Items View / Browse:** Double-click a **number** in the pivot, or select it and press **Enter**. Hover the cell first to see workbook, sheet, and cell in the tooltip. Do not double-click row or column labels (years, attribute names) — those do not open a file.

Click **?** on Navigator for in-app Excel Viewer help. In the viewer, press **F1** or the toolbar help icon for keyboard shortcuts.

#### Why open or edit a file

Model input lives in these Excel templates. Open a file to check or change that data in the browser — for example to fix a declaration, add a process or commodity, or update a value. After you **Save**, the change is on the KanORS server only. Use **Push** to send it to GitHub, and **Synchronize** to load it into the Veda database. See [Edit, Save, Push, and Synchronize](#edit-save-push-and-synchronize).

#### Keyboard shortcuts

In Excel Viewer, press **F1** or the help icon to open this list.


**File and editing**

| Shortcut | Action |
| --- | --- |
| Ctrl / Cmd + S | Save |
| Esc | Cancel cell edit, or close this help |
| Alt + Enter | New line inside a cell |
| F1 | Open this help |
| F2 | Edit the selected cell |
| Backspace / Delete | Clear cell text |
| Letter, number, or = | Start typing in the selected cell |

**Clipboard and format**

| Shortcut | Action |
| --- | --- |
| Ctrl / Cmd + C | Copy |
| Ctrl / Cmd + X | Cut |
| Ctrl / Cmd + V | Paste |
| Ctrl / Cmd + B | Bold |
| Ctrl / Cmd + I | Italic |
| Ctrl / Cmd + U | Underline |

**Navigation**

| Shortcut | Action |
| --- | --- |
| Arrow keys | Move selection |
| Shift + Arrow | Extend selection |
| Ctrl / Cmd + Arrow | Jump to the edge of the used range |
| Tab / Shift + Tab | Move right / left |
| Enter / Shift + Enter | Move down / up |
| Ctrl / Cmd + Space | Select column |
| Shift + Space | Select row |


#### Insert rows and columns

| Shortcut | Action |
| --- | --- |
| Right-click → Insert Row / Insert Column | Opens the insert box. Rows are added **below** the selected row; columns to the **right** of the selected column. |
| Count (1–300) | How many to add. If several rows or columns are selected, that count is the default. |
| Insert or Enter | Adds **blank** rows or columns. Fill and borders from the clicked row or column are not copied. |
| Esc | Closes the insert box without adding anything. |
| Right-click → Delete Row / Delete Column | Removes **one** row or column. There is no count box for delete. |

#### Worksheets

- Add a sheet with **+** on the bottom bar.
- At most **50** worksheets in Excel Viewer. Further adds show a warning.

#### GitHub

- If GitHub already has newer files (**GitHub is ahead**), a **view only** banner asks you to **Pull** first. Save and external-link updates are disabled until you Pull.
- If the file is on GitHub, **Pull** the latest files before you edit.
- You can **open** a file without a GitHub token. **Save** needs a token on [User Profile](../User-Profile.md#github-credentials), and GitHub must not have newer files than this folder.

#### External links

- If the workbook links to other files, you may be asked to **Update** or **Don't Update**.
- **Update** refreshes data from the linked files. **Don't Update** keeps the data already in the workbook.
- View-only files cannot update external links.

#### Save

- Use the toolbar **Save** button or **Ctrl + S**. If a cell is still being edited, Save commits that cell first.
- **Save stores the edited workbook on the KanORS server only.**
- Saving does **not** automatically send the workbook to GitHub. Use **Push** when you want the saved server copy on GitHub.
- Saving does **not** automatically update the Veda database. Use **Synchronize** when you want the workbook data imported into the database.
- Auto-save runs about **60 seconds** after your last edit.
- Closing the tab with unsaved edits shows a browser warning.
- After a successful save, Navigator refreshes that file row.

#### Tips

- Maximum file size is **50 MB**. Larger files cannot be opened in Excel Viewer.
- Charts are shown as static images. Saving writes **cell edits only**; original charts in the `.xlsx` file are preserved. To edit charts, open the file in Excel on your computer.

## Quadrants

- **SysSetting**: Used to declare the basic structure of the model, including regions, time slices, start year, and synchronization settings. There is only one such file, and it has a fixed name that stands for System Settings.
- **Base scenario \[BS\]**: Templates used to set up the base-year (B-Y) structure of the model, including existing commodities, current process stock, and base-year end-use demand levels. The B-Y templates are named as `VT_<workbook name>_<sector>_<Version>` (for example, `VT_REG_PRI_V1`). The number and names of these templates depend on the model structure and on how the input data is organized. The B-Y templates are introduced in `DemoS_001`.
    - **BY_Trans**: Transformation files used to update information already included in the B-Y templates or to insert new information for existing processes. They work like scenario files, but their rule-based filters and update or insert changes apply only to processes and commodities that already exist in the B-Y templates. The `BY_Trans` file is introduced in `DemoS_009`.
- **BaseTrans**: Operations on the BS templates.
- **SubRES \[SR\]**: Files used to introduce new commodities and processes in the RES that are not part of the B-Y templates. Unlike B-Y templates, SubRES files are region-independent. Each SubRES file has a corresponding transformation file for adding region-specific process attributes, including availability by region. The naming conventions are `SubRES_<name>` and `SubRES_<name>_Trans`.
- **Regular Scenarios \[RS\]**: Scenario files used to update existing information or insert new information in any part of the RES, including B-Y templates, SubRES files, and Trade files. They are also used to include additional user constraints in the model. The naming convention is `Scen_<scenario name>`. These files can insert or update attributes for previously declared RES components, but they cannot add new commodities or processes. Scenario files are introduced in `DemoS_004`.
- **Demand Scenarios \[DS\]**: Demand templates include the information required to project end-use demands for energy services in each region, such as macroeconomic drivers and sensitivity series. Multiple demand files may be used to model different demand growth scenarios. The naming convention is `ScenDem_<scenario name>`. This section also contains `Dem_Alloc+Series`, which assigns a demand driver and a sensitivity or elasticity series to each end-use demand in each region. Demand files and tables are described in `DemoS_010`.
- **Trade Scenarios \[TS\]**: This section contains files where unilateral and bilateral trade links between regions are declared, together with associated data where needed. It also contains all attribute specifications for trade processes. Multiple trade files may be used for different trade scenarios or commodities. The naming convention is `ScenTrade_<scenario name>`. Trade files are introduced in `DemoS_005`.
- **Parametric Scenarios \[PS\]**: Functionality designed to support multiple runs and parametric analysis through programmed multi-value scenario sets.
- **No Seed Values \[NSV\]**: Files that do not provide seed values to any other scenario. These are processed in parallel. Veda identifies which files can be converted into NSV scenarios. This feature was introduced in 2019.

!!! note

    - 1 contains comprehensive information about the model. Veda will not synchronize without this file.
    - 2 and 3 are calibration templates for the base year.
    - 5 to 8 are groups of flexible, rule-based scenario files.

## Options menu

Open the **Options** control on the left of the Navigator toolbar.

### NoSeedValue Scenario

Opens **NoSeedValue Candidates**: Excel files Veda has identified as NSV (they do not provide seed values to other scenarios). The list shows relative path, scenario name, and processing time. NSV files are also listed in the [No Seed Values](#quadrants) quadrant and can be processed in parallel during Synchronize.

### Tag Details

Opens a table of every Veda **tag** found in the model templates: workbook, sheet, cell, scenario type, scenario, tag name, processing time, and last processed time. Use filters and search to find a tag. Hover a file row in Navigator to see tag counts for that file. Tag processing order is described under [Tags processing order](../TagsProcOrder/Tags-proc-order.md).

### Model Trade Links

Opens a map of trade links declared in the model (window title **TradeLinks Scenario**). Each line is a trade between two regions. Use this to check that trade templates match the intended region pairs. Trade files themselves sit in the [Trade Scenarios](#quadrants) quadrant.

### Sync Logs

Shows the **Synchronize Log** from Navigator syncs.

- **All** — every stored sync-log entry for the model.
- **New** — entries from the latest Synchronize only.

The log lists warnings and errors (grouped by message, tag type, and workbook). If the lower pane has an **Open** action, it jumps to the matching deleted-rows list (same data as **Delete Logs**).

### Delete Logs

Shows rows **removed from the database** during Synchronize, grouped by reason and scenario. Choose the object type, then **All** or **New**:

- **Commodity** / **Process** / **Topology** — deleted commodities, processes, or topology links.
- **Step1** — deleted rows from model input (`veda_data`).
- **Step2** — deleted rows from the flat file used for TIMES/OSeMOSYS.

**All** is the full history; **New** is the latest Synchronize only.
