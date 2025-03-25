#################
OSeMOSYS in Veda
#################

Not a Black Box — Trust the Process? Allow us to explain.
##########################################################
When extending Veda to support OSeMOSYS, we didn’t build an entirely new system.  
The core of Veda — its robust and well-defined **data containers** (database tables) — was already in place, designed to store structured modeling information derived from TIMES input files.
 
Previously, a specific **reading methodology** and a set of processing rules allowed Veda to populate these containers using TIMES data.  
With the integration of OSeMOSYS, we have now implemented an **additional reading methodology** and made targeted **adjustments to the rules** to interpret OSeMOSYS CSV inputs in a consistent and reliable manner.
 
Through carefully designed **mappings** (see tables below), the OSeMOSYS data is translated and populated into the same underlying containers used by TIMES models.  
This reinforces a critical architectural strength of Veda:
 
    These data containers are **not bound to any one modeling framework** — they are designed to be flexible and extensible.
 
Once the data is correctly ingested, the full power of Veda becomes available to OSeMOSYS users:
 
- The input data can be explored instantly in a **rich, intuitive interface**
- Scenarios can be created and managed using the **Run Manager**
- Models can be launched directly from the UI
- Results are displayed with **powerful pivot tools and dynamic visualizations**
 
We’ve also validated the processing by comparing key model outputs — including **objective values** — and confirmed that results align as expected.  
Maintaining the **integrity of your model** is, and always will be, a top priority.
 
This integration means that the **OSeMOSYS community now gains access to a tool that has matured over 25 years**, shaped by the evolving needs of the TIMES modeling community.  
Every UI element, every workflow enhancement, and every analytical tool in Veda reflects years of feedback, iterations, and real-world usage.
 
Now, that same depth of capability is available to **OSeMOSYS users** — without compromise.
 

OSeMOSYS and TIMES Sets mapping
------------------------------------------
.. csv-table::  
   :file: sets.csv
   :header: "name","times_set","index"
   
   
OSeMOSYS and TIMES Parameters mapping
------------------------------------------
.. csv-table::  
   :file: parameter.csv
   :header: "name","times_parameter","indices","topology_in_out","process_set_name","commodity_set_name","category"


Topology is defined using the following parameters
------------------------------------------------------------------------------------
   * InputActivityRatio
   * OutputActivityRatio
   * EmissionActivityRatio

Type and Set Identification
------------------------------------------
   * Emission commdities - Commodity Set ENV 
   * Fuel commdities - Commodity Set NRG
   * ReserveMarginTagFuel comodities - Type and Set NRG, SubType ELC
   * All Technologies Set = PRE
   * All Technologies having TradeRoute parameter defined Type and Set  IRE 
   * ReserveMarginTagTechnology Technologies Type and Set ELE 
   * Commodities of SubType ELC which are defined as "IN" and "OUT" both in toplogy for such non storage processes. Type and Set IRE

Primary Commodity Group identification
------------------------------------------
   * Commodities of SubType ELC which are deined as "OUT" in toplogy for such process commodity combination. PCG = Commodity 
   * Commodities of SubType ELC which are deined as "IN" and "OUT" both in toplogy for such non storage processes. Type and Set IRE. PCG = NRG 

You can start with your CSV files and Veda will take care of the rest.
----------------------------------------------------------------------
Users are expected to have CSV files as starting point. Each file contains data for one parameter or set only.
All the data in OSeMOSYS model(CSV files) are treated as base scenario. With the help of Veda Application you can create multiple scenarios. 
