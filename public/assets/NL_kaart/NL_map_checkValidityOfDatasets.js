//Check if all loaded files are valid
function checkAllDataFiles() {
	
	var datasets = [request_covid19Reports, request_hospitalizationPerCity];
	var resultIsSuccess = true;
	
	//This weird forEach construction is needed, because a normal "for (var element in array)" copies both datasets before editing them.
	datasets.forEach(function(item, index, object) {
		var checkParameters_dataset = checkDataset(item);
		
		if (checkParameters_dataset.success === true) {
			//If dataset is VALID
			item.startDate = checkParameters_dataset.dateEarliest;
			item.endDate = checkParameters_dataset.dateLatest;
		} else {
			//If dataset is INVALID
			$("#errorAlert").html($("#errorAlert").html() + '<div class="alert alert-danger" role="alert"><strong>Error: </strong>Datum is ongeldig: ' + checkParameters_dataset.wrongDate + '</div>');
			resultIsSuccess = false;
		}
	});
	
	return resultIsSuccess;
}

/*This function checks:
* if all dates are correct
* for the earliest date
* for the latest date

Example good dataset response
{
	success : true,
	dateEarliest : //Date object "2020-02-27",
	dateLatest : //Date object "2020-04-21"
}

Example bad dataset response
{
	success : false,
	wrongDate : "02/32"
}
*/
function checkDataset(dataset) {
	//The earliest and latest date are like this un purpose, so they are always overwritten at least once.
	var dateEarliest = new Date("2099-01-01");
	var dateLatest = new Date("2000-01-01");
	
	//Loop through dates to find the earliest and latest date and check for errors.
	for (var dataEntryId in dataset.data) {
		//dataEntryId is a number. dataEntry is the JSON-inner-object assosiated with that ID.
		var dataEntryDate = new Date(dataEntryId + "T00:00:00.000Z");
		
		//If date gives an error, return invalid date.
		if (isNaN(dataEntryDate)) {
			return {
				success : false,
				wrongDate : dataEntryId
			};
		}
		
		//Update earliest and latest date
		if (dataEntryDate < dateEarliest) dateEarliest = dataEntryDate;
		if (dataEntryDate > dateLatest) dateLatest = dataEntryDate;
	}
	
	//On success, return this:
	return {
		success : true,
		dateEarliest : dateEarliest,
		dateLatest : dateLatest
	};
}
