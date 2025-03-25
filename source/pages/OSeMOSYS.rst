##########
OSeMOSYS
##########

How we have processed the OSeMOSYS csv files?
==============================================
At the core of this function is a flexible mapping system powered by below tables which defines how each OSeMOSYS parameters and sets corresponds to one or more TIMES parameters and sets.


OSeMOSYS Sets mapping TIMES Sets mapping
------------------------------------------

.. csv-table::  
   :file: sets.csv
   :header: "name","times_set","index"
   
   

OSeMOSYS and TIMES Parameters mapping
------------------------------------------
.. csv-table::  
   :file: parameter.csv
   :header: "name","times_parameter","indices","topology_in_out","process_set_name","commodity_set_name","category"
     



