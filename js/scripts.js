$("job").hover( 
	function () {
    	$(this).addclass("jobfocus");
	},
  	
  	function () {
  		$(this).removeclass("jobfocus");
  	}
	)