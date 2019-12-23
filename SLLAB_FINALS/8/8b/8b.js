window.onload=function(){


	var hosp={
		name:"Apollo Hospital",
		location:"BLR"
			 };


	var patient={
		name:"Raj",
		aadhar:123456789187,
		labtests:["X-RAY","BP"]

	};

	var a=document.getElementById("hosp")
	a.innerHTML=hosp.name + " " + hosp.location;


	pat=document.getElementById("pat");
	var tests="";
	patient["labtests"].forEach(function(a){
			tests+=a + " ";
		});

	pat.addEventListener("mouseover",function(e){
		e.target.style.color="red";
		var details=document.getElementById("details");
		details.innerHTML="Name:"+patient.name + "  aadhar no:"+patient.aadhar + "  Lab Tests:"+tests;
	})

		pat.addEventListener("mouseout",function(e){
		e.target.style.color="black";
		var details=document.getElementById("details");
		details.innerHTML="";
	})


};