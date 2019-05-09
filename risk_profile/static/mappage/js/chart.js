$(function() {
    "use strict";
    initC3Chart();    
});


function initC3Chart() {
    setTimeout(function(){   
        $(document).ready(function(){
            var chart = c3.generate({
                bindto: '#chart-pie', // id of chart wrapper
                data: {
                    columns: [
                        // each columns data
                        ['data1', 55],
                        ['data2', 25],
                        ['data3', 20],
                    ],
                    type: 'pie', // default type of chart
                    colors: {
                        data1: 'maroon',
                        data2: 'green',
                        data3: 'red'
                    },
                    names: {
                        // name of each serie
                        'data1': 'National',
                        'data2': 'Provincial',
                        'data3': 'state',
                    }
                },
                
                legend: {
                    show: true, //hide legend
                    position:'right',
                },
                padding: {
                    bottom: 0,
                    top: 0
                },
            });
        });

        $(document).ready(function(){
            var chart = c3.generate({
                bindto: '#chart-bar-rotated',
			    data: {
			        columns: [
					
			            ['Bed capacity	', 200, 10, 90, 240, 130, 220] 
			        ],
                    type: 'bar',
                    
			    },
				axis: {
                    rotated:true,
			        x: {
			            type: 'category',
			            categories: ['National', 'Provincial', 'District', 'Municipality', 'VDC', 'Ward']
			        }
			    },
			});
        });
        $(document).ready(function(){
            var chart = c3.generate({
                bindto: '#chart-bar',
				data: {
					x: 'x',
					type: 'bar',
					columns: [
						['x', '2069', '2070', '2071','2072','2073'],
						['data1', 30, 200, 100, 400, 150, 250],
						['data2', 130, 100, 140, 200, 150, 50],
						['data3', 300, 200, 150, 180, 190, 280],
                        ['data4', 10, 70, 80, 20, 50, 60],
                        ['data5', 70, 90, 110, 130, 150, 160]
					],
					names: {
                        data1: 'Basic',
                        data2: 'Secondary',
                        data3: 'College',
                        data4: 'technical Institute',
                        data5: 'Universities',
                    },
                    colors: {
                        data1: 'blue',
                        data2: 'red',
                        data3: 'green',
                        data4: 'maroon',
                        data5: 'pink',
                    }
                
				},
				bar: {
					width: {
						ratio: 0.5 // this makes bar width 50% of length between ticks
					},
					axis: {
                        x: {
                            type: 'timeseries',
                            tick: {
                                // format: '%Y-%m-%d'
                            }
                        }
					}
				
				},
			});
        });

        $(document).ready(function(){
            var chart = c3.generate({
                bindto: '#acadamic-spiline', // id of chart wrapper
                data: {
                    x: 'x',
					type: 'bar',
					columns: [
						['x', '2069', '2070', '2071','2072','2073'],
						['data1', 30, 200, 100, 400, 150, 250],
						['data2', 130, 100, 140, 200, 150, 50],
						['data3', 300, 200, 150, 180, 190, 280],
                        ['data4', 10, 70, 80, 20, 50, 60],
                        ['data5', 100, 150, 110, 130, 150, 160]
					],
                    
			        types: {
						data5 : 'spline',
			        },
                    colors: {
                        data1: 'maroon',
                        data2: 'pink',
                        data3: 'red',
                        data4: 'orange',
                        data5: 'green',
                    },
                    names: {
                        // name of each serie
                        'data1': 'Basic',
                        'data2': 'Secondary',
                        'data3': 'College',
                        'data4': 'Technical Instition',
                        'data5': 'Universities',
                    }
                },
                
                legend: {
                    show: true, //hide legend
                },
                padding: {
                    bottom: 0,
                    top: 0
                },
            });
        });
        $(document).ready(function(){
            var chart = c3.generate({
                bindto: '#chart-area-spline-sracked', // id of chart wrapper
                data: {
                    columns: [
                        // each columns data
                        ['data1', 21, 8, 32, 18, 19, 17, 23, 12, 25, 37],
                        ['data2', 7, 11, 5, 7, 9, 16, 15, 23, 14, 55],
                        ['data3', 13, 7, 9, 15, 9, 31, 8, 27, 42, 18],
                    ],
                    type: 'area-spline', // default type of chart
                    groups: [
                        [ 'data1', 'data2', 'data3']
                    ],
                    colors: {
                        'data1': "gray",
                        'data2': "teal",
                        'data3': "lime",
                    },
                    names: {
                        // name of each serie
                        'data1': 'male',
                        'data2': 'Female',
                        'data3': 'Total',
                    }
                },
                axis: {
                    x: {
                        type: 'category',
                        // name of each category
                        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'July', 'Aug', 'Sept', 'Oct']
                    },
                },
                legend: {
                    show: true, //hide legend
                },
                padding: {
                    bottom: 0,
                    top: 0
                },
            });
        }); 
        $(document).ready(function(){
            var chart = c3.generate({
                bindto: '#lineGraph',
                padding: {
                    top: 10,
                    left: 30,
                },		
                data: {
                    columns: [
                        ['data1', 14, 28, 31, 49, 57, 59, 52, 48, 55, 58, 62, 60, 62, 58, 55, 61, 70, 80, 77, 78, 82, 98, 99, 121, 136, 115, 112, 120, 103, 117, 121, 126],
                        ['data2', 3, 16, 19, 24, 27, 32, 38, 36, 32, 36, 40, 48, 41, 44, 46, 53, 58, 62, 65, 61, 64, 62, 59, 63, 87, 92, 72, 81, 75, 80, 97, 97],
                    ],
                    names: {
                        data1: 'onGoing',
                        data2: 'Completed'
                    },
                    colors: {
                        data1: '#da1113',
                        data2: '#3c3c3c'
                    },
                }
            });
        }); 
}, 500);
}