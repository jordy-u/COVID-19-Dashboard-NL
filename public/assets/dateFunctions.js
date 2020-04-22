//This file is used for getting the date as a string.
//This hardcoded method is needed because Safari does not know how to work with Date.toLocaleString('default', { month: 'long' });

//Get name of month in Dutch from month number.
function getMonthName(date) {
  var month = new Array();
  month[0] = "januari";
  month[1] = "februari";
  month[2] = "maart";
  month[3] = "april";
  month[4] = "mei";
  month[5] = "juni";
  month[6] = "juli";
  month[7] = "augustus";
  month[8] = "september";
  month[9] = "october";
  month[10] = "november";
  month[11] = "december";

  return month[date.getUTCMonth()];
}

//Returns date as "dd month"
function getDayAndMonth(date) {
	return date.getUTCDate() + " " + getMonthName(date);
}

//https://stackoverflow.com/questions/3224834/get-difference-between-2-dates-in-javascript
const _MS_PER_DAY = 1000 * 60 * 60 * 24;
// a and b are javascript Date objects
function dateDiffInDays(a, b) {
	// Discard the time and time-zone information.
	const utc1 = Date.UTC(a.getFullYear(), a.getMonth(), a.getDate());
	const utc2 = Date.UTC(b.getFullYear(), b.getMonth(), b.getDate());

	return Math.floor((utc2 - utc1) / _MS_PER_DAY);
}

function addDaysToDate(startDate, days) {
	// Discard the time and time-zone information.
	// When a date gets out of bounds, it's corrected automatically. Ex. 34th of Januari = 3rd of Februari.
	const utc1 = startDate.getTime();
	const utc2 = _MS_PER_DAY * days;
	
	return new Date(utc1 + utc2);
}
