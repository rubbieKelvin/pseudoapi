let app = new Vue({
    el: "#app",
    methods: {
        
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