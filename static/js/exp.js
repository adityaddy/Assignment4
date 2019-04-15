var eng = ["play","train","training","study","watch","walk","sit","book","booking","sleep","enjoy","travel","earn","teach","teaching","see","seeing","wait","waiting","bottle","park","stand","beat","beating","crawl","chair","happy","sofa","boy","child"];
var hin = ["खेल","रेलगाड़ी","अध्ययन","पढ़","सिखा","घड़ी","देख","चल","बैठ","पुस्तक","सोना","सो","कमा","बोतल","बाग","लड़का","लड़की","बालक"]
var map = new Map([["खेल", ["खेल","खेलना","खेलता","खेलते","खेलती","खेला","खेले","खेली","खेलेगा","खेलूँगा","खेलेगे","खेलोगे","खेलेगी","खेलूँगी"]], 
            ["रेलगाड़ी" , ["रेलगाड़ी","रेलगाड़ियाँ","रेलगाड़ियों"]],["पढ़",["पढ़","पढ़ना","पढ़ता","पढ़ते","पढ़ती","पढ़ा","पढ़े","पढ़ी","पढ़ेगा","पढूँगा","पढ़ेंगे","पढ़ोगे","पढ़ेगी","पढूँगी","पढ़ोगी"]],["सिखा",["सिखा","सिखाना","सिखाता","सिखाते","सिखाती","सिखाया","सिखाए","सिखाई","सिखाएँगा","सिखाऊँगा","सिखाएँगे","सिखाओगे","सिखाएँगी","सिखाऊँगी"]],["घड़ी",["घड़ी","घड़ियाँ","घड़ियों"]],["देख",["देख","देखना","देखता","देखते","देखती","देखा","देखे","देखी","देखेगा","देखूँगा","देखेंगे","देखोगे","देखेगी","देखूँगी","देखोगी"]],["चल",["चल","चलना","चलता","चलते","चलती","चला","चले","चली","चलेगा","चलूँगा","चलेंगे","चलोगे","चलेगी","चलूँगी","चलोगी"]],["बैठ",["बैठ","बैठना","बैठता","बैठते","बैठती","बैठा","बैठे","बैठी","बैठेगा","बैठूँगा","बैठेंगे","बैठोगे","बैठेगी","बैठूँगी","बैठोगी"]],["पुस्तक",["पुस्तक","पुस्तके","पुस्तकों"]],["अध्ययन",["अध्ययन"]],["सोना",["सोना"]],["सो",["सो","सोना","सोता","सोते","सोती","सोया","सोए","सोई","सोएँगा","सोऊँगा","सोएँगे","सोएँगी","सोसोऊँगी"]],["कमा",["कमा","कमाना","कमाता","कमाते","कमाती","कमाया","कमाएँ","कमाई","कमाएँगा","कमाऊँगा","कमाएँगे","कमाएँगी","कमाऊँगी"]],["बोतल",["बोतल","बोतलों","बोतले"]],["बाग",["बाग","बागों"]],["लड़का",["लड़का","लड़के","लड़को"]],["लड़की",["लड़की","लड़कियाँ","लड़कियों"]],["बालक",["बालक","बालको"]]]); 



var lang;

function getOption(temp){
	// console.log(temp);
	$("#root").empty();
	lang = temp;
	var x = document.getElementById("root");
	var i;
	var strin = "english";
	var n = strin.localeCompare(temp);
	var op = document.createElement("option");
	op.innerHTML = "---select root---"
	op.value = null
	x.appendChild(op); 

	if (n == 0) {
	for(i=0;i<30;i++)
	{
		// console.log("cccc");
		var op = document.createElement("option");
		op.innerHTML = eng[i];
		op.value = eng[i];
		x.appendChild(op); 
	}

	}

	else {
		for(i=0;i<18;i++)
	{
		var op = document.createElement("option");
		op.innerHTML = hin[i];
		op.value = hin[i];
		x.appendChild(op); 
	}

	} 

	$("#t1").show();
	$("#t2").show();
	$("#t3").show();
	$("#t4").show();
	$("#t5").show();

}	

	function getOption1(temp){
		// console.log(temp);
		// console.log(temp);
		$("#t3").empty();
		var x = document.getElementById("t3");

		if (lang == "english"){
			// console.log(eng);

		$.ajax({
		mimeType: 'text/plain; charset=x-user-defined',	
        type: "GET",
        url: "/file",
        dataType: "text",
        success: function(data) {processData(data);}
     	});

		function processData(data) {
			var lines = data.split(/\r\n|\n/);
			// console.log(lines);
			for (var j = 0; j < lines.length; j++) {
				var values = lines[j].split(',');
				// var n = temp.localeCompare(values[1]);
				// console.log(values[0]);

				if(temp == values[1])
				{	
					var op = document.createElement("option");
					op.innerHTML = values[0];
					op.value = values[0];
					x.appendChild(op);

				}

			}

			var op = document.createElement("option");
			op.innerHTML = "NONE";
			op.value = "NONE";
			x.appendChild(op);

	}

	}

	else {
		// console.log(temp); 
	for(var i=0;i<map.get(temp).length;i++)
	{
		var op = document.createElement("option");
		op.innerHTML = map.get(temp)[i];
		op.value = map.get(temp)[i];
		x.appendChild(op); 
	}

	var op = document.createElement("option");
	op.innerHTML = "NONE";
	op.value = "NONE";
	x.appendChild(op);

	}

}
