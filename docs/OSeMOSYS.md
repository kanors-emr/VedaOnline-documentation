---
description: How Veda Online supports OSeMOSYS models — data containers, CSV reading methodology, and working with OSeMOSYS in the browser.
---

# OSeMOSYS in Veda

## Not a Black Box — Trust the Process? Allow us to explain.

When extending Veda to support OSeMOSYS, we didn’t build an entirely new system. The core of Veda — its robust and well-defined **data containers** (database tables) — was already in place, designed to store structured modeling information derived from TIMES input files.

Previously, a specific **reading methodology** and a set of processing rules allowed Veda to populate these containers using TIMES data. With the integration of OSeMOSYS, we have now implemented an **additional reading methodology** and made targeted **adjustments to the rules** to interpret OSeMOSYS CSV inputs in a consistent and reliable manner.

Through carefully designed **mappings** (see tables below), the OSeMOSYS data is translated and populated into the same underlying containers used by TIMES models. This reinforces a critical architectural strength of Veda:

> These data containers are **not bound to any one modeling framework** — they are designed to be flexible and extensible.

Once the data is correctly ingested, the full power of Veda becomes available to OSeMOSYS users:

- The input data can be explored instantly in a **rich, intuitive interface**
- Scenarios can be created and managed using the **Run Manager**
- Models can be launched directly from the UI
- Results are displayed with **powerful pivot tools and dynamic visualizations**

We’ve also validated the processing by comparing key model outputs — including **objective values** — and confirmed that results align as expected. Maintaining the **integrity of your model** is, and always will be, a top priority.

This integration means that the **OSeMOSYS community now gains access to a tool that has matured over 25 years**, shaped by the evolving needs of the TIMES modeling community. Every UI element, every workflow enhancement, and every analytical tool in Veda reflects years of feedback, iterations, and real-world usage.

Now, that same depth of capability is available to **OSeMOSYS users** — without compromise.

### OSeMOSYS Parameters list

| name | indices | topology_in_out | process_set_name | commodity_set_name |
| --- | --- | --- | --- | --- |
| YearSplit | [l,y] |  |  |  |
| DiscountRate | [r] |  |  |  |
| DaySplit | [lh,y] |  |  |  |
| Conversionls | [l,ls] |  |  |  |
| Conversionld | [ld,l] |  |  |  |
| Conversionlh | [lh,l] |  |  |  |
| DaysInDayType | [ls,ld,y] |  |  |  |
| TradeRoute | [r,rr,f,y] |  | IRE |  |
| DepreciationMethod | [r] |  |  |  |
| SpecifiedAnnualDemand | [r,f,y] |  |  |  |
| SpecifiedDemandProfile | [r,f,l,y] |  |  |  |
| AccumulatedAnnualDemand | [r,f,y] |  |  | DEM |
| CapacityToActivityUnit | [r,t] |  |  |  |
| CapacityFactor | [r,t,l,y] |  |  |  |
| AvailabilityFactor | [r,t,y] |  |  |  |
| OperationalLife | [r,t] |  |  |  |
| ResidualCapacity | [r,t,y] |  |  |  |
| InputActivityRatio | [r,t,f,m,y] | in |  |  |
| OutputActivityRatio | [r,t,f,m,y] | out |  |  |
| CapitalCost | [r,t,y] |  |  |  |
| VariableCost | [r,t,m,y] |  |  |  |
| FixedCost | [r,t,y] |  |  |  |
| TechnologyToStorage | [r,t,s,m] |  |  |  |
| TechnologyFromStorage | [r,t,s,m] |  |  |  |
| StorageLevelStart | [r,s] |  |  |  |
| StorageMaxChargeRate | [r,s] |  |  |  |
| StorageMaxDischargeRate | [r,s] |  |  |  |
| MinStorageCharge | [r,s,y] |  |  |  |
| OperationalLifeStorage | [r,s] |  |  |  |
| CapitalCostStorage | [r,s,y] |  |  |  |
| ResidualStorageCapacity | [r,s,y] |  |  |  |
| CapacityOfOneTechnologyUnit | [r,t,y] |  |  |  |
| TotalAnnualMaxCapacity | [r,t,y] |  |  |  |
| TotalAnnualMinCapacity | [r,t,y] |  |  |  |
| TotalAnnualMaxCapacityInvestment | [r,t,y] |  |  |  |
| TotalAnnualMinCapacityInvestment | [r,t,y] |  |  |  |
| TotalTechnologyAnnualActivityUpperLimit | [r,t,y] |  |  |  |
| TotalTechnologyAnnualActivityLowerLimit | [r,t,y] |  |  |  |
| TotalTechnologyModelPeriodActivityUpperLimit | [r,t] |  |  |  |
| TotalTechnologyModelPeriodActivityLowerLimit | [r,t] |  |  |  |
| ReserveMarginTagTechnology | [r,t,y] |  |  |  |
| ReserveMarginTagFuel | [r,f,y] |  |  |  |
| ReserveMargin | [r,y] |  |  |  |
| RETagTechnology | [r,t,y] |  |  |  |
| RETagFuel | [r,f,y] |  |  |  |
| REMinProductionTarget | [r,y] |  |  |  |
| EmissionActivityRatio | [r,t,e,m,y] | out |  |  |
| EmissionsPenalty | [r,e,y] |  |  |  |
| AnnualExogenousEmission | [r,e,y] |  |  |  |
| AnnualEmissionLimit | [r,e,y] |  |  |  |
| ModelPeriodExogenousEmission | [r,e] |  |  |  |
| ModelPeriodEmissionLimit | [r,e] |  |  |  |
| DiscountRateStorage | [r,s] |  |  |  |


### OSeMOSYS and TIMES Parameters mapping

| times_parameter | osemosys_parameter |
| --- | --- |
| G_YRFR | YearSplit |
| G_DRATE | DiscountRate |
|  | DaySplit |
|  | Conversionls |
|  | Conversionld |
|  | Conversionlh |
|  | DaysInDayType |
|  | TradeRoute |
|  | DepreciationMethod |
| COM_PROJ | SpecifiedAnnualDemand |
| COM_FR | SpecifiedDemandProfile |
| COM_CUMNET | AccumulatedAnnualDemand |
| PRC_CAPACT | CapacityToActivityUnit |
| NCAP_AF | CapacityFactor |
| NCAP_AFA | AvailabilityFactor |
| NCAP_TLIFE | OperationalLife |
| PRC_RESID | ResidualCapacity |
| VDA_FLOP | InputActivityRatio |
| PRC_ACTFLO | OutputActivityRatio |
| NCAP_COST | CapitalCost |
| ACT_COST | VariableCost |
| NCAP_FOM | FixedCost |
|  | TechnologyToStorage |
|  | TechnologyFromStorage |
|  | StorageLevelStart |
|  | StorageMaxChargeRate |
|  | StorageMaxDischargeRate |
|  | MinStorageCharge |
| NCAP_TLIFE | OperationalLifeStorage |
| NCAP_COST | CapitalCostStorage |
| PRC_RESID | ResidualStorageCapacity |
| NCAP_DISC | CapacityOfOneTechnologyUnit |
| CAP_BND | TotalAnnualMaxCapacity |
| CAP_BND | TotalAnnualMinCapacity |
| NCAP_BND | TotalAnnualMaxCapacityInvestment |
| NCAP_BND | TotalAnnualMinCapacityInvestment |
| ACT_BND | TotalTechnologyAnnualActivityUpperLimit |
| ACT_BND | TotalTechnologyAnnualActivityLowerLimit |
| ACT_CUM | TotalTechnologyModelPeriodActivityUpperLimit |
| ACT_CUM | TotalTechnologyModelPeriodActivityLowerLimit |
| NCAP_PKCNT | ReserveMarginTagTechnology |
| COM_PEAK | ReserveMarginTagFuel |
| COM_PKRSV | ReserveMargin |
| UC_FLO (UCN=RPS) | RETagTechnology |
| UC_FLO (UCN=RPS) | RETagFuel |
| UC_RHS (UCN=RPS) | REMinProductionTarget |
| FLO_EMIS | EmissionActivityRatio |
| COM_TAXNET | EmissionsPenalty |
|  | AnnualExogenousEmission |
| COM_BNDNET | AnnualEmissionLimit |
|  | ModelPeriodExogenousEmission |
| COM_CUMNET | ModelPeriodEmissionLimit |
|  | DiscountRateStorage |


### OSeMOSYS and TIMES Sets mapping

| name | times_set | index |
| --- | --- | --- |
| YEAR | MILESTONYR | y |
| TECHNOLOGY | PRE,IRE,ELE,CHP,DMD | t |
| TIMESLICE | TIME_SLICE | l |
| FUEL | NRG,DEM | f |
| EMISSION | ENV | e |
| MODE_OF_OPERATION |  | m |
| REGION | REGION | r |
| SEASON | SEASON | ls |
| DAYTYPE | WEEKLY | ld |
| DAILYTIMEBRACKET | DAYNITE | lh |
| STORAGE | STG,STS | s |


### OSeMOSYS and TIMES result variables mapping

| name | veda_name | indices |
| --- | --- | --- |
| RateOfDemand |  | [r,l,f,y] |
| Demand |  | [r,l,f,y] |
| RateOfStorageCharge |  | [r,s,ls,ld,lh,y] |
| RateOfStorageDischarge |  | [r,s,ls,ld,lh,y] |
| NetChargeWithinYear |  | [r,s,ls,ld,lh,y] |
| NetChargeWithinDay |  | [r,s,ls,ld,lh,y] |
| StorageLevelYearStart |  | [r,s,y] |
| StorageLevelYearFinish |  | [r,s,y] |
| StorageLevelSeasonStart |  | [r,s,ls,y] |
| StorageLevelDayTypeStart |  | [r,s,ls,ld,y] |
| StorageLevelDayTypeFinish |  | [r,s,ls,ld,y] |
| StorageLowerLimit |  | [r,s,y] |
| StorageUpperLimit |  | [r,s,y] |
| AccumulatedNewStorageCapacity |  | [r,s,y] |
| NewStorageCapacity |  | [r,s,y] |
| CapitalInvestmentStorage |  | [r,s,y] |
| DiscountedCapitalInvestmentStorage |  | [r,s,y] |
| SalvageValueStorage |  | [r,s,y] |
| DiscountedSalvageValueStorage |  | [r,s,y] |
| TotalDiscountedStorageCost |  | [r,s,y] |
| NumberOfNewTechnologyUnits |  | [r,t,y] |
| NewCapacity | VAR_Ncap | [r,t,y] |
| AccumulatedNewCapacity |  | [r,t,y] |
| TotalCapacityAnnual | VAR_Cap | [r,t,y] |
| RateOfActivity |  | [r,l,t,m,y] |
| RateOfTotalActivity |  | [r,t,l,y] |
| TotalTechnologyAnnualActivity | VAR_Act | [r,t,y] |
| TotalAnnualTechnologyActivityByMode |  | [r,t,m,y] |
| TotalTechnologyModelPeriodActivity |  | [r,t] |
| RateOfProductionByTechnologyByMode |  | [r,l,t,m,f,y] |
| RateOfProductionByTechnology |  | [r,l,t,f,y] |
| ProductionByTechnology | VAR_FOut | [r,l,t,f,y] |
| ProductionByTechnologyAnnual |  | [r,t,f,y] |
| RateOfProduction |  | [r,l,f,y] |
| Production |  | [r,l,f,y] |
| RateOfUseByTechnologyByMode |  | [r,l,t,m,f,y] |
| RateOfUseByTechnology |  | [r,l,t,f,y] |
| UseByTechnologyAnnual |  | [r,t,f,y] |
| UseByTechnology | VAR_Fin | [r,l,t,f,y] |
| Use |  | [r,l,f,y] |
| Trade |  | [r,rr,l,f,y] |
| TradeAnnual |  | [r,rr,f,y] |
| ProductionAnnual |  | [r,f,y] |
| UseAnnual |  | [r,f,y] |
| CapitalInvestment | Cost_Inv | [r,t,y] |
| DiscountedCapitalInvestment |  | [r,t,y] |
| SalvageValue |  | [r,t,y] |
| DiscountedSalvageValue |  | [r,t,y] |
| OperatingCost |  | [r,t,y] |
| DiscountedOperatingCost |  | [r,t,y] |
| AnnualVariableOperatingCost | Cost_Act | [r,t,y] |
| AnnualFixedOperatingCost | Cost_Fom | [r,t,y] |
| TotalDiscountedCostByTechnology |  | [r,t,y] |
| TotalDiscountedCost | Reg_ACost | [r,y] |
| ModelPeriodCostByRegion | Reg_obj | [r] |
| TotalCapacityInReserveMargin |  | [r,y] |
| DemandNeedingReserveMargin |  | [r,l,y] |
| TotalREProductionAnnual |  | [r,y] |
| RETotalProductionOfTargetFuelAnnual |  | [r,y] |
| AnnualTechnologyEmissionByMode |  | [r,t,e,m,y] |
| AnnualTechnologyEmission | VAR_FOut | [r,t,e,y] |
| AnnualTechnologyEmissionPenaltyByEmission | Cost_Comx | [r,t,e,y] |
| AnnualTechnologyEmissionsPenalty |  | [r,t,y] |
| DiscountedTechnologyEmissionsPenalty |  | [r,t,y] |
| AnnualEmissions |  | [r,e,y] |
| ModelPeriodEmissions |  | [r,e] |


### Topology is defined using the following parameters

- InputActivityRatio
- OutputActivityRatio
- EmissionActivityRatio

### Type and Set Identification

- Emission commdities - Commodity Set ENV
- Fuel commdities - Commodity Set NRG
- ReserveMarginTagFuel comodities - Type and Set NRG, SubType ELC
- All Technologies Set = PRE
- All Technologies having TradeRoute parameter defined Type and Set IRE
- ReserveMarginTagTechnology Technologies Type and Set ELE
- Commodities of SubType ELC which are defined as "IN" and "OUT" both in toplogy for such non storage processes. Type and Set IRE

### Primary Commodity Group identification

- Commodities of SubType ELC which are deined as "OUT" in toplogy for such process commodity combination. PCG = Commodity
- Commodities of SubType ELC which are deined as "IN" and "OUT" both in toplogy for such non storage processes. Type and Set IRE. PCG = NRG

### You can start with your CSV files and Veda will take care of the rest.

Users are expected to have CSV files as starting point. Each file contains data for one parameter or set only. All the data in OSeMOSYS model(CSV files) are treated as base scenario. With the help of Veda Application you can create multiple scenarios.
