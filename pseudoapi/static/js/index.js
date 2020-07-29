let app = new Vue({
    el: "#app",
    methods: {
    	changeIndex(index){

    		if (index == 1){
    			$("#login-modal").modal({});
    		}else if (index == 2){
    			alert("about");
    		}
    	},

		openSignUp(e){
			$("#signup-modal").modal({})
		}
    },
    data(){
    	return {
    		pageindex: 0,
    		pallete: {
    			primary: "var(--primary)",
    			dark: 	 "var(--dark)",
    			lightBg: "var(--light-bg)",
    			primaryFaded: "var(--primary-faded)"
    		},

    		style: {
	    		body: {
	    			backgroundColor: "var(--light-bg)",
	    			height: "auto",
	    			paddingLeft: "10em",
	    			paddingRight: "10em",
	    			paddingTop: "2em"
	    		}
    		}
    	};
    }
});