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
- Send Excel edits to GitHub → [Push Excel files to GitHub](#push-excel-files-to-github)
- Get the latest files from GitHub → **Pull** on the toolbar. Then **Synchronize** if you also need the database to match those files.
- Undo local Excel edits without sending them to GitHub → **Discard** in the [Push](#push-excel-files-to-github) window
- Save or update your GitHub token → [User Profile](../User-Profile.md#github-credentials)

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

## How to use it?

### Toolbar actions

<img src="../images/navigator_toolbar.png" class="align-center" alt="Navigator toolbar" />

1.  **Options Menu** – Provides access to additional Navigator features:

    - **NoSeedValue Scenario**

        !!! note

            <span class="vo-coming-soon">Coming soon.</span> This section will be updated to describe the <strong>NoSeedValue Scenario</strong> in Veda Online.

    - **Tag Details**

        !!! note

            <span class="vo-coming-soon">Coming soon.</span> This section will be updated to describe <strong>Tag Details</strong> in Veda Online.

    - **Model Trade Links**

        !!! note

            <span class="vo-coming-soon">Coming soon.</span> This section will be updated to describe <strong>Model Trade Links</strong> in Veda Online.

    - **Sync Logs**

        !!! note

            <span class="vo-coming-soon">Coming soon.</span> This section will be updated to describe <strong>Sync Logs</strong> in Veda Online.

    - **Delete Logs**

        !!! note

            <span class="vo-coming-soon">Coming soon.</span> This section will be updated to describe <strong>Delete Logs</strong> in Veda Online.

2.  **Start from Scratch** – Deletes model data from the database (Reports are kept), then Pulls files from GitHub. You must **Synchronize** again afterwards. Private repository: saved token required ([GitHub credentials](#github-credentials)).
3.  **Pull** – Replaces the model folder on the server with GitHub. Local folder edits on the server are discarded. The database does **not** change until you **Synchronize**. Private repository: saved token required. If another git action is already running, wait and try again.
4.  **Push** – Sends selected Navigator Excel files to GitHub. Full steps: [Push Excel files to GitHub](#push-excel-files-to-github).
5.  **Commits** – Lets you review your GitHub commits directly in Veda Online.
6.  **File Status** – Provides feedback about the status of the various files and the integrated database managed by Veda, according to the color legend at the bottom of the form.
    - **Not imported** – not yet read into the database
    - **Imported** – selected for importing with the next SYNC
    - **Consistent** – template is in sync with the database
    - **Inconsistent** – file has been modified after the last SYNC operation
    - **ToRemove** – previously imported template now flagged for removal from the database
    - **FileMissing** – a previously imported template that no longer exists in the template folder
    - **Error** – the file has thrown an error
    - A **red marker** on a Navigator row (and a red count on **Push**) means that Excel file has local changes that have not been sent to GitHub.
7.  **Email Checkbox** – If this checkbox is cleared, VedaOnline will not send an email after synchronization finishes.
8.  **Synchronize** – Reads selected Excel files (`ToImport`, orange) into the Veda database. This is **not** Push: GitHub does not change.
    - Watch progress in the right-hand log or on the **Jobs Dashboard**.
    - If you edited Excel in Navigator and have not Pushed yet, Veda Online warns you. **Continue Sync** still loads the files into the database, but GitHub will not have those edits yet — the GitHub copy can differ from what you just synced. **Cancel** if you want to Push first.
    - An email is sent when sync finishes (unless you cleared the email checkbox).
    - After synchronizing a model, you can return to the Navigator.

### Push Excel files to GitHub

Use **Push** (shortcut **Alt + U**) after you edit Navigator Excel and want those workbooks on GitHub.

1. Click **Push**. A red badge shows how many Excel files have local changes.
2. Select the files to send.
3. Enter a **commit message** (required).
4. Click **Push**.

You need a GitHub token that can **write** that repository. Save it on [User Profile](../User-Profile.md#github-credentials).

If GitHub already has newer commits (**GitHub is ahead**), Push is blocked. **Pull** first. The window lists Excel files that Pull will replace. Veda Online does not Pull automatically when you click Push.

After success you get a confirmation and a link to the commit on GitHub. **Last Synced** still shows the last **Synchronize**, not this Push.

**Discard** uses the same checkboxes. It restores or deletes the selected local Excel files from what you last Pulled. It does not change GitHub. Confirm first; this cannot be undone. Discard is hidden when GitHub is ahead — use **Pull** instead. Unchecked files stay as they are.

### GitHub credentials

GitHub-linked models use the token saved on [User Profile](../User-Profile.md#github-credentials).

- **Public** repositories: Pull and Start from Scratch do not need a token. **Push** always needs a write token.
- **Private** repositories: Pull, Start from Scratch, and Push need a valid saved token.
- You can **open** Excel Viewer without a token. **Save** needs a saved token and a branch that is up to date with GitHub.

### Excel Viewer

Use **Excel Viewer** to view and edit a model Excel file in the browser.

<figure class="align-center">
<img src="../images/excel_viewer.png" alt="Excel Viewer" width="700" />
</figure>

#### How to open

- **Navigator:** Double-click a file row in any scenario grid. On SubRES rows, you can also open the matching `*_Trans` workbook.
- **Items View / Browse:** Double-click a pivot **value** (the number), or select it and press **Enter**. Hover the cell first to see workbook, sheet, and cell in the tooltip. Do not double-click row or column labels (years, attribute names) — those do not open a file.

Click **?** on Navigator for in-app Excel Viewer help. In the viewer, press **F1** or the toolbar help icon for keyboard shortcuts.

#### GitHub

- If the file is on GitHub, **Pull** the latest changes before you edit.
- When GitHub is ahead, the file still opens but in **view only**: Save is disabled, and a banner asks you to pull first. You cannot save or update external links until you Pull.
- You can **open** a file without a GitHub token. **Save** needs a token on [User Profile](../User-Profile.md#github-credentials) and a branch that is up to date with GitHub.

#### External links

- If the workbook links to other files, you may be asked to **Update** or **Don't Update** when it opens.
- **Update** refreshes data from the linked files. **Don't Update** keeps the data already in the workbook.
- View-only files cannot update external links.

#### Save

- Use the toolbar **Save** button or **Ctrl + S**. If a cell is still being edited, Save commits that cell first.
- Auto-save runs about **60 seconds** after your last edit.
- Closing the tab with unsaved edits shows a browser warning.
- After a successful save, Navigator refreshes that file row.

#### Tips

- Maximum file size is **50 MB**. Larger files cannot be opened in Excel Viewer.
- A workbook can have at most **50** worksheets.
- Charts are shown as static images. Saving writes **cell edits only**; original charts in the `.xlsx` file are preserved. To edit charts, open the file in Excel on your computer.
