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
					paddingRight: "10em",
					boxShadow: "0 .15rem 1.75rem 0 #3a3b4526 !important"
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
					<li class="nav-item active">
						<a v-on:click="changeIndex(0)" class="nav-link no-outline" v-bind:style="style.navlink" href="#">Home</a>
					</li>
					
					<li class="nav-item">
						<a v-on:click="changeIndex(1)" class="nav-link no-outline" v-bind:style="style.navlink" href="#">Login</a>
					</li>
					
					<li class="nav-item">
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
					width: "33.3%",
					height: "15em",
					borderRadius: "1em",
					backgroundColor: "#ffffff",
					// marginBottom: "1em",
					margin: "2em",
					boxShadow: "0 .15rem 1.75rem 0 #3a3b4526 !important"
				}
			}
		}
	},
	template: `
		<div class="api-card" v-bind:style="style.apiCard">
		</div>
	`
});


Vue.component("bottom-bar", {
	props: {
		sociallinks: Array,
		pallete: Object
	},
	methods: {},
	data(){
		return {
			style: {
				footer: {
					display: "flex",
					boxShadow: "0px -3px 20px rgba(91, 91, 91, 0.2) !important",
					height: "6em",
					justifyContent: "center",
					alignContent: "center"
				},

				footerNote: {
					fontSize: "1.1em",
					color: "#575757",
					width: "65%",
					margin: "0px",
					display: "flex",
					alignItems: "center"
				},

				socialLinks: {
					width: "20%",
					display: "flex"
				},

				socialLink: {
					width: "33.3%",
					display: "flex",
					justifyContent: "center",
					alignContent: "center"
				},

				socialLinkImg: {

				}
			}
		}
	},
	template: `
		<footer v-bind:style="style.footer">
			<p v-bind:style="style.footerNote" class="footer-note">Rubbie Kelvin</p>
			<div v-bind:style="style.socialLinks" class="footer-links">
				<a class="footer-link" v-bind:href="link.route" v-bind:style="style.socialLink" v-bind:key="link.id" v-for="link in sociallinks">
					<img v-bind:src="link.src" v-bind:style="style.socialLinkImg"/>
				</a>
			</div>
		</footer>
	`
});

Vue.component("signup-modal", {
	props: {},
	methods: {
		signUp(){
			let usr = this.data.username;
			let eml = this.data.email;
			let psw = this.data.password;

			postrequest("auth/users/", {
				username: usr,
				email: eml,
				password: psw
			})

			.then(function (response) {
				let data = response.data;

				console.log(`created account for ${data.username}`);

				if (Boolean(data.username)){
					console.log("loggin in...");

					postrequest("auth/token/login/", {
						username: data.username,
						password: psw
					})

					.then(function (response) {
						console.log(response.data);
						let token = response.data.auth_token;

						console.clear();

						if (Boolean(token)){
							window.localStorage.setItem("auth", token);
							window.location = "/home";
						}
					})

					.catch(function (error){

					});
				}
			})
			
			.catch(function (error) {
				console.log(error);
			});
		}
	},
	data(){
		return {
			data: {
				username: "",
				password: "",
				email: ""
			}
		}
	},
	template:`
		<div class="modal fade" data-backdrop="static" tabindex="-1" role="dialog" aria-labelledby="staticBackdropLabel" aria-hidden="true">
			<div class="modal-dialog" role="document">
				<form class="modal-content">
			
					<div class="modal-header">
						<h5 class="modal-title" id="staticBackdropLabel">Sign Up</h5>
						<button type="button" class="close" data-dismiss="modal" aria-label="Close">
							<span aria-hidden="true">&times;</span>
						</button>
					</div>
			
					<div class="modal-body">
						
					<div class="form-group">
						<label for="em__">Email address</label>
						<input v-model="data.email" type="email" class="form-control" id="em__" aria-describedby="emailHelp" required>
						<small id="emailHelp" class="form-text text-muted">We'll never send spam mails.</small>
					</div>

					<div class="form-group">
						<label for="us__">Username</label>
						<input v-model="data.username" type="text" class="form-control" id="us__" aria-describedby="Usr__help" required>
						<small id="Usr__help" class="form-text text-muted">Usernames must be unique.</small>
					</div>
					
					<div class="form-group">
						<label for="pa__">Password</label>
						<input v-model="data.password" type="password" class="form-control" id="pa__" required>
					</div>

					</div>
			
					<div class="modal-footer">
						<button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
						<button v-on:click.prevent="signUp" type="submit" class="btn btn-primary">sign up</button>
					</div>
				</form>
			</div>
		</div>
	`
})

Vue.component("login-modal", {
	props: {},
	methods: {},
	data(){
		return {}
	},
	template:`
		<div class="modal fade" data-backdrop="static" tabindex="-1" role="dialog" aria-labelledby="staticBackdropLabel" aria-hidden="true">
			<div class="modal-dialog" role="document">
				<div class="modal-content">
			
					<div class="modal-header">
						<h5 class="modal-title" id="staticBackdropLabel">Login</h5>
						<button type="button" class="close" data-dismiss="modal" aria-label="Close">
							<span aria-hidden="true">&times;</span>
						</button>
					</div>
			
					<div class="modal-body">
						...
					</div>
			
					<div class="modal-footer">
						<button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
						<button type="button" class="btn btn-primary">Understood</button>
					</div>
				</div>
			</div>
		</div>
	`
})