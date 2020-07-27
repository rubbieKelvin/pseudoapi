Vue.component("nav-bar", {
	props: {
		pallete: Object
	},
	methods: {
		changeIndex(index){
			this.current = index;
			this.$emit("change-index", index);
		}
	},
	data(){
		return {
			current: 0,
			style: {
				navbar: {
					color: this.pallete.dark,
					height: "7em",
					paddingLeft: "10em",
					paddingRight: "10em"
				},

				navlink: {
					color: this.pallete.dark,
					fontSize: "1.2em",
					paddingRight: "1.5em",
					paddingLeft: "1.5em",
					borderBottom: "1px solid transparent"
				},

				navbrand: {
					color: this.pallete.dark,
					fontSize: "2em",
					marginRight: "1em"
				},

				searchbar: {
					height: "3.5em"
				},

				searchbtn: {
					height: "3.5em",
					width: "7em",
					border: "1px solid "+this.pallete.primary,
					color: this.pallete.primary
				},
				toggler: {
					color: this.pallete.primary
				}
			}
		};
	},
	template: `
		<nav class="navbar navbar-expand-lg" v-bind:style="style.navbar">
			<a class="navbar-brand" href="/" v-bind:style="style.navbrand">
				&lt;<span v-bind:style="{color: pallete.primary}">PseudoAPI</span>/&gt;
			</a>
			
			<button class="navbar-toggler no-outline" v-bind:style="style.toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo02" aria-controls="navbarTogglerDemo02" aria-expanded="false" aria-label="Toggle navigation">
				 <svg height="25px" width="25px" xmlns="http://www.w3.org/2000/svg">
	                <line v-bind:style="{stroke: 'currentColor'}" x1="0" x2="30" y1="1" y2="1" stroke-width="2" stroke-linecap="square" />
	                <line v-bind:style="{stroke: 'currentColor'}" x1="0" x2="30" y1="9" y2="9" stroke-width="2" stroke-linecap="square" />
	                <line v-bind:style="{stroke: 'currentColor'}" x1="0" x2="30" y1="18" y2="18" stroke-width="2" stroke-linecap="square" />
	            </svg>
			</button>

			<div class="collapse navbar-collapse" id="navbarTogglerDemo02">
				<ul class="navbar-nav mx-auto mt-2 mt-lg-0">
					<li class="nav-item" v-bind:class="[(current===0)?'active':'inactive']">
						<a v-on:click="changeIndex(0)" class="nav-link no-outline" v-bind:style="style.navlink" href="#">Home</a>
					</li>
					
					<li class="nav-item" v-bind:class="[(current===1)?'active':'inactive']">
						<a v-on:click="changeIndex(1)" class="nav-link no-outline" v-bind:style="style.navlink" href="#">Login</a>
					</li>
					
					<li class="nav-item" v-bind:class="[(current===2)?'active':'inactive']">
						<a v-on:click="changeIndex(2)" class="nav-link no-outline" v-bind:style="style.navlink" href="#">About</a>
					</li>
				</ul>
			
				<form class="form-inline my-2 my-lg-0">
					<input class="form-control search-bar mr-sm-2" type="search" placeholder="Search" v-bind:style="style.searchbar">
					<button class="btn search-bar-btn my-2 my-sm-0" type="submit" v-bind:style="style.searchbtn">Search</button>
				</form>
			</div>
		</nav>
	`
});

Vue.component("api-card", {
	props: {
		pallete: Object
	},
	methods: {},
	data(){
		return {
			style: {
				apiCard: {
					width: "100%",
					height: "20em",
					borderRadius: "1em",
					backgroundColor: this.pallete.primaryFaded,
					// marginBottom: "1em",
					margin: "2em"
				}
			}
		}
	},
	template: `
	<div class="api-card col" v-bind:style="style.apiCard">

	</div>
	`
});