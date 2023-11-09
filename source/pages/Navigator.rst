#########
Navigator
#########

Demo:

* The Navigator provides a comprehensive view of all the templates in the various folders managed by Veda for the current model.
* The Navigator is the main vehicle for accessing, importing, and coordinating the various templates that make up a model.
* Its main screen is divided into sub-windows according to the various types of templates managed by Veda.

.. image:: images/navigator.png
   :width: 600


Quadrants
=========

Template containing comprehensive information about the model’s basic structure (regions, sub-regions, time-periods, time-slices, …)
**SysSetting**

Calibration templates for Base Year
**Base scenario** [BS] – current technology mix
**BaseTrans** – operations on the BS templates

Repository for the depiction of future technologies
**SubRES** [SR]

Three groups of flexible, “rule-based”, scenarios files:
**Regular Scenarios** [RS] - files for data addition and updates
**Demand Scenarios** [DS] - projection module tied to economic indicators, fine-tuned with analyst insight
**Parametric Scenarios** [PS] - functionality designed to handle easily multiple runs and parametric analysis


Two new components are presented:

* Parametric scenarios – “programmed” multi-value suite of scenarios
* No Seed Values – the files that do not provide seed values to any other scenario. These are processed in parallel.

Functionality
=============

* Start from Scratch
* Pull
* Commits
* Email CHeckbox
* Synchronize

* Options Menu
   * NoSeedValue Scenario 
   * Tag Details

* Provides feedback as to the status of the various files and the integrated database managed by Veda according to colour legend at the bottom of form
    * Not imported – not yet read into the database
    * Imported – selected for importing with next SYNC
    * Consistent – templates that are in sync with the database
    * InConsistent – file has been modified after the last SYNC operation
    * ToRemove – missing template imported previously now flagged for removal from the database
    * FileMissing – previously imported template that no longer exists in the template folder
    * Error – if a file has thrown an error

.. image:: images/nav_files_status_legend.png
   :width: 600

* The SYNCHRONIZE button will process all templates in the application folder marked as ToImport (orange)

SYNC Operation
===============

Synchronize imports all selected Excel workbooks into the Veda database

An e-mail is sent to the associated user to notify that the sync has started and another e-mail is sent upon completion. Whether successful or not, sync log details are also sent in the completion e-mail.

After synchronizing a model you can return to the Navigator.

