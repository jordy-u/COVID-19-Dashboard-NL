//https://codepen.io/onyx1812/pen/GRJxmva
const
	range = document.getElementById('country-map-slider'),
	rangeV = document.getElementById('rangeV'),
	setValue = ()=>{
		if (selectedDataset == null) return;
		//var mapDate = new Date(selectedDataset.startDate);
		var daysLater = parseInt(range.value);
		
		var mapDate = addDaysToDate(selectedDataset.startDate, daysLater);
		
		//Don't update the map if the reports are not downloaded yet (when this webpage is loaded).
		if (selectedDataset.data)
			updateMap(mapDate)
		
		//Convert the selected date to "dd month"
		var dateString = getDayAndMonth(mapDate)
		
		const
			newValue = Number( (range.value - range.min) * 100 / (range.max - range.min) ),
			newPosition = 10 - (newValue * 0.2);
		rangeV.innerHTML = `<span id="current-date">${dateString}</span>`;
		rangeV.style.left = `calc(${newValue}% + (${newPosition}px))`;
	};
document.addEventListener("DOMContentLoaded", setValue);
range.addEventListener('input', setValue);
