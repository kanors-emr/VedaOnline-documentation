---
description: Use Run Manager in Veda Online to define cases, compose groups, and submit TIMES model runs from the browser.
---

# Run Manager

## Introduction

- The Run Manager is used to compose and submit model runs

- Each model run is based on a Case definition comprising [Run Manager Groups](https://www.youtube.com/watch?v=tE58L8RIBFM&list=PLRCe_SRAk7hOvHdyCuLQ15-6JldaH8Ryu&index=6) :

  <img src="../images/run_manager_1.png" class="align-center" width="600" alt="image" />

## How to use it?

### 1-4 Run Manager Groups

The first four sections of Run Manager are:

- **1 - Scenario Groups**: Check BASE/SysSettings and the list of scenarios to be included in a "cluster" that is then given a name for inclusion later in a Case Definition for a model run.

- **2 - Region Groups**: Designation of the regions to be included in the Group definition.

- **3 - Parametric Groups**:

    !!! note

        <span class="vo-coming-soon">Coming soon.</span> This section will be updated to describe the <strong>Parametric Groups</strong> in Veda Online.

- **4 - Property Groups**: Which GAMS switches are to be employed for the run.

### Group Actions

The first four group sections support common actions such as creating, updating, and deleting groups.

- **New/Copy Groups** [Create/Edit/Delete Groups](https://www.youtube.com/watch?v=rKRSE-WC1Ns&list=PLRCe_SRAk7hOvHdyCuLQ15-6JldaH8Ryu&index=7)

    - Click **New/Copy** button.
    - Enter the required group name in the text box.
    - Click **Save** button.
    - The new group will be added to the list.

- **Update Groups**

    - Select the required saved group from the dropdown.
    - Modify the required checkboxes, selections, expandable items, or property values.
    - After making changes, the **Update Group** button appears.
    - Click **Update Group** to save the modified group.

- **Delete Groups**

    - Select the group you want to remove.
    - Click **Delete** button.
    - The selected group will be deleted.

    !!! note

        - **Delete** removes the whole group, not just individual selected items.
        - **Update Group** is used only after changing the selected items or settings for an existing group.
        - The item count helps you quickly confirm how many items are included in the selected group.
        - Depending on the section, the group may contain scenarios, regions, parametric items, or property settings.
        - Check the selected group carefully before deleting it.

### 5 - Settings panel

<img src="../images/run_manager_settings_panel.png" class="align-center" width="300" alt="image" />

- **Update Results and Reports**

     This option allows you to update the results and reports for the selected case.
    - This option is not supported with **Local Run** option.

- **Email**

    - This option allows you to send an email notification when the case is solved.

- **Study Name**

    !!! note

        <span class="vo-coming-soon">Coming soon.</span> This page will describe the <strong>Study Name</strong> in Veda Online.

- **Solve Time**

    - This section displays the available solving resources that can be used to run the case.

- **Local Run** [Solving a Locally](https://www.youtube.com/watch?v=VUXD7J4mjqE&list=PLRCe_SRAk7hOvHdyCuLQ15-6JldaH8Ryu&index=11)

    - The **Local Run** option allows the user to execute the case using their local system environment, provided the required setup is available.

- **Study Collaboration with**

    - Study Collaboration is used when a model owner wants to allow other users to view or work on a specific study. When the study is shared, the names of the users who have access to that study are displayed in the “Study collaboration with” section.

### 6 - Manage Saved Cases

Review and manage saved case definitions, then select one or more cases to run.

- **Create New Case**

    - Create a New Case by providing the core information for the case definition

    <img src="../images/case_definition.png" class="align-center" width="400" alt="image" />

    - Case Name - name of the case

    - Description - description of the case

    - Scenario Group - scenarios to be included in this run

    - Region Group - regions to be included in this run

    - Parametric Group - driver scenario for a suite of runs

    - Properties Group - what GAMS options/switch are to be employed

    - Periods Definition - period definition for the run

    - Ending Year - last period for the run

    - Source TIMES - where does the TIMES code reside

    - Solver - which solver is to be used

    - Solver Options - which solver options to use

  - **GDX References** - GDX files to be used for freezing periods, elastic demand base prices or IRE bounds/prices

- **Delete Case**

    - Select the case you want to delete.
    - Click **Delete** button.
    - The case will be deleted.

- **Edit Case**

    - Double click on the case to open a summary window.
    - Modify the required information.
    - Click **Save** button.
    - The case will be edited.

- **Case History**

  <img src="../images/gifs/Case_history.gif" class="align-center" width="600" alt="image" />

  - When you right-click a saved case, a context option named **Case History** is shown.
  - Clicking **Case History** opens a window that shows previous execution records for the selected saved case.
  - **Group history action**: Each case history row includes an action button on the right side. Use this button to open the group history for that specific case execution.
  - **Export to Excel**: Use this option to export the case history details to an Excel file.

- **Model run submission/Solve Case** [Solving a Case](https://www.youtube.com/watch?v=rBIdKZjcTtE&list=PLRCe_SRAk7hOvHdyCuLQ15-6JldaH8Ryu&index=10)

  <img src="../images/cases_grid.png" height="150" alt="image" />

  - Select one (or more) of the cases in the Managed Save Cases section and click **Solve** button.
  - Solve status of model case can be tracked in **JobsDashboard**.

## Modifying RUN files

There are new attributes to write TIMES switches or GAMS code at five different locations in the RUN file. Further, these declarations can also be made at the top or bottom of scenario DD files (last two attributes in the table below). The attributes are supported by regular INS/DINS tables, in any scenario file or in SysSettings.

| Attribute | Location | Alias |
| --- | --- | --- |
| RFCmd_GAMS  | <GAMSOPTIONS> | RFCmd_G, RFCmd |
| RFCmd_OPTIMIZER  | <OPTIMIZER> | RFCmd_O |
| RFCmd_FLAGS  | <SET FLAGS> | RFCmd_F |
| RFCmd_DD  | <INCLUDE DD FILES> | RFCmd_D |
| RFCmd_GLOBAL  | <GLOBAL Parameters> | RFCmd_Glb |
|  |  |  |
| SFCmd_top  | top of the scen DD file | SFCmd_T, SFCmd |
| SFCmd_bot  | bottom of the scen DD file | SFCmd_B |


There is no need to modify the RUN file template manually.

Commands will be ordered by Value column; only rows with value\>0 will be considered. If multiple scenarios send commands to the RUN file, the blocks will be ordered as per the order of scenarios in the case definition.

!!! note

    This also opens up some new possibilities. For example, you can run parametric scenarios where base prices for elastic demands are picked up from different Reference cases.

These examples are available in the [Advanced Demo](https://github.com/kanors-emr/Model_Demo_Adv_Veda.git) model.

**Example 1**

<table>
<thead>
<tr><th>~TFM_INS</th><th></th><th></th><th></th><th></th></tr>
<tr><th>Attribute</th><th>Other_Indexes</th><th>Value</th><th></th><th>Comment</th></tr>
</thead>
<tbody>
<tr><td>RFCmd_F</td><td>$SET BENCOST YES</td><td>1</td><td></td><td>Written to FLAG section of RUN file</td></tr>
<tr><td>RFCmd_F</td><td>$SET ANNCOST LEV</td><td>2</td><td></td><td></td></tr>
<tr><td>RFCmd_F</td><td>$SET WAVER YES</td><td>3</td><td></td><td></td></tr>
<tr><td>RFCmd_G</td><td>GAMS statement 1</td><td>1</td><td></td><td>Written GAMSOPT section</td></tr>
<tr><td>RFCmd_Glb</td><td>GAMS statement 2</td><td>2</td><td></td><td>Written to Global parameters section</td></tr>
<tr><td>RFCmd_Glb</td><td>GAMS statement 3</td><td>3</td><td></td><td></td></tr>
<tr><td>SFCmd_T</td><td>$OFFEPS</td><td>1</td><td></td><td>Top of the scen DD file</td></tr>
<tr><td>SFCmd_B</td><td>GAMS statement A</td><td>3</td><td></td><td>Bottom of the scen DD file</td></tr>
<tr><td>SFCmd_B</td><td>GAMS statement B</td><td>4</td><td></td><td></td></tr>
</tbody></table>


If you want to use single quotes <'> in your instructions, then it is necessary to use a DINS table, as shown below. DINS tables need process or commodity specification. You can use any valid process instead of IMPNRGZ; it will have no impact on the outcome.

**Example 2**

<table>
<thead>
<tr><th>~TFM_DINS-AT</th><th></th><th></th></tr>
<tr><th>RFCmd_DD </th><th>Other_Indexes</th><th>pset_pn</th></tr>
</thead>
<tbody>
<tr><td>3</td><td>set nr(all_reg);</td><td>IMPNRGZ</td></tr>
<tr><td>4</td><td>nr(all_reg)=yes$(not r(all_reg));</td><td>IMPNRGZ</td></tr>
<tr><td>5</td><td>\*--</td><td>IMPNRGZ</td></tr>
<tr><td>6</td><td>\*Python embedded code to remove invalid TU and TB trade processes</td><td>IMPNRGZ</td></tr>
<tr><td>7</td><td>set cb_p(r,p) all crossborder processes involved</td><td>IMPNRGZ</td></tr>
<tr><td>8</td><td>\*--</td><td>IMPNRGZ</td></tr>
<tr><td>9</td><td>;</td><td>IMPNRGZ</td></tr>
<tr><td>10</td><td>cb_p(r,p)=yes$gr_genmap(r,p,'CrossBorderTrade');</td><td>IMPNRGZ</td></tr>
<tr><td>11</td><td>\*--</td><td>IMPNRGZ</td></tr>
<tr><td>12</td><td>embeddedCode Python:</td><td>IMPNRGZ</td></tr>
<tr><td>13</td><td>ncb_p = []</td><td>IMPNRGZ</td></tr>
<tr><td>14</td><td>for r,p in gams.get('cb_p'):</td><td>IMPNRGZ</td></tr>
<tr><td>15</td><td>\*--</td><td>IMPNRGZ</td></tr>
<tr><td>16</td><td>\*--</td><td>IMPNRGZ</td></tr>
<tr><td>17</td><td>\*--</td><td>IMPNRGZ</td></tr>
<tr><td>18</td><td>gams.set('ncb_p',ncb_p)</td><td>IMPNRGZ</td></tr>
<tr><td>19</td><td>endEmbeddedCode ncb_p</td><td>IMPNRGZ</td></tr>
<tr><td>20</td><td>ACT_BND(R,T,P,S,'UP')$ncb_p(r,p) = EPS;</td><td>IMPNRGZ</td></tr>
</tbody></table>

