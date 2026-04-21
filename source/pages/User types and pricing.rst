########################
User types and pricing
########################

Veda online supports the following types of users:

* **Guest:** Visitors who are not logged in. They will have access to all open models on VO, with download premissions based on the settings used by model owners. They will not be able to save views under Results and Reports.
* **Trial:** A trial license is allocated by default after signing up on VO. This offers full functionality for 7 days with 5 hours of Solve time.

  * Users are requested to submit only modest runs during the Trial period. Less than 5GB RAM usage and Less than 10 Min of Solve time.

* **Free:** Trial users automatically transition to free users. Free users will have access to open models **and** models shared with them by Developer license holders.

  * Models and results created under trial period will be removed after one month if the user does not buy a license before that.

* **Developer:** Developer license will let you create models, run cases, and view results and reports. Any private and public model can be shared with *any* user who is registered on VO. You can purchase GAMS Engine hours to perform runs in the cloud; they can always be done locally if you have a GAMS license. VO can send up to 4 concurrent runs on the GAMS Engine.
* **Academic:** Developer functionality is offered at discounted prices to Academics (Degree-granting institutions). In addition, this license allows access to the NEOS server. VO can send up to 4 concurrent runs on the NEOS server.

  * **Dormant:** Developer and Academic license holders who do not wish to modify their models or make new runs can become Dormant users - to have continued access to their models and results.
  * Models and results will be removed one month after a subscription expires.

    * It will be possible to resurrect the model and runs if the user resubscribes in future. Model states are preserved in GitHub, and the output files can be saved locally - to be uploaded to VO under a new subscription.

**Annual subscription fee for the Veda online Platform**

*All prices are in US Dollars*

.. csv-table::
        :file: tables/pricing_vo.csv
        :widths: 1,1,1,1,2
        :header-rows: 1

**Solver time**

GAMS Engine is available at $12.37 - $13.11 per hour, depending on the machine size. Users can prepay for any number of hours (>= 40). The default machine size can be set under user profile, and it can be changed at the time of launching a set of runs from the VO Run manager. These hours can be transferred across years but they cannot be
refunded. Note that the GAMS Engine price is subject to change depending upon GAMS policy.

.. csv-table::
        :file: tables/pricing_ge.csv
        :widths: 1,1,1,1,1,2
        :header-rows: 1

Users can also buy GAMS Engine time from GAMS separately and launch runs from VO using their own credentials.
