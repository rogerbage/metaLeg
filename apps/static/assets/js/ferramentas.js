ferramentas = {
  wordFreq: function(string) {
    var words = string.replace(/[.]/g, '').split(/\s/);
    var freqMap = {};
    words.forEach(function(w) {
        if (!freqMap[w]) {
            freqMap[w] = 0;
        }
        freqMap[w] += 1;
    });
    return freqMap;
  },
  exportDivAsImage: function (chart, name){
    html2canvas(document.getElementById(chart)).then(function (canvas) {                   
    var anchorTag = document.createElement("a");
    document.body.appendChild(anchorTag);
    anchorTag.download = name + ".png";
    anchorTag.href = canvas.toDataURL("image/png");
    anchorTag.target = '_blank';
    anchorTag.click();
    
    // html2canvas(document.getElementById(div)).then(function (canvas) {                   
    //   var anchorTag = document.createElement("a");
    //                 document.body.appendChild(anchorTag);
    //                 //document.getElementById("previewImg").appendChild(canvas);
    //                 anchorTag.download = name + ".jpg";
    //                 anchorTag.href = canvas.toDataURL();
    //                 anchorTag.target = '_blank';
    //                 anchorTag.click();
    });
  },
	splitString: function (n,str){
    let arr = str?.split(' ');
    let result=[]
    let subStr=arr[0]
    for(let i = 1; i < arr.length; i++){
        let word = arr[i]
        if(subStr.length + word.length + 1 <= n){
            subStr = subStr + ' ' + word
        }
        else{
            result.push(subStr);
            subStr = word
        }
    }
    if(subStr.length){result.push(subStr)}
    return result
  },
  chunkSubstr: function(str, size) {
  const numChunks = Math.ceil(str.length / size)
  const chunks = new Array(numChunks)

  for (let i = 0, o = 0; i < numChunks; ++i, o += size) {
    chunks[i] = str.substr(o, size)
  }

  return chunks
  },

  getStringId: function (string){
    return string.slice(0, 25).replace(/[^A-Z0-9]+/ig, "_");
  },

  alerta: function(from, align, message) {
    color = Math.floor((Math.random() * 4) + 1);

    $.notify({
      icon: "tim-icons icon-bell-55",
      message: message

    }, {
      type: type[color],
      timer: 8000,
      placement: {
        from: from,
        align: align
      }
    });
  },
}