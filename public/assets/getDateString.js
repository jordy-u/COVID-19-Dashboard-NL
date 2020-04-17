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

  return month[date.getMonth()];
}

//Returns date as "dd month"
function getDayAndMonth(date) {
	return date.getDate() + " " + getMonthName(date);
}