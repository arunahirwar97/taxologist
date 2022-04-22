//
// Charts
//

'use strict';

//
// Sales chart
//

var SalesChart = (function() {

	// Variables

	var $chart = $('#chart-sales')	;

	// Methods

	function init($this) {
		var salesChart = new Chart($this, {
			type: 'line',
			options: {
				scales: {
					yAxes: [{
						gridLines: {
							color: Charts.colors.gray[200],
							zeroLineColor: Charts.colors.gray[200]
						},
						ticks: {

						}
					}]
				}
			},
			data: {
				labels: [],
				datasets: [{
					label: '',
					data: [10, 5, 15,25,85]
				}]
			}
		});

		// Save to jQuery object

		$this.data('chart', salesChart);

	};


	// Events

	if ($chart.length) {
		alert("vjhvbyd");
		init($chart);
	}

})();
