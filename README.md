# Challenge Post-Mortem


[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)
# Requirements
1. Need one endpoint called loanapp/ to take application. Should be able to consume this json.
Completed.
2. Need one endpoint called status/ to provide a status on an application submitted given a loanapp id. Be creative about the status to return.
Completed. Unsure about the "creative" portion as the data is not manipulated. The application would technically always be pending, unless some criteria for acceptance or rejection were supplied.
3. Develop some kind of algorithm to recognize duplicates in app submissions. A person could submit now on the phone and later on a desktop. A person could submit a new app 4 months down the road with almost the same information but a new mobile number. When a duplicate is found, the key thing to do is to update the original record and not to overwrite. And allow some ways to make note of this. It also removes duplicates in owners, searching for unique names and birthdate.
Django's Object.create_or_update function works well for this. I didn't analyze the run time of the function, but it seems to serve its purpose. There is an updated field on the application that shows when it was last updated. I'm sure there could be a more robust way to track changes.
4. Be mindful that each business can have one or multiple business owners.
Save data in models.
Completed.

### Observing DB Changes Through Admin Page
There are no retrieve and destroy endpoints, so the Django Admin page will suffice in observing DB changes.
https://stark-refuge-31370.herokuapp.com/admin/
User : admin
Password : password

### Create Loan Application
  POST https://stark-refuge-31370.herokuapp.com/loanapp/  
  ```
{
  "RequestHeader": {
    "CFRequestId": "500653901",
    "RequestDate": "2019-06-26T23:05:41.2898238Z",
    "CFApiUserId": null,
    "CFApiPassword": null,
    "IsTestLead": true
  },
  "Business": {
    "Name": "Wow Inc",
    "SelfReportedCashFlow": {
      "AnnualRevenue": 49999999.0,
      "MonthlyAverageBankBalance": 94941.0,
      "MonthlyAverageCreditCardVolume": 18191.0
    },
    "Address": {
      "Address1": "1234 Red Ln",
      "Address2": "5678 Blue Rd",
      "City": "Santa Monica",
      "State": "CA",
      "Zip": "45321"
    },
    "TaxID": "839674398",
    "Phone": "6573248876",
    "NAICS": "79232",
    "HasBeenProfitable": true,
    "HasBankruptedInLast7Years": false,
    "InceptionDate": "2008-06-28T23:04:03.5507585+00:00"
  },
  "Owners": [
    {
      "Name": "WH KennyTest",
      "FirstName": "WH",
      "LastName": "KennyTest",
      "Email": "whkennytest@caminofinancial.com",
      "HomeAddress": {
        "Address1": "5567 North Ridge Ct",
        "Address2": null,
        "City": "Berkeley",
        "State": "CA",
        "Zip": "94704"
      },
      "DateOfBirth": "1955-12-18T00:00:00",
      "HomePhone": "3451289776",
      "SSN": "435790261",
      "PercentageOfOwnership": 50.0
    },
    {
      "Name": "Test DoeTest",
      "FirstName": "Test",
      "LastName": "DoeTest",
      "Email": "Doetest@caminofinancial.com",
      "HomeAddress": {
        "Address1": "4512 East Ridge Ct",
        "Address2": null,
        "City": "Berkeley",
        "State": "CA",
        "Zip": "94704"
      },
      "DateOfBirth": "1955-12-18T00:00:00",
      "HomePhone": "3107654321",
      "SSN": "435790261",
      "PercentageOfOwnership": 50.0
    }
  ],
  "CFApplicationData": {
    "RequestedLoanAmount": "49999999",
    "StatedCreditHistory": 1,
    "LegalEntityType": "LLC",
    "FilterID": "897079"
  }
}
  ```
  returns
  ```
  {
    "Updated": <BOOLEAN>,
    "AppID": <AppID>
}
  ```

### Get status of application
  GET https://stark-refuge-31370.herokuapp.com/status/?id={AppID}
  returns
  ```
      {"Status":"Pending"}
  ```
