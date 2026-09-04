# DINS - Direct Insert tables

!!! note

    DINS tables are designed for adding large chunks of data, when it is fully enumerated.

<table>
<thead>
<tr><th>XX RFInput</th><th></th><th></th></tr>
<tr><th>S.No</th><th>Attribute</th><th>Text</th></tr>
</thead>
<tbody>
<tr><td>1</td><td>RFSwitch</td><td>\*GG\* Set LevelizedCost/OBJ Method/Cost_NPV switches</td></tr>
<tr><td>2</td><td>RFSwitch</td><td>$SET ANNCOST LEV</td></tr>
<tr><td>3</td><td>RFSwitch</td><td>$SET OBJ AUTO</td></tr>
<tr><td>4</td><td>RFSwitch</td><td>$SET OBLONG YES</td></tr>
<tr><td>5</td><td>RFSwitch</td><td>$SET MID_YEAR YES</td></tr>
<tr><td>6</td><td>RFSwitch</td><td>$SET RPT_OPT NCAP.1 -1</td></tr>
<tr><td>7</td><td>RFCmd</td><td>\*GG\* Invest $/HR split &amp; UC/PRC_MARK marginals to VBE</td></tr>
<tr><td>8</td><td>RFCmd</td><td>RPT_OPT('OBJ','1') = 1;</td></tr>
<tr><td>9</td><td>RFCmd</td><td>RPT_OPT('COMPRD','4') = 1; </td></tr>
</tbody></table>


<table>
<thead>
<tr><th>~TFM_DINS-AT</th><th></th><th></th><th></th></tr>
<tr><th>Pset_PN</th><th>RFCmd_FLAGS</th><th>RFCmd_GAMS</th><th>Other_Indexes</th></tr>
</thead>
<tbody>
<tr><td>IMPNRGZ</td><td>1</td><td></td><td>\*GG\* Set LevelizedCost/OBJ Method/Cost_NPV switches</td></tr>
<tr><td>IMPNRGZ</td><td>2</td><td></td><td>$SET ANNCOST LEV</td></tr>
<tr><td>IMPNRGZ</td><td>3</td><td></td><td>$SET OBJ AUTO</td></tr>
<tr><td>IMPNRGZ</td><td>4</td><td></td><td>$SET OBLONG YES</td></tr>
<tr><td>IMPNRGZ</td><td>5</td><td></td><td>$SET MID_YEAR YES</td></tr>
<tr><td>IMPNRGZ</td><td>6</td><td></td><td>$SET RPT_OPT NCAP.1 -1</td></tr>
<tr><td>IMPNRGZ</td><td></td><td>7</td><td>\*GG\* Invest $/HR split &amp; UC/PRC_MARK marginals to VBE</td></tr>
<tr><td>IMPNRGZ</td><td></td><td>8</td><td>RPT_OPT('OBJ','1') = 1;</td></tr>
<tr><td>IMPNRGZ</td><td></td><td>9</td><td>RPT_OPT('COMPRD','4') = 1; </td></tr>
</tbody></table>

