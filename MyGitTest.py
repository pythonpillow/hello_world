$(function(){
	$.ajax({
	        type:"GET",
iiiii      url:"https://www.baidu.com/",
			async: false,
	        success:function(data){
				alert(1111)
	        }
	});
});


$(function(){
	$.ajax({
		
		type:"GET",
		url:"http://127.0.0.1:8000/main",
		async:false,
		success:function(data){
			alert(111)
		}
	});
});
