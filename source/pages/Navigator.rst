#########
Navigator
#########


* The Navigator provides a comprehensive view of all the templates in the various folders managed by Veda for the current model.
* The Navigator is the main vehicle for accessing, importing, and coordinating the various templates that make up a model.
* Its main screen is divided into sub-windows according to the various types of templates managed by Veda.

.. image:: images/navigator.png
   :align: center


Quadrants
---------

   1. **SysSetting** - Template containing comprehensive information about the model’s basic structure (regions, sub-regions, time-periods, time-slices, …)
   2. **Base scenario** [BS] – current technology mix 
   3. **BaseTrans** – operations on the BS templates 
   4. **SubRES** [SR] - Repository for the depiction of future technologies
   5. **Regular Scenarios** [RS] - files for data addition and updates.
   6. **Demand Scenarios** [DS] - projection module tied to economic indicators, fine-tuned with analyst insight.
   7. **Parametric Scenarios** [PS] - functionality designed to handle easily multiple runs and parametric analysis. “programmed” multi-value suite of scenarios.
   #. **No Seed Values** [NSV] – the files that do not provide seed values to any other scenario. These are processed in parallel. Veda provides the information of which files can be converted into NSV scenarios. (Introduced in 2019)

.. note::
   - 1 contains comprehensive info about the model. Veda will not Synchronize without this file.
   - 2 and 3 - Calibration templates for Base Year
   - 5 to 8 - Groups of flexible, “rule-based”, scenarios files:


How to Use it?
---------------
SYNC Operation
^^^^^^^^^^^^^^
Synchronize imports all selected Excel workbooks into the Veda database. The processing can be seen live on the right logging window or on the JobsDashboard page. An e-mail is also sent to the associated user upon on completion. Whether successful or not, sync log details are also sent in the completion e-mail.
After synchronizing a model, you can return to the Navigator.

User Inputs
^^^^^^^^^^^
.. image:: images/navigator_menu.png
   :align: center
#. *Start from Scratch* - This button deletes the previous model data from the database and pulls all the files from the GitHub repository. You have to resynchronize your model. Reports Module data will not be deleted.
#. *Pull* - Here all the files from the git repository will be pulled but all your data in the VedaOnline database will not change.
#. *Commits* - Check your GitHub commits directly on VedaOnline.
#. *Email Checkbox* - After Synchronization is finished, if this checkbox is unchecked then VO will not send you the email. 
#. *Synchronize* - It will process all templates in the application folder marked(Selected files) as ToImport(orange)
#. *Options Menu*
 * NoSeedValue Scenario
 * Tag Details

File Status
^^^^^^^^^^^
.. image:: images/nav_files_status_legend.png
   :align: center
Provides feedback as to the status of the various files and the integrated database managed by Veda according to color legend at the bottom of form
 * *Not imported* – not yet read into the database
 * *Imported* – selected for importing with next SYNC
 * *Consistent* – templates that are in sync with the database
 * *InConsistent* – file has been modified after the last SYNC operation
 * *ToRemove* – missing template imported previously now flagged for removal from the database
 * *FileMissing* – a previously imported template that no longer exists in the template folder
 * *Error* – if a file has thrown an error





