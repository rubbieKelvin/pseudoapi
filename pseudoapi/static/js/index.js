let app = new Vue({
    el: "#app",
    methods: {
    	changeIndex(index){
    		alert(index);
    	}
    },
    data(){
    	return {
    		pallete: {
    			primary: "var(--primary)",
    			dark: 	 "var(--dark)",
    			lightBg: "var(--light-bg)"
    		},

    		style: {
	    		body: {
	    			backgroundColor: "var(--light-bg)",
	    			height: "90vh",
	    			paddingLeft: "10em",
	    			paddingRight: "10em",
	    			paddingTop: "2em"
	    		}
    		}
    	};
    }
});