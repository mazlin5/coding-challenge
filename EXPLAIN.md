## Thought process and approach
  - Initial steps included configuration and setup of my environment and AWS account. 
  - This was a good starting place as access to the s3 required a configured aws-cli client on my local machine.
  - Something I noticed later was I only needed the access_keys of the s3 bucket and could have saved time setting up     
    IAM user roles. 
  
## Coding approach
  - My outer function, testThis(), set the stage for pulling data from the s3 bucket (yipit-oscars-data) after my env was configured with access_keys.
  - Since the response returned from the s3.get_object function was json string format, I converted this response object into a list for indexing. 
  - Once I could breakout the items in the list, I setup my dictionary by splitting the string items up by the “:” colon delimiter to frame the key-value pair schema.
  - Handling the raw s3 data took up the bulk of my time as I kept trying to bypass the string dictionary conversion using the json library. 
  - Downstream I format my output dictionary with desired columns. 
 
Note: Poor time management resulted in not being able setup string variables for calculations and formatting.
The last step was to generate the csv from the output dictionary and save in working directory. 
