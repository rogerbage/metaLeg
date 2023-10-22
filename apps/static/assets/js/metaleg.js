var dXY = [];
var atualPage = '';
var dIndexados = [];
var ultimaBusca = [];
metaLeg = {
  

	initCharts: function(){
    	metaLeg.initBigChart();
    	metaLeg.initTopFiveChart();
    	metaLeg.initFirstFiveChart();
    	metaLeg.initTopYearChart();
  	},
  	initFirstFiveChart: function(){
    var ctx = document.getElementById("firstFiveChart").getContext("2d");

    var gradientStroke = ctx.createLinearGradient(0, 230, 0, 50);

    gradientStroke.addColorStop(1, 'rgba(72,72,176,0.2)');
    gradientStroke.addColorStop(0.2, 'rgba(72,72,176,0.0)');
    gradientStroke.addColorStop(0, 'rgba(119,52,169,0)'); //purple colors

    var data = {
      labels:   [],
      datasets: [{
        label: "Leis",
          fill: true,
          backgroundColor: gradientStroke,
          borderColor: '#d346b1',
          borderWidth: 2,
          borderDash: [],
          borderDashOffset: 0.0,
          pointBackgroundColor: '#d346b1',
          pointBorderColor: 'rgba(255,255,255,0)',
          pointHoverBackgroundColor: '#d346b1',
          pointBorderWidth: 20,
          pointHoverRadius: 4,
          pointHoverBorderWidth: 15,
          pointRadius: 4,
          data:   [],
      }]
    };

    firstFiveChart = new Chart(ctx, {
      type: 'bar',
      data: data,
      options: gradientBarChartConfiguration
    });
  },

  initTopYearChart: function(){
     var ctxGreen = document.getElementById("topYearCanvas").getContext("2d");

    var gradientStroke = ctxGreen.createLinearGradient(0, 230, 0, 50);

    gradientStroke.addColorStop(1, 'rgba(66,134,121,0.15)');
    gradientStroke.addColorStop(0.4, 'rgba(66,134,121,0.0)'); //green colors
    gradientStroke.addColorStop(0, 'rgba(66,134,121,0)'); //green colors

    var data = {
      labels: [],
      datasets: [{
        label: "Leis",
        fill: true,
        backgroundColor: gradientStroke,
        borderColor: '#00d6b4',
        borderWidth: 2,
        borderDash: [],
        borderDashOffset: 0.0,
        pointBackgroundColor: '#00d6b4',
        pointBorderColor: 'rgba(255,255,255,0)',
        pointHoverBackgroundColor: '#00d6b4',
        pointBorderWidth: 20,
        pointHoverRadius: 4,
        pointHoverBorderWidth: 15,
        pointRadius: 4,
        data: [],
      }]
    };

    topYearChart = new Chart(ctxGreen, {
      type: 'line',
      data: data,
      options: gradientChartOptionsConfigurationWithTooltipGreen

    });
  },
	 initChartsConfiguration: function() {

    gradientChartOptionsConfigurationWithTooltipBlue = {
      maintainAspectRatio: false,
      legend: {
        display: false
      },

      tooltips: {
        backgroundColor: '#f5f5f5',
        titleFontColor: '#333',
        bodyFontColor: '#666',
        bodySpacing: 4,
        xPadding: 12,
        mode: "nearest",
        intersect: 0,
        position: "nearest"
      },
      responsive: true,
      scales: {
        yAxes: [{
          barPercentage: 1.6,
          gridLines: {
            drawBorder: false,
            color: 'rgba(29,140,248,0.0)',
            zeroLineColor: "transparent",
          },
          ticks: {
            suggestedMin: 60,
            suggestedMax: 125,
            padding: 20,
            fontColor: "#2380f7"
          }
        }],

        xAxes: [{
          barPercentage: 1.6,
          gridLines: {
            drawBorder: false,
            color: 'rgba(29,140,248,0.1)',
            zeroLineColor: "transparent",
          },
          ticks: {
            padding: 20,
            fontColor: "#2380f7"
          }
        }]
      }
    };

    

    gradientChartOptionsConfigurationWithTooltipOrange = {
      maintainAspectRatio: false,
      legend: {
        display: false
      },

      tooltips: {
        backgroundColor: '#f5f5f5',
        titleFontColor: '#333',
        bodyFontColor: '#666',
        bodySpacing: 4,
        xPadding: 12,
        mode: "nearest",
        intersect: 0,
        position: "nearest"
      },
      responsive: true,
      scales: {
        yAxes: [{
          barPercentage: 1.6,
          gridLines: {
            drawBorder: false,
            color: 'rgba(29,140,248,0.0)',
            zeroLineColor: "transparent",
          },
          ticks: {
            suggestedMin: 50,
            suggestedMax: 110,
            padding: 20,
            fontColor: "#ff8a76"
          }
        }],

        xAxes: [{
          barPercentage: 1.6,
          gridLines: {
            drawBorder: false,
            color: 'rgba(220,53,69,0.1)',
            zeroLineColor: "transparent",
          },
          ticks: {
            padding: 20,
            fontColor: "#ff8a76"
          }
        }]
      }
    };

    gradientChartOptionsConfigurationWithTooltipGreen = {
      maintainAspectRatio: false,
      legend: {
        display: false
      },

      tooltips: {
        backgroundColor: '#f5f5f5',
        titleFontColor: '#333',
        bodyFontColor: '#666',
        bodySpacing: 4,
        xPadding: 12,
        mode: "nearest",
        intersect: 0,
        position: "nearest"
      },
      responsive: true,
      scales: {
        yAxes: [{
          barPercentage: 1.6,
          gridLines: {
            drawBorder: false,
            color: 'rgba(29,140,248,0.0)',
            zeroLineColor: "transparent",
          },
          ticks: {
            suggestedMin: 0,
            padding: 20,
            fontColor: "#9e9e9e",
            precision: 0,
            callback: function (value) { if (Number.isInteger(value)) { return value; } },
          }
        }],

        xAxes: [{
          barPercentage: 1.6,
          gridLines: {
            drawBorder: false,
            color: 'rgba(0,242,195,0.1)',
            zeroLineColor: "transparent",
          },
          ticks: {
            padding: 20,
            fontColor: "#9e9e9e"
          }
        }]
      }
    };


    gradientBarChartConfiguration = {
      maintainAspectRatio: false,
      legend: {
        display: false
      },

      tooltips: {
        backgroundColor: '#f5f5f5',
        titleFontColor: '#333',
        bodyFontColor: '#666',
        bodySpacing: 4,
        xPadding: 12,
        mode: "nearest",
        intersect: 0,
        position: "nearest"
      },
      responsive: true,
      scales: {
        yAxes: [{

          gridLines: {
            drawBorder: false,
            color: 'rgba(29,140,248,0.1)',
            zeroLineColor: "transparent",
          },
          ticks: {
            suggestedMin: 0,
            beginAtZero: true,
            padding: 20,
            fontColor: "#9e9e9e",
            precision: 0,
            callback: function (value) { if (Number.isInteger(value)) { return value; } },
          }
        }],

        xAxes: [{

          gridLines: {
            drawBorder: false,
            color: 'rgba(29,140,248,0.1)',
            zeroLineColor: "transparent",
          },
          ticks: {
            padding: 20,
            fontColor: "#9e9e9e"
          }
        }]
      }
    };
 

  },
	initTopFiveChart: function (){
    	var ctx = document.getElementById("Top5Chart").getContext("2d");
    	var gradientStroke = ctx.createLinearGradient(0, 230, 0, 50);
	    gradientStroke.addColorStop(1, 'rgba(29,140,248,0.2)');
    	gradientStroke.addColorStop(0.4, 'rgba(29,140,248,0.0)');
    	gradientStroke.addColorStop(0, 'rgba(29,140,248,0)'); //blue colors
    	topFiveChart = new Chart(ctx, {
      		type: 'bar',
      		responsive: true,
      		legend: {
        		display: false
      		},
      		data: {
        		labels: [],
        		datasets: [{
          			label: "Leis",
          			fill: true,
          			backgroundColor: gradientStroke,
          			hoverBackgroundColor: gradientStroke,
          			borderColor: '#1f8ef1',
          			borderWidth: 2,
          			borderDash: [],
          			borderDashOffset: 0.0,
          			data: [],
        		}]
      		},
      		options: gradientBarChartConfiguration
    	});
  	},
	setTopFiveChart: function(dXY){
	    var dTopFiveX = [];
	    var dTopFiveY = [];
	    var dSort = [];
	    var data = topFiveChart.config.data;
	    for (var ano in dXY) {
	      dSort.push([ano, dXY[ano]]);
	    }
	    dSort.sort(function(a, b) {
	      return a[1] - b[1];
	    });
	    dTopFiveXY = dSort.slice(-5);
	    dTopFiveXY.forEach((el, eli) => {
	      dTopFiveX.push(dTopFiveXY[eli][0]);
	      dTopFiveY.push(dTopFiveXY[eli][1]);
	    });
	    
	    data.datasets[0].data = dTopFiveY;
	    data.labels = dTopFiveX;
	    topFiveChart.update();
  	},
  	  setTopYearChart: function(dXY){

    var dEixoX = Object.keys(dXY);
    var dEixoY = Object.values(dXY);
    var dTopYearCount = Math.max(...dEixoY);
    var dTopYearIndex = dEixoY.indexOf(dTopYearCount);
    var dTopYear = dEixoX[dTopYearIndex]
    var dTopYearRangeX = dEixoX.slice((dTopYearIndex -3), (dTopYearIndex + 4));
    var dTopYearRangeY = dEixoY.slice((dTopYearIndex -3), (dTopYearIndex + 4));
    var data = topYearChart.config.data;
    data.datasets[0].data = dTopYearRangeY;
    data.labels = dTopYearRangeX;
    topYearChart.update();
  },

  setFirstFiveChart: function (dXY){
    var dFirstFive = [];
    var dFirstFiveX = [];
    var dFirstFiveY = [];
    var resultNotZero = Object.entries(dXY).filter(count => count[1] > 0);
    dFirstFive = resultNotZero.slice(0, 5);
    dFirstFive.forEach( (el, eli) => {
      dFirstFiveX.push(dFirstFive[eli][0]);
      dFirstFiveY.push(dFirstFive[eli][1]);
    });
     var data = firstFiveChart.config.data;
    data.datasets[0].data = dFirstFiveY;
    data.labels = dFirstFiveX;
    firstFiveChart.update();
  },

  	initBigChart: function(){
    gradientChartOptionsConfigurationWithTooltipPurple = {
      maintainAspectRatio: false,
      legend: {
        display: false
      },

      tooltips: {
        backgroundColor: '#f5f5f5',
        titleFontColor: '#333',
        bodyFontColor: '#666',
        bodySpacing: 4,
        xPadding: 12,
        mode: "nearest",
        intersect: 0,
        position: "nearest"
      },
      responsive: true,
      scales: {
        yAxes: [{
          barPercentage: 1.6,
          gridLines: {
            drawBorder: false,
            color: 'rgba(29,140,248,0.0)',
            zeroLineColor: "transparent",
          },
          ticks: {
            suggestedMin: 0,
            beginAtZero: true,
            padding: 20,
            fontColor: "#9a9a9a",
            precision: 0,
            callback: function (value) { if (Number.isInteger(value)) { return value; } },
          }
        }],

        xAxes: [{
          barPercentage: 1.6,
          gridLines: {
            drawBorder: false,
            color: 'rgba(225,78,202,0.1)',
            zeroLineColor: "transparent",
          },
          ticks: {
            padding: 20,
            fontColor: "#9a9a9a"
          }
        }]
      }
    };
    document.getElementById("1851_2023").classList.add("focus");
    document.getElementById("1851_2023").classList.add("active");
    document.getElementById("1851_1988").classList.remove("focus");
    document.getElementById("1851_1988").classList.remove("active");
    document.getElementById("1989_2023").classList.remove("focus");
    document.getElementById("1989_2023").classList.remove("active");
    var chart_labels = [];
    var chart_data = [];
    //decretosEixoX = chart_labels;
    //decretosEixoY = chart_data;


    var ctx = document.getElementById("chartBig1").getContext('2d');

    var gradientStroke = ctx.createLinearGradient(0, 230, 0, 50);

    gradientStroke.addColorStop(1, 'rgba(72,72,176,0.1)');
    gradientStroke.addColorStop(0.4, 'rgba(72,72,176,0.0)');
    gradientStroke.addColorStop(0, 'rgba(119,52,169,0)'); //purple colors
    var config = {
      type: 'line',
      data: {
        labels: chart_labels,
        datasets: [{
          label: "Leis",
          fill: true,
          backgroundColor: gradientStroke,
          borderColor: '#d346b1',
          borderWidth: 2,
          borderDash: [],
          borderDashOffset: 0.0,
          pointBackgroundColor: '#d346b1',
          pointBorderColor: 'rgba(255,255,255,0)',
          pointHoverBackgroundColor: '#d346b1',
          pointBorderWidth: 20,
          pointHoverRadius: 4,
          pointHoverBorderWidth: 15,
          pointRadius: 4,
          data: chart_data,
        }]
      },
      options: gradientChartOptionsConfigurationWithTooltipPurple
    };
    bigChart = new Chart(ctx, config);

  },
	setBigChart: function(nXY, minDate, maxDate){
	    var data = bigChart.config.data;
	    var dEixoX = [];
	    var dEixoY = [];
	    for (i=minDate; i<=maxDate; i++){
	      dEixoX.push(i);
	      if (nXY[i]){
	        dEixoY.push(nXY[i]);  
	      }
	      else{
	        dEixoY.push(0);
	      }
	    }
	    data.datasets[0].data = dEixoY;
	    data.labels = dEixoX;
	    bigChart.update(); 
	},
	setCharts: function (su){
    search_input.value = su.search;
    ultimaBusca = su.search;

    dXY = su.contador;
    metaLeg.setBigChart(dXY, 1851, 2023);
    metaLeg.setTopFiveChart(dXY);
    metaLeg.setFirstFiveChart(dXY);
    metaLeg.setTopYearChart(dXY);
    metaLeg.showLawsList(su.laws, su.type);
    search_loading.style.display = "none";
    document.getElementById("1851_2023").classList.add("focus");
    document.getElementById("1851_2023").classList.add("active");
    document.getElementById("1851_1988").classList.remove("focus");
    document.getElementById("1851_1988").classList.remove("active");
    document.getElementById("1989_2023").classList.remove("focus");
    document.getElementById("1989_2023").classList.remove("active");
    document.getElementById("inputTopFiveTerm").innerText = su.search;
    document.getElementById("inputFirstFiveTerm").innerText = su.search;
    document.getElementById("inputTopYearTerm").innerText = su.search;
    document.getElementById('d_total_search').innerText = su.search;

  },
	searchTerm: function(search, type, semantic){
    console.log("SearchTemr");
    document.getElementById('search_loading').style.display = "inline-block";
    var action = '/api';
    var data = {
      type: type,
      semantic: semantic,
      search: search
    };
    $.ajax({
      url: action,
      data: data,
      type: "get",
      dataType: "json",
      beforeSend: function (load) {
        
      }
    })
    .done(function (su) {
      console.log("done: ", su);
      if (su.contador){
        metaLeg.setCharts(su);  
      }
      else{
        console.log("Error Getting Data:");
        console.log(su);
      }
      
    } )
    .fail (function (erro){
      console.log(erro.responseText);
    }

    );
  },
  exportLeg: function(event, id, type){
    event.preventDefault();
    var action = '/getLeg';
    var data = {
      id: id,
      type: type
    };
    var ementaFinal = "";
    var leftBrasao = 50;
    var topBrasao = 50;
    var widthBrasao = 128;
    var heightBrasao = 72;
    var ementaSplits;
    var pdfMarginLeft = 50;
    var pdfMarginRight = 50;
    $.ajax({
      url: action,
      data: data,
      type: "get",
      dataType: "json",
      beforeSend: function (load) {
      }
    })
    .done(function (su) {
      if (su.result){
        var fileName = su.result['lei'].slice(0, 25).replace(/[^A-Z0-9]+/ig, "_");
        fileName = 'D_' + fileName + '.pdf';
        const { jsPDF } = window.jspdf;
        var doc = new jsPDF("p", "pt", "a4");
        var pdfWidth = doc.internal.pageSize.getWidth();
        var pdfHeight = doc.internal.pageSize.getHeight();
        leftBrasao = (pdfWidth - widthBrasao)/2;
        doc.addImage("/static/assets/img/brasao.png", "PNG", leftBrasao, topBrasao, widthBrasao, heightBrasao);
        doc.setFontSize(12);
        doc.text(su.result['lei'], doc.internal.pageSize.getWidth() / 2, 150, { align: "center"});
        ementaSplits = ferramentas.splitString(70, su.result['ementa']);
        var y = 200;
        for (var i = 0; i < ementaSplits.length; i++) {                
          doc.text(ementaSplits[i], pdfWidth-pdfMarginRight, y, { align: "right"});
          y = y + 13;
        }
        var inteiroTeor = su.result['inteiroTeor'].trim();
        var splitTitle = inteiroTeor.split(/\r\n|\r|\n/g);
        var newInteiroTeor = [];
        for (var i = 0; i < splitTitle.length; i++) {
          var newSplit = ferramentas.splitString(80, splitTitle[i]);
          for (var a = 0; a < newSplit.length; a++) {
              newInteiroTeor.push(newSplit[a]);
          }
        }
        
        splitTitle = newInteiroTeor;
        doc.setFontSize("11");
        y = y + 30;
        for (var i = 0; i < splitTitle.length; i++) {                
          if (y > 790) {
            y = 50;
            doc.addPage();
          }
          doc.text(splitTitle[i], 50, y);
          y = y + 13;
        }
        doc.save(fileName);
      }
    })
    .fail (function (erro){
      console.log(erro.responseText);
    });
  },
  openModal: function(event, id, type){
    event.preventDefault();
    var action = '/getLeg';
    var data = {
      id: id,
      type: type,
    };
    $.ajax({
      url: action,
      data: data,
      type: "get",
      dataType: "json",
      beforeSend: function (load) {
      }
    })
    .done(function (su) {
      if (su.result){
        modalBody.innerText = "Por favor aguarde";
          modalTitle.innerText = "Carregando";
          modalEmenta.innerText = "";
        $("#modal").modal();
        
        $('#modal').on('shown.bs.modal', function () {
          modalBody.innerText = su.result['inteiroTeor'];
          modalTitle.innerText = su.result['lei'];
          modalEmenta.innerText = su.result['ementa'];
          modalFooter.innerHTML = `
          	<button type="button" class="btn btn-secondary" data-dismiss="modal">Fechar</button>
            <button type="button" onclick="metaLeg.exportLeg(event, ${su.result['id']}, '${su.type}')" class="btn btn-primary">Baixar PDF</button>`;
          //decretoSelecionadoId = su.result['id'];
          document.getElementById('modalTitle').scrollIntoView();
        })
        

      }
    })
    .fail (function (erro){
      console.log(erro.responseText);
    });
  },

  showOneMetaLeg: function(event, id, type){
    event.preventDefault();
    console.log(event, id, type);
    var action = '/getLeg';
    var data = {
      id: id,
      type: type,
    };
    $.ajax({
      url: action,
      data: data,
      type: "get",
      dataType: "json",
      beforeSend: function (load) {
      }
    })
    .done(function (su) {
      if (su.result){
      var lei = su.result;  
      console.log(lei.id);
      console.log(lei.ano);
      console.log(lei.ementa);
      var freqs = ferramentas.wordFreq(lei.inteiroTeor);
      console.log(freqs);
      let sortable = [];
      for (var word in freqs) {
        if (word.length >= 4){
          sortable.push([word, freqs[word]]);  
        }
        
      }

      sortable.sort(function(a, b) {
        return a[1] - b[1];
      });
      console.log("Palavra mais citada (com mais de 3 letras): ", sortable[sortable.length - 1]);
      console.log("Total de palavras: ", lei.inteiroTeor.split(" ").length);
      console.log("Total de caracteres(incluindo espaços)", lei.inteiroTeor.length);
      
      }
    })
    .fail (function (erro){
      console.log(erro.responseText);
    });
  },

    addLawList: function(value, position, type){
    var trId = ferramentas.getStringId(value['lei']);
        
    var tr = document.createElement('tr');
    tr.id = 'd_' + value['id'];
    var html = `
        <td>
          <a href="#" onclick="metaLeg.openModal(event, ${value['id']}, '${type}')" class="title">${value['lei']}</a>
          <p class="text-muted">${value['ementa']}</p>
        </td>
        <td class="td-actions text-right">
          <button type="button" onclick="metaLeg.exportLeg(event, ${value['id']}, '${type}')" rel="tooltip" title="" class="btn btn-link" data-original-title="Edit Task">
            <i class="tim-icons icon-cloud-download-93"></i>
          </button>
          <button type="button" onclick="metaLeg.showOneMetaLeg(event, ${value['id']}, '${type}')" rel="tooltip" title="" class="btn btn-link" data-original-title="Edit Task">
            <i class="fa-solid fa-table-list"></i>
          </button>
        </td>
    `;
    tr.innerHTML = html;
    if (position == 'begin'){
      tbody_laws_list.insertBefore(tr, tbody_laws_list.firstChild);
    }
    else{
      tbody_laws_list.append(tr);
    }
    
  },
  removeFromList: function(id){
    const div = document.getElementById(id);
    if (div){
      div.remove();
    }
  },
  showLawsList: function(laws, type){
    var i = 0;
    tbody_laws_list.innerHTML = "";
    dIndexados = [];
    d_total.innerText = Object.keys(laws).length;
    for (const [key, value] of Object.entries(laws)) {
      dIndexados[i] = laws[key];
      i++;
    }
    dListBegin = 0;
    for (i=0; i<=199; i++){
      if (i in dIndexados){
        metaLeg.addLawList(dIndexados[i], 'end', type);
        dListEnd = i;
      }
    
    }
    
  },
  listLoadBegin: function(){
    if (dListBegin > 0){
      var firstD = dListBegin;

      for (i=(firstD-1); i>=(firstD-100); i--){
        if (i in dIndexados){
          metaLeg.addLawList(dIndexados[i], 'begin');
          if ((i+200) in dIndexados){
            metaLeg.removeFromList('d_' + dIndexados[i+200].id);
            dListEnd = (i+199);  
          }
          dListBegin = i;
        }
      }
    }
    if ( firstD in dIndexados){
      console.log(firstD);
        elemento = document.getElementById('d_' + dIndexados[firstD].id);  
        elemento.scrollIntoView();  
    }

  },
  listLoadEnd: function(){
    var lastD = dListEnd;
        
    if (dListEnd >= 199){    
      for (i=(lastD+1); i<=(lastD+100); i++){
        if (i in dIndexados){
          metaLeg.addLawList(dIndexados[i], 'end');
          dListEnd = i;
          if ((i-200) in dIndexados){
            metaLeg.removeFromList('d_' + dIndexados[dListEnd-200].id);
            dListBegin = (dListEnd-199);  
          }
        }
        
      }
    }
    if (( (lastD-3) in dIndexados) && ((lastD+1) in dIndexados)){
        elemento = document.getElementById('d_' + dIndexados[lastD-3].id);  
        elemento.scrollIntoView();  
    }
    
    
  },
}